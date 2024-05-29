import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL der API für D&D-Zauber
API_URL = "https://www.dnd5eapi.co/api/spells"


@app.route("/")
def index():
    # Abrufen der Liste der verfügbaren Zauber
    response = requests.get(API_URL)
    if response.status_code == 200:
        spells = response.json()["results"]
    else:
        spells = []

    return render_template("index.htm", spells=spells)


@app.route("/search", methods=["POST"])
def search():
    # Suchparameter aus dem Formular erhalten
    search_term = request.form.get("search")

    # API-Anfrage mit dem Suchparameter senden
    response = requests.get(f"{API_URL}?name={search_term}")

    if response.status_code == 200:
        spell_data = response.json()["results"]
    else:
        spell_data = []

    if not spell_data:
        return render_template(
            "index.htm", spells=[], search_term=search_term, not_found=True
        )

    # Vollständige Informationen zu allen gefundenen Zaubern abrufen
    spells = []
    for spell_info in spell_data:
        spell_url = spell_info["url"]
        spell_response = requests.get(f"https://www.dnd5eapi.co{spell_url}")
        if spell_response.status_code == 200:
            spell = spell_response.json()
            spells.append(spell)

    return render_template("index.htm", spells=spells, search_term=search_term)


@app.route("/spell/<index>")
def spell_details(index):
    # API-Anfrage, um die Details des Zaubers basierend auf dem Index zu erhalten
    response = requests.get(f"{API_URL}/{index}")

    if response.status_code == 200:
        spell = response.json()
        return render_template("spell_details.htm", spell=spell)
    else:
        return "Spell not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
