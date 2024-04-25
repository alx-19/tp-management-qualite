import os
os.environ['FLASK_APP'] = 'app.py'

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clients = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extraction des données du formulaire
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        # Ajout du client à la "base de données"
        clients.append({'nom': nom, 'prenom': prenom})
        return redirect(url_for('index'))
    return render_template('index.html', clients=clients)

if __name__ == '__main__':
    app.run(debug=True)
