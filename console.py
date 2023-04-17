from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/config', methods=['POST'])
def update_config():
    proxy_host = request.form['proxy_host']
    proxy_port = int(request.form['proxy_port'])
    target_host = request.form['target_host']
    target_port = int(request.form['target_port'])

    # Update proxy server configuration
    os.environ['PROXY_HOST'] = proxy_host
    os.environ['PROXY_PORT'] = str(proxy_port)
    os.environ['TARGET_HOST'] = target_host
    os.environ['TARGET_PORT'] = str(target_port)

    return render_template('index.html', message='Configuration updated.')

if __name__ == '__main__':
    app.run(debug=True)
