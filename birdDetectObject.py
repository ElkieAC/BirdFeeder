from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import io
import time
import picamera

# Replace with your subscription key and endpoint
subscription_key = "ea47d9ba135d4c018484bb0f3ff17439"
endpoint = "https://birdfeeder-nscc.cognitiveservices.azure.com/"

# Set the threshold for the percentage of image occupied by the bird
threshold = 50

# Authenticate with the Computer Vision API
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)

# Create a stream to capture photos
stream = io.BytesIO()

# Capture a photo from the camera module and save it to the stream
with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.rotation = 180
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

# Check if the photo contains a bird that occupies over threshold% of the total image size
for obj in results.objects:
    if obj.object_property.lower() == 'bird':
        image_width, image_height = results.metadata.width, results.metadata.height
        bird_area = obj.rectangle.w * obj.rectangle.h
        image_area = image_width * image_height
        bird_percentage = (bird_area / image_area) * 100
        if bird_percentage > threshold:
            # Transmit the photo to your dashboard
            print("Transmitting photo to dashboard...")
        else:
            print(f"Bird detected but does not occupy more than {threshold}% of image")
        break # stop looking for objects once a bird is found
else:
    print("No birds detected in image")
