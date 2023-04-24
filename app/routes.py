from flask import Blueprint, jsonify

class Crystal:
    def __init__(self, id, name, color, powers):
        self.id = id
        self.name = name
        self.color = color
        self.powers = powers

### create a list of crystals

crystals = [
    Crystal(1, "Amethyst", "Purple", "Cleansing, protection, intuition"),
    Crystal(2, "Tiger's Eye", "Golden brown", "Strength, power, confidence, intelligence, daring"),
    Crystal(3, "Rose Quartz", "Pink", "Love, compassion, partnership")]

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

@crystal_bp.route("", methods=["GET"])

def handle_crystals():
    crystal_response = []
    
    for crystal in crystals:
        crystal_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        })

    return jsonify(crystal_response)

@crystal_bp.route("/<crystal_id>", methods=["GET"])

def handle_crystal_ids(crystal_id):
    for crystal in crystals:
        if crystal.id == int(crystal_id):
            return {
                "id": crystal.id,
                "name": crystal.name,
                "color": crystal.color,
                "powers": crystal.powers
            }