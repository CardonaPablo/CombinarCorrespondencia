# populate_db.py
import csv
from app import create_app, db
from app.models import User
from datetime import datetime

app = create_app()

def populate_db_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = []
        for row in reader:
            user = User(
                nombre=row['nombre'],
                apellido1=row['apellido1'],
                apellido2=row['apellido2'],
                correoElectronico=row['correoElectronico'],
                fechaNacimiento=datetime.strptime(row['fechaNacimiento'], '%Y-%m-%d').date(),
                cargo=row['cargo'],
                empresa=row['empresa'],
                calle=row['calle'],
                numeroExt=row['numeroExt'],
                numeroInt=row['numeroInt'],
                colonia=row['colonia'],
                municipio=row['municipio'],
                estado=row['estado'],
                codigoPostal=row['codigoPostal'],
                telefono=row['telefono'],
                edad=int(row['edad'])
            )
            users.append(user)
        
        with app.app_context():
            db.create_all()
            db.session.bulk_save_objects(users)
            db.session.commit()
            print("Database populated with users from CSV.")

if __name__ == '__main__':
    csv_file_path = 'users.csv'  # Path to your CSV file
    populate_db_from_csv(csv_file_path)