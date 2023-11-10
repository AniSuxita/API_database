from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'Users'
    table_id = db.Column(db.Integer(), primary_key = True, autoincrement = True )
    User_id = db.Column(db.String())
    hate_speech_count = db.Column(db.Integer, default = 0)
    misogony_count = db.Column(db.Integer, default = 0)

    def get_misogony_count(user_id):
        user = Users.query.filter_by(User_id=user_id).first()
        if user:
            misogony_count = user.misogony_count + 1
            return misogony_count
        return None

    def get_hate_speech_count(user_id):
        user = Users.query.filter_by(User_id=user_id).first()
        if user:
            hate_speech_count = user.hate_speech_count + 1
            return hate_speech_count
        return None



# class Hateful_comments(db.Model):
#     __tablename__ = 'Hateful_texts'
#     comment_id = db.Column(db.String())
#     comment_text = db.Column(db.String())



