from sqlalchemy import String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from database.base import Model, Column


class Video(Model):
    __tablename__ = "video"

    video_src = Column("video_src", String(500))
    video_title = Column("video_title", String(200))
    video_length = Column("video_length", String(10))
    is_favourite = Column("is_favourite", Boolean(), default=False)

    def __str__(self):
        return f"{self.id} : {self.video_title}"
    
    def __repr__(self):
        return f"{self.id} : {self.video_title}"


class Note(Model):
    __tablename__ = "note"

    note_text = Column("note_text", String(500))
    note_timestamp = Column("note_timestamp", String(10))
    video = Column("video", UUID(as_uuid=True))

    def __str__(self):
        return f"{self.id} : {self.note_text}"
    
    def __repr__(self):
        return f"{self.id} : {self.note_text}"
