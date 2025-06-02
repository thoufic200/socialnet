from flask import Flask, render_template, flash, request, session, send_file
from flask import render_template, redirect, url_for, request
import datetime
import mysql.connector

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/Post")
def Post():
    return render_template('Post.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM register ")
            data = cur.fetchall()
            return render_template('AdminHome.html', data=data)

        else:
            return render_template('AdminLogin.html', error=error)


@app.route("/AdminHome", methods=['GET', 'POST'])
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/CommentInfo", methods=['GET', 'POST'])
def CommentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb ")
    data = cur.fetchall()
    return render_template('CommentInfo.html', data=data)


@app.route("/UploadInfo", methods=['GET', 'POST'])
def UploadInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT distinct UserName, ImageInfo,Image	 FROM sharetb ")
    data = cur.fetchall()
    return render_template('UploadInfo.html', data=data)


@app.route("/WordTraining", methods=['GET', 'POST'])
def WordTraining():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM negtb ")
    data = cur.fetchall()
    return render_template('WordTraining.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    error = None
    if request.method == 'POST':
        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        address = request.form['address']
        email = request.form['email']
        pnumber = request.form['phone']

        uname = request.form['name']
        password = request.form['psw']
        file = request.files['file']
        file.save("static/uploads/" + file.filename)

        mydb = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        cursor = mydb.cursor()
        mycursor = mydb.cursor()

        mycursor.execute("select max(id) from register")

        myresult = mycursor.fetchall()

        for x in myresult:
            y = x[0]
            break
        if y == None:
            print("No such charater available in string")
            x1 = 1
        else:
            y1 = y
            x1 = int(y1) + 1
            print(x1)
        cursor.execute(
            "INSERT INTO register VALUES ('" + str(
                x1) + "','" + name1 + "','" + gender1 + "','" + Age + "','" + address + "','" + email + "','" + pnumber + "','" + uname + "','" + password + "','" + file.filename + "','Active')")

        mycursor1 = mydb.cursor()
        mycursor1.execute("select * from register where id!='" + str(x1) + "' and Status='Active' ")
        myresult1 = mycursor1.fetchall()
        for z in myresult1:
            frid = z[0]
            fname = z[7]
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "insert into frlist(id,uname,frname,status)values('','" + name1 + "','" + str(fname) + "','0')")
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "insert into frlist(id,uname,frname,status)values('','" + str(fname) + "','" + name1 + "','0')")

        mydb.commit()
        mydb.close()

        return render_template('UserLogin.html', data=myresult1, data1=myresult)


@app.route("/neword", methods=['GET', 'POST'])
def neword():
    error = None
    if request.method == 'POST':
        nword = request.form['nword']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        mycursor = conn.cursor()
        mycursor.execute(
            "insert into negtb values('','" + nword + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * 	 FROM negtb ")
        data = cur.fetchall()

        return render_template('WordTraining.html', data=data)


@app.route("/delete", methods=['GET'])
def delete():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    cursor = conn.cursor()
    cursor.execute("delete from  negtb  where id='" + id + "'  ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    cur = conn.cursor()
    cur.execute("SELECT * FROM negtb ")
    data = cur.fetchall()

    return render_template('WordTraining.html', data=data)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['uname']
        session['uname'] = request.form['uname']
        password = request.form['password']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * from register where uname='" + username + "' and password='" + password + "' ")
        data = cursor.fetchone()

        if data is None:
            return 'Username or Password is wrong'
        else:

            if data[10] == 'Blocked':
                return 'Your Id Is Blocked..!'
            else:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
                # cursor = conn.cursor()
                cur = conn.cursor()
                cur.execute("SELECT * FROM register where uname='" + username + "' and Password='" + password + "'")
                data = cur.fetchall()

                return render_template('UserHome.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register  where uname='" + uname + "'  ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)


@app.route("/Friend")
def Friend():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM frlist  where uname='" + uname + "' and status='0' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM frlist  where frname='" + uname + "' and Status='waiting' ")
    data2 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()

    cur.execute("SELECT * FROM frlist  where uname='" + uname + "'   and Status='Accept'  ")
    data3 = cur.fetchall()

    return render_template('Friend.html', data1=data1, data2=data2, data3=data3)


def Friend1():
    rdata = ''
    adata = ''
    fdata = ''
    data24 = ''

    n = session['uname']
    my_list = []

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    cursor = conn.cursor()
    cursor.execute("SELECT * from register where uname='" + n + "' and Status='Active' ")
    data = cursor.fetchall()
    for x in data:
        uid = x[0]
        print(uid)
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
    mycursor = mydb.cursor()

    mycursor.execute("select * from frlist where id='" + str(uid) + "' && status='0'")
    data1 = mycursor.fetchall()
    for x1 in data1:
        frid = str(x1[3])
        print(frid)
        mycursor1 = mydb.cursor()

        mycursor1.execute("select * from register where id='" + str(frid) + "' and Status='Active'")
        data2 = mycursor1.fetchall()

        for f in data2:
            print(f[9])
            fs = str(f[9])

            my_list.append(f[9])
            print(my_list)

    mycursor.execute("select * from frlist where frid='" + str(uid) + "' && status='1'")
    data12 = mycursor.fetchone()
    if data12 is None:
        print('no accept')
        # return render_template('accept.html')
        data22 = ''
    else:
        aList = []
        mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor1 = mydb1.cursor()

        mycursor1.execute("select * from frlist where frid='" + str(uid) + "' && status='1'")
        data21 = mycursor1.fetchall()
        for x1 in data21:
            frid = str(x1[0])
            print(frid)
            mycursor11 = mydb1.cursor()

            mycursor11.execute(
                "SELECT register.id, register.uname, register.image FROM register INNER JOIN frlist ON register.id=frlist.id WHERE (frlist.frid ='" + str(
                    uid) + "' && frlist.status='1')  && register.id!='" + str(uid) + "'")
            data22 = mycursor11.fetchall()
            for v in data22:
                print(v[1])
                aList.append(v[1])

        print("Updated List : ", aList)
        d = aList
        print(d)

    mycursor1.execute("select * from frlist where name='" + str(n) + "' && status='2'")
    data23 = mycursor1.fetchone()
    if data23 is None:
        print('no frlist')
        data25 = ''
        # return render_template('frlist.html')
    else:
        aList = []

        mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor1 = mydb1.cursor()

        mycursor1.execute("select * from frlist where name='" + str(n) + "' && status='2'")
        data24 = mycursor1.fetchall()
        for x1 in data24:
            frid = str(x1[0])
            print(frid)
            mycursor11 = mydb1.cursor()

            mycursor11.execute("select * from register where id='" + frid + "'")
            data25 = mycursor11.fetchall()
            for v in data25:
                print(v[9])
                aList.append(v[1])

        print("Updated List : ", aList)
        d = aList
        print(d)

    return render_template('Friend.html', data=data1, data1=data22, data2=data24)


@app.route("/list1", methods=['GET'])
def list1():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    cursor = conn.cursor()
    cursor.execute("update frlist set Status='waiting' where id='" + id + "'  ")
    conn.commit()
    conn.close()

    return Friend()


@app.route("/accept1", methods=['GET'])
def accept1():
    n = request.args.get('act')
    id = request.args.get('id')
    fname = request.args.get('name')
    uname = session['uname']

    print(fname)
    print(uname)

    if n == "snt":
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor = mydb.cursor()

        mycursor.execute(
            "update frlist set status='Accept' where id='" + str(id) + "'  ")
        mydb.commit()
        mydb.close()

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor = mydb.cursor()

        mycursor.execute(
            "update frlist set status='Accept' where uname='" + str(uname) + "' and frname='" + fname + "'")
        mydb.commit()
        mydb.close()

        mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor1 = mydb1.cursor()

        mycursor1.execute(
            "update frlist set status='Accept' where uname='" + str(fname) + "' and frname='" + uname + "'")
        mydb1.commit()
        mydb1.close()

        return Friend()
    if n == "rejt":
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor = mydb.cursor()

        mycursor.execute(
            "update frlist set status='Reject' where id='" + str(id) + "'  ")
        mydb.commit()
        mydb.close()

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor = mydb.cursor()
        mycursor.execute(
            "update frlist set status='Reject' where uname='" + str(uname) + "' and frname='" + fname + "'")
        mydb.commit()
        mydb.close()

        mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
        mycursor1 = mydb1.cursor()
        mycursor1.execute(
            "update frlist set status='Reject' where uname='" + str(fname) + "' and frname='" + uname + "'")
        mydb1.commit()
        mydb1.close()

        return Friend()


@app.route("/Home")
def Home():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sharetb  where frname='" + uname + "' ")
    data = cur.fetchall()

    return render_template('Home.html', data=data)


@app.route("/post1", methods=['GET', 'POST'])
def post1():
    if request.method == 'POST':
        out = 0  # Default to 0 (good post)
        import cv2
        import random

        place = request.form['caption']
        f = request.files['file']

        fnew = random.randint(111, 999)
        savename = str(fnew) + f.filename
        f.save("static/uploads/" + savename)
        uname = session['uname']

        # Image text analysis
        try:
            import easyocr
            reader = easyocr.Reader(['en'])
            filename = "static/uploads/" + savename
            img = cv2.imread(filename)
            result = reader.readtext(img)

            final_text = place + " " + " ".join([text for _, text, __ in result])  # Combine caption and image text

            # Sentiment analysis - only mark as negative if strongly negative
            sid_obj = SentimentIntensityAnalyzer()
            sentiment_dict = sid_obj.polarity_scores(final_text)

            # Only mark as inappropriate if clearly negative (threshold -0.2)
            if sentiment_dict['compound'] <= -0.2:
                out = 1  # Negative content
        except Exception as e:
            print(f"Error in content analysis: {e}")
            # If analysis fails, assume good content

        # Generate unique ID for the post
        fnew = random.randint(1111, 9999)

        # Save post to database
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        mycursor = conn.cursor()
        mycursor.execute("INSERT INTO sharetb VALUES('" + str(
            fnew) + "','" + uname + "','" + place + "','" + savename + "','" + uname + "','" + str(out) + "')")
        conn.commit()

        # Only check for warnings if this was actually a bad post
        if out == 1:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) as count FROM sharetb WHERE UserName='" + uname + "' AND Ccount='1'")
            data2 = cursor.fetchone()

            ccount = data2[0] if data2 else 0

            if ccount == 1:  # First warning
                flash('Warning: You have posted 1 inappropriate content. One more may result in account blocking.')
            elif ccount >= 2:  # Block after 2 violations
                mycursor.execute("UPDATE register SET status='Blocked' WHERE uname='" + uname + "'")
                conn.commit()
                conn.close()
                flash('Your account has been blocked due to multiple inappropriate posts')
                return redirect(url_for('homepage'))

        # Share with friends
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM frlist WHERE uname='" + uname + "' AND status='Accept'")
        data = cursor.fetchall()
        for x1 in data:
            fname = str(x1[2])
            mycursor.execute("INSERT INTO sharetb VALUES('" + str(
                fnew) + "','" + uname + "','" + place + "','" + savename + "','" + fname + "','" + str(out) + "')")

        conn.commit()
        conn.close()

        if out == 0:
            flash('Post shared successfully!')
        return redirect(url_for('Home'))
@app.route("/cmt", methods=['GET'])
def cmt():
    id = request.args.get('id')
    session['id'] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT distinct id,UserName,ImageInfo,Image	FrName FROM sharetb  where id='" + id + "'     ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where shareid='" + id + "'  and Ccount='0'    ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Smile1) as count1,sum(Smile2) as count2, sum(Smile3) as count3, sum(Smile4) as count4, sum(Smile5) as count5, sum(Smile6) as count6 FROM  comtb    where shareid='" + id + "'  and Ccount='0' ")
    datas = cursor.fetchone()
    if datas:
        smile1 = datas[0]
        smile2 = datas[1]
        smile3 = datas[2]
        smile4 = datas[3]
        smile5 = datas[4]
        smile6 = datas[5]
    else:
        return 'Incorrect username / password !'

    return render_template('Comment.html', data=data, data1=data1, smile1=smile1, smile2=smile2, smile3=smile3,
                           smile4=smile4, smile5=smile5, smile6=smile6)


@app.route("/postcomment", methods=['GET', 'POST'])
def postcomment():
    if request.method == 'POST':

        comm = request.form['comm']
        id = session['id']
        frname = session['uname']

        emoj = request.form['ar']

        em1 = 0
        em2 = 0
        em3 = 0
        em4 = 0
        em5 = 0
        em6 = 0
        emj = 0

        if (int(emoj) == 6):
            em1 = 1
            emj = 0
        if (int(emoj) == 5):
            em2 = 1
            emj = 0
        if (int(emoj) == 4):
            em3 = 1
            emj = 0
        if (int(emoj) == 3):
            em4 = 1
            emj = 1
        if (int(emoj) == 2):
            em5 = 1
            emj = 1
        if (int(emoj) == 1):
            em6 = 1
            emj = 1

        ucomment = comm

        bert = SentimentIntensityAnalyzer()

        # polarity_scores method of SentimentIntensityAnalyzer
        # object gives a sentiment dictionary.
        # which contains pos, neg, neu, and compound scores.
        sentiment_dict = bert.polarity_scores(comm)

        string = str(sentiment_dict['neg'] * 100) + "% Negative"
        # negativeField.insert(10, string)

        string = str(sentiment_dict['neu'] * 100) + "% Neutral"
        # neutralField.insert(10, string)

        string = str(sentiment_dict['pos'] * 100) + "% Positive"
        # positiveField.insert(10, string)

        # decide sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05:
            string = "Positive"
            i = 0;

        elif sentiment_dict['compound'] <= - 0.05:
            string = "Negative"

            i = 1;


        else:
            string = "Neutral"
            i = 0;

        j = int(i) + int(em5)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        cursor = conn.cursor()
        cursor.execute("SELECT *  FROM sharetb WHERE id  ='" + id + "'  ")
        data2 = cursor.fetchone()
        if data2:
            uname = data2[1]

        else:
            print('no data')

        if (j >= 1):

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
            mycursor = conn.cursor()
            mycursor.execute(
                "insert into comtb values('','" + uname + "','" + frname + "','" + comm + "','1','" + id + "','" + str(
                    em1) + "','" + str(em2) + "','" + str(em3) + "','" + str(em4) + "','" + str(em5) + "','" + str(
                    em6) + "')")
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
            mycursor = conn.cursor()
            mycursor.execute(
                "insert into comtb values('','" + uname + "','" + frname + "','" + comm + "','0','" + id + "','" + str(
                    em1) + "','" + str(em2) + "','" + str(em3) + "','" + str(em4) + "','" + str(em5) + "','" + str(
                    em6) + "')")
            conn.commit()
            conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        cursor = conn.cursor()
        cursor.execute("SELECT sum(Ccount) as count  FROM comtb WHERE uname  ='" + uname + "' and frname='" + str(
            session['uname']) + "'  ")
        data2 = cursor.fetchone()
        if data2:
            ccount = data2[0]

        else:
            print('no data')

        if (ccount == 2):

            return 'You Have one More Time Give unwanted comment'

        elif (ccount > 2):

            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
            mycursor = mydb.cursor()
            mycursor.execute(
                "update frlist set status='Blocked' where uname='" + str(uname) + "' and frname='" + str(
                    session['uname']) + "'")
            mydb.commit()
            mydb.close()

            mydb1 = mysql.connector.connect(host="localhost", user="root", password="", database="2socialnetpyemo")
            mycursor1 = mydb1.cursor()
            mycursor1.execute(
                "update frlist set status='Blocked' where uname='" + str(session['uname']) + "' and frname='" + str(
                    uname) + "'")
            mydb1.commit()
            mydb1.close()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
            cursor = conn.cursor()
            cursor.execute("SELECT *   FROM register WHERE uname  ='" + uname + "'   ")
            data2 = cursor.fetchone()
            if data2:
                pname = data2[6]

                sendmsg(pname, str(session['uname']) + ' User Has Blocked!')


            else:
                print('no data')

            return 'Your id Is Blocked'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT distinct id,UserName,ImageInfo,Image FROM sharetb  where id='" + id + "'     ")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM comtb  where shareid='" + id + "'  and Ccount='0'    ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  sum(Smile1) as count1,sum(Smile2) as count2, sum(Smile3) as count3, sum(Smile4) as count4, sum(Smile5) as count5, sum(Smile6) as count6 FROM  comtb    where shareid='" + id + "'  and Ccount='0' ")
        datas = cursor.fetchone()
        if datas:
            smile1 = datas[0]
            smile2 = datas[1]
            smile3 = datas[2]
            smile4 = datas[3]
            smile5 = datas[4]
            smile6 = datas[5]
        else:
            return 'Incorrect username / password !'

        return render_template('Comment.html', data=data, data1=data1, smile1=smile1, smile2=smile2, smile3=smile3,
                               smile4=smile4, smile5=smile5, smile6=smile6)


@app.route("/share", methods=['GET'])
def share():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    cursor = conn.cursor()
    cursor.execute("SELECT *   FROM sharetb WHERE id  ='" + id + "'   ")
    data2 = cursor.fetchone()
    if data2:
        imginfo = data2[2]
        img = data2[3]

        print(imginfo)



    else:
        print('no data')

    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    cursor = conn.cursor()
    cursor.execute("select * from frlist where uname='" + uname + "' and status='Accept'")
    data = cursor.fetchall()
    for x1 in data:
        fname = str(x1[2])

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
        mycursor = conn.cursor()
        mycursor.execute(
            "insert into sharetb values('','" + uname + "','" + imginfo + "','" + img + "','" + fname + "')")
        conn.commit()
        conn.close()

    return Home()


@app.route("/Notification")
def Notification():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where uname='" + uname + "'   and Ccount='1'  ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where uname='" + uname + "'   and Ccount='0'  ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM comtb  where uname='" + uname + "'   and Ccount='2'  ")
    data2 = cur.fetchall()

    return render_template('Notification.html', data=data, data1=data1, data2=data2)


@app.route("/CAccept", methods=['GET'])
def CAccept():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    mycursor = conn.cursor()
    mycursor.execute(
        "update   comtb set Ccount='0' where id='" + id + "' ")
    conn.commit()
    conn.close()

    return Notification()


@app.route("/CReject", methods=['GET'])
def CReject():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2socialnetpyemo')
    mycursor = conn.cursor()
    mycursor.execute(
        "update   comtb set Ccount='2' where id='" + id + "' ")
    conn.commit()
    conn.close()

    return Notification()


def sendmsg(targetno, message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your USER is " + message + "  Sent By SOCIALMEME")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
