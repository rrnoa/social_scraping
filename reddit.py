from flask import Flask, jsonify
import praw

# Configurar PRAW con los datos obtenidos
reddit = praw.Reddit(
    client_id='lSogjOT8uNdHUAeRJqkUjg',
    client_secret='iTCJl7HmEntNeO4w6mxm5dXr4r_J5w',
    user_agent='my_reddit_scraper by /u/Shot-Cod-1189',
    username='Shot-Cod-1189',
    password='Baracoa.1982!'
)

# Verificar conexión a Reddit
try:
    # Intentar acceder a los datos del usuario actual
    user = reddit.user.me()
    print(f"Conectado a Reddit como: {user}")
except Exception as e:
    print(f"Error al conectar a Reddit: {e}")

# Iniciar la aplicación Flask
app = Flask(__name__)

# Ruta para buscar temas en Reddit
@app.route('/buscar/<string:tema>', methods=['GET'])
def buscar_temas(tema):
    resultados = []
    try:
        # Buscar temas en Reddit
        for resultado in reddit.subreddit('all').search(tema, limit=15):
            # Si el post tiene texto (selftext), lo obtenemos, de lo contrario, dejamos el campo vacío
            contenido = resultado.selftext if resultado.selftext else "No hay contenido en texto (selftext)."
            
            resultados.append({
                "titulo": resultado.title,
                "subreddit": str(resultado.subreddit),
                "url": resultado.url,
                "ups": resultado.ups,
                "comentarios": resultado.num_comments,
                "contenido": contenido  # Aquí incluimos el contenido del post
            })
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": f"Error al buscar en Reddit: {str(e)}"}), 500

# Iniciar el servidor Flask
if __name__ == '__main__':
    print("Iniciando el servidor Flask...")
    app.run(debug=True)
