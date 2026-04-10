"""Unit tests for the Emotion Detection module."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class EmotionDetectionTests(unittest.TestCase):
    def test_valid_input_returns_scores(self):
        payload = "I am happy and excited but a little nervous."
        result = emotion_detector(payload)

        self.assertIsInstance(result, dict)
        self.assertIn("joy", result)
        self.assertIn("sadness", result)
        self.assertIn("anger", result)
        self.assertIn("fear", result)
        self.assertIn("disgust", result)
        self.assertIn("dominant_emotion", result)
        self.assertAlmostEqual(
            result["joy"] + result["sadness"] + result["anger"] + result["fear"] + result["disgust"],
            1.0,
            delta=0.01,
        )
        self.assertIsInstance(result["dominant_emotion"], str)

    def test_empty_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            emotion_detector("   \n\t")

    def test_invalid_input_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            emotion_detector(100)

    def test_edge_case_punctuation_and_caps(self):
        payload = "Happy! scared? Angry... disgusted, sad"
        result = emotion_detector(payload)

        self.assertEqual(len(result), 6)
        self.assertTrue(0.0 <= result["joy"] <= 1.0)
        self.assertTrue(0.0 <= result["fear"] <= 1.0)
        self.assertIn(result["dominant_emotion"], ["joy", "sadness", "anger", "fear", "disgust"])


if __name__ == "__main__":
    unittest.main()
