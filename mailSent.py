import smtplib     #smtp stands for Simple mail transfer protocol
server = smtplib.SMTP("smtp.gmail.com",587) # we are importing login and sendmailfunctions from SMTP class
server.starttls() # tls stands for transfer  layer security
server.login("mail address" , "mail password") #("gmail" ,"password")
server.sendmail("sent mail address" ," receiver mail address" , " message that we want to sent") #("sent mail" ,"receiver mail" , "msg that we want to sent")
print ("mail sent")