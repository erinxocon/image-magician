# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/images/args/', methods=['GET'])
def get_args():
    return "hello world!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8000)
