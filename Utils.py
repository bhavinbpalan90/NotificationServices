import smtplib
import pymysql
import boto3
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import html

from dotenv import dotenv_values
config = dotenv_values(".env")

# AWS SES SMTP server and port
SMTP_SERVER = "email-smtp.us-east-1.amazonaws.com"  # Use the correct region
SMTP_PORT = 587  # For STARTTLS, use port 587. For SSL, use port 465.

# Replace with your SMTP credentials
SMTP_USERNAME = config['SMTP_USERNAME']
SMTP_PASSWORD = config['SMTP_PASSWORD']


# AWS RDS configuration
rds_host = "notificationdb.cdzgh7cofuep.us-east-1.rds.amazonaws.com"  # Endpoint of your RDS instance
db_name = "notificationdb"
username = config['MYSQL_USER']
password = config['MYSQL_PASS']
port = 3306


# Function to execute a query and display the results
def query_rds(query):
    # Establish a connection to the RDS MySQL database
    try:
        # Connect without specifying the database
        connection = pymysql.connect(
            host=rds_host,
            user=username,
            password=password,
            port=port
        )
        
        with connection.cursor() as cursor:
            # Connect to the specific database
            connection.select_db("notificationdb")
            
            # Execute the query
            cursor.execute(query)
            
            # Fetch all results
            results = cursor.fetchall()
            
            # Get column names from cursor description
            columns = [desc[0] for desc in cursor.description]
            
            # Convert to a DataFrame
            df = pd.DataFrame(results, columns=columns)
            
            return df

            
                
    except pymysql.MySQLError as e:
        print("Error connecting to RDS MySQL:", e)
    finally:
        # Close the connection
        if connection:
            connection.close()


def getAppointmentTemplate(templateType):
    sqlQry = "SELECT * FROM email_templates where template_name = '" + templateType + "'"
    template = query_rds(sqlQry)
    return template


def format_email(row, vars_dict):
        # Merge additional variables directly passed to the function
        all_vars = vars_dict

        # Escape HTML special characters in the variables to prevent breaking HTML
        all_vars_safe = {key: html.escape(str(value)) for key, value in all_vars.items()}

        
        # Format the subject and body using the provided variables
        subject = row['subject'].format(**all_vars_safe)
        # Replace new line characters with <br> tags for HTML formatting
        body = row['body'].format(**all_vars_safe).replace('\n', '<br>')
        return pd.Series([subject, body])


def sendNewAppointmentNotification(emailId, extra_vars):
    sampleTemplate = getAppointmentTemplate('appointment_schedule')
    # Apply the function to each row, passing the corresponding variable dictionary from extra_vars
    sampleTemplate[['formatted_subject', 'formatted_body']] = [
        format_email(row, extra_vars[i]) for i, row in sampleTemplate.iterrows()
        ]

    subject = str(sampleTemplate.iloc[0]['formatted_subject'])
    body = str(sampleTemplate.iloc[0]['formatted_body'])

    ## Print Subject & Body
    #print("Subject is: ", subject)
    #print("Body of Email is: ", body)

    sendEmail(subject,emailId,body,body)

def sendAppointmentCancellationNotification(emailId, extra_vars):
    sampleTemplate = getAppointmentTemplate('appointment_cancel')
    # Apply the function to each row, passing the corresponding variable dictionary from extra_vars
    sampleTemplate[['formatted_subject', 'formatted_body']] = [
        format_email(row, extra_vars[i]) for i, row in sampleTemplate.iterrows()
        ]

    subject = str(sampleTemplate.iloc[0]['formatted_subject'])
    body = str(sampleTemplate.iloc[0]['formatted_body'])

    ## Print Subject & Body
    #print("Subject is: ", subject)
    #print("Body of Email is: ", body)

    sendEmail(subject,emailId,body,body)

def sendAppointmentRescheduleNotification(emailId, extra_vars):
    sampleTemplate = getAppointmentTemplate('appointment_reschedule')
    # Apply the function to each row, passing the corresponding variable dictionary from extra_vars
    sampleTemplate[['formatted_subject', 'formatted_body']] = [
        format_email(row, extra_vars[i]) for i, row in sampleTemplate.iterrows()
        ]

    subject = str(sampleTemplate.iloc[0]['formatted_subject'])
    body = str(sampleTemplate.iloc[0]['formatted_body'])

    ## Print Subject & Body
    #print("Subject is: ", subject)
    #print("Body of Email is: ", body)

    sendEmail(subject,emailId,body,body)



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


