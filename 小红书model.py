from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Xiaohongshu(BaseModel):
    titles: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
    content: str = Field(description="小红书的正文内容")