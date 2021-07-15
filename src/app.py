from flask import Flask
  
import os
import socket

app = Flask(__name__)
@app.route("/")
def hello():
    html = "<head><title>問合せフォーム</title></head><body><h3>お問い合わせフォーム</h3><form><label>e-mail</label><input ></input></br><label>本文</label><textarea row=\"4\"></textarea></form></body>"
    return html.format()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
