import requests
import json

# URL of the API endpoint
url = 'http://a04aec4ee247c4b74afe0a0b88e403bc-1942226443.us-east-1.elb.amazonaws.com/notify/new_appointment'

# Headers for the request
headers = {
    'Content-Type': 'application/json',  # Specify the data format
    #'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # Example for Bearer token
    'Custom-Header': 'CustomValue'  # Additional custom headers, if needed
}

# Body of the request
data = {
  "recipient_email": "bhavinbpalan90@gmail.com",
  "appointment_date": "11/10/24",
  "appointment_time": "05:00 PM",
  "patient_name": "Bhavin Palan",
  "doctor_name": "Dr Patel"
}

json_data = json.dumps(data)

# Sending the POST request
response = requests.post(url, headers=headers, json=data)

print(response)

# Checking the response
if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.status_code, response.text)
