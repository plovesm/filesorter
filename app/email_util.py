# Import smtplib for the actual sending function
import smtplib


SENDER = ("", "")
RECEIVER = ""


class EmailUtils:

    @staticmethod
    def send_email(msg, sender=SENDER, receiver=RECEIVER):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender[0], sender[1])

        server.sendmail(sender[0], receiver, msg)
        server.quit()