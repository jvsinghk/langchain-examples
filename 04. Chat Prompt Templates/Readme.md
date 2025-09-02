# Flag Colors with LangChain + OpenAI

This project uses LangChain with OpenAI to identify the colors present in a country's flag.

## Installation

```bash
pip install langchain-openai langchain-core python-dotenv
```

## Setup

Create a .env file with your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script:

```bash
python script.py
```

Example output for `France`
```python
['blue', 'white', 'red']
```