from flask import Flask
  
import os
import socket

app = Flask(__name__)
@app.route("/")
def hello():
    html = "<head><meta charset=\"UTF-8\"><title>問合せフォーム</title><meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\"><link rel=\"stylesheet\" href=\"style.css\"></head><body><div class=\"container\"><h3>お問い合わせフォーム</h3><form><label class=\"label\" for=\"e-mail\">e-mail</label><input ></input></br><label class=\"label\" for=\"message\">本文</label><textarea row=\"4\"></textarea><button id=\"btn_submit\">送信する</button></form></div></body>"
    return html.format()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
