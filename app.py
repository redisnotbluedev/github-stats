from flask import Flask

app = Flask(__name__)

@app.route("/repo/<path:repo>")
def repo(repo):
    return f"<h1>Repository: {repo}</h1>"

@app.errorhandler(404)
def not_found(error):
    return "<h1>404</h1><p>Page not found. That's a good thing, knowing my code.</p>", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)