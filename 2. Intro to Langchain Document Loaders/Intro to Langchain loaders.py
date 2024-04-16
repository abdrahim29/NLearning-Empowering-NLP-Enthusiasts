from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

class document_loaders:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf_using_pypdf(self):
        try:
            loader = PyPDFLoader(self.file_path)
            pages = loader.load()
            return pages
        
        except Exception as e:
            print(f"Error: {e}")    
    
    def load_pdf_using_pymupdf(self):
        try:
            loader = PyMuPDFLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")

    def load_pdf_using_unstruct_pdf(self):
        loader = UnstructuredPDFLoader(self.file_path)
        data= loader.load()
        return data


    def load_pdf_using_online_pdf(self):
        try:
            loader = OnlinePDFLoader(self.file_path)
            data = loader.load()
            return data    
        except Exception as e:
             print(f"Error: {e}")


dl = document_loaders("HBR_How_Apple_Is_Organized_For_Innovation-4.pdf")
# pypdf_results = dl.load_pdf_using_pypdf()
# print(pypdf_results)

pymupdf_results = dl.load_pdf_using_pymupdf()
print(pymupdf_results)

# py_unstruct_results = dl.load_pdf_using_unstruct_pdf()
# print(py_unstruct_results)

# py_onlinepdf_results = dl.load_pdf_using_online_pdf()
# print(py_onlinepdf_results)