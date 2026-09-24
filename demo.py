from flask import *
app=Flask(__name__)  #demo.py run

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def services():
    return render_template("service.html")



if __name__=="__main__":
    app.run(debug=True)