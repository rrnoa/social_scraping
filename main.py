from flask import Flask
from app.reddit_routes import reddit_bp
#from app.twitter_routes import twitter_bp  # Ruta futura para Twitter
# Importar otros blueprints si es necesario

app = Flask(__name__)

# Registrar los blueprints de cada red social
app.register_blueprint(reddit_bp, url_prefix='/reddit')
#app.register_blueprint(twitter_bp, url_prefix='/twitter')  # Para Twitter en el futuro

if __name__ == '__main__':
    app.run(debug=True)