from flask import Flask, request,render_template
from pymongo import MongoClient
import subprocess as sp

app=Flask("myiiec")

@app.route('/webapp')
def myform():
    return render_template("basic.html")
    


@app.route('/database',methods=['GET'])
def mydata():
    if request.method=='GET':
       data=request.args.get("x")
       output = sp.getoutput(data + "| jc -p --"+data)    
       cmd=[ { data : output }  ]
       client= MongoClient("mongodb://127.0.0.1:27017")
       client['linux']['command'].insert(cmd)
       return output


app.run(host="0.0.0.0", port=5555, debug=True)
