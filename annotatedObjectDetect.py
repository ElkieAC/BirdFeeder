from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import io
import time
import picamera
from PIL import Image, ImageDraw, ImageFont

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

# Load the image with Pillow
image = Image.open("object.jpg")

# Add text annotations to the image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/arial.ttf", size=16)


for obj in results.objects:
    # Get the object name and location
    object_name = obj.object_property
    object_location = (obj.rectangle.x, obj.rectangle.y, obj.rectangle.x + obj.rectangle.w, obj.rectangle.y + obj.rectangle.h)

    # Draw a rectangle around the object
    draw.rectangle(object_location, outline="red", width=2)

    # Add the object name as a label
    draw.text((obj.rectangle.x + 5, obj.rectangle.y - 20), object_name, font=font, fill="red")

# Save the annotated image with a new name
image.save("annotated_object.jpg")

# Print the detected objects and their locations in the photo
for obj in results.objects:
    print(f"\nObject: {obj.object_property}")
    print(f"Location: ({obj.rectangle.x},{obj.rectangle.y})-({obj.rectangle.x + obj.rectangle.w},{obj.rectangle.y + obj.rectangle.h})")

# Show the annotated image
image.show()

