import smtplib
to =input("Enter the email of recipient:\n")
content =input("Enter the content for email:\n")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()  #make the communication between smtp server and gmail
    server.starttls() #start
    server.login('sendergmail.com','12345678')
    server.sendmail('sendergmail.com',to,content)
    server.close()

    sendEmail(to,content)
