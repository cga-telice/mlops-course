# SafeMate

Welcome to **SafeMate**, an occupational health and safety assistant designed to serve construction field workers. This project is currently in the proof of concept stage and aims to provide immediate, accessible safety guidelines and answers derived from authoritative sources. The core of this assistant is built upon a chat interface that draws its responses from the safety manual provided by the Port of Seattle, offering a practical and user-friendly approach to workplace safety.

## Project Overview

SafeMate is crafted to transform the way construction workers interact with safety manuals, making it easier than ever to get answers to crucial safety questions on the job. By leveraging state-of-the-art machine learning models and natural language processing techniques, SafeMate delivers relevant safety information through a simple chat interface.

### Current State of the Project

This project is in its early stages, and the current implementation serves as a proof of concept. The backbone of SafeMate is a chat interface that allows users to query a safety manual, specifically the one provided by the Port of Seattle, which is publicly available online.

### Project Structure

The project is organized as follows:

D:.
├───.chainlit
│   └───translations
├───.files
├───app
├───data
│   ├───processed
│   ├───raw
│   └───results
├───models
├───notebooks
│   └───.ipynb_checkpoints
├───scripts
├───utils
└───__pycache__

Note: Some folders have been created to accommodate future developments and are not in use at the moment.

### Achievements So Far

1. **Synthetic QA Development**: Utilization of the RAGAS library to assess embeddings and models for effective question-answering.
2. **Data Processing**: Transformation of the raw PDF manual into a structured format, with embeddings stored in a vector store for quick retrieval.
3. **User Interface**: Implementation of ChainLit as the user interface, facilitating a seamless interaction where users can prompt questions, and the system retrieves context to provide informed responses.
4. **Accessibility**: The project's code is hosted on GitHub, with a live demo available on a Hugging Face space, demonstrating the capabilities and potential of SafeMate.

## Future Directions

As SafeMate evolves, we plan to expand the knowledge base beyond the Port of Seattle's safety manual, incorporate feedback mechanisms for continuous improvement, and refine our models for better accuracy and user experience.

## Contact

Cesáreo González Alvarez
Github: cga-telice
Linkedin: (https://www.linkedin.com/in/caesaripse/)

## License

SafeMate is released under the [MIT License](LICENSE).

## Acknowledgments

A special thank you to the Port of Seattle for making their safety manual publicly accessible and serving as the foundation for this project.

---

For more information, updates, and to try out the SafeMate proof of concept, please visit our [GitHub repository](link-to-repo) and [Hugging Face demo space](link-to-demo).

