import json
FEATURES_PATH = "feature_names.json"

with open(FEATURES_PATH) as f:
    feature_names = json.load(f)["feature_names"]

print(feature_names)
print("Number of features:", len(feature_names))
