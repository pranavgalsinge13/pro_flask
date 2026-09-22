from flask import *
app=Flask(__name__)  #demo.py run

@app.route("/")
def home():
    return "Hello Flsk"


@app.route("/about")
def about():
    return "<h1> This is about page </h1>"



if __name__=="__main__":
    app.run(debug=True,port=4000)