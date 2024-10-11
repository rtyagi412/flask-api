from flask import Flask, jsonify, request

app= Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "welcome to my flask API!"})

@app.route('/data', methods=['GET'])
def get_data():
    sample_data={
        "id":1,
        "name": "Flask API example",
        "description": "Sample end point only"
    }

    return jsonify(sample_data)

@app.route('/data',methods=['POST'])
def post_data():
    data=request.get_json();
    response={
        "message": "Data Received!",
        "data": data
    }

    return jsonify(response), 201

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
