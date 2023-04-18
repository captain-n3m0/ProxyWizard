from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Define a list of valid usernames and passwords for login validation
valid_users = {'admin': 'password', 'user1': '123456'}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/config', methods=['POST'])
def update_config():
    # Get input values from form
    username = request.form['username']
    password = request.form['password']
    proxy_host = request.form['proxy_host']
    proxy_port = int(request.form['proxy_port'])
    target_host = request.form['target_host']
    target_port = int(request.form['target_port'])

    # Perform login validation
    if username in valid_users and valid_users[username] == password:
        # Update proxy server configuration
        os.environ['PROXY_HOST'] = proxy_host
        os.environ['PROXY_PORT'] = str(proxy_port)
        os.environ['TARGET_HOST'] = target_host
        os.environ['TARGET_PORT'] = str(target_port)

        return render_template('index.html', message='Configuration updated.')
    else:
        # Redirect to login page with error message
        return redirect(url_for('home', error='Invalid username or password.'))

if __name__ == '__main__':
    app.run(debug=True)
