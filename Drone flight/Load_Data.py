import json

def load_path(file_path = "Flight_paths.json"):
    with open(file_path, "r") as f:
        data = json.load(f)
    primary = data["primary_mission"]
    other = data["other_drones"]
    return primary, other
