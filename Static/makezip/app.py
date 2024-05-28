import flask
from flask import render_template, request, jsonify, session
import warnings
warnings.filterwarnings("ignore")
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_session import Session
import datetime, os
import cv2
import numpy as np
import requests, json
import pickle
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import qrcode
import random
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import re
from bs4 import BeautifulSoup
import geocoder

app = flask.Flask(__name__, template_folder='Templates')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = ''#password
#in my case password is null so i am keeping empty
app.config['MYSQL_DB'] = 'easy_luggage'#database name

mysql = MySQL(app)
@app.route('/')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('login.html'))
    
@app.route('/zonecomfort', methods=['GET', 'POST'])
def zonecomfort():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
@app.route('/goodsreceive', methods=['GET', 'POST'])
def goodsreceive():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
@app.route('/customerdashboard', methods=['GET', 'POST'])
def customerdashboard():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
@app.route('/customerparceldetails', methods=['GET', 'POST'])
def customerparceldetails():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))

@app.route('/currentzone', methods=['GET', 'POST'])
def currentzone():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
@app.route('/hubdistance', methods=['GET', 'POST'])
def hubdistance():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))

@app.route('/admindashboard', methods=['GET', 'POST'])
def admindashboard():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))

@app.route('/curloc', methods=['GET', 'POST'])
def curloc():
    if flask.request.method == 'GET':
        return(flask.render_template('currentMap.html'))

@app.route('/parcelhistory', methods=['GET', 'POST'])
def parcelhistory():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
@app.route('/customerqueries', methods=['GET', 'POST'])
def customerqueries():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
@app.route('/adminquery', methods=['GET', 'POST'])
def adminquery():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
   
@app.route('/empdetails', methods=['GET', 'POST'])
def empdetails():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
@app.route('/luggagesafe', methods=['GET', 'POST'])
def luggagesafe():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
        
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if flask.request.method == 'GET':
        return(flask.render_template('login.html'))

# function to remove html elements from the reviews
def removeHTML(raw_text):
    clean_HTML = BeautifulSoup(raw_text, 'lxml').get_text() 
    return clean_HTML

# function to remove special characters and numbers from the reviews4961
def removeSpecialChar(raw_text):
    clean_SpecialChar = re.sub("[^a-zA-Z]", " ", raw_text)  
    clean_SpecialChar = " ".join(filter(lambda x:x[0]!='&',  clean_SpecialChar.split()))
    clean_SpecialChar = " ".join(filter(lambda x:x[0]!='\\', clean_SpecialChar.split()))
    clean_SpecialChar = clean_SpecialChar.replace("\n", '')
    clean_SpecialChar = clean_SpecialChar.replace("\r", '')
    return clean_SpecialChar

# function to convert all reviews into lower case
def toLowerCase(raw_text):
    clean_LowerCase = raw_text.lower().split()
    return( " ".join(clean_LowerCase))

@app.route('/getqueryanalysis', methods=['GET', 'POST'])
def getqueryanalysis():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    if flask.request.method == 'POST':
        qry = "SELECT * FROM cust_query"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(qry)
        result = cursor.fetchall()
        
        data = pd.read_csv('data/amazon_sentiment_data.csv', encoding='cp437')
        data = data.sample(frac=1)
        X = data['review_body']
        Y = data['sentiment']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)

        # X_training clean set
        X_train_cleaned = []

        for val in X_train:
            val = removeHTML(val)
            val = removeSpecialChar(val)
            val = toLowerCase(val)
            X_train_cleaned.append(val) 
            
        tvec = TfidfVectorizer(use_idf=True, strip_accents='ascii')

        X_train_tvec = tvec.fit_transform(X_train_cleaned)

        #Prediction
        model = pickle.load(open('Model/electronicSentimentAnalyzer.pkl', 'rb'))
        svr_lin = LinearSVC(multi_class='ovr',C=1.0,loss='squared_hinge', dual=False)
        model = svr_lin.fit(X_train_tvec, Y_train)
         
        result = list(result)
        review = []
        for i in range(0, len(result)):
            
            demo_review = np.array([result[i]['query']])
            print(demo_review)
            demo_review_X_test = tvec.transform(demo_review)
            
            prediction = model.predict(demo_review_X_test)
            if prediction == 1:
                pred = "Good"
            else:
                pred = "Not good"
            review.append(pred)
        
        retdata = {
           "result":result,
           "analyse":review
           }
        return jsonify(retdata)
        
@app.route('/registeruser', methods=['GET', 'POST'])
def registeruser():
    if flask.request.method == 'GET':
        return(flask.render_template('login.html'))
    if flask.request.method == 'POST':
        usertype    = request.form['regusertype']
        name        = request.form['name']
        phone       = request.form['regphone']
        address     = request.form['address']
        email       = request.form['email']
        password    = request.form['password']
        
        temprefid = qry2 = qry1 = qry = ''
        
        if usertype == "user":
            qry1 = "SELECT * FROM user_details WHERE  verified = 1 AND phone = "+phone
            qry = "INSERT INTO user_details(user_name, phone, email, address, password) VALUES('"+name+"','"+phone+"','"+email+"','"+address+"','"+password+"')"
            print(qry)
        elif usertype == "serviceman":
            qry1 = "SELECT * FROM service_man WHERE verified = 1 AND phone = "+phone
            qry = "INSERT INTO service_man(serviceman_name, phone, email, address, password) VALUES('"+name+"','"+phone+"','"+email+"','"+address+"','"+password+"')"
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(qry1)
        result = cursor.fetchone()
        
        if result:
            msg = "2"
        else: 
            cursor.execute(qry)
            refid = cursor.lastrowid
            mysql.connection.commit()
            
            if refid:
                temprefid = refid
                otp = str(random.randint(1000,9999))
                if usertype == "user":
                    qry2 = "UPDATE user_details SET otp = "+otp+" WHERE user_id = '"+str(refid)+"'"
                    #print(qry2)
                elif usertype == "serviceman":
                    qry2 = "UPDATE service_man SET otp = "+otp+" WHERE serviceman_id = '"+str(refid)+"'"
                updotp = cursor.execute(qry2)
                #print(updotp)
                mysql.connection.commit()
                if updotp:
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login("prithivirajk2503@gmail.com", "vkdm wcla xvkz ebif")
                    # Email details
                    sender_email_id = "prithivirajk2503@gmail.com"
                    recipient_email = email
                    subject = "Welcome to Easy Luggage Career Service!"
                    name = name
                    
                    # Message content
                    body = f"Hi Mr./Mrs. {name},\n\nThank you for joining with Easy Luggage Career Service!.\n\nHere is your OTP for the Email Verification: {otp}\n\nRegards,\nTeam Luggage Carrier"
                    
                    # Create a MIMEText object
                    msg = MIMEMultipart()
                    msg['From'] = sender_email_id
                    msg['To'] = recipient_email
                    msg['Subject'] = subject
                    
                    # Attach the message body
                    msg.attach(MIMEText(body, 'plain'))
                    
                    # sending the mail
                    s.sendmail(sender_email_id, recipient_email, msg.as_string())
                    s.quit()
                    msg = 1
        output = {"msg":msg,"refid":temprefid}
        return jsonify(output)
        
@app.route('/verifyotp', methods=['GET', 'POST'])
def verifyotp():
    if flask.request.method == 'POST':    
        usertype    = request.form['regusertype']
        otp         = request.form['otp']
        refid       = request.form['refid']
        
        if usertype == "user":
            qry = "SELECT * FROM user_details WHERE user_id = '"+refid+"' AND otp = '"+otp+"' "
        elif usertype == "serviceman":
            qry = "SELECT * FROM service_man WHERE serviceman_id = '"+refid+"' AND otp = '"+otp+"' "
            
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(qry)
        result = cursor.fetchone()
        msg = 0
        if result:
            if usertype == "user":
                qry2 = "UPDATE user_details SET verified = 1 WHERE user_id = '"+str(refid)+"'"
            elif usertype == "serviceman":
                qry2 = "UPDATE service_man SET verified = 1 WHERE serviceman_id = '"+str(refid)+"'"
            updotp = cursor.execute(qry2)
            mysql.connection.commit()
            msg = 1
    output = {"msg":msg,"refid":refid}
    return jsonify(output)
            
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return(flask.render_template('login.html'))
    if flask.request.method == 'POST':
        usertype    = request.form['usertype']
        phone       = request.form['phone']
        password    = request.form['password']
        qry = ''
        
        if usertype == "user":
            qry = "SELECT * FROM user_details WHERE phone = '"+phone+"' AND password = '"+password+"' AND verified = 1"
        elif usertype == "serviceman":
            qry = "SELECT * FROM service_man WHERE phone = '"+phone+"' AND password = '"+password+"' AND verified = 1"
        elif usertype == "admin":
            qry = "SELECT * FROM admin WHERE phone = '"+phone+"' AND password = '"+password+"'"
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(qry)
        result = cursor.fetchone()
        
        if result:
            msg = "1"
            if usertype == "user":
                session["userid"]   = result["user_id"]
                endurl = "userdashboard"
            elif usertype == "serviceman":
                session["userid"]   = result["serviceman_id"]
                session["username"]   = result["serviceman_name"]
                endurl = "servicemandashboard"
            elif usertype == "admin":
                session["userid"]   = result["admin_id"]
                endurl = "admindashboard"
            session["usertype"] = usertype
        else:
           msg = "0"
           
        
        pred = {"msg":msg}
    return jsonify(pred)

@app.route('/servicemandashboard', methods=['GET', 'POST'])
def servicemandashboard():
    if flask.request.method == 'GET':
        if not session.get("userid"):
            return(flask.render_template('login.html'))
        elif session.get("userid") is None:
            return(flask.render_template('login.html'))
        else:
            return(flask.render_template('home.html'))

@app.route('/luggagedetails', methods=['GET', 'POST'])
def luggagedetails():
    if flask.request.method == 'GET':
        if not session.get("userid"):
            return(flask.render_template('login.html'))
        elif session.get("userid") is None:
            return(flask.render_template('login.html'))
        else:
            return(flask.render_template('home.html'))

@app.route('/manageluggages', methods=['GET', 'POST'])
def manageluggages():
    if flask.request.method == 'GET':
        if not session.get("userid"):
            return(flask.render_template('login.html'))
        elif session.get("userid") is None:
            return(flask.render_template('login.html'))
        else:
            return(flask.render_template('home.html'))

@app.route('/getopenluggagelist', methods=['GET', 'POST'])
def getopenluggagelist():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM luggage WHERE status != "closed" ')
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getallparcels', methods=['GET', 'POST'])
def getallparcels():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM parcel WHERE status = "open" OR status = "progress" AND user_id = '+str(session['userid']))
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getparcelhistory', methods=['GET', 'POST'])
def getparcelhistory():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM parcel WHERE status = "delivered" OR status = "returned" AND user_id = '+str(session['userid']))
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/gethubname', methods=['GET', 'POST'])
def gethubname():
    if flask.request.method == 'POST':
        branchid       = request.form['branchid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM branch_details WHERE branch_id ='+branchid)
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getallluggages', methods=['GET', 'POST'])
def getallluggages():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM luggage ORDER BY created_at DESC')
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getempdetails', methods=['GET', 'POST'])
def getempdetails():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM service_man')
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getparcelcount', methods=['GET', 'POST'])
def getparcelcount():
    if flask.request.method == 'POST':
        luggageid   = request.form['luggageid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT COUNT(parcel_id) AS total FROM parcel WHERE luggage_id='+str(luggageid))
        result = cursor.fetchall();
    return jsonify(result)


@app.route('/getparceldetail', methods=['GET', 'POST'])
def getparceldetail():
    if flask.request.method == 'POST':
        parcelid       = request.form['parcelid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM parcel WHERE parcel_id = '+str(parcelid))
        result = cursor.fetchall();
        cursor.execute('SELECT branch_name FROM branch_details WHERE branch_id = '+str(result[0]['from_branch']))
        result2 = cursor.fetchall();
        cursor.execute('SELECT * FROM indian_cities_database WHERE city= "'+result2[0]["branch_name"]+'" ')
        result3 = cursor.fetchall();
        
        finres = {"city": result2[0]["branch_name"], "lat":result3[0]["lat"] , "lang":result3[0]["longt"]}
    return jsonify(finres)

@app.route('/getparcelcompdetail', methods=['GET', 'POST'])
def getparcelcompdetail():
    if flask.request.method == 'POST':
        parcelid       = request.form['parcelid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM parcel WHERE parcel_id = '+str(parcelid))
        result = cursor.fetchall();
        cursor.execute('SELECT * FROM user_details WHERE user_id = '+str(result[0]["user_id"]))
        result2 = cursor.fetchall();
        res = {"parcel":result, "userdetail":result2}
        return jsonify(res)

@app.route('/verifydeliver', methods=['GET', 'POST'])
def verifydeliver():
    if flask.request.method == 'GET':
        return(flask.render_template('home.html'))
    
import webbrowser  
@app.route('/verifyuser', methods=['GET', 'POST'])
def verifyuser():
    if flask.request.method == 'POST':
        parcelid       = request.form['parcelid']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM parcel WHERE parcel_id = '+str(parcelid))
        result = cursor.fetchall();
        
        cap = cv2.VideoCapture(0) 
        # initialize the cv2 QRCode detector 
        detector = cv2.QRCodeDetector()
        
        while True: 
           _, img = cap.read()
           
           data, bbox, _ = detector.detectAndDecode(img)  
           if data: 
               a = data 
               break
           cv2.imshow("QRCODEscanner", img)     
           if cv2.waitKey(1) == ord("q"): 
               break
        cap.release() 
        cv2.destroyAllWindows()
           
        if result[0]["sentotp"] == a:
            msg =  "yes"
        else:
            msg = "no"
    return jsonify(msg)

@app.route('/getluggagedetails', methods=['GET', 'POST'])
def getluggagedetails():
    if flask.request.method == 'POST':
        luggageid       = request.form['luggageid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM luggage WHERE luggage_id= '+luggageid )
        result1 = cursor.fetchall();
        cursor.execute('SELECT * FROM indian_cities_database WHERE city= "'+result1[0]["from_branch"]+'" OR city = "' +result1[0]["to_branch"]+'"')
        result2 = cursor.fetchall();
        #cursor.execute('SELECT * FROM indian_cities_database WHERE longt <= "'+result2[0]["longt"]+'" AND longt >= "'+result2[1]["longt"]+'" AND state = "'+result2[0]["state"]+'" OR state = "'+result2[1]["state"]+'"')
        #result3 = cursor.fetchall();
        
        # Assuming result2 contains latitude and longitude values
        min_lat = min(result2[0]['lat'], result2[1]['lat'])
        max_lat = max(result2[0]['lat'], result2[1]['lat'])
        min_lon = min(result2[0]['longt'], result2[1]['longt'])
        max_lon = max(result2[0]['longt'], result2[1]['longt'])
        # Formulating SQL query with filtering conditions
        
        qry = f'''
            SELECT * FROM indian_cities_database
            WHERE lat BETWEEN {min_lat} AND {max_lat}
            AND longt BETWEEN {min_lon} AND {max_lon}
            AND (state = "{result2[0]["state"]}" OR state = "{result2[1]["state"]}")
        '''

        #cursor.execute('SELECT * FROM indian_cities_database WHERE longt <= "'+result2[0]["longt"]+'" AND longt >= "'+result2[1]["longt"]+'" AND state = "'+result2[0]["state"]+'" OR state = "'+result2[1]["state"]+'"')
        cursor.execute(qry)
        result3 = cursor.fetchall();
        
        #print(result3)
        return_data = [
                {
                  "from": result1[0]["from_branch"],
                  "to": result1[0]["to_branch"]
                }
            ]
        if len(result3) >= 1:
           for i in range(len(result3)):
               dest_data =  gettraveldetails(result3[i]["longt"], result3[i]["lat"], result3[i]["city"])
               return_data.append(dest_data)
        else:
            dest_data =  gettraveldetails(result2[0]["longt"], result2[0]["lat"], result3[i]["city"])
            return_data.append(dest_data)
            
            
        return jsonify(return_data)

#Prediction
model = pickle.load(open('Model/accidentSeverityPredictor.pkl', 'rb'))
def gettraveldetails(long, lat, city):
    roveg            = 0
    typeveg          = 3
    cclass           = 0
    
    accesskey = "9049542e1e37e55f186381e0fcbd2053"
    base_url = "http://api.weatherstack.com/current?"
    full_url = base_url+"access_key="+accesskey+"&query="+lat+","+long
    response = requests.get(full_url) 
    x = response.json()
    #print(x)
    
    roadsurf        = "0"
    light           = ""
    weather         = ""
    basicroadsurf  = x['current']['weather_code']
    wind_speed     = x['current']['wind_speed']
    is_day         = x['current']['is_day']
    
    if basicroadsurf in [389, 353, 176, 302, 299, 296, 386, 284, 281, 266, 263]:
        roadsurf = 4  #Wet
        if wind_speed > 24:
            weather = 5  #Raining with high winds
        else:
            weather = 4  #Raining without high winds
    elif basicroadsurf in [143, 179, 182, 185, 248, 260, 395, 338, 335, 260]:
        roadsurf = 1  #Frost
        weather = 1  #Fog or mist – if hazard
    elif basicroadsurf in [359, 356, 308, 305, 320, 314, 311, 293, 317]:
        roadsurf = 2  #Flood
    elif basicroadsurf in [200, 227, 230, 263, 392, 377, 374, 371, 368, 365, 362, 350, 332, 329, 326, 323]:
        roadsurf = 3  #Snow
        if wind_speed > 24:
            weather = 7  #Snow with high winds
        else:
            weather = 6  #Snow without high winds
    else:
        roadsurf = 0  #Dry
        if wind_speed > 24:
            weather = 2  #Fine with high winds
        else:
            weather = 0  #Fine without high winds
    
    if is_day == "no":
        light = 3
    else:
        light = 0

    
    input_variables = pd.DataFrame([[roveg, roadsurf, light, weather, cclass,  typeveg]],
                                  columns=['1st Road Class', 'Road Surface','Lighting Conditions','Weather Conditions','Casualty Class','Type of Vehicle'], dtype=float)
    
    
    prediction = model.predict(input_variables)[0]
      
   
    if prediction == 1:
       prediction="not fine"
    else:
       prediction="fine"
       
    finalpred  = {"place":city,"prediction":prediction}
    return finalpred

@app.route('/getdistancedetails', methods=['GET', 'POST'])
def getdistancedetails():
    if flask.request.method == 'POST':
        luggageid       = request.form['luggageid']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM luggage WHERE luggage_id= '+luggageid )
        result1 = cursor.fetchall();
        cursor.execute('SELECT * FROM indian_cities_database WHERE city= "'+result1[0]["from_branch"]+'" OR city = "' +result1[0]["to_branch"]+'"')
        result2 = cursor.fetchall();
        
        # Assuming result2 contains latitude and longitude values
        min_lat = min(result2[0]['lat'], result2[1]['lat'])
        max_lat = max(result2[0]['lat'], result2[1]['lat'])
        min_lon = min(result2[0]['longt'], result2[1]['longt'])
        max_lon = max(result2[0]['longt'], result2[1]['longt'])
        # Formulating SQL query with filtering conditions
        
        qry = f'''
            SELECT * FROM indian_cities_database
            WHERE lat BETWEEN {min_lat} AND {max_lat}
            AND longt BETWEEN {min_lon} AND {max_lon}
            AND (state = "{result2[0]["state"]}" OR state = "{result2[1]["state"]}")
        '''

        #cursor.execute('SELECT * FROM indian_cities_database WHERE longt <= "'+result2[0]["longt"]+'" AND longt >= "'+result2[1]["longt"]+'" AND state = "'+result2[0]["state"]+'" OR state = "'+result2[1]["state"]+'"')
        cursor.execute(qry)
        result3 = cursor.fetchall();
        
        cursor.execute('SELECT * FROM indian_cities_database WHERE  city = "' +result1[0]["to_branch"]+'"')
        result4 = cursor.fetchall();
        return_data = [
                {
                  "from": result1[0]["from_branch"],
                  "to": result1[0]["to_branch"],
                  "distance":'0'
                }
            ]
        if len(result3) >= 1:
           for i in range(len(result3)):
               city = result3[i]["city"]
               dest_data =  distance(result4[0]["lat"], result3[i]["lat"], result4[0]["longt"], result3[i]["longt"], city)
               return_data.append(dest_data)
        else:
            city = result2[0]["city"]
            dest_data =  distance(result4[0]["lat"], result2[0]["lat"], result4[0]["longt"], result2[0]["longt"], city)
            return_data.append(dest_data)
        
        return_data1  = sorted(return_data, key=lambda d: d['distance']) 
        return jsonify(return_data1)

def distance(lat1, lat2, lon1, lon2, city):

    lon1 = radians(float(lon1))
    lon2 = radians(float(lon2))
    lat1 = radians(float(lat1))
    lat2 = radians(float(lat2))
      
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a)) 
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
    
    dist = c * r
    dist = "{:.2f}".format(dist)
    
    ret_data = {"city":city, "distance":dist}
    # calculate the result
    return ret_data

    
@app.route('/getuserlist', methods=['GET', 'POST'])
def getuserlist():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_details')
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getbranchlist', methods=['GET', 'POST'])
def getbranchlist():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM branch_details')
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getopenlug', methods=['GET', 'POST'])
def getopenlug():
    if flask.request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM luggage WHERE status = "open"')
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/getusername', methods=['GET', 'POST'])
def getusername():
    if flask.request.method == 'POST':
        phone       = request.form['userphone']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_details WHERE user_id = '+phone)
        result = cursor.fetchall();
    return jsonify(result)

@app.route('/addquery', methods=['GET', 'POST'])
def addquery():
    if flask.request.method == 'POST':
        subject     = request.form['subject']
        query       = request.form['query']
        userid = session['userid']
        qry = 'INSERT INTO cust_query(user_id, subject, query) VALUES("'+str(userid)+'","'+subject+'","'+query+'")'
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(qry)
        refid = cursor.lastrowid
        mysql.connection.commit()
        if refid:
            return jsonify("1")
        else:
            return jsonify("0")

def get_output_layers(net):
    layer_names = net.getLayerNames()
    try:
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    except:
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

@app.route('/objcount', methods=['GET', 'POST'])
def objcount():
    if flask.request.method == 'POST':    
       isthisFile = request.files.get('file')
       path = 'Static/Objcount/' + isthisFile.filename
       current_time = datetime.datetime.now()

       if os.path.exists(path):
           filename = str(current_time.year+current_time.month+current_time.day+current_time.hour+current_time.minute+current_time.second) + isthisFile.filename
       else:
           filename = isthisFile.filename
    
       upload = isthisFile.save('Static/Objcount/' + filename)
       
       sefile = './Static/Objcount/' + filename
       image = cv2.imread(sefile)

       Width = image.shape[1]
       Height = image.shape[0]
       scale = 0.00392

       with open('Static/yolov3.txt', 'r') as f:
           classes = [line.strip() for line in f.readlines()]

       net = cv2.dnn.readNet('Static/yolov3.weights', 'Static/yolov3.cfg')

       blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

       net.setInput(blob)

       outs = net.forward(get_output_layers(net))

       class_ids = []
       confidences = []
       boxes = []
       conf_threshold = 0.5
       nms_threshold = 0.4

       for out in outs:
           for detection in out:
               scores = detection[5:]
               class_id = np.argmax(scores)
               confidence = scores[class_id]
               if confidence > 0.5:
                   center_x = int(detection[0] * Width)
                   center_y = int(detection[1] * Height)
                   w = int(detection[2] * Width)
                   h = int(detection[3] * Height)
                   x = center_x - w / 2
                   y = center_y - h / 2
                   class_ids.append(class_id)
                   confidences.append(float(confidence))
                   boxes.append([x, y, w, h])
       bxs = str(len(boxes))
       return bxs

@app.route('/addgrnotes', methods=['GET', 'POST'])
def addgrnotes():
    if flask.request.method == 'POST':  
        luggageid    = request.form['luggageid']
        frombranch   = request.form['frombranch']
        tobranch     = request.form['tobranch']
        actualno     = request.form['actualno']
        receivedno   = request.form['receivedno']
        missed       = request.form['missed']
        comments     = request.form['comments']
        userid = session['userid']
    
        qry = 'INSERT INTO goods_receiving(from_branch,to_branch,luggage_id,actual,received,missed,comments,admin_id) VALUES("'+str(frombranch)+'","'+tobranch+'","'+luggageid+'","'+str(actualno)+'","'+receivedno+'","'+str(missed)+'","'+str(comments)+'","'+str(userid)+'")'
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(qry)
        refid = cursor.lastrowid
        mysql.connection.commit()
        
        cursor.execute('SELECT * FROM branch_details WHERE branch_id ='+str(tobranch))
        result = cursor.fetchall();
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("prithivirajk2503@gmail.com", "vkdm wcla xvkz ebif")
        # Email details
        sender_email_id = "prithivirajk2503@gmail.com"
        recipient_email = result[0]["manager_mail"]
        subject = "Easy Luggage  Goods Receieve Note"
        name = result[0]["manager_name"]
        lugid = 'LUG-'+str(luggageid)
        
        # Get the current date and time
        current_time = datetime.datetime.now()
        
        # Format and print only the current time
        formatted_time = current_time.strftime("%H:%M:%S")

        curdate = formatted_time
        # Message content
        body = f"Hi Mr./Mrs. {name},\n\nThe luggage with id {lugid} receieved at {result[0]['branch_name']} hub on {curdate}.\n\nRegards,\nEasy luggage service"
        
        # Create a MIMEText object
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the message body
        msg.attach(MIMEText(body, 'plain'))
        
        # sending the mail
        s.sendmail(sender_email_id, recipient_email, msg.as_string())
        s.quit()
        
        return jsonify("1")
    
        
@app.route('/addluggage', methods=['GET', 'POST'])
def addluggage():
    if flask.request.method == 'POST':  
        servicemanid    = request.form['servicemanid']
        userphone       = request.form['userphone']
        username        = request.form['username']
        openlug         = request.form['openlug']
        branchfrom      = request.form['branchfrom']
        branchto        = request.form['branchto']
        payamount       = request.form['payamount']
        parcelcount     = request.form['parcelcount']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO parcel(luggage_id, serviceman_id, user_id, from_branch, to_branch, pay_amount, sentotp, present_hub) VALUES ("'+openlug+'","'+servicemanid+'","'+userphone+'","'+username+'","'+branchfrom+'","'+branchto+'","'+payamount+'", "'+branchfrom+'")')
        refid = str(cursor.lastrowid)
        generate_random = str(random.randint(1000,9999))
        encs = generate_random.encode(encoding="utf-8")
        hash_obj = hashlib.md5(encs)
        enc = str(hash_obj.hexdigest())
        qry = "UPDATE parcel SET sentotp = '"+enc+"' WHERE parcel_id = "+refid

        img = qrcode.make(enc)
        img.save("Static/barcodes/lug"+str(refid)+".png")
        
        cursor.execute(qry)
        mysql.connection.commit()
    
    return "1"

@app.route('/deliveruser', methods=['GET', 'POST'])
def deliveruser():
    if flask.request.method == 'POST': 
        curlugid     = request.form['curlugid']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM parcel WHERE parcel_id ='+str(curlugid))
        result = cursor.fetchall();
        
        qry = "UPDATE parcel SET status = 'delivered' WHERE parcel_id = "+curlugid
        cursor.execute(qry)
        mysql.connection.commit()
        
        userid = result[0]['user_id']
        cursor.execute('SELECT * FROM user_details WHERE user_id ='+str(userid))
        userdet = cursor.fetchall();
        
        usermail = userdet[0]['email']
        uname = userdet[0]['user_name']
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("prithivirajk2503@gmail.com", "vkdm wcla xvkz ebif")
        # Email details
        sender_email_id = "prithivirajk2503@gmail.com"
        recipient_email = usermail
        subject = "Easy Luggage - Delivery Notification"
        
        lugid = 'LUG-'+str(curlugid)
        
        # Get the current date and time
        current_time = datetime.datetime.now()
        
        # Format and print only the current time
        formatted_time = current_time.strftime("%H:%M:%S")

        curdate = formatted_time
        # Message content
        body = f"Hi Mr./Mrs. {uname},\n\nThe luggage with id {lugid} delivered on {curdate} by our service person.\n\nRegards,\nEasy luggage service"
        
        # Create a MIMEText object
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the message body
        msg.attach(MIMEText(body, 'plain'))
        
        # sending the mail
        s.sendmail(sender_email_id, recipient_email, msg.as_string())
        s.quit()
        
        return "1"
    
@app.route('/track', methods=['GET', 'POST'])
def track():
    luggageid       = request.form['luggageid']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM luggage WHERE luggage_id= '+luggageid )
    result1 = cursor.fetchall();
    cursor.execute('SELECT * FROM indian_cities_database WHERE city= "'+result1[0]["from_branch"]+'" OR city = "' +result1[0]["to_branch"]+'"')
    result2 = cursor.fetchall();
   
    # Assuming result2 contains latitude and longitude values
    min_lat = min(result2[0]['lat'], result2[1]['lat'])
    max_lat = max(result2[0]['lat'], result2[1]['lat'])
    min_lon = min(result2[0]['longt'], result2[1]['longt'])
    max_lon = max(result2[0]['longt'], result2[1]['longt'])
    # Formulating SQL query with filtering conditions
    qry = f'''
        SELECT * FROM indian_cities_database
        WHERE lat BETWEEN {min_lat} AND {max_lat}
        AND longt BETWEEN {min_lon} AND {max_lon}
        AND (state = "{result2[0]["state"]}" OR state = "{result2[1]["state"]}")
    '''
    cursor.execute(qry)
    result3 = cursor.fetchall();
    
    location = geocoder.ip('me')
    curcity = location.city
    
    contains_curcity = any(city_info['city'].lower() == curcity for city_info in result3)
    cities_str = ', '.join(city_info['city'] for city_info in result3)

    resultmap = {
        "actualcities": cities_str,
        "curcity" : curcity,
        "isright" : contains_curcity
    }
    return jsonify(resultmap)
    
if __name__ == '__main__':
    app.run(debug=True)