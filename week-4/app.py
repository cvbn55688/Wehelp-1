from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session


app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key="test"

@app.route("/") #首頁
def index():
    session["isLogin"] = False
    return render_template("index.html")

@app.route("/signin", methods=["POST"]) #驗證帳密
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        session["isLogin"] = True #設定為已登入
        return redirect ("/member")
    elif account == "" or password == "":
        return redirect ("/error?message=請輸入帳號、密碼")
    else:
        return redirect ("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member") #會員頁
def member():
    if session["isLogin"] == True: #判斷是否已登入
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error") #錯誤頁
def error():
    errorMes = request.args.get("message", "")
    return render_template("error.html", errorMes = errorMes) #回傳error訊息

@app.route("/signout") #登出
def signout():
    session["isLogin"] = False #設定為未登入
    return redirect("/")

@app.route("/calculate")
def calculate():
    num = request.args.get("number")
    return redirect("/square/"+num)

@app.route("/square/<num>")
def square(num):
    num = int(num)**2
    return render_template("square.html", ans = num)

app.run(port = 3000, debug = True)
