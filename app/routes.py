from flask import current_app as app, redirect, render_template, request, url_for
from .models import User
from . import db

@app.route('/')
def index():
    print("Index route")
    return render_template('index.html')

@app.route('/usuarios')
def users():
    print("Users route")
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/documentos')
def documents():
    print("Documents route")
    users = User.query.all()
    return render_template('documents.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    print("Add user route")
    user_id = request.form.get('userId')
    nombre = request.form.get('nombre')
    apellido1 = request.form.get('apellido1')
    apellido2 = request.form.get('apellido2')
    correoElectronico = request.form.get('correoElectronico')
    fechaNacimiento = request.form.get('fechaNacimiento')
    cargo = request.form.get('cargo')
    empresa = request.form.get('empresa')
    calle = request.form.get('calle')
    numeroExt = request.form.get('numeroExt')
    numeroInt = request.form.get('numeroInt')
    colonia = request.form.get('colonia')
    municipio = request.form.get('municipio')
    estado = request.form.get('estado')
    codigoPostal = request.form.get('codigoPostal')
    telefono = request.form.get('telefono')
    edad = 2024 - int(fechaNacimiento.split('-')[0])

    if user_id:
        # Update existing user
        user = User.query.get(user_id)
        user.nombre = nombre
        user.apellido1 = apellido1
        user.apellido2 = apellido2
        user.correoElectronico = correoElectronico
        user.fechaNacimiento = fechaNacimiento
        user.cargo = cargo
        user.empresa = empresa
        user.calle = calle
        user.numeroExt = numeroExt
        user.numeroInt = numeroInt
        user.colonia = colonia
        user.municipio = municipio
        user.estado = estado
        user.codigoPostal = codigoPostal
        user.telefono = telefono
        user.edad = edad
    else:
        # Create a new user
        user = User(
            nombre=nombre,
            apellido1=apellido1,
            apellido2=apellido2,
            correoElectronico=correoElectronico,
            fechaNacimiento=fechaNacimiento,
            cargo=cargo,
            empresa=empresa,
            calle=calle,
            numeroExt=numeroExt,
            numeroInt=numeroInt,
            colonia=colonia,
            municipio=municipio,
            estado=estado,
            codigoPostal=codigoPostal,
            telefono=telefono,
            edad=edad
        )
        db.session.add(user)

    db.session.commit()
    return redirect(url_for('users'))