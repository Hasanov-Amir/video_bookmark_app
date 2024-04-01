from marshmallow import fields

from core.extensions import ma
from app.utils.filetypes import FolderType, FileType


class VideosSerializer(ma.Schema):
    id = fields.UUID(dump_only=True)
    create_date = fields.DateTime(dump_only=True)
    edit_date = fields.DateTime(dump_only=True)

    product_title = fields.Str(required=True)
    product_owner_shop = fields.Str(dump_only=True)
    product_owner_shop_title = fields.Str(dump_only=True)
    product_count = fields.Int(required=True)
    product_properties = fields.Dict(required=True)
    product_images = fields.Dict(dump_only=True)

    def __init__(self, method=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if method == "PUT":
            self.fields['product_title'].required = False
            self.fields['product_count'].required = False
            self.fields['product_properties'].required = False


class FolderPathSerializer(ma.Schema):
    path = FolderType(required=True)

class VideoPathSerializer(ma.Schema):
    path = FileType(required=True)
