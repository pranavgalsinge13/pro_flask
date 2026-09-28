from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return "Web Templating System Task "

@app.route("/test1")
def test1():
    name="Python Framework"

    return render_template("test1.html",s_name=name)

@app.route("/test2")
def test2():
    num=12

    return render_template("test2.html",n=num)

@app.route("/test3")
def test3():
    stu_list=["ram","Rohan","Pranav","Tanmay"]

    return render_template("test3.html",stu_list=stu_list)

@app.route("/test4")
def test4():
    stu_dict={1:"xyz",2:"abc",3:"pqr",4:"efg",5:"mno"}

    return render_template("test4.html",stu_dict=stu_dict)

if __name__=="__main__":
    app.run(debug=True,port=1000)