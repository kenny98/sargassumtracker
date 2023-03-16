from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome to Sargassum Tracker</h1>'

# Route for IOT devices to publish data to server
@app.route('/publish', methods=["POST"])
def publish():
    if (request.data):
        f = open("logs.txt", "a")
        f.write(str(request.json) + "\n")
        f.close()
        return 'Successful Request'
    else:
        return 'Empty Request'

if __name__ == "__main__":
    app.run(debug=True)