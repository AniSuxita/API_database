import requests
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from database_code import Users

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('text', type=str,location='args')
parser.add_argument('user_id', type=str,location='args')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ikoplvux:HkrlNxAYOj4K3gIbGXCdu0ifac2tKhgj@cornelius.db.elephantsql.com/ikoplvux'

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

class Post(Resource):
    def post(self):
        args = parser.parse_args()
        comment = args['text']
        user_id = args['user_id']
        new_user = Users(User_id=user_id )
        #vagzavnit requests ai-tan
        ai_url = 'http://127.0.0.1:5000/AI'
        ai_response = requests.post(ai_url, json={"text": comment})
        if ai_response.status_code == 200:
            try:
                ai_json = ai_response.json()
                ai_integer = ai_response.json()['type']
                if ai_integer == 1:
                    misogony_count = Users.get_misogony_count(user_id)
                    if(misogony_count is None):
                        new_user = Users(User_id=user_id, misogony_count = 1)
                    else:
                        misogony_count
                elif ai_integer == 2:
                    hate_speech_count = Users.get_hate_speech_count(user_id)
                    if (hate_speech_count is None):
                        new_user = Users(User_id=user_id, hate_speech_count = 1)


                return ai_json, 200
            except (ValueError, TypeError):
                return  400
            else:
                return {"error": "AI service error"}, 500

api.add_resource(Post, '/post_text')

class AI(Resource):
    def post(self):
        args = parser.parse_args()
        comment = args['text']
        print(comment)
        com_type = {'type': 3}
        return com_type,200

api.add_resource(AI, '/AI')



if __name__ == "__main__":
    app.run(debug=True)