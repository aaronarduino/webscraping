from flask import Flask
from flask.ext.socketio import SocketIO

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

app = CustomFlask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

socketio = SocketIO(app)

from . import views
from . import websockets