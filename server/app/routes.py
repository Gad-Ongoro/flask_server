from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user
from app.controllers.car_controller import create_car, get_cars, get_car, update_car, delete_car

bp = Blueprint('bp', __name__)

# home(/)
@bp.route('/')
def home():
    return '<h1>User API</h1>'


# (/user) C
@bp.route('/users', methods=['POST'])
def add_user():
    return create_user()

# (/user) R
@bp.route('/users', methods=['GET'])
def list_users():
    return get_users()


# (/user/id) R
@bp.route('/users/<int:user_id>', methods=['GET'])
def list_user(user_id):
    return get_user(user_id)

# (/user/id) U
@bp.route('/users/<int:user_id>', methods=['PATCH'])
def edit_user(user_id):
    return update_user(user_id)


# (/cars) C
@bp.route('/cars', methods=['POST'])
def add_car():
    return create_car()

# (/cars) R
@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()

# (/cars/car_id) R
@bp.route('/cars/<int:car_id>')
def read_car(car_id):
    return get_car(car_id)

# (/cars/car_id) U
@bp.route('/cars/<int:car_id>', methods = ["PATCH"])
def patch_car(car_id):
    return update_car(car_id)

# (/cars/car_id) D
@bp.route('/cars/<int:car_id>', methods = ['DELETE'])
def remove_car(car_id):
    return(delete_car(car_id))