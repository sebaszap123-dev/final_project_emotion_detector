"""Module for serve a web application for AI analysis of sentiments with Watson AI."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    """Index HTML page for run the sentiment analysis in web."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """API Route for get analysis for sentiments with Watson AI."""

    text_to_analyze = request.args.get("textToAnalyze", "")
    print(text_to_analyze)
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    emotions = emotion_detector(text_to_analyze)

    return jsonify(emotions)


if __name__ == "__main__":
    app.run(debug=True)
