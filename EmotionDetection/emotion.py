import requests


def emotion_detector(text_to_analyze: str):
    json_payload = {"raw_document": {"text": text_to_analyze}}
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send the POST request
    resp = requests.post(url, json=json_payload, headers=headers)
    # Check if the response was successful
    if resp.status_code == 200:
        # Use .json() to get the response body as a dictionary
        json = resp.json()
        emotions = json["emotionPredictions"][0]["emotion"]
        return _find_dominant_emotion(emotions)
    else:
        # Print the error details if request failed
        print(f"Error: {resp.status_code} - {resp.text}")
        return None


def _find_dominant_emotion(emotions: dict):
    """Find the dominant emotion into the dictionary of emotions without and threshold."""
    dominant_emotion = max(emotions, key=emotions.get)

    # Add the dominant emotion to the dictionary
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
