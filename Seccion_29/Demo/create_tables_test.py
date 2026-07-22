from sqlalchemy import inspect

from app import app, db, Data


def create_tables_if_needed():
    with app.app_context():
        inspector = inspect(db.engine)
        existing_tables = set(inspector.get_table_names())
        required_tables = {Data.__tablename__}
        missing_tables = required_tables - existing_tables

        if not missing_tables:
            print("Las tablas ya existen. No se creo ninguna tabla nueva.")
            return

        db.create_all()
        print("Tablas creadas correctamente: " + ", ".join(sorted(missing_tables)))


if __name__ == '__main__':
    create_tables_if_needed()
