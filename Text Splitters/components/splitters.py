from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

class textSplitter:
    def __init__(self, chunk_size, chunk_overlap):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text_character(self, content):
        try:
            text_splitter = CharacterTextSplitter(
                separator = "\n",
                chunk_size = self.chunk_size,
                chunk_overlap = self.chunk_overlap ,
                length_function=len,
                is_separator_regex=False,
            )
            doc_list = []
            for page in content:
                #filename = page.metadata['source'].split("\\")[-1]
                page_splits = text_splitter.split_text(page.page_content)
                for page_sub_split in page_splits:
                    #metadata = {"source": filename}
                    doc_string = Document(page_content=page_sub_split)
                    doc_list.append(doc_string)
            return doc_list

        except Exception as e:
            print(f"Error: {e}")    

    def split_recurrsive_character(self, content):
        try:
            text_splitter = RecursiveCharacterTextSplitter(
                separators=["\n\n", "\n", " ", ".",],
                chunk_size= self.chunk_size,
                chunk_overlap= self.chunk_overlap,
                length_function=len,
                is_separator_regex=False,
            )
            doc_list = []
            for page in content:
                filename = page.metadata['source'].split("\\")[-1]
                page_splits = text_splitter.split_text(page.page_content)
                for page_sub_split in page_splits:
                    metadata = {"source": filename}
                    doc_string = Document(page_content=page_sub_split, metadata=metadata)
                    doc_list.append(doc_string)
            return doc_list

        except Exception as e:
            print(f"Error: {e}")    
