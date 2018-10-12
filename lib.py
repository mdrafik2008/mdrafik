import smtplib
import getpass

myemail="mahammdarafik2000@gmail.com"
password=getpass.getpass()
recemail="mpnaveenkumr@gmail.com"

s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

#authentication
s.login("mahammdarafik2000@gmail.com",7022803781)
#message to be send
message="hi"
#sending the mail
s.sendmail(myemail,recemail,message)

s.quit()