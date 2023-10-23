from flask import Flask,request

app=Flask(__name__)

@app.before_request
def a():
    print(request.headers)

@app.route('/',methods=['GET','POST'])
def index():
    return ''


app.run()