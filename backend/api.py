import time
from flask import Flask

app = Flask(__name__)

# Blah-blah
@app.route('api/time')
def get_current_time():
    return {'time': time.time()}