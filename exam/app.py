from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/letsencrypt/live/gpt.wx2486.me/fullchain.pem', '/etc/letsencrypt/live/gpt.wx2486.me/privkey.pem'))
