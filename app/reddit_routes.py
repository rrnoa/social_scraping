from flask import Blueprint, jsonify, request
from app.services.reddit_service import buscar_temas_en_subreddits

# Crear un blueprint para Reddit
reddit_bp = Blueprint('reddit', __name__)

# Ruta para buscar temas en múltiples subreddits
@reddit_bp.route('/buscar', methods=['GET'])
def buscar_temas():
    # Obtener los subreddits, la consulta de búsqueda y el parámetro de orden desde la URL
    subreddits = request.args.get('subreddits')  # Ejemplo: 'personalfinance,frugal'
    query = request.args.get('query')  # El término de búsqueda
    sort = request.args.get('sort', 'hot')  # Valor por defecto: 'hot'
    comments_limit = request.args.get('comments_limit', default=3, type=int)  # Limitar los comentarios

    if not subreddits or not query:
        return jsonify({"error": "Debe proporcionar subreddits y un criterio de búsqueda."}), 400

    # Convertir los subreddits en una lista
    subreddits_list = subreddits.split(',')

    # Validar que el valor de `sort` sea uno de los valores permitidos
    if sort not in ['hot', 'new', 'top', 'comments']:
        return jsonify({"error": f"Valor de 'sort' no válido: {sort}. Los valores válidos son 'hot', 'new', 'top', 'comments'."}), 400

    try:
        # Obtener los resultados desde el servicio de Reddit
        resultados = buscar_temas_en_subreddits(subreddits_list, query, sort=sort, comentarios_limite=comments_limit)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
