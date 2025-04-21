import json

def get_json_structure(data):
    if isinstance(data, dict):
        return {k: get_json_structure(v) for k, v in data.items()}
    elif isinstance(data, list) and data:
        return [get_json_structure(data[0])]
    else:
        return type(data).__name__

# Step 1: Load your JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Step 2: Get the structure
structure = get_json_structure(data)

# Step 3: Print it nicely
print(json.dumps(structure, indent=2))
