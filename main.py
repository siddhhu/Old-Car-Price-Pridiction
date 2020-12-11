from flask import Flask,render_template,request
import pickle
with open("model.pkl","rb") as f:
    mdl=pickle.load(f)
 
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        km_driven=int(request.form["km_driven"])
        year_old=int(request.form["year_old"])
        fuel=int(request.form["fuel"])
        seller_type=int(request.form["seller_type"])
        trans=int(request.form["trans"])
        owner=int(request.form["owner"])
        list1=[km_driven,fuel,seller_type,trans,owner,year_old]
        result=mdl.predict([list1])
        print(result)
        return render_template("older.html",res=result)  
    return render_template("newer.html")
    
if __name__ == "__main__":
    app.run(debug=True)

