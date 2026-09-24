from flask import *
app=Flask(__name__) 


@app.route("/")
def home():
    return "URL_BUILDING TASK"


@app.route("/Welcome/name")
def welcome():
    name='xyz'

    return "Welcome %s"%name

@app.route("/age/<int:num>")
def age(num):
    return "Your age is %d"%num

@app.route("/roll_no/<int:num>")
def roll_no(num):
    return "Your roll_no is %d"%num


if __name__=="__main__":
    app.run(debug=True)