from flask import Blueprint, jsonify
from app.services.reddit_service import buscar_temas_en_reddit

# Crear un blueprint para Reddit
reddit_bp = Blueprint('reddit', __name__)

# Ruta para buscar temas en Reddit
@reddit_bp.route('/buscar/<string:tema>', methods=['GET'])
def buscar_temas(tema):
    try:
        resultados = buscar_temas_en_reddit(tema)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
