from .user_route import user_bp
from .empresa_route import empresa_bp


def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(empresa_bp, url_prefix='/company')
