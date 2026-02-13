from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/pru'
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

#db.create_all() # create tables if not exist

@app.route('/')
def hello_world():
    person = Person.query.first()
    if person:  
        return f'Hello, {person.name}!'
    return 'Hello, World!'  

# Alternative for running flask app: 
# FLASK_APP=flask-hello-app.py FLASK_DEBUG=true flask run

# if __name__ == "__main__":
#     app.run()    # localhost:5000  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    #app.debug = True
    app.run(host='0.0.0.0', port=3000)    
# 127.0.0.1 - - [17/Jan/2026 13:30:39] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [17/Jan/2026 13:30:39] "GET /favicon.ico HTTP/1.1" 404 - ??????