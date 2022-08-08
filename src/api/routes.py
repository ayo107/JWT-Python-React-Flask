from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import JWTManager, create_access_token,jwt_required, get_jwt_identity
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)


api = Blueprint('api', __name__)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super12mega-secret"  # Change this "super secret" with something else!
jwt = JWTManager(app)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/pepe', methods=['GET'])
def handle_pepe():

    response_body = {
        "message": "Hello! soy pepe"
    }

    return jsonify(response_body), 200

@api.route("/signup", methods=["POST"])
def sign_up():
   email = request.json.get("email",None)
   password = request.json.get("password", None)
   is_active = request.json.get("is_active", None)
       
   user = User(email = email, password = password, is_active = is_active)
   json= request.get_json()

   db.session.add(user)
   db.session.commit()
       
   return jsonify([]), 200

@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    users = list(map (lambda user: user.serialize(), users))
    
    return jsonify(users), 200

@api.route("/login", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    # Query your database for email and password
    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
    
        data = {
        "id": user.id,
        'email': user.email
    }     
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=120))
    return jsonify({ "token": access_token, "user_id": user.id })

@api.route("/protected", methods=["GET"])
@jwt_required(optional=True)
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
  
    return jsonify({"id": user.id, "email": user.email , "msg": "ok"}), 200
