import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test Case: Checking if the system successfully outputs a result
        result = emotion_detector("I am so happy this is working!")
        
        # Verify that the dominant emotion calculation returned 'joy'
        self.assertEqual(result['dominant_emotion'], 'joy')
        
        # Verify that the dictionary contains all required emotion keys
        self.assertIn('anger', result)
        self.assertIn('sadness', result)

if __name__ == '__main__':
    unittest.main()