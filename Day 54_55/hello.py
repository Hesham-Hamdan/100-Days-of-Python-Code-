from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_function():
        return f"<b>{func()}</b>"

    return wrapper_function


@app.route("/")
@make_bold
def hello_world():
    return "hi people"


@app.route("/<name>")
def greeting(name):
    return f"Hello {name}, how are you?"


if __name__ == "__main__":
    app.run(debug=True)
