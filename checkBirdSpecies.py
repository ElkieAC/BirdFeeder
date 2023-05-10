from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

import os

# Get path to images folder
dirname = os.path.dirname(__file__)
images_folder = os.path.join(dirname, 'img')

# Create variables for your project
publish_iteration_name = "Iteration1"
project_id = "cd101e31-24b1-412e-9d00-558fd525e44f"

# Create variables for your prediction resource
prediction_key = "e3ee0751443c43d9888408b9d6ee5fcd"
endpoint = "https://birdfeedernscc-prediction.cognitiveservices.azure.com/"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)

# Open an image and make a prediction
with open(os.path.join(images_folder, "blueJay.jpg"), "rb") as image_contents:
    results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())

# Display the results
for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability * 100 :.2f}%")
