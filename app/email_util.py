# Import smtplib for the actual sending function
import smtplib

from app.key_store import KeyStore

key_store = KeyStore()

SENDER = (key_store.get_sender_email(), key_store.get_sender_pwd())
RECEIVER = key_store.get_receiver()


class EmailUtils:

    @staticmethod
    def send_email(msg, sender=SENDER, receiver=RECEIVER):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender[0], sender[1])

        server.sendmail(sender[0], receiver, msg)
        server.quit()
