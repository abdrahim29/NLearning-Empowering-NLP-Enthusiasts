from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders.image import UnstructuredImageLoader


# loader = UnstructuredMarkdownLoader(r"C:\Users\Abdul Rahim\Self Projects\NLP bootcamp\class3-20240324T101254Z-001\documents\markdown-sample.md") 
# data = loader.load()
# print(data)

loader = UnstructuredImageLoader(r"C:\Users\Abdul Rahim\Self Projects\NLP bootcamp\class3-20240324T101254Z-001\documents\The_river_effect_in_justified_text.jpg")
data = loader.load()
print(data)
        