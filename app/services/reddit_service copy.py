import praw

# Configurar PRAW
reddit = praw.Reddit(
    client_id='lSogjOT8uNdHUAeRJqkUjg',
    client_secret='iTCJl7HmEntNeO4w6mxm5dXr4r_J5w',
    user_agent='my_reddit_scraper by /u/Shot-Cod-1189',
    username='Shot-Cod-1189',
    password='Baracoa.1982!'
)

def buscar_temas_en_reddit(tema, limite=50):
    resultados = []
    for resultado in reddit.subreddit('all').search(tema, limit=limite):
        contenido = resultado.selftext if resultado.selftext else "No hay contenido."
        resultados.append({
            "titulo": resultado.title,
            "subreddit": str(resultado.subreddit),
            "url": resultado.url,
            "ups": resultado.ups,
            "comentarios": resultado.num_comments,
            "contenido": contenido
        })
    return resultados
