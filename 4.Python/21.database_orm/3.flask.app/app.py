#pip install flask-sqlalchemy
from flask import Flask, render_template, request, redirect
from model import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///example.db'
db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    #필요한 에러체크를 넣어야함
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')    #redirect(url_for('index'))가 좀 더 나은 코드이기는 함

@app.route('/delete/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print('사용자 없음: ', id)
    return redirect('/')

@app.route('/modify/<int:id>', methods=['GET', 'POST'])
def modify_user(id):
    user = db.session.get(User, id)
    if request.method == 'POST':
        age = request.form['age']
        name = request.form['name']
        user.age = int(age)
        user.name = name
        db.session.commit()
        return redirect('/')
    return render_template('modify.html', user=user)


if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)

