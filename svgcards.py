def repo(repo_data):
	name = repo_data["name"]
	desc = repo_data["description"] or "No description"
	stars = repo_data["stargazers_count"]
	forks = repo_data["forks_count"]
	language = repo_data["language"] or "Unknown"
	
	svg = f"""<svg width="450" height="180" xmlns="http://www.w3.org/2000/svg">
		<!-- Background -->
		<rect width="450" height="180" fill="#0d1117" rx="6"/>
		<rect width="450" height="40" fill="#161b22" rx="6"/>
		
		<!-- Title -->
		<text x="15" y="27" fill="#58a6ff" font-size="18" font-weight="bold" font-family="system-ui">{name}</text>
		
		<!-- Description -->
		<text x="15" y="70" fill="#c9d1d9" font-size="13" font-family="system-ui">{desc[:60]}</text>
		
		<!-- Language -->
		<circle cx="20" cy="110" r="6" fill="#3572A5"/>
		<text x="32" y="115" fill="#8b949e" font-size="12" font-family="system-ui">{language}</text>
		
		<!-- Stats -->
		<text x="15" y="145" fill="#8b949e" font-size="12" font-family="system-ui">⭐ {stars}</text>
		<text x="80" y="145" fill="#8b949e" font-size="12" font-family="system-ui">🍴 {forks}</text>
	</svg>"""
	
	return svg