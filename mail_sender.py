import smtplib

    #FOR  TLS
#smtpObj = smtplib.SMTP('smtp.gmailcom ' , 587)
#smtpObj.ehlo()


    #FOR SSH 
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com ' , 465)
smtpObj.ehlo()


#starting TLS encryption 
smtpObj.starttls()

password = input("ENTER YOUR PASSWORD ")
#LOGGING INTO THE smtp server 
smtpObj.login('haedermaikwando@gmail.com' ,password)
#SENDING THE EMAIL MESSAGE 
smtpObj.sendmail('haedermaikwando#gmail.com' ,'thegreatesthumanbeign@gmail.com', 'subject:so  long .\nDera Alice  , so  long thanks for the fish . sincerely, Ali')

#finishing and quiting 
smtpObj.quit()
