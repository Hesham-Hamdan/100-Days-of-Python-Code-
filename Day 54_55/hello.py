from flask import Flask

app = Flask(__name__)


def hello_world():
    return "hi people"


@app.route("/<name>")
def greeting(name):
    return f"Hello {name}, how are you?"


if __name__ == "__main__":
    app.run(debug=True)
