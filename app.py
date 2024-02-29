from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_user:password@localhost/flask_api_db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.query.all()
        users_list = []
        for user in users:
            users_list.append({'id': user.id, 'name': user.name})
        return jsonify(users_list)
    
    elif request.method == 'POST':
        data = request.get_json()
        new_user = User(name=data['name'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User added successfully !'})

if __name__ == '__main__':
    app.run(debug=True)
