"""Emotion detection module using IBM Watson NLP mock analysis."""
from __future__ import annotations
import re
from collections import Counter
from typing import Dict

EMOTION_KEYWORDS = {
    "joy": [
        "happy",
        "joy",
        "delight",
        "pleased",
        "excited",
        "glad",
        "love",
        "smile",
        "wonderful",
        "amazing",
    ],
    "sadness": [
        "sad",
        "down",
        "unhappy",
        "sorrow",
        "blue",
        "lonely",
        "mourn",
        "cry",
        "regret",
        "depressed",
    ],
    "anger": [
        "angry",
        "mad",
        "furious",
        "annoyed",
        "frustrated",
        "hate",
        "irritated",
        "rage",
        "attack",
        "upset",
    ],
    "fear": [
        "fear",
        "scared",
        "afraid",
        "terrified",
        "nervous",
        "anxious",
        "worried",
        "panic",
        "unsafe",
        "dread",
    ],
    "disgust": [
        "disgust",
        "gross",
        "nasty",
        "sick",
        "hate",
        "repulsed",
        "revolting",
        "distaste",
        "filthy",
        "offensive",
    ],
}

DEFAULT_BASE_SCORE = 0.05


def _normalize_scores(scores: Dict[str, float]) -> Dict[str, float]:
    """Normalize emotion scores so they sum to 1.0."""
    total = sum(scores.values())
    if total <= 0:
        return {emotion: 0.0 for emotion in scores}
    return {emotion: round(value / total, 3) for emotion, value in scores.items()}


def _mock_watson_analysis(text: str) -> Dict[str, float]:
    """Mock Watson NLP emotion analysis using a keyword-driven scoring model."""
    tokens = re.findall(r"\b\w+\b", text.lower())
    counts = Counter(tokens)
    scores = {emotion: DEFAULT_BASE_SCORE for emotion in EMOTION_KEYWORDS}

    for emotion, keywords in EMOTION_KEYWORDS.items():
        for keyword in keywords:
            scores[emotion] += counts[keyword] * 0.35

    return _normalize_scores(scores)


def emotion_detector(text: str) -> Dict[str, object]:
    """Detect emotions in text and return structured output.

    Args:
        text: User-provided text to analyze.

    Returns:
        A dict containing emotion scores and the dominant emotion.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """
    if not isinstance(text, str):
        raise TypeError("Invalid input type: text must be a string.")

    cleaned_text = text.strip()
    if not cleaned_text:
        raise ValueError("Input text is required for emotion detection.")

    scores = _mock_watson_analysis(cleaned_text)
    dominant_emotion = max(scores, key=scores.get)

    return {
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "anger": scores["anger"],
        "fear": scores["fear"],
        "disgust": scores["disgust"],
        "dominant_emotion": dominant_emotion,
    }
