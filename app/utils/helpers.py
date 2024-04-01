from flask import current_app


def allowed_extension(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["VIDEO_ALLOWED_EXTENSIONS"]
    )
