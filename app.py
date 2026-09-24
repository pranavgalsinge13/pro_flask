from flask import Flask
app=Flask(__name__)


@app.route("/")
def home():
    return "Welcome to my website!"

@app.route("/about")
def about():
    return "This is my About page"

@app.route("/contact")
def contact():
    return "Contact me here"





app.run(debug=True)