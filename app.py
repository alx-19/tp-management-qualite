from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    date_naissance = db.Column(db.String(10), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    cp = db.Column(db.String(5), nullable=False)
    ville = db.Column(db.String(100), nullable=False)

# Mettre en place le contexte de l'application pour créer les tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_client = Client(
            nom=request.form['nom'],
            prenom=request.form['prenom'],
            date_naissance=request.form['date_naissance'],
            adresse=request.form['adresse'],
            cp=request.form['cp'],
            ville=request.form['ville']
        )
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('index'))
    clients = Client.query.all()
    return render_template('index.html', clients=clients)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    client = Client.query.get_or_404(id)
    if request.method == 'POST':
        client.nom = request.form['nom']
        client.prenom = request.form['prenom']
        client.date_naissance = request.form['date_naissance']
        client.adresse = request.form['adresse']
        client.cp = request.form['cp']
        client.ville = request.form['ville']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', client=client)

@app.route('/delete/<int:id>')
def delete(id):
    client_to_delete = Client.query.get_or_404(id)
    db.session.delete(client_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
