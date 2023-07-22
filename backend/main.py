import os
from thinkgpt.llm import ThinkGPT

os.environ['OPENAI_API_KEY'] = "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"

llm = ThinkGPT(model_name="gpt-3.5-turbo", openai_api_key=os.environ['OPENAI_API_KEY'])

rules = llm.abstract(observations=[
    "in swahili, I did not eat is \"sikula\"",
    "I did not work is \"ma sikufanya kazi\"",
    "I did not go is \"sikuenda\"",
], instruction_hint="output the rule in french")
llm.memorize(rules)

llm.memorize("in swahili, I studied is \"nilisoma\"")

task = "translate to Tunisian: I didn't study"
llm.predict(task, remember=llm.remember(task))


