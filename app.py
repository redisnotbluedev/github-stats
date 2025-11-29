from flask import Flask, Response, request
import svgcards, requests

app = Flask(__name__)

@app.route("/repo/<owner>/<repo>")
def repo_card(owner, repo):
	# Fetch from GitHub API
	url = f"https://api.github.com/repos/{owner}/{repo}"
	resp = requests.get(url)
	data = resp.json()
	
	theme = request.args.get("theme", "auto")
	svg = svgcards.repo(data, theme)
	return Response(svg, mimetype="image/svg+xml")

@app.errorhandler(404)
def not_found(error):
	return "<h1>404</h1><p>Page not found. That's a good thing, knowing my code.</p>", 404

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)