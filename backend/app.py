import os
from sqlalchemy import and_, text 
from flask import Flask, render_template, request, Response, send_file , redirect, session, url_for, jsonify
import psycopg2 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from users import Users
from extensions import db, migrate
from flask_session import Session
from sqlalchemy import create_engine
import pymysql
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
import traceback

from api.api1 import api1
from api.api2 import api2
from api.api3 import api3
from api.api4 import api4
from api.api5 import api5
from api.api6 import api6
from api.api7 import api7
from api.api8 import api8
from api.api9 import api9
from api.api10 import api10
from api.api11 import api11
from api.api12 import api12
from api.api13 import api13
from api.api14 import api14
from api.api15 import api15
from api.api16 import api16
from api.api17 import api17
from api.api18 import api18
from api.api19 import api19
from api.api20 import api20
from api.api21 import api21
from api.api22 import api22
from api.api23 import api23
from api.api24 import api24
from api.api25 import api25
from api.api26 import api26

app = Flask(__name__) 
CORS(app)

pymysql.install_as_MySQLdb()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CA_CERT_PATH = os.path.join(BASE_DIR, "tidb-ca.pem")


app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://2ADR4DDCyc1Ewaj.root:fuTF796MjrxRtEx4"
    f"@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"
    f"?ssl_ca={CA_CERT_PATH}"
)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://2ADR4DDCyc1Ewaj.root:fuTF796MjrxRtEx4@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:swapna234@localhost/bma_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     

db.init_app(app)
migrate.init_app(app, db)
Session(app)
app.debug = True

app.register_blueprint(api1)
app.register_blueprint(api2)
app.register_blueprint(api3)
app.register_blueprint(api4)
app.register_blueprint(api5)
app.register_blueprint(api6)
app.register_blueprint(api7)
app.register_blueprint(api8)
app.register_blueprint(api9)
app.register_blueprint(api10)
app.register_blueprint(api11)
app.register_blueprint(api12)
app.register_blueprint(api13)
app.register_blueprint(api14)
app.register_blueprint(api15)
app.register_blueprint(api16)
app.register_blueprint(api17)
app.register_blueprint(api18)
app.register_blueprint(api19)
app.register_blueprint(api20)
app.register_blueprint(api21)
app.register_blueprint(api22)
app.register_blueprint(api23)
app.register_blueprint(api24)
app.register_blueprint(api25)
app.register_blueprint(api26)

@app.route('/login', methods=['POST']) 
def login_verify(): 
    data = request.get_json()
    result = "fail"
    session_data = {}

    try:
        get_user = Users.query.filter(
            and_(
                Users.email == str(data['l_userName']).strip(),
                Users.password == str(data['l_userPass']).strip()
            )
        ).one()
        
        session["username"] = str(get_user.username).strip()
        session["userId"] = str(get_user.id).strip()
        
        result = "success"
        session_data = dict(session)

    except NoResultFound:
        # Wrong username/password — user not found
        result = "fail"

    except SQLAlchemyError as e:
        # Any DB error
        print("SQLAlchemy Error:", str(e))
        result = "error"
    
    except Exception as e:
        app.logger.error("Unexpected Error during login:\n" + traceback.format_exc())
        result = "error"

    return jsonify({
        "data": result,
        "sessionData": session_data
    })

@app.route('/get_user', methods=['POST']) 
def user_index(): 
    data = request.get_json()
    userName = str(data['l_Username'])
    userId = str(data['l_userId'])
    user_data = Users.query.get(int(userId))
    user_d = []
    user_d.append(user_data.map())
    return jsonify({"user_data": user_d})

@app.route('/update_user_profile', methods=['POST']) 
def updated_user_index(): 
    data = request.get_json()
    userId = str(data['u_userId'])
    user_data = Users.query.get(int(userId))
    user_data.fullname = str(data['u_fullName'])
    user_data.email = str(data['u_userEmail'])
    user_data.phone = str(data['u_userPhone'])
    user_data.department = str(data['u_department'])
    user_data.designation = str(data['u_designation'])
    user_data.description = str(data['u_descrip'])
    user_data.language = str(data['u_language'])
    db.session.flush()
    db.session.commit()
    return jsonify({"data":"updated"})

@app.route('/change_Password', methods=['POST']) 
def change_pass_index(): 
    data = request.get_json()
    userId = str(data['u_userId'])
    user_data = Users.query.get(int(userId))
    user_data.password = str(data['u_newPass'])
    db.session.flush()
    db.session.commit()
    return jsonify({"data":"updated"})

@app.route('/logout') 
def logout_index(): 
    session.clear()
    return jsonify({"data":"success"})

if __name__ == '__main__': 
	app.run()
