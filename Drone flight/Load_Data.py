import json

def load_path(file_path="Flight_paths.json", mission_index=0):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Load the selected primary mission
    primary = data["primary_missions"][mission_index]
    
    # Load all other drones
    others = data["other_drones"]
    
    return primary, others
