from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import flash
import mysql.connector


def connectDB():
    connection = mysql.connector.connect(host = 'localhost',
                                        port= "3306",
                                        user = 'root',
                                        password = 'password',
                                        database = 'website_HW')
    return connection


app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)


app.secret_key="test"

#首頁
@app.route("/") 
def index():
    loginSession = session.get("userid")
    if loginSession != None:
        mes = "您已登入，若要登出請按'登出系統"
        flash(mes)
        return redirect ("/member")
    else:
        return render_template("index.html")

#註冊帳號
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    connection = connectDB()
    cursor = connection.cursor()
    cursor.execute(f'select * from member where username="{username}";')
    records = cursor.fetchall()

    if records == []:
        cursor.execute(f'insert member(name, username, password) values("{name}", "{username}", "{password}");')
        cursor.close()
        connection.commit()
        connection.close()
        mes = "已成功註冊帳號"
        flash(mes)
        return redirect("/")
    else:
        cursor.close()
        connection.commit()
        connection.close()
        return redirect ("/error?message=帳號已經被註冊")

#驗證帳密
@app.route("/signin", methods=["POST"]) 
def signin():
    account = request.form["account"] #username
    password = request.form["password"]

    connection = connectDB()
    cursor = connection.cursor()
    cursor.execute(f'select * from member where username="{account}" and password = "{password}";')
    records = cursor.fetchall()
    cursor.close()
    connection.close()

    if account == "" or password == "":
        return redirect ("/error?message=請輸入帳號、密碼")
    elif records == []: #沒東西代表輸入有誤
        return redirect ("/error?message=帳號或密碼輸入錯誤")
    else:
        useridDB = records[0][0]
        nameDB = records[0][1]
        accountDB = records[0][2]
        session["userid"] = useridDB
        session["name"] = nameDB
        return redirect ("/member")            


#會員頁
@app.route("/member") 
def member():
    loginSession = session.get("userid")
    if loginSession != None: #判斷是否已登入
        connection = connectDB()
        cursor = connection.cursor()
        cursor.execute(f'select member.name, content from message inner join member on member.id = message.userid;')
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template("member.html", data = records, username = session["name"])
    else:
        mes = "您尚未登入，請登入系統"
        flash(mes)
        return redirect("/")

#留言系統
@app.route("/message", methods=["POST"])
def message():
    content = request.form["content"]
    
    connection = connectDB()
    cursor = connection.cursor()
    cursor.execute(f'insert message(userid, content) values({session["userid"]}, "{content}");')
    cursor.close()
    connection.commit()
    connection.close()
    return redirect("/member")


#錯誤頁
@app.route("/error") 
def error():
    errorMes = request.args.get("message", "")
    return render_template("error.html", errorMes = errorMes) #回傳error訊息

#登出
@app.route("/signout")
def signout():
    session.clear() #清空session狀態
    return redirect("/")


# @app.route("/square/<num>")
# def square(num):
#     num = int(num)**2
#     return render_template("square.html", ans = num)


app.run(port = 3000, debug = True)
