from flask import Flask, request

from connection import db_conn

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "INFO: This Microservice is used for adding record to the Database"

@app.route('/create', methods=['POST'])
def create():

    data = request.get_json()
    stud_name = data.get('name')
    db_cursor = db_conn.cursor()
    query = "INSERT INTO student (name) VALUES (%s)"
    value = {stud_name} 
    db_cursor.execute(query, value)
    db_conn.commit()

    return f"Record added for {stud_name} successfully!"
  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)
db_conn.close()



