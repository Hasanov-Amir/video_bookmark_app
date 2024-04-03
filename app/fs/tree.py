import os
import uuid

from pymediainfo import MediaInfo

from app.data.models import Folder, Note, Video
from core.settings.base import Config


class FS:
    def find_parent(self, child_key):
        parent = Folder.filter(id=child_key)
        return parent.first()

    def add_note_to_video(self, video_id, text, timestamp):
        note = Note.create(
            video=uuid.UUID(video_id), note_text=text, note_timestamp=timestamp
        )
        return note

    def inspect(self, path):
        for dirpath, dirnames, filenames in os.walk(path):
            parent_folder_name = dirpath.split("\\")[-1]
            parent_folder = Folder.filter(folder_name=parent_folder_name)
            if parent_folder:
                parent_folder = parent_folder[0]
            else:
                parent_folder = Folder.create(folder_name=parent_folder_name)
            folders = []
            for child_folder_name in dirnames:
                if not Folder.filter(
                    folder_name=child_folder_name, folder_parent=parent_folder.id
                ):
                    folders.append(
                        Folder(
                            folder_name=child_folder_name,
                            folder_parent=parent_folder.id,
                        )
                    )
            Folder.bulk_create(folders)

            videos = []
            for child_file_name in filenames:
                info = self._validate_file(dirpath, child_file_name)
                if info:
                    file_path, file_name, duration_in_ms = info
                    if not Video.filter(video_src=file_path):
                        videos.append(
                            Video(
                                video_src=file_path,
                                video_title=file_name,
                                video_length=duration_in_ms,
                                folder=parent_folder.id,
                            )
                        )
            Video.bulk_create(videos)

    def _validate_file(self, dirpath, file_name):
        file_path = os.path.join(dirpath, file_name)
        file_extension = file_name.split(".")[-1]
        if file_extension not in Config.VIDEO_ALLOWED_EXTENSIONS:
            return False
        file_info = MediaInfo.parse(file_path)
        duration_in_ms = file_info.tracks[0].duration
        return (file_path, file_name, duration_in_ms)


fs = FS()
