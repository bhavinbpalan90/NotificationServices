import pymysql
import boto3

# AWS RDS configuration
rds_host = "notificationdb.cdzgh7cofuep.us-east-1.rds.amazonaws.com"  # Endpoint of your RDS instance
db_name = "notificationdb"
username = "admin"
password = "Bits_ndb2010"
port = 3306


def create_database_and_table():
    try:
        # Connect without specifying the database
        connection = pymysql.connect(
            host=rds_host,
            user=username,
            password=password,
            port=port
        )

        with connection.cursor() as cursor:
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS notificationdb;")
            print("Database 'notificationdb' created or already exists.")

            # Now connect to the specific database to create the table
            connection.select_db("notificationdb")

            # SQL query to create a table
            create_table_query = """
            CREATE TABLE email_templates (
                id INT PRIMARY KEY AUTO_INCREMENT,
                template_name VARCHAR(50) NOT NULL,
                subject TEXT NOT NULL,
                body TEXT NOT NULL
            );
            """
            # Execute the query to create the table
            cursor.execute(create_table_query)
            print("Table 'email_templates' created successfully.")

        # Commit changes
        connection.commit()

    except pymysql.MySQLError as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()


def insertTemplate():
    try:
        # Connect without specifying the database
        connection = pymysql.connect(
            host=rds_host,
            user=username,
            password=password,
            port=port
        )

        with connection.cursor() as cursor:
        
            # Now connect to the specific database to create the table
            connection.select_db("notificationdb")

            # SQL query to create a table
            insert_query = """
            INSERT INTO email_templates (template_name, subject, body) VALUES
                ("appointment_schedule", 
                "Appointment Scheduled with {{ doctor_name }} on {{ appointment_date }}", 
                "Dear {{ patient_name }},\n\nYour appointment has been scheduled.\n\nAppointment Details:\n- Date: {{ appointment_date }}\n- Time: {{ appointment_time }}\n- Doctor: {{ doctor_name }}\n- Location: {{ location }}\n\nBest regards,\nYour Healthcare Team"
                );
            """
            # Execute the query to create the table
            cursor.execute(insert_query)
            print("Insert for Appointment Schedule completed successfully.")

            # Commit changes
            connection.commit()

            # SQL query to create a table
            insert_query = """
            INSERT INTO email_templates (template_name, subject, body) VALUES
                ("appointment_cancel", 
                "Appointment Cancellation Notice with {{ doctor_name }} on {{ appointment_date }}", 
                "Dear {{ patient_name }},\n\nWe regret to inform you that your appointment scheduled for {{ appointment_date }} with {{ doctor_name }} has been canceled.\n\nBest regards,\nYour Healthcare Team"
                );
            """
            # Execute the query to create the table
            cursor.execute(insert_query)
            print("Insert for Appointment Cancel completed successfully.")

            # Commit changes
            connection.commit()


            # SQL query to create a table
            insert_query = """
            INSERT INTO email_templates (template_name, subject, body) VALUES
            ("appointment_reschedule", 
             "Appointment Rescheduled with {{ doctor_name }} to {{ new_date }}", 
             "Dear {{ patient_name }},\n\nYour appointment originally scheduled for {{ old_date }} at {{ old_time }} with {{ doctor_name }} has been rescheduled.\n\nNew Appointment Details:\n- Date: {{ new_date }}\n- Time: {{ new_time }}\n\nBest regards,\nYour Healthcare Team"
            );

            """
            # Execute the query to create the table
            cursor.execute(insert_query)
            print("Insert for Appointment Reschedule completed successfully.")

            # Commit changes
            connection.commit()

    except pymysql.MySQLError as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()
    return 'Completed'


def insertTemplate():
    try:
        # Connect without specifying the database
        connection = pymysql.connect(
            host=rds_host,
            user=username,
            password=password,
            port=port
        )

        with connection.cursor() as cursor:
        
            # Now connect to the specific database to create the table
            connection.select_db("notificationdb")

            # SQL query to create a table
            insert_query = """
            select * from email_templates
            """
            # Execute the query to create the table
            cursor.execute(insert_query)
            print("Insert for Appointment Schedule completed successfully.")

            # Commit changes
            connection.commit()

            # SQL query to create a table
            insert_query = """
            INSERT INTO email_templates (template_name, subject, body) VALUES
                ("appointment_cancel", 
                "Appointment Cancellation Notice with {{ doctor_name }} on {{ appointment_date }}", 
                "Dear {{ patient_name }},\n\nWe regret to inform you that your appointment scheduled for {{ appointment_date }} with {{ doctor_name }} has been canceled.\n\nBest regards,\nYour Healthcare Team"
                );
            """
            # Execute the query to create the table
            cursor.execute(insert_query)
            print("Insert for Appointment Cancel completed successfully.")

            # Commit changes
            connection.commit()


            # SQL query to create a table
            insert_query = """
            INSERT INTO email_templates (template_name, subject, body) VALUES
            ("appointment_reschedule", 
             "Appointment Rescheduled with {{ doctor_name }} to {{ new_date }}", 
             "Dear {{ patient_name }},\n\nYour appointment originally scheduled for {{ old_date }} at {{ old_time }} with {{ doctor_name }} has been rescheduled.\n\nNew Appointment Details:\n- Date: {{ new_date }}\n- Time: {{ new_time }}\n\nBest regards,\nYour Healthcare Team"
            );

            """
            # Execute the query to create the table
            cursor.execute(insert_query)
            print("Insert for Appointment Reschedule completed successfully.")

            # Commit changes
            connection.commit()

    except pymysql.MySQLError as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()
    return 'Completed'


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

            # Now connect to the specific database to create the table
            connection.select_db("notificationdb")
            
            # Execute the query
            cursor.execute(query)
            # Fetch all results
            results = cursor.fetchall()
            
            # Print each row in the results
            for row in results:
                print(row)
                
    except pymysql.MySQLError as e:
        print("Error connecting to RDS MySQL:", e)
    finally:
        # Close the connection
        if connection:
            connection.close()

# Example Usage
query = "SELECT * FROM email_templates;"
query_rds(query)


### Run the function to create the database and table

#create_database_and_table()

### Run the function to Insert Templates into the DB

#print(insertTemplate())

