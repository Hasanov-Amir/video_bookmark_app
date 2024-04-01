import os

from flask import current_app
from marshmallow import ValidationError, fields

from app.utils.helpers import allowed_extension


class FolderType(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        folder_path = value

        if not folder_path:
            error = "No folder selected for uploading."
            return ValidationError(error)

        if not os.access(folder_path, os.W_OK):
            error = "Invalid folder path"
            return ValidationError(error)

        return value


class FileType(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        file_path = value

        if not file_path:
            error = "No file selected for uploading."
            return ValidationError(error)
        
        if not os.access(file_path, os.W_OK):
            error = "Invalid folder path"
            return ValidationError(error)

        if not allowed_extension(file_path):
            error = f'Allowed file types are {current_app.config["VIDEO_ALLOWED_EXTENSIONS"]}.'
            return ValidationError(error)

        return value
