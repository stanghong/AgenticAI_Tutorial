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

## Vision web-browser example

[`vision_web_browser.py`](notebooks/unit2/smolagents/vision_web_browser.py) combines a `smolagents` code agent with Selenium and Helium. It captures the current browser window after each step and sends the screenshot to an OpenAI vision-capable model so the agent can navigate visually.

The script uses `OpenAIServerModel` directly, defaults to `gpt-4.1-mini`, and expects agent-generated Python inside `<code>...</code>` tags. Install its dependencies with:

```bash
pip install "smolagents[openai]" helium selenium pillow python-dotenv
```

Then run the built-in example or provide a custom prompt:

```bash
python notebooks/unit2/smolagents/vision_web_browser.py
python notebooks/unit2/smolagents/vision_web_browser.py "Find the latest smolagents release notes"
```

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
export OPENAI_MODEL="gpt-4o-mini"  # optional notebook override
```

The vision browser defaults to `gpt-4.1-mini`; override it with `OPENAI_MODEL` or its `--model-id` option. If `OPENAI_API_KEY` is not set, the featured notebook prompts for it securely at runtime, while the standalone vision browser exits with a configuration error.

## Secret safety

`.env`, virtual environments, notebook checkpoints, and common cache files are excluded by `.gitignore`. Never commit API keys or access tokens. The repository does not contain the local `.env` file.

## Attribution

These notebooks are adapted from the [Hugging Face Agents Course notebooks](https://github.com/huggingface/agents-course-notebooks). See [LICENSE](LICENSE) and the upstream project for attribution and licensing details.
