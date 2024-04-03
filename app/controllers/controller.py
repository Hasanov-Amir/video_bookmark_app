from flask import Blueprint, request

from app.fs.tree import fs_json
from app.controllers.serializer import FolderPathSerializer, NoteSerializer

bp = Blueprint("main", __name__)


@bp.route("/open/folder", methods=("POST", ))
def open_folder():
    data = request.json
    serializer = FolderPathSerializer()
    validated_data = serializer.load(data)
    path = validated_data.get("path")
    fs_json.inspect(path)
    return {}, 200


@bp.route("/<video_id>/add/note", methods=("POST", ))
def add_note(video_id):
    data = request.json
    serializer = NoteSerializer()
    validated_data = serializer.load(data)
    note = fs_json.add_note_to_video(video_id, validated_data["note_text"], validated_data["note_timestamp"])
    response = serializer.dump(note)
    return response, 200


@bp.route("/<folder_id>/content", methods=("GET", ))
def get_content(folder_id):
    # TODO: create endpoint for getting provided folder content
    ...
