# AsiliBora 

## Vision
To bridge the gap between Industry experts and beginners in the world.

## Chatbot API for local languages.

![AsiliBora Logo](./images/logo.png)


## Local Language Understanding with LLM Model - PyTorch and FastAPI Backend

## Overview

Welcome to the Local Language Understanding (LLU) project! This repository houses the codebase and resources for training an LLM (Local Language Model) with the goal of understanding and processing various local languages. The project has been implemented in PyTorch, and it includes a FastAPI backend for serving the trained model via APIs.

## Table of Contents

- [Overview](#overview)
- [Background](#background)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Data Collection](#data-collection)
- [Training the LLM Model](#training-the-llm-model)
- [API Server with FastAPI](#api-server-with-fastapi)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Background

In today's interconnected world, there is a growing need to bridge the communication gap between people who speak different languages. While many machine learning models excel in major languages, local languages often remain underrepresented. The Local Language Understanding (LLU) project aims to address this issue by developing an LLM model that can comprehend and process various local languages effectively.

## Getting Started

To use and contribute to this project, follow the instructions below.

### Prerequisites

- Python 3.6+
- PyTorch
- Transformers library (Hugging Face)
- FastAPI
- Uvicorn
- Llama V2

### Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your-username/local-language-understanding.git
cd local-language-understanding
```

2. Create a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Data Collection

To train the LLM model effectively, we need a diverse and representative dataset of local language texts. If you have a suitable dataset, place it in the `data` directory with appropriate labels. If you'd like to contribute your dataset to this project, please reach out to us via email (provide-email-here) or create an issue in the repository.

## Training the LLM Model

The training process for the LLM model involves fine-tuning a pre-trained language model on the local language dataset. Before training, ensure that you have the required dataset and have installed all the necessary dependencies.

To train the LLM model, execute the following command:

```
python train_llm_model.py
```

The script will load the pre-trained model and fine-tune it on the provided dataset.

## API Server with FastAPI

The LLM model can be served as an API using FastAPI, allowing other applications to interact with it programmatically. To start the API server, run the following command:

```
uvicorn app.main:app --reload
```

This will start the FastAPI server, and you can make POST requests to the specified endpoints to interact with the LLM model.

## Evaluation

Evaluation of the LLM model is crucial to assess its performance on various tasks and datasets. To evaluate the trained model, run the evaluation script:

```
python evaluate_llm_model.py
```

The script will present metrics and performance results on the test dataset.

## Contributing

We welcome contributions to this project! Whether you want to improve the model, add support for new languages, enhance the FastAPI backend, or update documentation, your help is valuable. To contribute, please follow our [contribution guidelines](CONTRIBUTING.md) or email [paulmwaura254@gmail.com](paulmwaura@gmail.com).

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per the terms of the license.
