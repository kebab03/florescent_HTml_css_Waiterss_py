from flask import Flask,render_template,request
from waitress import serve
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="GET":
        return render_template("indexP.html")
    if request.method=="POST":
        return render_template("greet.html",name = request.form.get("name","world"))

#        "TODO"
if __name__ == '__main__':
    serve(app, host='0.0.0.0',port=80,threads=2)



