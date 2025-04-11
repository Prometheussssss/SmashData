from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import json
import plotly

app = Flask(__name__)

@app.route('/')
def index():
    # Charger les données ELO (tu dois avoir un fichier avec au moins ces colonnes : 'date', 'elo', 'joueur')
    df = pd.read_csv('elo_timeseries_long.csv')
    df['date'] = pd.to_datetime(df['date'])

    # Créer le graphique interactif
    fig = px.line(
        df,
        x='date',
        y='elo',
        color='joueur',
        title='Evolution des cotes ELO des joueurs dans le temps'
    )

    fig.update_layout(template="plotly_white")

    # Convertir le graphique en JSON pour l'afficher dans HTML
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run()