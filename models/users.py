from pydantic import BaseModel
from typing import Optional

class Posts(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True