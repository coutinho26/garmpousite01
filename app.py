from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>✅ Garimpou site online!</h1><p>Acesse <code>/callback</code> após autorizar no Mercado Livre.</p>"

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if code:
        return f"""
            <h2>✅ Código de autorização recebido!</h2>
            <p><strong>Code:</strong> {code}</p>
            <p>Copie esse código e volte ao seu sistema local para trocar pelo token.</p>
        """
    else:
        return "<h2>⚠️ Nenhum código foi recebido.</h2><p>Verifique a URL de redirecionamento na app do Mercado Livre.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

