# OpenAI Models with LangChain

This project demonstrates how to use **LangChain with OpenAI models** to build simple LLM-powered applications.

## Features
- Load environment variables securely with `python-dotenv`
- Initialize and call OpenAI's GPT models via `langchain-openai`
- Run a simple example prompt with `gpt-4o-mini`


## Installation

Clone this repository and install the required dependencies:

```bash
pip install langchain-openai
pip install python-dotenv
```

## Environment Setup

Create a .env file in the root directory and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script to test LangChain with OpenAI:

```bash
python openai.py
```

Expected output: The model will generate a response with three reasons for using LangChain in LLM application development.