import praw

# Configurar PRAW
reddit = praw.Reddit(
    client_id='lSogjOT8uNdHUAeRJqkUjg',
    client_secret='iTCJl7HmEntNeO4w6mxm5dXr4r_J5w',
    user_agent='my_reddit_scraper by /u/Shot-Cod-1189',
    username='Shot-Cod-1189',
    password='Baracoa.1982!'
)

def obtener_comentarios(post, limite=3):
    """Obtener los primeros `limite` comentarios de una publicación."""
    comentarios = []
    post.comments.replace_more(limit=0)  # Esto elimina los comentarios "more" (cargar más)
    
    # Iterar sobre los primeros comentarios
    for comment in post.comments[:limite]:
        comentarios.append({
            "autor": str(comment.author),
            "contenido": comment.body,
            "ups": comment.ups,
            "creado": comment.created_utc
        })
    return comentarios

def buscar_temas_en_subreddits(subreddits_list, query, limite=40, sort='hot', comentarios_limite=3):
    resultados = []
    try:
        # Iterar sobre cada subreddit de la lista proporcionada
        for subreddit_name in subreddits_list:
            subreddit = reddit.subreddit(subreddit_name.strip())  # Limpiar espacios
            
            # Buscar en el subreddit con el criterio de orden (sort)
            for post in subreddit.search(query, limit=limite, sort=sort):
                # Obtener los comentarios de la publicación
                comentarios = obtener_comentarios(post, limite=comentarios_limite)
                
                resultados.append({
                    "subreddit": subreddit_name,
                    "titulo": post.title,
                    "url": post.url,
                    "ups": post.ups,
                    "comentarios_totales": post.num_comments,
                    "contenido": post.selftext if post.selftext else "No hay contenido en texto.",
                    "comentarios": comentarios  # Incluir los comentarios
                })
        return resultados
    except Exception as e:
        raise RuntimeError(f"Error al buscar en Reddit: {str(e)}")
