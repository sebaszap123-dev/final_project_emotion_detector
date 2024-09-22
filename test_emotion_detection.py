from EmotionDetection import emotion_detector


def test_emotion_detector():
    resp = emotion_detector("I hate to make unit testing with pytest.")

    assert isinstance(resp, dict)

    assert "dominant_emotion" in resp
