from com.run import db


'''
    Esto existe porque SQL Alchemy es un ORM  Object Relational Model
    
    
'''

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_admin = False
        self.password = "123"

    # def __repr__(self):
    #    return '<User %r>' % self.username

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = password

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
