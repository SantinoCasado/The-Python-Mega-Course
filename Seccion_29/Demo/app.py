from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from send_email import send_email
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:46184393@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Float, nullable=False)

    def __init__(self, email, height):
        self.email = email
        self.height = height


def create_tables_if_needed():
    inspector = inspect(db.engine)
    existing_tables = set(inspector.get_table_names())
    required_tables = {Data.__tablename__}
    missing_tables = required_tables - existing_tables

    if missing_tables:
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = float(request.form['height_name'])
        # Verificar si el email ya existe en la base de datos
        if db.session.query(Data).filter(Data.email == email).count() == 0: 
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 2) if average_height else 0
            count = db.session.query(func.count(Data.height)).scalar()
            try:
                send_email(email, height, average_height, count)
            except Exception as e:
                # Keep form flow working even if SMTP fails.
                print(f"Email could not be sent: {e}")
            return render_template('success.html')
        else:
            error_message = "Seems like we already have your email. Please use a different email."
            return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    with app.app_context():
        create_tables_if_needed()
    app.run(debug=True)