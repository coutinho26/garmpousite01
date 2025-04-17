
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🟢 Garimpou está online!"

@app.route('/callback')
def callback():
    return "🔁 Callback recebido com sucesso!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
