import os
import sys
from dotenv import load_dotenv
load_dotenv()

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from graph.graph import app


if __name__ == "__main__":
    question = "What is agent memory in context of LLMs?"
    print(app.invoke(input={"question": question}))
