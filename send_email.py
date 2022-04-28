
import smtplib
conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('eldhopaulose2001@gmail.com', 'eldho_025')

# conn.sendmail('eldhopaulose2001@gmail.com','eldhopaulose0485@gmail.com','Subject: What you like? \n\n Reply Reply Reply')
# conn.quit()