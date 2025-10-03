import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    use_mockup = True
    if use_mockup:
        with open("/home/kamil/Projects/Coursera-Developing-AI-Applications-with-Python-and-Flask/final_project/response-example.json", "r") as f:
            formatted_response = json.load(f)
    else:
        response = requests.post(url, json=myobj, headers=header)
        formatted_response = json.loads(response.text)

    print("Response from the API:", formatted_response)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    return emotions
