"""Flask server for the Emotion Detector AI web application."""
from __future__ import annotations
from flask import Flask, jsonify, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/", methods=["GET"])
def index() -> str:
    """Render the homepage with the emotion detector form."""
    return render_template("index.html", result=None, error=None, input_text="")


def _build_response(result: dict, status_code: int = 200):
    """Return a JSON response object."""
    return jsonify(result), status_code


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Analyze input text and return emotion detection output."""
    if request.method == "POST":
        user_text = request.form.get("text_input", "")
    else:
        user_text = request.args.get("text", "")

    try:
        result = emotion_detector(user_text)
    except ValueError as error:
        error_message = str(error)
        error_payload = {"error": error_message}
        if request.method == "GET" and request.args.get("text") is not None:
            return _build_response(error_payload, 400)
        return (
            render_template(
                "index.html",
                result=None,
                error=error_message,
                input_text=user_text,
            ),
            400,
        )
    except TypeError:
        error_payload = {"error": "Invalid input type."}
        if request.method == "GET" and request.args.get("text") is not None:
            return _build_response(error_payload, 400)
        return (
            render_template(
                "index.html",
                result=None,
                error=error_payload["error"],
                input_text=user_text,
            ),
            400,
        )

    if request.method == "GET" and request.args.get("text") is not None:
        return _build_response(result)

    return render_template("index.html", result=result, error=None, input_text=user_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
