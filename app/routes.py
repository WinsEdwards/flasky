from flask import Blueprint, jsonify, abort, make_response
from app import db
from app.models.crystal import Crystal

# class Crystal:
#     def __init__(self, id, name, color, powers):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.powers = powers

# ### create a list of crystals

# crystals = [
#     Crystal(1, "Amethyst", "Purple", "Cleansing, protection, intuition"),
#     Crystal(2, "Tiger's Eye", "Golden brown", "Strength, power, confidence, intelligence, daring"),
#     Crystal(3, "Rose Quartz", "Pink", "Love, compassion, partnership")]

# def validate_crystal(crystal_id):
#     ### responsible for validating crystal input, ie checks id is valid
#     try:
#         int_crystal_id = int(crystal_id)
#     except:
#         abort(make_response({"message": f"400 BAD REQUEST: Crystal id {crystal_id} is not a valid type. Must be an integer"}, 400))

#     for crystal in crystals:
#         if crystal.id == int_crystal_id:
#             return crystal
    
#     abort(make_response({"message": f"404 NOT FOUND: Crystal id {crystal_id} does not exist"}, 404))

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

# @crystal_bp.route("", methods=["GET"])

# def handle_crystals():
#     crystal_response = []
    
#     for crystal in crystals:
#         crystal_response.append({
#             "id": crystal.id,
#             "name": crystal.name,
#             "color": crystal.color,
#             "powers": crystal.powers
#         })

#     return jsonify(crystal_response)

# @crystal_bp.route("/<crystal_id>", methods=["GET"])

# def handle_crystal_ids(crystal_id):
#     crystal = validate_crystal(crystal_id)
    
#     return {
#         "id": crystal.id,
#         "name": crystal.name,
#         "color": crystal.color,
#         "powers": crystal.powers
#     }

@crystal_bp.route("", methods=['POST'])

# define a route for creating a crystal resource
def handle_crustals():
    request_bodu = request.get_json()

    new_crystal = Crystal(
        name = request_body["name"],
        color = request_body["color"],
        powers = request_body["powers"]
    )

    db.session.add(new_crystal)
    db.session.commit()

    return make_response(f"Crystal {new_crystal.name} successfully created!", 201)