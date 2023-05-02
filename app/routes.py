from flask import Blueprint, jsonify, abort, make_response, request
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

def validate_crystal(crystal_id):
    ### responsible for validating crystal input, ie checks id is valid
    try:
        int_crystal_id = int(crystal_id)
    except:
        abort(make_response({"message": f"400 BAD REQUEST: Crystal id {crystal_id} is not a valid type. Must be an integer"}, 400))

    crystal = Crystal.query.get(crystal_id)
    
    if not crystal:
        abort(make_response({"message": f"404 NOT FOUND: Crystal id {crystal_id} does not exist"}, 404))
    
    return crystal

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
def handle_crystals():
    request_body = request.get_json()

    new_crystal = Crystal(
        name = request_body["name"],
        color = request_body["color"],
        powers = request_body["powers"]
    )

    db.session.add(new_crystal)
    db.session.commit()

    return make_response(f"Crystal {new_crystal.name} successfully created!", 201)

@crystal_bp.route("", methods=["GET"])

def read_all_crystals():
    crystals = Crystal.query.all() 
    crystals_response = []

    for crystal in crystals:
        crystals_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        })
        
    return jsonify(crystals_response)

@crystal_bp.route("/<crystal_id>", methods=["GET"])

def read_one_crystals(crystal_id):
    crystal = Crystal.query.get(crystal_id) 

    return {
        "id": crystal.id,
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers
        }, 200

@crystal_bp.route("/<crystal_id>", methods=["PUT"])
def update_crystal(crystal_id):
    crystal = Crystal.query.get(crystal_id) 

    request_body = request.get_json()

    crystal.name = request_body["name"]
    crystal.color = request_body["color"]
    crystal.powers = request_body["powers"]

    db.session.commit()

    return make_response(f"Crystal #{crystal.id} successfully updated", 200)

@crystal_bp.route("/<crystal_id>", methods = ['Delete'])

def delete_crystal(crystal_id):
    crystal = Crystal.query.get(crystal_id)

    db.session.delete(crystal)
    db.session.commit()

    return make_response(f"Crystal #{crystal_id} successfully deleted", 200)