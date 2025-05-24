from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def wish():
    return '<p style="color:Blue">Hello Ganesha</p>'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
