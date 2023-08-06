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
        "in swahili, I did not eat is \"ndinaria\"",
        "I did not work is \"ma ndinaruta wera\"",
        "I did not go is \"ndinathii\"",
    ], instruction_hint="output the rule in kikuyu")
    llm.memorize(rules)

    llm.memorize("in kikuyu, I studied is \"ni ndiranthomire\"")

    task = "translate to Kikuyu: I didn't study"
    pred = llm.predict(task, remember=llm.remember(task))
    
    return {
        "pred": pred,
    }


if __name__ == "__main__":
    uvicorn.run(app)