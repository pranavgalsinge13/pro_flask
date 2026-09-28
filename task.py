from flask import *
app=Flask(__name__)

@app.route("/")
def Home():
    return redirect(url_for("login"))

@app.route("/login/val")
def Login(val):
    if val=="stu_dash":
         return redirect(url_for("stu_dash"))
    elif val=="hr_dash":
        return redirect(url_for("hr_dash"))
    else:
        return "Page Not Found"

@app.route("/stu_dash")
def stu_dash():
    return "This is student Dashboard"

@app.route("/hr_dash")
def hr_dash():
    return "This is hr Dashboard"


if __name__=="__main__":
    app.run(debug=True)