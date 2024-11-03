import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import dotenv_values
config = dotenv_values(".env")

# AWS SES SMTP server and port
SMTP_SERVER = "email-smtp.us-east-1.amazonaws.com"  # Use the correct region
SMTP_PORT = 587  # For STARTTLS, use port 587. For SSL, use port 465.

# Replace with your SMTP credentials
SMTP_USERNAME = config['SMTP_USERNAME']
SMTP_PASSWORD = config['SMTP_PASSWORD']


def sendEmail(subject, recipient_email, body_text, body_html):

    sender_email = "admin@bhavinpalan.com"

    # Create the email content
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    # Add the plain-text and HTML parts to the message
    part1 = MIMEText(body_text, "plain")
    part2 = MIMEText(body_html, "html")
    message.attach(part1)
    message.attach(part2)

    # Send the email using SMTP
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

def newAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName):
    # Replace with the recipient's email
    subject = "New Appointment Confirmation"
    body_text = f"""Dear {patientName}, 
                This is to confirm your appointment {appointmentNo} on {appointmentDate} with {doctorName}. 
                Please reach out to us in case of any changes needed. Thanks, Healthcare"""
    body_html = f"""<html>
    <head></head>
    <body>
    <h1>Appointment Confirmation</h1>
    <p><br>Dear {patientName}, <br><br>
                This is to confirm your appointment {appointmentNo} on {appointmentDate} with {doctorName}. <br> <br>
                Please reach out to us in case of any changes needed. 
                <br><br>
                Thanks, Healthcare</p>
    </body>
    </html>
    """
    sendEmail(subject, recipient_email, body_text, body_html)


def cancelAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName):
    # Replace with the recipient's email
    subject = "Appointment Cancellation Confirmation"
    body_text = f"""Dear {patientName}, 
                This is to confirm cancellation of your appointment {appointmentNo} on {appointmentDate} with {doctorName}. 
                Please reach out to us in case if you need to setup new appointment. Thanks, Healthcare"""
    body_html = f"""<html>
    <head></head>
    <body>
    <h1>Appointment Cancellation Confirmation</h1>
    <p><br>Dear {patientName}, <br><br>
                This is to confirm cancellation of your appointment {appointmentNo} on {appointmentDate} with {doctorName}. <br> <br>
                Please reach out to us in case if you need to setup new appointment. 
                <br><br>
                Thanks, Healthcare</p>
    </body>
    </html>
    """
    sendEmail(subject, recipient_email, body_text, body_html)


def rescheduleAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName):
    # Replace with the recipient's email
    subject = "Appointment Reschedule Confirmation"
    body_text = f"""Dear {patientName}, 
                This is to confirm reschedule of your appointment {appointmentNo} to new data {appointmentDate} with {doctorName}. 
                Please reach out to us in case if needed any assistance. Thanks, Healthcare"""
    body_html = f"""<html>
    <head></head>
    <body>
    <h1>Appointment Reschedule Confirmation</h1>
    <p><br>Dear {patientName}, <br><br>
                This is to confirm reschedule of your appointment {appointmentNo} to new data {appointmentDate} with {doctorName}. <br> <br>
                Please reach out to us in case if needed any assistance. 
                <br><br>
                Thanks, Healthcare</p>
    </body>
    </html>
    """
    sendEmail(subject, recipient_email, body_text, body_html)


recipient_email = "bhavinbpalan90@gmail.com" 
appointmentNo = "AAJH123XS"
appointmentDate = "11/10/24"
patientName = "Bhavin Palan"
doctorName = "Dr Test"

newAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName)
cancelAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName)
rescheduleAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName)