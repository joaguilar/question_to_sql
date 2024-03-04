from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = create_sql_query_chain(llm, db)
# response = chain.invoke({"question": "How many employees are there"})
# response = chain.invoke({"question": "what are the invoice items for invoce 1"})
response = chain.invoke({"question": "what are the names of the tracks invoiced in invoice 1"})

print(response)

# Run the query:
connection = sqlite3.connect("Chinook.db")
cursor = connection.cursor()
rows = cursor.execute(response).fetchall()
print(rows)
