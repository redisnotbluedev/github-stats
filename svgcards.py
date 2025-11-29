def repo(repo_data, theme="auto"):
	name = repo_data["name"]
	desc = repo_data["description"] or "No description"
	stars = repo_data["stargazers_count"]
	forks = repo_data["forks_count"]
	language = repo_data["language"] or "Unknown"
	
	# Theme colors
	if theme == "dark":
		bg_color = "#0d1117"
		header_bg = "#161b22"
		border_color = "#30363d"
		title_color = "#58a6ff"
		text_color = "#c9d1d9"
		muted_color = "#8b949e"
		icon_color = "#8b949e"
	elif theme == "light":
		bg_color = "#ffffff"
		header_bg = "#f6f8fa"
		border_color = "#d1d9e0"
		title_color = "#0969da"
		text_color = "#24292f"
		muted_color = "#656d76"
		icon_color = "#656d76"
	else:  # auto theme - will use CSS variables and media queries
		bg_color = "var(--bg-color)"
		header_bg = "var(--header-bg)"
		border_color = "var(--border-color)"
		title_color = "var(--title-color)"
		text_color = "var(--text-color)"
		muted_color = "var(--muted-color)"
		icon_color = "var(--icon-color)"
	
	# Language color mapping (common languages)
	language_colors = {
		"Python": "#3572A5",
		"JavaScript": "#f1e05a",
		"TypeScript": "#3178c6",
		"Java": "#b07219",
		"C++": "#f34b7d",
		"C": "#555555",
		"C#": "#239120",
		"Go": "#00ADD8",
		"Rust": "#dea584",
		"PHP": "#4F5D95",
		"Ruby": "#701516",
		"Swift": "#fa7343",
		"Kotlin": "#A97BFF",
		"HTML": "#e34c26",
		"CSS": "#1572B6",
		"Shell": "#89e051",
		"Unknown": "#8b949e"
	}
	
	lang_color = language_colors.get(language, "#8b949e")
	
	# CSS for auto theme
	css_styles = ""
	if theme == "auto":
		css_styles = """
		<style>
			:root {
				--bg-color: #ffffff;
				--header-bg: #f6f8fa;
				--border-color: #d1d9e0;
				--title-color: #0969da;
				--text-color: #24292f;
				--muted-color: #656d76;
				--icon-color: #656d76;
			}
			
			@media (prefers-color-scheme: dark) {
				:root {
					--bg-color: #0d1117;
					--header-bg: #161b22;
					--border-color: #30363d;
					--title-color: #58a6ff;
					--text-color: #c9d1d9;
					--muted-color: #8b949e;
					--icon-color: #8b949e;
				}
			}
		</style>
		"""
	
	svg = f"""<svg width="450" height="180" xmlns="http://www.w3.org/2000/svg">
		{css_styles}
		<!-- Definitions for gradients and shadows -->
		<defs>
			<linearGradient id="bgGradient" x1="0%" y1="0%" x2="0%" y2="100%">
				<stop offset="0%" style="stop-color:{header_bg};stop-opacity:1" />
				<stop offset="100%" style="stop-color:{bg_color};stop-opacity:1" />
			</linearGradient>
			<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
				<feDropShadow dx="0" dy="2" flood-color="#000000" flood-opacity="0.1"/>
			</filter>
		</defs>
		
		<!-- Background with gradient and border -->
		<rect width="450" height="180" fill="url(#bgGradient)" rx="8" stroke="{border_color}" stroke-width="1" filter="url(#shadow)"/>
		
		<!-- Header section -->
		<rect width="450" height="50" fill="{header_bg}" rx="8"/>
		<rect y="42" width="450" height="8" fill="url(#bgGradient)"/>
		
		<!-- Repository icon -->
		<g transform="translate(15, 18)">
			<svg width="16" height="16" viewBox="0 0 16 16" fill="{title_color}">
				<path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/>
			</svg>
		</g>
		
		<!-- Title -->
		<text x="40" y="30" fill="{title_color}" font-size="16" font-weight="600" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">{name}</text>
		
		<!-- Description -->
		<text x="20" y="75" fill="{text_color}" font-size="13" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">
			<tspan>{desc[:65]}{"..." if len(desc) > 65 else ""}</tspan>
		</text>
		
		<!-- Language indicator -->
		<circle cx="25" cy="105" r="6" fill="{lang_color}"/>
		<text x="40" y="110" fill="{muted_color}" font-size="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">{language}</text>
		
		<!-- Stars with icon -->
		<g transform="translate(20, 130)">
			<svg width="14" height="14" viewBox="0 0 16 16" fill="{icon_color}">
				<path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"/>
			</svg>
		</g>
		<text x="42" y="142" fill="{muted_color}" font-size="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">{stars:,}</text>
		
		<!-- Forks with icon -->
		<g transform="translate(100, 130)">
			<svg width="14" height="14" viewBox="0 0 16 16" fill="{icon_color}">
				<path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"/>
			</svg>
		</g>
		<text x="122" y="142" fill="{muted_color}" font-size="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">{forks:,}</text>
		
		<!-- Updated timestamp -->
		<text x="350" y="170" fill="{muted_color}" font-size="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" opacity="0.7">Updated recently</text>
	</svg>"""
	
	return svg