from quart import Quart, request, jsonify
from .database import db
from .models import Wardrobe, Item

def create_app():
    app = Quart(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'virtual_wardrobe',
        'host': 'localhost',
        'port': 27017
    }
    db.init_app(app)

    @app.route('/wardrobe', methods=['GET'])
    async def get_wardrobe():
        user_id = request.args.get('user_id')
        wardrobe = await Wardrobe.objects(user_id=user_id).first()
        return jsonify(wardrobe.to_json()), 200

    @app.route('/wardrobe/add', methods=['POST'])
    async def add_item():
        data = await request.json
        user_id = data['user_id']
        item_data = data['item']
        wardrobe = await Wardrobe.objects(user_id=user_id).first()
        if not wardrobe:
            wardrobe = Wardrobe(user_id=user_id)
        item = Item(**item_data)
        wardrobe.items.append(item)
        await wardrobe.save()
        return jsonify({'message': 'Item added successfully'}), 201

    return app