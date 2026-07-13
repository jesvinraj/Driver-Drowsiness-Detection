# main.py

from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
from camera import VideoCamera
import cv2
# import shutil
# import PIL.Image
# from PIL import Image
# import imagehash
import mysql.connector
import urllib.request
import urllib.parse

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  charset="utf8",
  database="eye_monitor"

)
app = Flask(__name__)


@app.route('/')
def index():
    
        
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=""
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        #print('SELECT * FROM admin WHERE username = %s AND password = %s', (uname, pwd))
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            #session['loggedin'] = True
            #session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('admin'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('login.html',msg=msg)


@app.route('/driver', methods=['GET', 'POST'])
def driver():
    msg = ""
    carno = ""
    lat = ""
    lon = ""
    if request.method == 'POST':
        carno = request.form['carno']
        pass1 = request.form['pass']
        lat = request.form['lat']
        lon = request.form['lon']
        print(carno)
        cursor1 = mydb.cursor()

        cursor1.execute('SELECT * FROM register WHERE carno = %s and mobile = %s', (carno, pass1))
        account = cursor1.fetchone()
        if account:
            # session['loggedin'] = True
            # session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('monitor', carno=carno, lat=lat, lon=lon))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect Car No. or Password!'
    return render_template('driver.html', msg=msg, carno=carno, lat=lat, lon=lon)

@app.route('/home', methods=['GET', 'POST'])
def home():
    
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM register')
    data = cursor.fetchall()
    if request.method=='GET':
        carno = request.args.get('carno')
        cursor1 = mydb.cursor()
        cursor1.execute("delete from register where carno=%s", (carno, ))
        mydb.commit()
        if cursor1.rowcount==1:
            return redirect(url_for('home'))
    return render_template('home.html',data=data)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM admin')
    data = cursor.fetchone()
    if request.method=='POST':
        mobile=request.form['mobile']
        cursor1 = mydb.cursor()
        sql = "update admin set mobile=%s"
        val = (mobile, )
        cursor1.execute(sql, val)
        mydb.commit()            
    
    return render_template('admin.html',data=data)


@app.route('/add_new', methods=['GET', 'POST'])
def add_new():
    #import student
    msg=""
    if request.method=='POST':
        carno=request.form['carno']
        name=request.form['name']
        mobile=request.form['mobile']
        mobile2=request.form['mobile2']
        email=request.form['email']
        address=request.form['address']
        cursor = mydb.cursor()
        sql = "INSERT INTO register(carno,name,mobile,mobile2,email,address) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (carno,name,mobile,mobile2,email,address)
        cursor.execute(sql, val)
        mydb.commit()            
        print(cursor.rowcount, "Registered Success")
        result="sucess"
        if cursor.rowcount==1:
            return redirect(url_for('home'))
        else:
            msg='Already Exist'
    return render_template('add_new.html',msg=msg)


@app.route('/capture', methods=['GET', 'POST'])
def capture():
    if request.method == 'GET':
        carno = request.args.get('carno')
    mobile = ""
    mobile2 = ""
    mobile3 = ""
    name = ""
    lat = ""
    lon = ""
    loc = ""
    vv = 0
    st = "no"
    n = 0
    f2 = open("log.txt", "r")
    vv = f2.read()
    f2.close()

    n = str(vv)
    print("n",n)

    if request.method == 'POST':
        # carno = request.args.get('carno')
        # lat= request.args.get('lat')
        # lon= request.args.get('lon')
        carno = request.form['carno']
        lat = request.form['lat']
        lon = request.form['lon']
        # cursor1 = mydb.cursor()
        # cursor1.execute('SELECT * FROM register WHERE carno = %s', (carno,))
        # account = cursor1.fetchone()
        #
        # mobile = account[2]
        # mobile2 = account[3]
        # name = account[1]
        #
        # cursor2 = mydb.cursor()
        # cursor2.execute('SELECT * FROM admin')
        # account2 = cursor2.fetchone()
        # mobile3 = account2[2]

    if n=="Sleep":
        st = "yes"
        import winsound
        freq = 500
        dur = 3000
        winsound.Beep(freq, dur)


    return render_template('capture.html', value=vv, st=st, carno=carno, lat=lat, lon=lon)





@app.route('/monitor', methods=['GET', 'POST'])
def monitor():
    carno = request.args.get('carno')
    #lat = request.args.get('lat')
    #lon = request.args.get('lon')
    
    return render_template('monitor.html',carno=carno)

@app.route('/view', methods=['GET', 'POST'])
def view():
    carno = request.args.get('carno')
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM details where id>1 && carno=%s order by id desc', (carno, ))
    data = cursor.fetchall()
    if request.method=='POST':
        carno=request.form['carno']
        cursor1 = mydb.cursor()
        cursor1.execute("delete from details where id>1 && carno=%s", (carno, ))
        mydb.commit()
        if cursor1.rowcount==1:
            return redirect(url_for('home'))
    return render_template('view.html',data=data, carno=carno)


def gen(camera):
    while True:
        frame = camera.get_frame()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('login.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
