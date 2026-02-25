from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sandbox")
def sandbox():
    return render_template("sandbox.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    p1 = data["parent1"]
    p2 = data["parent2"]
    litter = int(data["litter"])

    offspring = []
    for _ in range(litter):
        allele1 = random.choice(p1)
        allele2 = random.choice(p2)
        offspring.append(allele1 + allele2)

    return jsonify({"offspring": offspring})

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
