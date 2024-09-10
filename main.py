from flask import Flask
from app.reddit_routes import reddit_bp

# Crear la aplicación Flask
app = Flask(__name__)

# Registrar el blueprint de Reddit con el prefijo '/reddit'
app.register_blueprint(reddit_bp, url_prefix='/reddit')

if __name__ == '__main__':
    print("Iniciando el servidor Flask...")
    app.run(debug=True)