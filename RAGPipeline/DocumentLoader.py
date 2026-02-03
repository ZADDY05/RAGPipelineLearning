from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader, UnstructuredExcelLoader, JSONLoader


def load_all_docs(data_directory: str) -> list[any]:
    """
    Docstring for load_all_docs
    
    :param data_path: Description
    :type data_path: str
    :return: Description
    :rtype: list
    """
    data_path=Path(data_directory).resolve()
    print(f"[DEBUG] Data Path to find documents is {data_path}")
    documents=[]

    ###PDF FILES

    pdf_files=list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] found {len(pdf_files)} pdf_files : {[str(f) for f in pdf_files]}")

    for pdf in pdf_files:
        print(f"Loading the pdf file : {pdf}")
        try:
            loader=PyPDFLoader(
                str(pdf)
            )
            loaded_docs=loader.load()
            documents.extend(loaded_docs)

        except Exception as e:
            print(f"Failed to load the {pdf} : {e}")

    text_files=list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] found {len(text_files)} text_files : {[str(f) for f in text_files]}")

    for txt in text_files:
        print(f"Loading the text file : {txt}")
        try:
            loader=TextLoader(
                str(txt)
            )
            loaded_docs=loader.load()
            documents.extend(loaded_docs)

        except Exception as e:
            print(f"Failed to load the {txt} : {e}")
    return documents

