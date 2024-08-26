# Usa una immagine base Python
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice nell'immagine
COPY . .

# Espone la porta su cui l'app Flask gira
EXPOSE 5000

# Comando per eseguire l'app Flask
CMD ["python", "app.py"]
