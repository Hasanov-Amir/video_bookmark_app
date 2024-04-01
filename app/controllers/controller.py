from flask import Blueprint, request

from app.controllers.serializer import FolderPathSerializer, VideoPathSerializer

bp = Blueprint("main", __name__)


@bp.route("/add/folder", methods=("POST",))
def add_folder():
    data = request.json
    serializer = FolderPathSerializer()
    validated_data = serializer.load(data)
    return data


@bp.route("/add/video", methods=("POST",))
def about():
    data = request.json
    serializer = VideoPathSerializer()
    validated_data = serializer.load(data)
    return data
