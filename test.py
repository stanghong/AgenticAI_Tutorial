import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIModel

load_dotenv()

model = OpenAIModel(
    model_id="gpt-4o",
    api_base="https://api.openai.com/v1",
    api_key=os.environ["OPENAI_API_KEY"],
)

agent = CodeAgent(
    tools=[],
    model=model,
)

result = agent.run("Calculate the sum of the first 20 prime numbers.")
print(result)