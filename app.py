from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🧬 Nightingale Genetics Lab</h1>
    <p>If you can see this, your deployment works.</p>
    """

if __name__ == "__main__":
    app.run()