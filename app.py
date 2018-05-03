from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')



# login
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try agian.'
		else:
			return redirect(url_for('dashboard'))
	return render_template('login.html', error=error)



if __name__ == '__main__':
	app.run(debug=True)