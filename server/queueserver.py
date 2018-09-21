from flask import Flask, request, jsonify
from queueservice import queueutil

app = Flask(__name__)

@app.route('/',methods=('get', 'post'))
def hello_world():
    return 'Hello, World!'


@app.route('/getvalues',methods=('get', 'post'))
def getqueuevalues():
    numvalues = int(request.args.get("numvals"))
    values = queueutil.getvalues(numvalues)
    return jsonify(values)

@app.route('/putvalues',methods=('get', 'post'))
def putqueuevalues():
    queueutil.populatequeue(1000)
    return jsonify({"current_size_is": queueutil.mqueue.size})



def create_app(database_uri=None, debug=False):
    global app
    app.debug = debug
    return app

if __name__ == '__main__':
    queueutil.populatequeue(1000)
    app = create_app(debug=True)
    app.run(port=5000)
