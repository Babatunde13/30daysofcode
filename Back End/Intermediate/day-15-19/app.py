from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from forms import AddToDo, load_db, save_db
from hashlib import sha224
app = Flask(__name__)

manager = Manager(app)

mail = Mail(app)
bootstrap = Bootstrap(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)

app.config['SECRET_KEY']='565acc74f58aa1c55de7c8cf080646ef'

@app.route('/')
def home():
    return render_template('home.html')

total_data = load_db()

@app.route('/add-app/', methods=['POST', 'GET'])
def add_todo():
    forms = AddToDo()
    if request.method == 'POST':
        user = 'babatunde'
         
        for details in total_data:
            if details["user"]==user:
                user_data = details["details"]
                for item in request.form:
                    if item in user_data['app']:
                        user_data['app'][item].append(request.form[item])
                print(user_data)
                save_db(total_data)
                len_ = 1 #len(user_data['title'])
                return redirect(url_for('todo', data=user_data, len_=len_))
        
    # forms = AddToDo

    return render_template('add_app.html', form=forms)

@app.route('/todolist/')
def todo():

    return render_template('app.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        for data in total_data:
            if data['user']==user and data['details']['password']==sha224(request.form['password'].encode('utf-8')).hexdigest():
                return redirect(url_for('todo', name=user))
        else:
            flash('Invalid Email or Password')
            return render_template('login.html')
    return render_template('login.html')



@app.route('/signup/', methods=['POST', 'GET'])
def signup():
	if request.method == 'POST':
		user = request.form['username']
		object_user = {
			'user': user,
            "details": {
                "app": {
                    "title": [], 
                        "date": [], 
                        "description": []
                        },
			'email': request.form['email'],
			'password': sha224(request.form['password'].encode('utf-8')).hexdigest(),
            'full name': request.form['First Name']+ ' '+ request.form['Last Name']
		}
		for d in total_data:
			if d['user'] == object_user['user']:
					flash('Already a registered user Login again')
					return render_template('login.html')
		total_data.append(object_user)
		save_db(total_data)

		return redirect(url_for('todolist', name=user))

	return render_template('signup.html', title='SignUp Page')


if __name__ == "__main__":
    app.run()