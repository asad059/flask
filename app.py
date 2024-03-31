from flask import Flask
import psycopg2

app = Flask(__name__)

# Function to connect to PostgreSQL database
def connect_to_database():
    connection = psycopg2.connect(
        dbname='postgres',
        user='asad',
        password='PakistaN24@123',
        host='demo-db.postgres.database.azure.com',
        port='5432'
    )
    return connection

@app.route('/hello')
def hello():
    # Connect to the database
    connection = connect_to_database()
    cursor = connection.cursor()

    # Example: Execute a SQL query
    cursor.execute("SELECT * FROM demo_table")
    data = cursor.fetchall()

    # Close database connection
    cursor.close()
    connection.close()

    return str(data)

if __name__ == '__main__':
    app.run(debug=True)
