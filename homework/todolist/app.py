import database as db
from flask import Flask, request, send_file

app = Flask(__name__)

db.create_table()

@app.route('/')
def index():
    return send_file('todolist.html')

# @app.route('/')

if __name__ == '__main__':
    app.run(debug=True)
