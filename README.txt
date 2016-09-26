					README

Instructions: you will have three files, one will be this file with the instructions, second one is the dict.txt which have many english words. Third one is thepython code which is the most important part of the assignment. 
Step1: open Linux on VM, download all the three files on VM
Step2: command ls to view if all the files are there in the directory that you saved in, cd to the folder they are saved in
step3: create a user, set the password, also add the password in the dist.txt file including all of the ones that were there already to crack the password, if you don't add the password in the dist.txt and save it, it will display an error message.
step4: then command "sudo python assignment2.py /etc/shadow" which will crack all user passwords.
Step5: it will display all errors if user does not exist or if password does not exist after the above command.
