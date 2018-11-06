from email.mime.text import MIMEText
import smtplib

def send_email(email, height, avg, count):
    from_email="maritonski@gmail.com"
    from_password="********"
    to_email=email

    subject="Height data"
    message="Zdravo machkice tvojata visina e <strong>%s</strong>  <3 <3 <3 <3 <3. <br> Average height of all entries is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br> Danke. " % (height, avg, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
