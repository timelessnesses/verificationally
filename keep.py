import flask
import threading
app = flask.Flask('a')

@app.route('/')
def a():
    return "a"

def run():
    app.run('0.0.0.0')

def a():
    threading.Thread(target=run).start()