from flask import Flask,request
from flask import jsonify
from flask_cors import CORS, cross_origin
from mongo.app import Workbase

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*.*"}})
version = '1.0.0'

# Home
@app.route("/", methods=['GET']) 
@cross_origin()
def home(): 
    return jsonify({
        "api": "API FLASK",
        "version": "1.0.0"
    })

# User - Craate User
@app.route(f"/api/v{version}/users", methods=['POST']) 
@cross_origin()
def creatuser(): 
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        print(token)
        if token['token'] == "valid":
            a = Workbase(obj).creatuser()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Authentication
@app.route(f"/api/v{version}/authenticate", methods=['POST']) 
@cross_origin()
def authenticate(): 
    try:
        obj = request.get_json()
        a = Workbase(obj).validateuser()
        return jsonify(a[0]), a[1]
    except:
        return {"message": "internal server erro"}, 500

# User - Fetching data by id
@app.route(f"/api/v{version}/users/<ID>", methods=['GET']) 
@cross_origin()
def idusers(ID):  
    try:
        obj={'user_id': ID,}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).idselectuser()
            return jsonify(a[0]), a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# User - Changing and querying
@app.route(f"/api/v{version}/users/<ID>", methods=['PUT']) 
@cross_origin()
def putuser(ID): 
    try:
        obj = request.get_json()
        obj['user_id'] = ID
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).putuser()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Projects - Create and quering
@app.route(f"/api/v{version}/projects", methods=['POST'])
@cross_origin()
def createproject():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).createproject()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Projects - Quering
@app.route(f"/api/v{version}/projects", methods=['GET']) 
@cross_origin()
def selectprojects():
    try:
        obj = {}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).selectprojects()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Projects - Fetching data by id
@app.route(f"/api/v{version}/projects/<ID>", methods=['GET']) 
@cross_origin()
def selectprojectid(ID):
    try:
        obj = {'project_id': ID,}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).selectprojectid()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Projects - Changing and querying
@app.route(f"/api/v{version}/projects/<ID>", methods=['PUT']) 
@cross_origin()
def putproject(ID):
    try:
        obj = request.get_json()
        obj['project_id'] = ID
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).putproject()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Time - Create and quering
@app.route(f"/api/v{version}/times", methods=['POST']) 
@cross_origin()
def times():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).registertime()
            return jsonify(a[0]), a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Times - Fetching data by id
@app.route(f"/api/v{version}/times/<ID>", methods=['GET']) 
@cross_origin()
def idselecttime(ID):
    try:
        obj = {'time_id': ID,}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).idselecttime()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Times - Changing and querying
@app.route(f"/api/v{version}/times/<ID>", methods=['PUT']) 
@cross_origin()
def puttime(ID):
    try:
        obj = request.get_json()
        obj['time_id'] = ID
        header = request.headers['token']
        obj["currenttoken"] = header
        token = Workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = Workbase(obj).puttime()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)