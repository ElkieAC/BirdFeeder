# Smart Bird House
# Bird Feeder with Weather Data and Image Capture

This project involves building a bird feeder station that collects weather data and captures images of birds visiting the feeder. The captured images are then loaded onto a dashboard viewer that runs on a Raspberry Pi. The bird feeder station can be built using either two Raspberry Pi's or one Raspberry Pi and one Arduino MKR 1010.

## Hardware Required

- 1 x Raspberry Pi (or Arduino MKR 1010)
- 1 x Camera module (compatible with Raspberry Pi)
- 1 x Temperature and Humidity Sensor (DHT11 or DHT22)
- 1 x Breadboard
- 1 x Bird feeder
- 1 x Power Supply
- 1 x Micro SD Card (minimum 8GB)

## Software Required

- Python 3
- Flask
- Adafruit DHT Library
- OpenCV
- NumPy
- Matplotlib

## Installation

1. Install Raspbian or Arduino IDE on the Raspberry Pi or Arduino MKR 1010, respectively.
2. Connect the camera module to the Raspberry Pi or Arduino MKR 1010.
3. Connect the temperature and humidity sensor to the Raspberry Pi or Arduino MKR 1010 using the breadboard.
4. Clone the repository to your Raspberry Pi or Arduino MKR 1010.
5. Install the required Python libraries using the following command: 

   ```
   pip3 install flask adafruit-circuitpython-dht opencv-python numpy matplotlib
   ```

## Usage

1. Navigate to the project directory on your Raspberry Pi or Arduino MKR 1010.
2. Run the `app.py` file using the following command: 

   ```
   python3 app.py
   ```

3. Access the dashboard viewer on your web browser by entering the IP address of your Raspberry Pi or Arduino MKR 1010, followed by the port number (default port is 5000). For example, if your IP address is `192.168.0.10`, enter `192.168.0.10:5000` on your web browser.
4. Wait for birds to visit the feeder and for the camera to capture images.
5. The captured images and weather data will be displayed on the dashboard viewer.

## Credits

This project is inspired by the [Raspberry Pi Bird Box](https://www.raspberrypi.org/blog/bird-box-with-pi-noir/) and the [Arduino MKR 1010 Weather Station](https://create.arduino.cc/projecthub/Arduino_Genuino/mkr1010-wifi-weather-station-0df23b). 

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

