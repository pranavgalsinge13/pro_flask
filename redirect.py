from flask import *
app=Flask(__name__) 


@app.route("/")
def home():
    return "Redirect Task"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/service")
def service():
    return redirect (url_for("about"))




if __name__=="__main__":
    app.run(debug=True)