from com import app
from flask_sqlalchemy import SQLAlchemy


app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userdb:Atenea_2010@192.168.0.135:3306/curso'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


def main():
    with app.app_context():
        db.init_app(app)
        db.create_all()
        return db


if __name__ == "__main__":
    db = main()
    app.run()
