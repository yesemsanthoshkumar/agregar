"""Swen chatbot"""

from flask import Flask, jsonify, request

from processing.message import reply

APP = Flask('SWEN')

@APP.route('/')
def home():
    """Homepage"""
    return jsonify({
        "status": "success"
    })

@APP.route('/chat', methods=['POST'])
def input_message():
    """Receives input message and sends response message"""
    response_msg = reply(request.json)
    return jsonify(response_msg)

if __name__ == '__main__':
    APP.run(
        '127.0.0.1',
        5234,
        debug=False
    )
