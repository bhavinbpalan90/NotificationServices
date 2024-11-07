# Use the official Python image
FROM amazonlinux:2

# Install necessary dependencies (example: install python3 and pip)
RUN yum install -y python3

# Set the working directory
WORKDIR /app

# Copy the entire contents of the current directory (local machine) into the /app directory in the container
COPY . /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]
