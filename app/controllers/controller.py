import uuid

from flask import Blueprint, request

from app.controllers.serializer import (
    FileContentSerializer,
    FolderContentSerializer,
    FolderPathSerializer,
    NoteSerializer,
)
from app.data.models import Folder, Video, Note
from app.fs.tree import fs

bp = Blueprint("main", __name__)


@bp.route("/open/folder", methods=("POST",))
def open_folder():
    data = request.json
    serializer = FolderPathSerializer()
    validated_data = serializer.load(data)
    path = validated_data.get("path")
    fs.inspect(path)
    return {}, 200


@bp.route("/<video_id>/add/note", methods=("POST",))
def add_note(video_id):
    data = request.json
    serializer = NoteSerializer()
    validated_data = serializer.load(data)
    note = fs.add_note_to_video(
        video_id, validated_data["note_text"], validated_data["note_timestamp"]
    )

    response = serializer.dump(note)
    return response, 200


@bp.route("/<folder_id>/content", methods=("GET",))
def get_content(folder_id):
    try:
        folder_id = uuid.UUID(folder_id)
    except ValueError:
        folder_id = None

    child_folders = Folder.filter(folder_parent=folder_id)
    child_videos = Video.filter(folder=folder_id)

    folder_serializer = FolderContentSerializer()
    video_serializer = FileContentSerializer()

    response = {
        "folders": folder_serializer.dump(child_folders, many=True),
        "videos": video_serializer.dump(child_videos, many=True),
    }
    return response, 200


@bp.route("/<video_id>/notes", methods=("GET",))
def get_video_notes(video_id):
    video_id = uuid.UUID(video_id)
    notes = Note.filter(video=video_id)
    serializer = NoteSerializer()

    response = serializer.dump(notes, many=True)
    return response, 200


@bp.route("/notes", methods=("GET",))
def get_all_notes():
    notes = Note.filter()
    serializer = NoteSerializer()

    response = serializer.dump(notes, many=True)
    return response, 200
