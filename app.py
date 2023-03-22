from flask import Flask, request
import requests
import sys

def print_to_stderr(*a):
	print(*a, file=sys.stderr)

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome to Sargassum Tracker</h1> <h2>POST /publish to send Sargassum Data to the server</h2>'

# Route for IOT devices to publish data to server
@app.route('/publish', methods=["POST"])
def publish():
    if (request.data):
        iotdata = request.get_json() # IOT Device will send this data randomly

        # Get weather and ocean data based on location of IOT device, store in dictionary objects
        weatherresponse = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={iotdata["lat"]}&longitude={iotdata["lon"]}&current_weather=true')
        oceanresponse = requests.get(f'https://marine-api.open-meteo.com/v1/marine?latitude={iotdata["lat"]}&longitude={iotdata["lon"]}&timezone=auto&daily=wave_height_max,wave_direction_dominant')
        weatherdict = weatherresponse.json()
        oceandict = oceanresponse.json()

        # Open Log File, Write to Log File, Close Log File
        f = open("logs.txt", "a")
        new_log = '[' + str(request.json) + ", " + str(weatherdict.get('current_weather')) + ", " + f'{{"waveheight": {oceandict["daily"]["wave_height_max"][0]}, ' + f'"wavedirection": {oceandict["daily"]["wave_direction_dominant"][0]}' + "}"+ ']' + "\n"
        f.write(new_log)
        print_to_stderr(new_log)
        f.close()

        return "Successful Request"
    else:
        return 'Empty Request'

if __name__ == "__main__":
    app.run(debug=True)