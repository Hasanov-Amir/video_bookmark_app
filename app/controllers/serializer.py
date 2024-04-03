from marshmallow import fields

from app.utils.filetypes import FileType, FolderType, NoteTimeType
from core.extensions import ma


class VideosSerializer(ma.Schema):
    id = fields.UUID(dump_only=True)
    create_date = fields.DateTime(dump_only=True)
    edit_date = fields.DateTime(dump_only=True)


class FolderPathSerializer(ma.Schema):
    path = FolderType(required=True)


class VideoPathSerializer(ma.Schema):
    path = FileType(required=True)


class NoteSerializer(ma.Schema):
    note_text = fields.String(required=True)
    note_timestamp = NoteTimeType(required=True)
