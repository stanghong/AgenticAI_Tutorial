# Agentic AI Notebooks

A focused collection of executable Jupyter notebooks for learning and experimenting with AI agents in Python. The repository contains notebook material only, including local exercises and compatibility updates based on the open-source Hugging Face Agents Course.

## What's included

- Agent fundamentals and a minimal agent library
- `smolagents` code agents, tool-calling agents, retrieval agents, and vision agents
- Multi-agent orchestration
- LangGraph agent workflows
- LlamaIndex agents and workflows
- Observability and evaluation examples
- Bonus and French-language notebooks

## Notebook index

| Area | Location |
| --- | --- |
| Agent fundamentals | [`notebooks/unit1/`](notebooks/unit1/) |
| Smolagents | [`notebooks/unit2/smolagents/`](notebooks/unit2/smolagents/) |
| LangGraph | [`notebooks/unit2/langgraph/`](notebooks/unit2/langgraph/) |
| LlamaIndex | [`notebooks/unit2/llama-index/`](notebooks/unit2/llama-index/) |
| Bonus notebooks | [`notebooks/bonus-unit1/`](notebooks/bonus-unit1/) and [`notebooks/bonus-unit2/`](notebooks/bonus-unit2/) |
| French notebooks | [`notebooks/fr/`](notebooks/fr/) |

## Featured multi-agent example

[`multiagent_notebook.ipynb`](notebooks/unit2/smolagents/multiagent_notebook.ipynb) builds a manager agent and a web-search agent. They research Batman filming locations and supercar factories, calculate cargo-plane travel times, and export a Plotly map.

Related outputs:

- [`batman_supercar_travel_times.csv`](notebooks/unit2/smolagents/batman_supercar_travel_times.csv)
- [`saved_map.png`](notebooks/unit2/smolagents/saved_map.png)

The notebook includes compatibility fixes for current `smolagents` releases:

- Explicit authorization for `plotly.express` and `plotly.graph_objects`
- The current final-answer-check callback signature
- Consistent use of `saved_map.png` for PNG export

## Getting started

```bash
git clone https://github.com/stanghong/AgenticAI_Tutorial.git
cd AgenticAI_Tutorial
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install jupyter
jupyter lab
```

Most notebooks contain installation cells for their own dependencies. To run the featured multi-agent notebook directly, install:

```bash
pip install "smolagents[openai]" plotly geopandas shapely kaleido jupyter
```

Plotly static-image export through Kaleido requires a compatible Chrome or Chromium installation.

## API configuration

Set your key before starting Jupyter:

```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4o-mini"  # optional
```

If `OPENAI_API_KEY` is not set, the featured notebook prompts for it securely at runtime.

## Secret safety

`.env`, virtual environments, notebook checkpoints, and common cache files are excluded by `.gitignore`. Never commit API keys or access tokens. The repository does not contain the local `.env` file.

## Attribution

These notebooks are adapted from the [Hugging Face Agents Course notebooks](https://github.com/huggingface/agents-course-notebooks). See [LICENSE](LICENSE) and the upstream project for attribution and licensing details.
