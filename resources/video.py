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

# Parser para solicitudes PUT (crear video)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Nombre del video es requerido", required=True)
video_put_args.add_argument("views", type=int, help="Número de vistas del video", required=True)
video_put_args.add_argument("likes", type=int, help="Número de likes del video", required=True)

# Parser para solicitudes PATCH (actualizar video)
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Nombre del video")
video_update_args.add_argument("views", type=int, help="Número de vistas del video")
video_update_args.add_argument("likes", type=int, help="Número de likes del video")

def abort_if_video_doesnt_exist(video_id):
    """
    Verifica si un video existe, y si no, aborta la solicitud
    """
    video = VideoModel.query.filter_by(id=video_id).first()
    if not video:
        abort(404, message=f"No se encontró un video con el ID {video_id}")
    return video

class Video(Resource):
    @marshal_with(resource_fields)
    def put(self, video_id):
        """
        Crea un nuevo video con un ID específico
        ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID del nuevo video
          - in: body
            name: body
            required: true
            schema:
              id: Video
              required:
                - name
                - views
                - likes
              properties:
                name:
                  type: string
                  description: Título del video
                views:
                  type: integer
                  description: Número de vistas
                likes:
                  type: integer
                  description: Número de likes
        responses:
          201:
            description: Video creado exitosamente
        """
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    def get(self, video_id):
        """
        Obtiene un video por su ID
        ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID del video a consultar
        responses:
          200:
            description: Video encontrado exitosamente
          404:
            description: Video no encontrado
        """
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Video no encontrado")
        return video   

    @marshal_with(resource_fields)
    def patch(self, video_id):
        """
        Actualiza parcialmente un video existente
        ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID del video a actualizar
          - in: body
            name: body
            required: true
            schema:
              id: VideoUpdate
              properties:
                name:
                  type: string
                  description: Nuevo título del video
                views:
                  type: integer
                  description: Nuevas vistas
                likes:
                  type: integer
                  description: Nuevos likes
        responses:
          200:
            description: Video actualizado exitosamente
          404:
            description: Video no encontrado
        """
        args = video_update_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Video no encontrado")

        if args['name']:
            video.name = args['name']
        if args['views']:
            video.views = args['views']
        if args['likes']:
            video.likes = args['likes']

        db.session.commit()
        return video    
    
    def delete(self, video_id):
        """
        Elimina un video por su ID
        ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID del video a eliminar
        responses:
          204:
            description: Video eliminado exitosamente
          404:
            description: Video no encontrado
        """
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Video no encontrado")

        db.session.delete(video)
        db.session.commit()
        return '', 204    