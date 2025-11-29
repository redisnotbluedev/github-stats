from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return "<h1>404</h1>", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)