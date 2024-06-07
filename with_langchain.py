from langchain_community.llms.llamafile import Llamafile

llm = Llamafile()

query = "Tell me a joke"

cmpt = llm.invoke(query)
print(cmpt)

# for chunks in llm.stream(query):
#     print(chunks, end="")

