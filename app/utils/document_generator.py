import os

base_path = os.path.abspath(os.path.dirname(__file__))
base_path = os.path.join(base_path, '..')

def create_copies(oficio, data):
    # Crear un oficio por cada registro
    generated_files = []
    for row in data:
        print("QUE PUTA VERGA")
        oficio_persona = oficio.format(**row)
        print("I anu", row)
        new_file_name = f'oficio_{row["id"]}.txt'
        new_file_path = os.path.join(base_path, 'static', 'generated_documents', new_file_name)
        with open(new_file_path, 'w') as file:
            file.write(oficio_persona)
        generated_files.append(new_file_name)
    return generated_files

def generate_copies_for_users(user_data):
    file_path = os.path.join(base_path, 'static', 'template', 'oficio.txt')
    with open(file_path, 'r') as file:
        oficio = file.read()
    generated_files = create_copies(oficio, user_data)
    return generated_files