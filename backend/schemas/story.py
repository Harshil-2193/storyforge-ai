from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

class StoryopttionsSchema(BaseModel):
    text: str
    node_id : Optional[int] = None

class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False

class CompleteStoryNodeRespose(BaseModel):
    id: int
    options: List[StoryopttionsSchema] = []

    class Config:
        from_attributes = True

class StoryBase(BaseModel):
    title: str
    session_id:Optional[str] = None

    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme: str


class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_nodes: List[CompleteStoryNodeRespose] = []
    all_nodes: Dict[int, CompleteStoryNodeRespose]

    class Config:
        from_attributes = True
    