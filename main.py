from flask import Flask, render_template
from flask_socketio import socketio, send, SocketIO

app = Flask(__name__)
app.config["SECRET"] = "secret!123"
socketIo = SocketIO(app, cors_allowed_origins="*")


@socketIo.on('message')
def handle_message(message):
    print("Resived message: " + message)
    if message != "User Conected!":
        send(message, broadcast=True)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketIo.run(app, host="ip del pc")
