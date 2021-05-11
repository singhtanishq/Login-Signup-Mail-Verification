"""This module is being created to handle mail"""

#importing some required modules
import smtplib, ssl
import random

#defining a function to send mail
#taking 2 parameters email and name of reciever
def send_mail(para_email,para_name):
	#generating 4 dgit otp using randint function of random module
	gen_otp=random.randint(1111,9999)
	#storing valid informtions
	port = 465  
	smtp_server = "smtp.gmail.com"
	#here senders email is written
	sender_email = "senders_email_address"  
	#here receiver email will be assigned from parameter
	receiver_email = para_email
	#password of sender's email for login
	password = "senders_password"
	#message to be sent is written here
	#format of writing should be neccesarily the same to get the required result
	message = """\
Subject: Hello """+para_name+"""!
	
Welcome to TANISHQ ACCOUNTS,
OTP for account verification is """+str(gen_otp)+""".
	
Please do not share this OTP with anyone,
TANISHQ ACCOUNTS never calls you for OTP.
If this was a mistake and you are not the owner of this account,
kindly ignore this mail and do not forward this mail at any circumstances.
	
Thank You
Team TANISHQ ACCOUNTS"""
	
	#using built in function
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    #loging in
	    server.login(sender_email, password)
	    #sending mail to provided email id
	    server.sendmail(sender_email, receiver_email, message)
	#returning otp to verify in main menu
	return gen_otp
	

