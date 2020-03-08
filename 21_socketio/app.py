import os, flask, flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

# ...

@socketio.on('connect')
def on_connect():
    socketio.emit("hello to client", {
        'message': "Hey there!"
    })
    
@socketio.on('new message')
def on_new_message(data):
    socketio.emit('got your message', {
        'your message': data['my message']
    })


if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
