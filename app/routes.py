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