import os
import json
import boto3
import Utils
from flask import Flask, request, jsonify


app = Flask(__name__)

# 1. Route for New Appointment Notification
@app.route('/notify/new_appointment', methods=['POST'])
def new_appointment_notification():
    data = request.json
    recipient_email = data.get("recipient_email", "bhavinbpalan90@gmail.com")
    appointment_date = data.get("appointment_date", "11/10/24")
    appointment_time = data.get("appointment_time", "05:00 PM")
    patient_name = data.get("patient_name", "Bhavin Palan")
    doctor_name = data.get("doctor_name", "Dr Patel")
    
    extra_vars = [{
        'appointment_date': appointment_date,
        'appointment_time': appointment_time,
        'patient_name': patient_name,
        'doctor_name': doctor_name
    }]
    
    Utils.sendNewAppointmentNotification(recipient_email, extra_vars)
    return jsonify({'message': 'New appointment email sent'}), 200

# 2. Route for Appointment Cancellation Notification
@app.route('/notify/cancel_appointment', methods=['POST'])
def cancel_appointment_notification():
    data = request.json
    recipient_email = data.get("recipient_email", "bhavinbpalan90@gmail.com")
    appointment_date = data.get("appointment_date", "11/10/24")
    appointment_time = data.get("appointment_time", "05:00 PM")
    patient_name = data.get("patient_name", "Bhavin Palan")
    doctor_name = data.get("doctor_name", "Dr Patel")
    
    extra_vars = [{
        'appointment_date': appointment_date,
        'appointment_time': appointment_time,
        'patient_name': patient_name,
        'doctor_name': doctor_name
    }]
    
    Utils.sendAppointmentCancellationNotification(recipient_email, extra_vars)
    return jsonify({'message': 'Cancellation email sent'}), 200

# 3. Route for Appointment Reschedule Notification
@app.route('/notify/reschedule_appointment', methods=['POST'])
def reschedule_appointment_notification():
    data = request.json
    recipient_email = data.get("recipient_email", "bhavinbpalan90@gmail.com")
    new_date = data.get("new_date", "11/14/24")
    old_date = data.get("old_date", "11/10/24")
    new_time = data.get("new_time", "1:00 PM")
    old_time = data.get("old_time", "11:00 AM")
    patient_name = data.get("patient_name", "Bhavin Palan")
    doctor_name = data.get("doctor_name", "Dr Patel")
    
    extra_vars = [{
        'new_date': new_date,
        'old_date': old_date,
        'new_time': new_time,
        'old_time': old_time,
        'patient_name': patient_name,
        'doctor_name': doctor_name
    }]
    
    Utils.sendAppointmentRescheduleNotification(recipient_email, extra_vars)
    return jsonify({'message': 'Reschedule email sent'}), 200

@app.route('/', methods=['GET'])
def notificationServerRunning():
    print("Server is Running...")
    return jsonify({'message': 'Server is Running...'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
