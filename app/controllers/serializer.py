from marshmallow import fields

from app.utils.filetypes import FolderType, NoteTimeType
from core.extensions import ma


class FolderPathSerializer(ma.Schema):
    path = FolderType(required=True)


class NoteSerializer(ma.Schema):
    id = fields.String(dump_only=True)
    note_text = fields.String(required=True)
    note_timestamp = NoteTimeType(required=True)


class FolderContentSerializer(ma.Schema):
    id = fields.String()
    folder_name = fields.String()


class FileContentSerializer(ma.Schema):
    id = fields.String()
    video_title = fields.String()
    video_src = fields.String()
    video_length = fields.Integer()
    is_favourite = fields.Boolean()
