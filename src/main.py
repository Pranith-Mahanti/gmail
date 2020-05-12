#!/usr/bin/env python3.7
import sys
import smtplib
def read_creds():
    with open("mailto.conf", "r") as file:
        creds = file.readlines()
    return creds

def send_mail():
    creds = read_creds()
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(creds[0], creds[1])

        to = sys.argv[1]
        try:
            subject = sys.argv[2]
        except:
            subject = input("Enter the subject: ")
        try:
            body = sys.argv[3]
        except:
            body = input("Enter the message: ")

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(creds[0], to, msg)

if __name__ == "__main__":
    send_mail()
