from pydantic import BaseModel
from typing import List, Tuple, Optional

class Request(BaseModel):
    id: str
    algorithm: str
    # parameters: List[Tuple[str, str]]


