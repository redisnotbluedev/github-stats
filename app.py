from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>404</h1>", 404

if __name__ == "__main__":
    app.run(port=80)