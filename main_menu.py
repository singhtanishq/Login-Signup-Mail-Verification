#MAIN MENU of sign in/sign up

#importing inbuilt pickle module
import pickle
#importing user created module email_sending
import email_sending

#printing some welcoming lines
print('Welcome to TANISHQ ACCOUNTS')
print('Where you can create a secure account')
print()

#giving some options to the user
print('Options are as follows:')
print('     1. Sign in')
print('     2. Sign up')
print('Choose the appropriate one')
print()

#asking user to choose option and enter
ask=int(input('Enter your choice: '))
print()

#opening binary file in reading mode to load all data
mfile=open('database.dat','rb')
#trying to load data using load function of pickle module
try:
	data_dict=pickle.load(mfile)
	mfile.close()
#to avoid error if binary file is empty
except EOFError:
	mfile.close()
	data_dict=dict()

#case when user enters 1 to sign in
if ask==1:
	#case when database is not empty
	if len(data_dict)!=0:
		print('Your response shows that you are already a registered user')
		print()
		print('Now give some details of yours to proceed')
		#accepting login id and password
		user_id=input('     Enter your user ID: ')
		passwd=input('     Enter your password: ')
		print()
		#case when user id exists and password is also correct
		if user_id in data_dict.keys() and data_dict[user_id][2]==passwd:
			#fetching name and email from database
			name=data_dict[user_id][0]
			email=data_dict[user_id][3]
			print('We are sending an OTP to your email id')
			print()
			#sending otp through email and assigning that otp to an identifier
			OTP=email_sending.send_mail(email,name)
			print('An OTP has been sent to your email ID')
			#asking otp from the user
			passcode=int(input('Enter OTP: '))
			#case when user enters correct otp
			if passcode==OTP:
				#displaying successfully logged in
				print('Successfully logged in')
				mfile.close()
			#case when wrong otp entered
			else:
				print('Wrong OTP entered')
		#case when user id does not exists
		elif user_id not in data_dict.keys():
			print('User ID does not exist')
			ask=2
		#case when user id exists but password entered is incorrect
		else:
			print('Password incorect!')
    #case when database is empty
	else:
		mfile.close()
		print('Database is empty')
		ask=2
	
#case when user enters 2 to sign up			
elif ask==2:
	print('Since you are new user, let us register your new account')
	#asking user to enter details
	print('Give your informations:')
	#one by one accepting informations and saving in an identifier
	f_name=input('     Enter your first name: ')
	l_name=input('     Enter your last name: ')
	#concatenating first and last name
	name=f_name+' '+l_name
	age=int(input('     Enter your age: '))
	print()
	#asking user to create user id
	user_id=input('Create your user ID: ')
	#user id must not be already in use so asking again and again till the user id is unique
	while user_id in data_dict.keys():
		user_id=input('User ID you entered is already in use, try some other: ')
	#asking user to create password
	passwd=input('Create your password: ')
	#password must be alphanumeric if not asking user to create some other password
	while passwd.isalnum()==False:
		passwd=input('The password should be alpha numeric, try some other: ')
	print()
	#asking user to enter email id
	email=input('  Enter your email ID: ')
	print('Now the last step to confirm your identity')
	print('We are sending an OTP to your email...')
	print()
	#sending otp to given email id using our created function of email_sendind module
	OTP=email_sending.send_mail(email,name)
	print('An OTP has been sent to your email ID')
	#asking user to enter otp
	passcode=int(input('Enter OTP: '))
	#case when otp entered is correct
	if passcode==OTP:
		print('All your information has been saved.')
		#adding all informations to a dictionary
		data_dict[user_id]=[name,age,passwd,email]
		#opening binary file in writing mode
		myfile=open('database.dat','wb')
		#dumping the updated dictionary to binary file
		pickle.dump(data_dict,myfile)
		#closing the file
		myfile.close()
		print('Successfully Signed up')
	#case when otp entered is wromg
	else:
		print('Wrong OTP entered')

#case when wrong option is chosen
else:
	print('Wrong option chosen!')
	
