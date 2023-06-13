from datetime import datetime
from pydantic import BaseModel, HttpUrl
from videos.models import ReactionType


class VideoRead(BaseModel):
    video_id: int
    name: str
    username: str
    video_url: HttpUrl
    preview_url: HttpUrl
    count_reactions: int
    upload_at: datetime


class CommentRead(BaseModel):
    video_id: int
    user_id: int
    create_at: datetime
    text: str


class ReactionRead(BaseModel):
    user_id: int
    video_id: int
    reaction_type: ReactionType


