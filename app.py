from flask import Flask
app=Flask(__name__)
@app.route("/")
def wish():
    return'<p style="color:Blue">Hello Ganesha</p>'
if __name__=='__main__':
    app.run(debug=True)
