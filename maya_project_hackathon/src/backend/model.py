from .database import db

class Item(db.EmbeddedDocument):
    name = db.StringField(required=True)
    category = db.StringField(required=True)
    color = db.StringField()
    size = db.StringField()
    brand = db.StringField()
    price = db.FloatField()
    image_url = db.URLField()

class Wardrobe(db.Document):
    user_id = db.StringField(required=True, unique=True)
    items = db.ListField(db.EmbeddedDocumentField(Item))
    created_at = db.DateTimeField()
    updated_at = db.DateTimeField()

    meta = {
        'indexes': [
            {'fields': ['user_id'], 'unique': True}
        ]
    }