# Verwende ein offizielles Python 3.9 Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die requirements-Datei und installiere die Abhängigkeiten
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install werkzeug

# Kopiere den Inhalt des aktuellen Verzeichnisses in das Arbeitsverzeichnis im Container
COPY . .

# Exponiere den Port, auf dem die App läuft
EXPOSE 5000

# Setze die Umgebungsvariable für Flask
ENV FLASK_APP=app.py

# Starte die Flask-Anwendung
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
