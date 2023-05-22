import logging
from flask import Flask, request
from generator import generator
from consumer import consumer

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "my-next-game api"

@app.route('/generate')
def gen():
    return generator.generate()

@app.route('/consume/<dataType>',methods=['POST'])
def consume(dataType):
    if request.method == "POST":
        data = request.get_json()
        return consumer.consumeData(dataType,data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')