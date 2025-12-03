#!/usr/bin/python3
#!/usr/bin/env python3
"""
Task 05 - API Security with Basic Auth, JWT, and Role-Based Access Control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# -----------------------------
# In-memory user storage
# -----------------------------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# -----------------------------
# BASIC AUTH SECTION
# -----------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth"""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------------
# JWT LOGIN
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    """Login with username and password to get JWT"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Create token containing username & role
    token = create_access_token(identity={"username": username, "role": user["role"]})

    return jsonify({"access_token": token}), 200


# -----------------------------
# JWT PROTECTED ROUTE
# -----------------------------
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# -----------------------------
# ROLE-BASED ROUTE
# -----------------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()  # returns {"username": ..., "role": ...}

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -----------------------------
# JWT ERROR HANDLERS (ALL MUST RETURN 401)
# -----------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# Run server
if __name__ == "__main__":
    app.run()
#!/usr/bin/env python3
"""
Task 05 - API Security with Basic Auth, JWT, and Role-Based Access Control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# -----------------------------
# In-memory user storage
# -----------------------------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# -----------------------------
# BASIC AUTH SECTION
# -----------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth"""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------------
# JWT LOGIN
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    """Login with username and password to get JWT"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Create token containing username & role
    token = create_access_token(identity={"username": username, "role": user["role"]})

    return jsonify({"access_token": token}), 200


# -----------------------------
# JWT PROTECTED ROUTE
# -----------------------------
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# -----------------------------
# ROLE-BASED ROUTE
# -----------------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()  # returns {"username": ..., "role": ...}

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -----------------------------
# JWT ERROR HANDLERS (ALL MUST RETURN 401)
# -----------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# Run server
if __name__ == "__main__":
    app.run()
