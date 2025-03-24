from flask import Flask

app = Flask(__name__)


# Define a route that responds to the root URL ("/") and returns a string
@app.route("/")
def hello():
    return "Hello from Alex!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)