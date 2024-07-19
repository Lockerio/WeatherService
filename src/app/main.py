from flask import Flask

from app.routes.api_routes import api_routes_blueprint
from app.routes.site_routes import site_routes_blueprint


app = Flask(__name__)
app.register_blueprint(site_routes_blueprint)
app.register_blueprint(api_routes_blueprint)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
