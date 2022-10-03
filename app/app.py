import time
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    # ts stores the time in seconds
    ts = time.time()
    # print the current timestamp
    print(ts)
    return str(ts)
