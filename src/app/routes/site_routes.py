from flask import Blueprint,  render_template


site_routes_blueprint = Blueprint(
    'site_routes_blueprint',
    __name__,
    template_folder='../templates',
    static_folder='../static'
)


@site_routes_blueprint.route('/')
def index():
    return render_template('index.html')
