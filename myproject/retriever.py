from lazyllm import Retriever, Document
def create_retriever(path: str, query: str):
    """
 创建并执行检索
Args:
Google风格的文档
path (str): 文档的绝对路径 • 简短描述
query (str): 查询语句 • Args（参数列表）
list: 检索结果
"""
doc = Document(path)
retriever = Retriever(doc,
group_name="CoarseChunk",
similarity="bm25_chinese", topk=3)