import os
import config
from thinkgpt.llm import ThinkGPT
from fastapi import FastAPI

app = FastAPI()

os.environ['OPENAI_API_KEY'] = config.api_key
llm = ThinkGPT(model_name="gpt-3.5-turbo", openai_api_key=os.environ['OPENAI_API_KEY'])

# learn a new language
@app.post("/learn_language")
async def learn():
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

@app.post("/replay_expand_memory")
async def replay_expand_memory():
    # Load old memory
    old_memory = [
        "Klaus Mueller is writing a research paper",
        "Klaus Mueller enjoys reading a book on gentrification",
        "Klaus Mueller is conversing with Ayesha Khan about exercising"
    ]

    # Teach the LLM the old memory
    llm.memorize(old_memory)

    # Induce reflections based on the old memory
    new_observations = llm.infer(facts=llm.remember())
    print('new thoughts:')
    print('\n'.join(new_observations))

    llm.memorize(new_observations)
    return {
        "pred": new_observations
    }


# Self code refinement
@app.post("/code_refinement")
async def code_refinement():
    code_refine = llm.refine(
    content="""
    import re
        print('hello world')
            """,
        critics=[
            'File "/Users/alaeddine/Library/Application Support/JetBrains/PyCharm2022.3/scratches/scratch_166.py", line 2',
            "  print('hello world')",
            'IndentationError: unexpected indent'
        ],
        instruction_hint="Fix the code snippet based on the error provided. Only provide the fixed code snippet between `` and nothing else.")
    
    return {
        "code": code_refine
    }


if __name__ == "__main__":
    uvicorn.run(app)