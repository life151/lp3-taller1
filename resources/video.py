"""
Recursos y rutas para la API de videos
"""
from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models.video import VideoModel
from models import db

# Campos para serializar respuestas
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# Parser para los argumentos en solicitudes PUT (crear video)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Nombre del video es requerido", required=True)
video_put_args.add_argument("views", type=int, help="Número de vistas del video", required=True)
video_put_args.add_argument("likes", type=int, help="Número de likes del video", required=True)

# Parser para los argumentos en solicitudes PATCH (actualizar video)
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Nombre del video")
video_update_args.add_argument("views", type=int, help="Número de vistas del video")
video_update_args.add_argument("likes", type=int, help="Número de likes del video")

def abort_if_video_doesnt_exist(video_id):
    """
    Verifica si un video existe, y si no, aborta la solicitud
    
    Args:
        video_id (int): ID del video a verificar
    """
    video = VideoModel.query.filter_by(id=video_id).first()
    if not video:
        abort(404, message=f"No se encontró un video con el ID {video_id}")
    return video

class Videolist(Resource):
    
        

    
    """
    Recurso para gestionar videos individuales
    
    Métodos:
        get: Obtener un video por ID
        put: Crear un nuevo video
        patch: Actualizar un video existente
        delete: Eliminar un video
    """
    def get(self):
        
        
        """
        Obtiene un video por su ID
        
        Args:
            video_id (int): ID del video a obtener
            
        Returns:
            VideoModel: El video solicitado
        """
        # TODO
        # Obtener parámetros de búsqueda y paginación      
        search = request.args.get('search', '', type=str) 
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Construir la consulta
        query = VideoModel.query
        if search:
            query = query.filter(VideoModel.name.ilike(f"%{search}%"))

        # Paginación
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        videos = pagination.items
        

        result = []
        for video in videos:
            result.append({
                "id": video.id,
                "name": video.name,
                "views": video.views,
                "likes": video.likes
            })

        return jsonify({
            "videos": result,
            "total": pagination.total,
            "page": page,
            "per_page": per_page
        })
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        """
        Crea un nuevo video con un ID específico
        
        Args:
            video_id (int): ID para el nuevo video
            
        Returns:
            VideoModel: El video creado
        """
        # TODO
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        pass
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        """
        Actualiza un video existente
        
        Args:
            video_id (int): ID del video a actualizar
            
        Returns:
            VideoModel: El video actualizado
        """
        # TODO
        args = video_update_args.parse_args()
        video = abort_if_video_doesnt_exist(video_id)
        if args['name']:
            video.name = args['name']
        if args['views']:
            video.views = args['views']
        if args['likes']:
            video.likes = args['likes']
        db.session.commit()
        return video
        pass
    
    def delete(self, video_id):
        """
        Elimina un video existente
        
        Args:
            video_id (int): ID del video a eliminar
            
        Returns:
            str: Mensaje vacío con código 204
        """
        # TODO
        video =abort_if_video_doesnt_exist(video_id)
        db.session.delete(video)
        db.session.commit()
        return '', 204
        pass
