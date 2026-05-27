import json

def emotion_detector(text_to_analyze):
    # Task 7: Handle blank or empty input errors
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # --- TEMPORARY MOCK FOR LOCAL TESTING ---
    # Since we are local, we create a fake response object with perfect Python spacing
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.text = json.dumps({
                "emotionPredictions": [{
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.002,
                        "fear": 0.004,
                        "joy": 0.85,
                        "sadness": 0.02
                    }
                }]
            })
            
    response = MockResponse()
    # ----------------------------------------
    
    # Task 7: Handle system error response (Status Code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # Task 3: Format the successful response text into a Python dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the dictionary of emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Find the emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Add the dominant emotion key/value to our dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions