#import flask--we need all the confugurations 
from flask import *
import pymysql

import os
#initializing app
app=Flask(__name__)

#configure my project to save image to our folder
app.config["UPLOAD_FOLDER"]='static/images'


#creating routes

@app.route("/api/signup",methods=["POST"])

#defining a function---a block of code that do a specific task

def signup():

    #extracting user inputs from a form
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

#connecting to our database
#pymysql--python library that allows us to connect our api to the database
    connection=pymysql.connect(user="root",host="localhost",password="",database="simba-sokogarden")

    cursor=connection.cursor()

    sql="insert into users(username,password,email,phone)values(%s,%s,%s,%s)"
    #it avoids sql injections----input of malecious commands

    data=(username,password,email,phone)

    #execute our data
    cursor.execute(sql,data)

    #save to database

    connection.commit()


    return jsonify ({"message":"Thank you for joining"})

#----------------------------------------------sign in api-------------------------------------------

@app.route("/api/signin",methods=['POST'])

def signin():
    email=request.form['email']
    password=request.form['password']

    connection=pymysql.connect(user='root',host='localhost',password='',database='simba-sokogarden')

    cursor=connection.cursor(pymysql.cursors.DictCursor)

    sql="select*from users where email=%s and password=%s"

    data=(email,password)

    cursor.execute(sql,data)



    

    if cursor.rowcount==0:
        return jsonify({'message':'login failed'})
    
    else:
        user=cursor.fetchone()

        return jsonify({'message':'login successful','user':user})
    
#creating a route
@app.route("/api/addproducts",methods=["POST"])
def addproduct():

    #extracting product details

    product_name=request.form['product_name']
    product_description=request.form['product_description']
    product_cost=request.form['product_cost']
    photo=request.files['photo']  

    #extracting the file name from the product photo
    
    filename=photo.filename

    #specify the path to our static folder that contains the images folder 
    photopath=os.path.join(app.config["UPLOAD_FOLDER"],filename)

    photo.save(photopath)


    


    connection=pymysql.connect(user="root",host="localhost",password="",database="simba-sokogarden")

    cursor=connection.cursor(pymysql.cursors.DictCursor)

    sql="INSERT INTO product_details(product_name, product_description, product_cost, photo) VALUES (%s,%s,%s,%s)"

    data=( product_name, product_description, product_cost,filename)


    cursor.execute(sql,data)
#saving to database

    connection.commit()

    return jsonify ({"message":"Product details added successfully"})














# get products endpoint
@app.route("/api/getproductdetails")

def getproductdetails():
    connection=pymysql.connect(user="root" ,host="localhost" ,password="" ,database="simba-sokogarden")

    cursor=connection.cursor(pymysql.cursors.DictCursor)

    


    cursor.execute("select * from product_details")

    productdetails=cursor.fetchall()

    return jsonify(productdetails)

# MPESA PAYMENT API
# Making HTTP Requests to Safaricom Services
import requests
# Is a standard python module that allows you to get the current date and time, we will use it to generate the timestamp required by safaricom
import datetime
# library from flask that allows us to encode data to base64 format, this is required by safaricom to generate the password
import base64
# used to authenticate the user
from requests.auth import HTTPBasicAuth
# Creating route
@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
    # Extract POST Values sent
        amount = request.form['amount']
        phone = request.form['phone']

        # Provide consumer_key and consumer_secret provided by safaricom to authenticate your application to their services, this is used to generate the access token, which is a security token that allows you to make transactions with safaricom services
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        # Authenticate Yourself using above credentials to Safaricom Services, and Bearer Token this is used by safaricom for security identification purposes - Your are given Access
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" # AUTH URL
        # Provide your consumer_key and consumer_secret
        response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        # Get response as Dictionary
        data = response.json()
        # Retrieve the Provide Token
        # Token allows you to proceed with the transaction
        access_token = "Bearer" + ' ' + data['access_token']

        # GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S') # Current Time
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' # Passkey(Safaricom Provided)
        business_short_code = "174379" # Test Paybile (Safaricom Provided)
        # Combine above 3 Strings to get data variable
        data = business_short_code + passkey + timestamp
        # Encode to Base64
        encoded = base64.b64encode(data.encode())
        password = encoded.decode()

        # BODY OR PAYLOAD
        payload = {
        "BusinessShortCode": "174379",
        "Password":password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": '1', # use 1 when testing
        "PartyA": phone, # change to your number
        "PartyB": "174379",
        "PhoneNumber": phone,
        "CallBackURL": "https://coding.co.ke/api/confirm.php",
        "AccountReference": " chui SokoGarden Online",
        "TransactionDesc": "Payments for Products"
        }

        # POPULAING THE HTTP HEADER, PROVIDE THE TOKEN ISSUED EARLIER
        headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
        }

        # Specify STK Push Trigger URL
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        # Create a POST Request to above url, providing headers, payload
        # Below triggers an STK Push to the phone number indicated in the payload and the amount.
        response = requests.post(url, json=payload, headers=headers)
        print(response.text) #
        # Give a Response
        return jsonify({"message": "An MPESA Prompt has been sent to Your Phone, Please Check & Complete Payment"})







app.run(debug=True)
