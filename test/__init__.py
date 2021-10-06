import connexion

def create_app():
    connexion_app = connexion.FlaskApp(__name__)
    app = connexion_app.app
    connexion_app.add_api('../swagger/swagger.yaml', validate_responses=True)
    return app