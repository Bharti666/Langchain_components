from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings()
vector = embeddings.embed_query("Bharti is learning LangChain.")
print(vector[:5])