from flask import Flask, jsonify, render_template
import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import platform

app = Flask(__name__)

# --- Paramètres seuils ---
SEUIL_TEMP = 35
SEUIL_HUM = 30
SEUIL_SOUND = 70

# --- Paramètres Email ---
EMAIL_FROM = "chaimaabidi909@gmail.com"
EMAIL_TO = "chaimaabidi909@gmail.com"
EMAIL_PASSWORD = "yfbuomotvufcopgo"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# --- Fonction pour envoyer un mail ---
def send_alert(subject, message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("⚡ Email envoyé !")
    except Exception as e:
        print("Erreur lors de l'envoi de l'email:", e)

# --- API Capteurs (simulés dynamiques) ---
@app.route('/capteurs')
def capteurs():
    # Température système
    temperature = 25
    if platform.system() == "Linux":
        temps = psutil.sensors_temperatures()
        if temps and "coretemp" in temps:
            temperature = temps["coretemp"][0].current
    else:
        # Sur Windows ou si psutil ne donne rien → simulation aléatoire
        temperature = round(random.uniform(20, 45), 1)

    # Humidité et son simulés dynamiques
    humidity = round(random.uniform(20, 70), 1)
    sound = round(random.uniform(20, 90), 1)

    # Vérification des seuils et envoi mail
    if temperature > SEUIL_TEMP:
        send_alert("⚠ Température Critique !", f"Température actuelle: {temperature} °C")
    if humidity < SEUIL_HUM:
        send_alert("⚠ Humidité Trop Basse !", f"Humidité actuelle: {humidity} %")
    if sound > SEUIL_SOUND:
        send_alert("⚠ Niveau Sonore Élevé !", f"Niveau sonore: {sound} dB")

    return jsonify({'temperature': temperature, 'humidity': humidity, 'sound': sound})

# --- Page Dashboard ---
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
