import os
import config
from thinkgpt.llm import ThinkGPT
from fastapi import FastAPI

app = FastAPI()

os.environ['OPENAI_API_KEY'] = config.api_key


@app.post("/learn")
async def learn():
    llm = ThinkGPT(model_name="gpt-3.5-turbo", openai_api_key=os.environ['OPENAI_API_KEY'])

    rules = llm.abstract(observations=[
        "in swahili, I did not eat is \"sikula\"",
        "I did not work is \"ma sikufanya kazi\"",
        "I did not go is \"sikuenda\"",
    ], instruction_hint="output the rule in swahili")
    llm.memorize(rules)

    llm.memorize("in swahili, I studied is \"nilisoma\"")

    task = "translate to Tunisian: I didn't study"
    llm.predict(task, remember=llm.remember(task))


if __name__ == "__main__":
    uvicorn.run(app)