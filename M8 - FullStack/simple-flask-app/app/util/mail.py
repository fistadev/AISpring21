import smtplib, ssl
# dotenv is the library to parse .env values
from dotenv import dotenv_values

config = dotenv_values(".env")

# instead of host , port , database and user we can use the following connection url
EMAIL_SENDER = config.get('EMAIL_SENDER')
EMAIL_PASSWORD = config.get('EMAIL_PASSWORD')
class Mail:

    def __init__(self):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = EMAIL_SENDER
        self.password = EMAIL_PASSWORD

    def send(self, email, subject, content):
        try:
            service = smtplib.SMTP(self.smtp_server_domain_name , self.port)
            service.ehlo()
            service.starttls()
            service.login(self.sender_mail, self.password)
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")
            print(result)
            service.quit()
            return True
        except smtplib.SMTPException as e:
            return False




