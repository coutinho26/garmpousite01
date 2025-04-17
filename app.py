from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Garimpou site online!</h1><p>Acesse /callback para testar o redirecionamento do Mercado Livre.</p>"

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if code:
        return f"<h2>✅ Código de autorização recebido com sucesso!</h2><p>code: {code}</p>"
    else:
        return "<h2>⚠️ Nenhum código recebido.</h2><p>Verifique se a URL de redirect no Mercado Livre está correta.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

            
