import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

# --- CREDENCIALES ---
TELEGRAM_BOT_TOKEN = "8553728262:AAG8etggxHJzjE7Z6POphudVXYmr9jsP65w" 
ADMIN_CHAT_ID = "8345213799" 
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

app = Flask(__name__)
CORS(app)

@app.route('/send-telegram', methods=['POST'])
def send_telegram():
    data = request.json
    print("📩 Recibiendo solicitud...")

    mensaje = f"""
*✨ Nueva Cita en Pink Bliss ✨*
👤 *Cliente:* {data.get('clientName')}
📱 *Contacto:* `{data.get('clientContact')}`
💇‍♀️ *Servicio:* {data.get('serviceName')}
📅 *Fecha:* {data.get('formattedTime')}
"""

    try:
        response = requests.post(TELEGRAM_API_URL, json={
            "chat_id": ADMIN_CHAT_ID, 
            "text": mensaje, 
            "parse_mode": "Markdown"
        })
        
        if response.status_code == 200:
            print("✅ Mensaje enviado a Telegram")
            return jsonify({"status": "success"})
        else:
            print(f"❌ Error Telegram: {response.text}")
            return jsonify({"status": "error", "telegram_error": response.text}), 500

    except Exception as e:
        print(f"❌ Error interno: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("--- 🚀 SERVIDOR LISTO ---")
    app.run(host='127.0.0.1', port=5000, debug=True)