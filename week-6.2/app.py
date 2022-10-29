import os
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import flash
import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error
import time



connection_pool = pooling.MySQLConnectionPool(
                                            host = 'localhost',
                                            port= "3306",
                                            user = 'root',
                                            password = 'password',
                                            database = 'website_HW',
                                            pool_name="my_pool",
                                            pool_size = 5
                                            )



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

    try:
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        sql = 'select * from member where username= %s;'
        cursor.execute(sql, (username,))
        records = cursor.fetchall()

        if records == []:
            sql = 'insert member(name, username, password) values(%s, %s, %s);'
            cursor.execute(sql, (name, username, password))
            mes = "已成功註冊帳號"
            flash(mes)
            return redirect("/")
        else:
            return redirect ("/error?message=帳號已經被註冊")

    except Error as e:
        print(e)

    finally:
            cursor.close()
            connection.commit()
            connection.close()


#驗證帳密
@app.route("/signin", methods=["POST"]) 
def signin():
    account = request.form["account"] #username
    password = request.form["password"]

    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = 'select * from member where username = %s and password = %s ;'
    cursor.execute(sql, (account, password))
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
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        print(connection.connection_id)
        cursor.execute(f'select member.name, content, time, member.headIMG from message inner join member on member.id = message.userid order by time ASC;')
        records1 = cursor.fetchall()
        cursor.execute(f'select headIMG from member where id = "{session["userid"]}";')
        records2 = cursor.fetchall()[0][0]
        cursor.close()
        connection.close()
        return render_template("member.html", data = records1, username = session["name"], img_name = records2)
    else:
        mes = "您尚未登入，請登入系統"
        flash(mes)
        return redirect("/")

#留言系統
@app.route("/message", methods=["POST"])
def message():
    content = request.form["content"]
    
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = 'insert message(userid, content) values(%s, %s);'
    cursor.execute(sql, (session["userid"], content))
    cursor.close()
    connection.commit()
    connection.close()
    return redirect("/member")

#會員專頁
@app.route("/userPage")
def userPage():
    loginSession = session.get("userid")
    if loginSession != None: #判斷是否已登入
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        sql = ('select headIMG from member where id = %s;')
        cursor.execute(sql, (session["userid"],))
        img_name = cursor.fetchall()[0][0]
        cursor.close()
        connection.close()
        return render_template("userPage.html", name = session["name"], img_name = img_name)
    else:
        mes = "您尚未登入，請登入系統"
        flash(mes)
        return redirect("/")

#上傳圖片
@app.route("/upload", methods = ["POST"])
def upload():
    img = request.files.get("userIMG")
    suffix = "." + img.filename.split(".")[-1] #留下副檔名
    imgName = str(time.time()) + suffix #可保證每個名子都不一樣
    baseDir = os.path.abspath(os.path.dirname(__file__))
    photoDir = "/static/uploads/" + imgName
    img_path = baseDir + photoDir
    img.save(img_path) #把圖片存在本地磁碟
    print(imgName)

    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    sql = 'update member set headIMG = %s where id = %s;' #在mySQL存入圖片檔名
    cursor.execute(sql, (imgName, session["userid"]),)
    cursor.close()
    connection.commit()
    connection.close()
    return redirect("/userPage")

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
