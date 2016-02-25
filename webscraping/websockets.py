from flask.ext.socketio import emit
 
from . import socketio
 
@socketio.on('connect', namespace='/webscraping')
def test_connect():
    pass
 
@socketio.on('disconnect', namespace='/webscraping')
def test_disconnect():
    pass