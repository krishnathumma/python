import smtplib
import imghdr
from email.message import EmailMessage

SENDER = "pythonuser156@gmail.com"
PASSWORD = ""
RECEIVER = "pythonuser156@gmail.com"


def send_email(image_path):
    print("Send Email Function Start!")
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer Showed Up!"
    email_message.set_content("Hey! we just seen new Customer")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

    print("Send Email Function Ended!")


if __name__ == "__main__":
    send_email(image_path="images/11.png")
