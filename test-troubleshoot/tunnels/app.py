from flask import Flask, json, jsonify

# init a flask web app
app = Flask(__name__)

# a basic route
@app.route('/', methods=['GET'])
def get_message():
    message = json.loads('{"message": "Got it!"}')
    return jsonify(message)

@app.route('/message', methods=['POST'])
def recv_message():
    message = json.loads('{"message": "Received the POST"}')
    return jsonify(message)

if __name__ == '__main__':
    # run app
    app.run(port=5000, debug=False)

