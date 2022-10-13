from distutils.log import info
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import make_response
from flask import flash

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key="test"

@app.route("/") #首頁
def index():
    loginCookie = request.cookies.get("isLogin")
    if loginCookie == "True": #判斷是否已登入，如果已登入就自動跳轉到member
        flash("您已登入，若要登出請按'登出系統'")
        return redirect ("/member")
    else:
        return render_template("index.html")
    

@app.route("/signin", methods=["POST"]) #驗證帳密
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        resp = make_response(redirect ("/member"))
        resp.set_cookie(key="isLogin", value="True") #設定cookie
        return resp
    elif account == "" or password == "":
        return redirect ("/error?message=請輸入帳號、密碼")
    else:
        return redirect ("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member") #會員頁
def member():
    loginCookie = request.cookies.get("isLogin")
    if loginCookie == "True": #判斷是否已登入
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error") #錯誤頁
def error():
    errorMes = request.args.get("message", "")
    return render_template("error.html", errorMes = errorMes) #回傳error訊息

@app.route("/signout") #登出
def signout():
    resp = make_response(redirect ("/")) #清除cookie的登入狀態
    resp.set_cookie(key="isLogin", value="", expires=0) #把時限設定為0就可以把cookie刪掉
    return resp

@app.route("/square/<num>")
def square(num):
    num = int(num)**2
    return render_template("square.html", ans = num)

app.run(port = 3000, debug = True)
