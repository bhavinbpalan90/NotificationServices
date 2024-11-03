import os
import json
import boto3
import Utils
from flask import Flask, request


app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    recipient_email = "bhavinbpalan90@gmail.com" 
    appointment_date = "11/10/24"
    appointment_time = "05:00 PM"
    patient_name = "Bhavin Palan"
    doctor_name = "Dr Test"
    new_date = "11/14/24"
    old_date = "11/10/24"
    new_time = "1:00 PM"
    old_time = "11:00 AM"

    extra_vars = [{'appointment_date': appointment_date, 'patient_name' : patient_name, 'doctor_name' : doctor_name,
                'appointment_time' : appointment_time, 'new_date' : new_date, 'old_date' : old_date
                    , 'new_time' : new_time, 'old_time' : old_time }]

    Utils.sendNewAppointmentNotification(recipient_email, extra_vars)
    Utils.sendAppointmentCancellationNotification(recipient_email, extra_vars)
    Utils.sendAppointmentRescheduleNotification(recipient_email, extra_vars)
    return {'message': 'Email sent', 'response': 'Completed'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
