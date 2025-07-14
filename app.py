import os
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import sqlite3

# Set Gemini API Key
os.environ["GOOGLE_API_KEY"] = "your-gemini-api-key"

# Connect to your SQLite DB
db = SQLDatabase.from_uri("sqlite:///database.db")

# Gemini LLM setup
llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.2)

# Create Text-to-SQL Chain
text_to_sql_chain = create_sql_query_chain(llm, db)

# Optional: Add a second chain that runs the SQL and returns result
full_chain = (
    RunnablePassthrough.assign(query=text_to_sql_chain)
    | RunnablePassthrough.assign(result=lambda x: db.run(x["query"]))
)

# CLI Chat Loop
while True:
    user_input = input("\nAsk your database: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    try:
        result = full_chain.invoke({"question": user_input})
        print("\n🔎 SQL:", result["query"])
        print("📊 Result:", result["result"])
    except Exception as e:
        print("❌ Error:", e)
