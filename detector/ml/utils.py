import joblib
import json
import os
from urllib.parse import urlparse
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "phishing_rf_model.joblib")
FEATURES_PATH = os.path.join(BASE_DIR, "feature_names.json")

model = joblib.load(MODEL_PATH)

with open(FEATURES_PATH) as f:
    feature_names = json.load(f)["feature_names"]

def extract_features_from_url(url):
    parsed = urlparse(url)
    netloc = parsed.netloc or parsed.path
    path = parsed.path or ''

    # Compute real features
    features = {
        "PrefixSuffix-": 1 if '-' in netloc else 0,
        "SubDomains": max(0, netloc.count('.') - 1),  
        "HTTPS": 0 if parsed.scheme == 'https' else 1,
        "AnchorURL": 0.2,        
        "WebsiteTraffic": 0.5,
        "LinksInScriptTags":0.05,
        "RequestURL":0.1,
        "LinksPointingToPage":0.0,
        "ServerFormHandler":0.1

    }

    return [features[name] for name in feature_names]


def predict_url(url):
    """
    Predict if a URL is Phishing or Legitimate
    """
    features_vector = [extract_features_from_url(url)]
    df = pd.DataFrame(features_vector, columns=feature_names)
    proba = model.predict_proba(df)[0] 
    percent_legit = round(proba[0] * 100, 2)
    percent_phish = round(proba[1] * 100, 2)

    # Get prediction label
    label = "Phishing" if percent_phish > percent_legit else "Legitimate"
    percentage = percent_phish if label == "Phishing" else percent_legit

    if label == "Legitimate":
        message = f"This website is {percentage}% save to visit."
    else:
        message = f"Warning! This website is {percentage}% likely to be a phishing site"
    return {
        
        "prediction": label,
        "percentage":percentage,
        "message": message
    }
