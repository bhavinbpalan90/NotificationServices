import Utils

recipient_email = "bhavinbpalan90@gmail.com" 
appointmentNo = "AAJH123XS"
appointmentDate = "11/10/24"
patientName = "Bhavin Palan"
doctorName = "Dr Test"

Utils.newAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName)
Utils.cancelAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName)
Utils.rescheduleAppointment(recipient_email,appointmentNo,appointmentDate,patientName,doctorName)