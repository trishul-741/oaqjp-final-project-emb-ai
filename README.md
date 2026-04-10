# Final Project

## Description
Emotion Detector is a production-ready Python web application that performs emotion analysis on user text using a mocked IBM Watson NLP workflow. The app detects five core emotions: joy, sadness, anger, fear, and disgust, and returns both weighted scores and a dominant emotion.

## Features
- Mocked IBM Watson NLP emotion detection
- Structured JSON output with emotion scores
- Flask-based web application with a clean HTML interface
- Error handling for empty and invalid input
- Unit tests with `unittest`
- Static code analysis with `pylint`

## Project Structure
```
EmotionDetector/
│── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
│── static/
│   ├── style.css
│── templates/
│   ├── index.html
│── test_emotion_detection.py
│── server.py
│── requirements.txt
│── README.md
```

## Setup Instructions
1. Clone or download the repository.
2. Change into the project directory:
   ```bash
   cd EmotionDetector
   ```
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage Instructions
- Start the Flask app:
  ```bash
  python server.py
  ```
- Open your browser and visit:
  ```
  http://127.0.0.1:5000/
  ```
- Enter text and submit to view detected emotions.

## API Endpoint
- `GET /emotionDetector?text=YOUR_TEXT`
- Example:
  ```bash
  curl "http://127.0.0.1:5000/emotionDetector?text=I+feel+happy"
  ```

## Testing
Run the unit tests with:
```bash
python test_emotion_detection.py
```

## Static Analysis
Check code quality:
```bash
pylint server.py
```

## Screenshots
- `6b_deployment_test.png` - deployment test interface placeholder
- `7c_error_handling_interface.png` - error handling UI placeholder

## Notes
- The current emotion detection uses a keyword-based mock implementation to emulate IBM Watson NLP.
- Replace the mock implementation with the real Watson NLP SDK when an API key is available.
