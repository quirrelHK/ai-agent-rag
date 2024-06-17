import os
from llama_index.core import Settings
from llama_index.readers.file import PDFReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import StorageContext, VectorStoreIndex, load_indices_from_storage

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

DATA_PATH = "./data"


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_indices_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index

pdf_path = os.path.join(DATA_PATH,"India.pdf")
pdf_file = PDFReader().load_data(file = pdf_path)

pdf_index = get_index(pdf_file,"india")
# print(pdf_index)
pdf_engine = pdf_index[0].as_query_engine()