import crypt
 

def testPass(cryptPass,user):

	dicFile = open ('dict.txt','r')
	ctype = cryptPass.split("$")[1]
	passwordFound = False
	salt = cryptPass.split ("$")[2]
	insalt= "$" + ctype + "$" + salt + "$"
	for word in dicFile.readlines():
		word= word.strip('\n')
		cryptWord = crypt.crypt(word,insalt)
	if( cryptWord == cryptPass):
                passwordFound = True
		print "User: " + user + " Password: " + word +" \n"			
	if(passwordFound == False): 
		print "Password not found in dictionary."
			
exit	

def main(): 
                passwordFound = False
		passFile = open ('/etc/shadow','r')
         	for line in passFile.readlines():
			line = line.replace("\n","").split(":")
           	  	if  not line[1] in [ 'x', '*','!' ]:
          	 		user = line[0]
           	  		cryptPass = line[1]
				print "Cracking for user: " + user
           	  		testPass(cryptPass,user)
		if(passwordFound == None):
			print "User does not have a password"
                if(user == None):
                        print "User does not exist"
if __name__ == "__main__" :
	main()
	
