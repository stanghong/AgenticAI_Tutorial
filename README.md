# Agentic AI Tutorial

A hands-on collection of lessons and notebooks for learning how to build AI agents with Python. The repository covers agent fundamentals, tool use, planning, multi-agent systems, retrieval-augmented generation, observability, and evaluation.

This project is adapted from the open-source [Hugging Face Agents Course](https://github.com/huggingface/agents-course) and includes local experiments and compatibility updates.

## Highlights

- Introductory material on language models and agent workflows
- Examples using `smolagents`, LangGraph, and LlamaIndex
- Tool-calling, web-search, and code-agent notebooks
- Multi-agent orchestration examples
- Agentic RAG and evaluation material
- English and translated course content

## Featured notebook

The multi-agent tutorial builds a manager agent and a dedicated web-search agent. Together they research Batman filming locations and supercar factories, calculate cargo-plane travel times, and export the result as a Plotly map.

- Notebook: [`notebooks/unit2/smolagents/multiagent_notebook.ipynb`](notebooks/unit2/smolagents/multiagent_notebook.ipynb)
- Example output: [`notebooks/unit2/smolagents/saved_map.png`](notebooks/unit2/smolagents/saved_map.png)

The notebook includes compatibility fixes for current `smolagents` releases, including explicit Plotly submodule authorization, the current final-answer-check callback signature, and consistent PNG output naming.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/stanghong/AgenticAI_Tutorial.git
cd AgenticAI_Tutorial
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Install notebook dependencies

The notebooks contain their own installation cells. For the featured multi-agent notebook, install:

```bash
pip install "smolagents[openai]" plotly geopandas shapely kaleido jupyter
```

Plotly static-image export uses Kaleido and requires a compatible Chrome or Chromium installation.

### 4. Configure the OpenAI API

Set the key in your shell before launching Jupyter:

```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4o-mini"  # optional
jupyter lab
```

If `OPENAI_API_KEY` is not already set, the featured notebook requests it securely at runtime.

## Repository layout

```text
notebooks/  Executable tutorials and experiments
units/      Course lessons in multiple languages
quiz/       Quiz data and supporting utilities
scripts/    Translation and maintenance scripts
```

## Keeping secrets safe

The repository's `.gitignore` excludes `.env` and common virtual-environment directories. Never commit API keys, access tokens, or other credentials. If you store credentials in a local `.env` file, keep that file only on your machine.

## Attribution

The original course content was created by the Hugging Face Agents Course contributors. See the upstream [course repository](https://github.com/huggingface/agents-course) and this repository's [LICENSE](LICENSE) for details.
