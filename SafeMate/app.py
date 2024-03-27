# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion
import os
from dotenv import load_dotenv
from getpass import getpass
from operator import itemgetter

import openai
from openai import AsyncOpenAI  # importing openai for API usage

import chainlit as cl  # importing chainlit for our app
from chainlit.prompt import Prompt, PromptMessage  # importing prompt tools
from chainlit.playground.providers import ChatOpenAI  # importing ChatOpenAI tools

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain import hub
from langchain.prompts import ChatPromptTemplate
import faiss

# Working directory
# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)

# Set the enviroment variables

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the document vector store
file_name = "Seattle" 
path_raw = "data//raw//" + file_name + ".pdf" # The path where the raw documents are stored
path_processed = "data//processed//" + file_name + ".faiss" # The path where we will store the index

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = FAISS.from_texts([""], embeddings)

vs=vector_store.load_local(path_processed, embeddings, allow_dangerous_deserialization=True)

# Build the retriever

retriever = vs.as_retriever()

# Configure the Prompt templates

system_template = """You are a helpful but prudent occupational health and
safety assistant. Your anwswers will be grounded on the context.
If you don´t know an answer you will say that you don´t know.
"""

user_template = """
# Context:
{context}

# Question:
{question}
"""

@cl.on_chat_start  # marks a function that will be executed at the start of a user session
async def start_chat():
    settings = {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    cl.user_session.set("settings", settings)


@cl.on_message  # marks a function that should be run each time the chatbot receives a message from a user
async def main(message: cl.Message):
    settings = cl.user_session.get("settings") # gets the settings of the started session

    client = AsyncOpenAI()

    document_list = retriever.invoke(message.content)
    context = " ".join([doc.page_content for doc in document_list])
    
    print(message.content)

    print(context)

    prompt = Prompt(
        provider=ChatOpenAI.id,
        messages=[
            PromptMessage(
                role="system",
                template=system_template,
                formatted=system_template,
            ),
            PromptMessage(
                role="user",
                template=user_template,
                formatted=user_template.format(question=message.content, context=context),
            ),
        ],
        inputs={"question": message.content, "context": context},
        settings=settings,
    )

    print([m.to_openai() for m in prompt.messages])

    msg = cl.Message(content="")

    # Call OpenAI
    async for stream_resp in await client.chat.completions.create(
        messages=[m.to_openai() for m in prompt.messages], stream=True, **settings
    ):
        token = stream_resp.choices[0].delta.content
        if not token:
            token = ""
        await msg.stream_token(token)

    # Update the prompt object with the completion
    prompt.completion = msg.content
    msg.prompt = prompt

    # Send and close the message stream
    await msg.send()
