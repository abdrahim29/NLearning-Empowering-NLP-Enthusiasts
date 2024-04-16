from components.document_loaders import documentLoaders
from components.splitters import textSplitter
#from components.vectorstsore import vectorStore
#from langchain.embeddings import HuggingFaceEmbeddings
from config import *

# initialize the embedding model
# embed_fn = HuggingFaceEmbeddings(model_name=embed_model)

def load_content(file_path, file_extension=None):
    loader = documentLoaders(file_path) # Create a document loader object
    if file_extension == "pdf":
        file_content = loader.load_pdf_using_pymupdf() #extract the content of pdf file from pymupdf loader
    elif file_extension == "csv":
        file_content = loader.load_csv() #extract the content of csv file from CSV loader
    elif file_extension == "png":
        file_content = loader.load_image()
    return file_content


def split_content(file_content):
    splitter = textSplitter(CHUNK_SIZE, CHUNK_OVERLAP) 
    texts = splitter.split_recurrsive_character(file_content)
    return texts

# def create_vector_store(chunks):
#     init_vectorstore = vectorStore(is_load, index_name)
#     vector_db = init_vectorstore.vectorstore_faiss(embed_fn, chunks)
#     return vector_db

def main():
    supported_files = ["pdf", "csv", "png"]
    file_index = int(input("Enter 1 to select a pdf file. \nEnter 2 to select a csv file. \nEnter 3 to select a image file. \nNumber: ")) 
    if file_index == 1:
        FILE_PATH = PDF_FILE_PATH
    elif file_index == 2:
        FILE_PATH = CSV_FILE_PATH
    elif file_index == 3:
        FILE_PATH = PNG_FILE_PATH 

    file_extension = FILE_PATH.split('\\')[-1].split(".")[-1] #extract the file extension e.g. pdf from the file path
    if file_extension not in supported_files: #if the file extension is not lie in supported files list, then return exception
        return("This file is not supported at the moment.")
    """
    Load the file content
    """
    file_content = load_content(FILE_PATH, file_extension)
    """
    Split the file content
    """
    texts = split_content(file_content)
    """
    Create a vector store
    """
    # vector_db = create_vector_store(texts)
    # print(texts)


if __name__ == "__main__":
    main()
