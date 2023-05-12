from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import io
import time
import picamera

# Replace with your subscription key and endpoint
subscription_key = "ea47d9ba135d4c018484bb0f3ff17439"
endpoint = "https://birdfeeder-nscc.cognitiveservices.azure.com/"

# Authenticate with the Computer Vision API
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)

# Create a stream to capture photos
stream = io.BytesIO()

# Capture a photo from the camera module and save it to the stream
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format="jpeg")
    camera.stop_preview()

# Reset the stream pointer to the beginning
stream.seek(0)

# Save the photo to a local file
with open("object.jpg", "wb") as file:
    file.write(stream.getbuffer())

# Call the Computer Vision API to analyze the photo
features = [VisualFeatureTypes.objects]
results = client.analyze_image_in_stream(stream, features)

# Print the detected objects and their locations in the photo
for obj in results.objects:
    print(f"Object: {obj.object_property}")
    print(f"Location: ({obj.rectangle.x},{obj.rectangle.y})-({obj.rectangle.x + obj.rectangle.w},{obj.rectangle.y + obj.rectangle.h})")
