from flask import Flask, send_from_directory, jsonify, render_template
from scraper import TrainScraper
import os

app = Flask(__name__)

@app.route('/trains_data/<train_destination>', methods=['GET'])
def get_trains_data(train_destination):
    # URL da cui recuperare i dati
    url = "https://iechub.rfi.it/ArriviPartenze/ArrivalsDepartures/Monitor?placeId=2416&arrivals=False"
    
    # Creazione dell'oggetto TrainScraper
    scraper = TrainScraper(url)
    
    # Parsing dei dati per la destinazione specificata
    try:
        train_data = scraper.parse_trains(train_destination)
        
        # Salva i dati in un file JSON
        file_path = 'trains_data.json'
        scraper.save_to_json(train_data, file_path)
        
        # Controlla se il file esiste e restituisci il file JSON
        if os.path.exists(file_path):
            return send_from_directory(directory='.', path=file_path, mimetype='application/json')
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        # Gestisci eventuali eccezioni
        return jsonify({"error": str(e)}), 500


# Route per servire la pagina HTML
@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
