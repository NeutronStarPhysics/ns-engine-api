from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class ExecutionRequest(BaseModel):
    id: str = Field(min_length=10)
    algorithm: str = Field(min_length=5)
    request_time: datetime = datetime.now()
