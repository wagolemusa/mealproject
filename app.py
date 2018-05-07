from flask import Flask, jsonify, render_template, redirect, request, url_for, session, flash

from functools import wraps

from data import Articles

app = Flask(__name__)


app.secret_key = "my precious"

Articles = Articles()

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap
 



@app.route('/')
def home():
	return render_template('index.html')

@app.route('/welcome')
@login_required
def welcome():
	return render_template('welcome.html')

@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html')


@app.route('/register')
def register():
	return redirect(url_for('register_page'))
@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
def register_page():
	error = None
	if request.method == 'POST':
	    return redirect(url_for('register.html'))
	return render_template('register.html', error=error)


@app.route('/meals')
def meals():
	return render_template('meals.html', articles=Articles)

# login
@app.route('/login')
def login():
	return redirect(url_for('login_page'))

@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login_page():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try agian.'
		else:
			session['logged_in'] = True
			flash('You were just logged_in!')
			return redirect(url_for('welcome'))
	return render_template('login.html', error=error)



@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(debug=True)