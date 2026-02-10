from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/home")
def api_home():
    return jsonify({
        "title": "Hi, I'm Agnel 👋",
        "message": "I’m learning Python and building web apps using Flask."
    })

@app.route("/api/about")
def api_about():
    return jsonify({
        "title": "About Me",
        "message": "I am a beginner web developer learning Python, HTML, CSS, and JavaScript."
    })

@app.route("/api/projects")
def api_projects():
    return jsonify({
        "title": "My Projects",
        "projects": [
            "My First Python Website",
            "Flask API App",
            "Single Page Portfolio Website"
        ]
    })

if __name__ == "__main__":
    app.run()
