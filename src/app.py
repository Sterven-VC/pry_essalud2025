from flask import Flask, render_template, request, redirect, url_for, flash , jsonify, send_from_directory, send_file
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import config
from werkzeug.security import generate_password_hash
from db import get_connection

import os
from werkzeug.utils import secure_filename
import uuid

# Models:
from models.ModelUser import ModelUser
from models.ModelJuntaDirectiva import ModelJuntaDirectiva
from models.ModelActa import ModelActa
from models.ModelNoticia import ModelNoticia
from models.ModelMemoria import ModelMemoria


# Entities:git
from models.entities.User import User
from models.entities.JuntaDirectiva import JuntaDirectiva
from models.entities.Acta import Acta
from models.entities.Noticia import Noticia
from models.entities.Memoria import Memoria

#CAMBIO PARA IGNORAR EL ENTORNO VIRTUAKL
app = Flask(__name__)
csrf = CSRFProtect(app)
#db = MySQL(app)
db=get_connection()

login_manager_app = LoginManager(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'src', 'static', 'archivos')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        fullname = request.form['fullname']
        if not username or not password or not confirm_password or not fullname:
            flash("Por favor, complete todos los campos.")
        elif password != confirm_password:
            flash("Las contraseñas no coinciden.")
        else:
            # Crea un nuevo usuario y lo guarda en la base de datos
            new_user = User(0, username, password, fullname)
            result = ModelUser.register(db, new_user, confirm_password)
            if result:
                flash("Registro exitoso. ¡Ahora puedes iniciar sesión!")
                return redirect(url_for('login'))
    return render_template('auth/register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/junta_directiva', methods=['GET'])
@login_required
def junta_directiva():
    juntas_directivas = ModelJuntaDirectiva.get_all_juntas_directivas(db)
    return render_template('navs/junta_directiva.html', juntas_directivas=juntas_directivas)

@app.route('/register_JuntaDirectiva', methods=['POST'])
@login_required
def register_JuntaDirectiva():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        miembro1 = request.form['miembro1']
        cargo1 = request.form['cargo1']
        miembro2 = request.form['miembro2']
        cargo2 = request.form['cargo2']
        miembro3 = request.form['miembro3']
        cargo3 = request.form['cargo3']
        miembro4 = request.form['miembro4']
        cargo4 = request.form['cargo4']
        miembro5 = request.form['miembro5']
        cargo5 = request.form['cargo5']
        miembro6 = request.form['miembro6']
        cargo6 = request.form['cargo6']
        miembro7 = request.form['miembro7']
        cargo7 = request.form['cargo7']
        miembro8 = request.form['miembro8']
        cargo8 = request.form['cargo8']
        vigencia = request.form.get('vigencia') == 'on'  # True if checkbox is checked, otherwise False

        if not nombre or not fecha_inicio or not fecha_fin or not miembro1 or not cargo1:
            flash("Por favor, complete todos los campos obligatorios.")
            return redirect(url_for('junta_directiva'))
        
        new_junta_directiva = JuntaDirectiva(0, nombre, fecha_inicio, fecha_fin, miembro1, cargo1, miembro2, cargo2, miembro3, cargo3, miembro4, cargo4, miembro5, cargo5, miembro6, cargo6, miembro7, cargo7, miembro8, cargo8, vigencia)
        result = ModelJuntaDirectiva.register_JuntaDirectiva(db, new_junta_directiva)
        if result:
            return redirect(url_for('junta_directiva'))
        else:
            return redirect(url_for('junta_directiva'))
    return render_template('navs/junta_directiva.html')

@app.route('/junta_directiva/<int:id>', methods=['GET'])
@login_required
def get_junta_directiva(id):
    junta_directiva = ModelJuntaDirectiva.get_junta_directiva_by_id(db, id)
    if junta_directiva:
        return jsonify({
            'id': junta_directiva.id,
            'nombre': junta_directiva.nombre,
            'fecha_inicio': str(junta_directiva.fecha_inicio),
            'fecha_fin': str(junta_directiva.fecha_fin),
            'miembro1': junta_directiva.miembro1,
            'cargo1': junta_directiva.cargo1,
            'miembro2': junta_directiva.miembro2,
            'cargo2': junta_directiva.cargo2,
            'miembro3': junta_directiva.miembro3,
            'cargo3': junta_directiva.cargo3,
            'miembro4': junta_directiva.miembro4,
            'cargo4': junta_directiva.cargo4,
            'miembro5': junta_directiva.miembro5,
            'cargo5': junta_directiva.cargo5,
            'miembro6': junta_directiva.miembro6,
            'cargo6': junta_directiva.cargo6,
            'miembro7': junta_directiva.miembro7,
            'cargo7': junta_directiva.cargo7,
            'miembro8': junta_directiva.miembro8,
            'cargo8': junta_directiva.cargo8,
            'vigencia': junta_directiva.vigencia
        })
    return jsonify({'error': 'Junta Directiva no encontrada'}), 404

@app.route('/update_JuntaDirectiva', methods=['POST'])
@login_required
def update_JuntaDirectiva():
    id = request.form['id']
    nombre = request.form['nombre']
    fecha_inicio = request.form['fecha_inicio']
    fecha_fin = request.form['fecha_fin']
    miembro1 = request.form['miembro1']
    cargo1 = request.form['cargo1']
    miembro2 = request.form['miembro2']
    cargo2 = request.form['cargo2']
    miembro3 = request.form['miembro3']
    cargo3 = request.form['cargo3']
    miembro4 = request.form['miembro4']
    cargo4 = request.form['cargo4']
    miembro5 = request.form['miembro5']
    cargo5 = request.form['cargo5']
    miembro6 = request.form['miembro6']
    cargo6 = request.form['cargo6']
    miembro7 = request.form['miembro7']
    cargo7 = request.form['cargo7']
    miembro8 = request.form['miembro8']
    cargo8 = request.form['cargo8']
    vigencia = request.form.get('vigencia') == 'on'  # True if checkbox is checked, otherwise False

    if not id or not nombre or not fecha_inicio or not fecha_fin or not miembro1 or not cargo1:
        flash("Por favor, complete todos los campos obligatorios.")
    else:
        junta_directiva = JuntaDirectiva(id, nombre, fecha_inicio, fecha_fin, miembro1, cargo1, miembro2, cargo2, miembro3, cargo3, miembro4, cargo4, miembro5, cargo5, miembro6, cargo6, miembro7, cargo7, miembro8, cargo8, vigencia)
        result = ModelJuntaDirectiva.update_junta_directiva(db, junta_directiva)
        if result:
            return redirect(url_for('junta_directiva'))
        else:
            flash("Error al actualizar.")
            return redirect(url_for('junta_directiva'))
    return render_template('navs/junta_directiva.html')

@app.route('/delete_JuntaDirectiva/<int:id>', methods=['POST'])
@login_required
def delete_JuntaDirectiva(id):
    result = ModelJuntaDirectiva.delete_junta_directiva(db, id)
    if result:
        return redirect(url_for('junta_directiva'))
    else:
        flash("Error al eliminar la junta directiva.")
    return render_template('navs/junta_directiva.html')

#######################################################################################3
@app.route('/actas', methods=['GET'])
@login_required
def actas():
    actas = ModelActa.get_actas_with_cuorum_status(db)
    junta_vigente = ModelJuntaDirectiva.get_junta_directiva_vigente(db)
    # Crear la lista de miembros
    miembros = [
        {'nombre': junta_vigente.miembro1, 'cargo': junta_vigente.cargo1},
        {'nombre': junta_vigente.miembro2, 'cargo': junta_vigente.cargo2},
        {'nombre': junta_vigente.miembro3, 'cargo': junta_vigente.cargo3},
        {'nombre': junta_vigente.miembro4, 'cargo': junta_vigente.cargo4},
        {'nombre': junta_vigente.miembro5, 'cargo': junta_vigente.cargo5},
        {'nombre': junta_vigente.miembro6, 'cargo': junta_vigente.cargo6},
        {'nombre': junta_vigente.miembro7, 'cargo': junta_vigente.cargo7},
        {'nombre': junta_vigente.miembro8, 'cargo': junta_vigente.cargo8}
    ]
    return render_template('navs/actas.html', actas=actas, miembros=miembros)

@app.route('/register_Actas', methods=['POST'])
@login_required
def register_Actas():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('actas'))
    file = request.files['file']
    if file.filename == '':
        flash('No select file')
        return redirect(url_for('actas'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        new_filename = uuid.uuid4().hex + extension
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        file.save(file_path)
        
        relative_file_path = os.path.relpath(file_path, start=os.getcwd())
        
        nombre = request.form['nombre']
        fecha = request.form['fecha']  # Fecha en formato YYYY-MM-DD
        asistencia_1 = request.form.get('asistencia_1') == 'on'
        asistencia_2 = request.form.get('asistencia_2') == 'on'
        asistencia_3 = request.form.get('asistencia_3') == 'on'
        asistencia_4 = request.form.get('asistencia_4') == 'on'
        asistencia_5 = request.form.get('asistencia_5') == 'on'
        asistencia_6 = request.form.get('asistencia_6') == 'on'
        asistencia_7 = request.form.get('asistencia_7') == 'on'
        asistencia_8 = request.form.get('asistencia_8') == 'on'

        # Obtener la junta directiva vigente
        id_junta_directiva = ModelActa.get_vigente_junta_id(db)
        
        if not nombre or not fecha or not id_junta_directiva:
            flash("Por favor, complete todos los campos.")
        else:
            new_acta = Acta(0, nombre, fecha, relative_file_path, id_junta_directiva, asistencia_1, asistencia_2, asistencia_3, asistencia_4, asistencia_5, asistencia_6, asistencia_7, asistencia_8)
            result = ModelActa.register_acta(db, new_acta)
            if result:
                return redirect(url_for('actas'))
            else:
                flash("Por favor, complete todos los campos2.")
                return redirect(url_for('actas'))
    return render_template('navs/actas.html')

@app.route('/actas/<int:id>', methods=['GET'])
@login_required
def get_acta(id):
    acta = ModelActa.get_acta_by_id(db, id)
    if acta:
        return jsonify({
            'id': acta.id,
            'nombre': acta.nombre,
            'fecha': str(acta.fecha),
            'asistencia_1': acta.asistencia_1,
            'asistencia_2': acta.asistencia_2,
            'asistencia_3': acta.asistencia_3,
            'asistencia_4': acta.asistencia_4,
            'asistencia_5': acta.asistencia_5,
            'asistencia_6': acta.asistencia_6,
            'asistencia_7': acta.asistencia_7,
            'asistencia_8': acta.asistencia_8
        })
    return jsonify({'error': 'Acta no encontrada'}), 404

@app.route('/update_Acta', methods=['POST'])
@login_required
def update_Acta():
    id = request.form.get('id')
    nombre = request.form.get('nombre')
    fecha = request.form.get('fecha')  # Fecha en formato YYYY-MM-DD
    file = request.files.get('file', None)
    
    # Validación de asistencia
    asistencia = {
        'asistencia_1': request.form.get('asistencia_1') == 'on',
        'asistencia_2': request.form.get('asistencia_2') == 'on',
        'asistencia_3': request.form.get('asistencia_3') == 'on',
        'asistencia_4': request.form.get('asistencia_4') == 'on',
        'asistencia_5': request.form.get('asistencia_5') == 'on',
        'asistencia_6': request.form.get('asistencia_6') == 'on',
        'asistencia_7': request.form.get('asistencia_7') == 'on',
        'asistencia_8': request.form.get('asistencia_8') == 'on'
    }

    if not id or not nombre or not fecha:
        flash("Por favor, complete todos los campos.")
    else:
        acta = ModelActa.get_acta_by_id(db, id)
        if acta:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                extension = os.path.splitext(filename)[1]
                new_filename = uuid.uuid4().hex + extension
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                file.save(file_path)
                ruta_pdf = os.path.relpath(file_path, start=os.getcwd())
            else:
                ruta_pdf = acta.ruta_pdf
            
            # Obtener la junta directiva vigente
            id_junta_directiva = ModelActa.get_vigente_junta_id(db)
            
            # Actualizar la acta
            updated_acta = Acta(
                id, nombre, fecha, ruta_pdf, id_junta_directiva,
                asistencia['asistencia_1'], asistencia['asistencia_2'], asistencia['asistencia_3'],
                asistencia['asistencia_4'], asistencia['asistencia_5'], asistencia['asistencia_6'],
                asistencia['asistencia_7'], asistencia['asistencia_8']
            )
            result = ModelActa.update_acta(db, updated_acta)
            if result:
                return redirect(url_for('actas'))
            else:
                flash("Error al actualizar el acta.")
                return redirect(url_for('actas'))
    return render_template('navs/actas.html')


@app.route('/delete_Acta/<int:id>', methods=['POST'])
@login_required
def delete_Acta(id):
    result = ModelActa.delete_acta(db, id)
    if result:
        return redirect(url_for('actas'))
    else:
        flash("Error al eliminar el acta.")
    return render_template('navs/actas.html')

@app.route('/download/<int:id>', methods=['GET'])
@login_required
def download_file(id):
    acta = ModelActa.get_acta_by_id(db, id)
    if acta:
        file_path = os.path.join(os.getcwd(), acta.ruta_pdf)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            flash("Archivo no encontrado.")
            return redirect(url_for('actas'))
    else:
        flash("Acta no encontrada.")
        return redirect(url_for('actas'))
    

###################
@app.route('/ver_junta/<id>', methods=['GET'])
@login_required
def ver_junta(id):
    cur = db.cursor()
    cur.execute("SELECT * FROM junta_directiva WHERE id = %s", (id,))
    junta_directiva = cur.fetchone()

    if junta_directiva is None:
        flash("Junta Directiva no encontrada.")
        cur.close()
        return redirect(url_for('actas'))  # Redirige a la página de actas u otra página relevante



    # Obtener actas asociadas a la junta directiva
    cur.execute("SELECT * FROM acta WHERE id_junta_directiva = %s", (id,))
    actas = cur.fetchall()



    # Obtener memorias asociadas a la junta directiva
    cur.execute("SELECT * FROM memoria WHERE id_directiva = %s", (id,))
    memorias = cur.fetchall()


    cur.close()
    return render_template("navs/ver_junta.html", junta_directiva=junta_directiva, actas=actas, memorias=memorias)


############


@app.route('/memorias', methods=['GET'])
@login_required
def memorias():
    memorias = ModelMemoria.get_all_memorias(db)
    return render_template('navs/memorias.html', memorias=memorias)

@app.route('/register_Memorias', methods=['POST'])
@login_required
def register_Memorias():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        new_filename = uuid.uuid4().hex + extension
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        file.save(file_path)
        
        relative_file_path = os.path.relpath(file_path, start=os.getcwd())
        
        nombre = request.form['nombre']
        anio = request.form['anio']
        
        if not nombre or not anio:
            flash("Por favor, complete todos los campos.")
        else:
            # Obtener la junta directiva vigente
            id_directiva = ModelMemoria.get_vigente_junta_id(db)
            if id_directiva is None:
                flash("No hay una junta directiva vigente.")
                return redirect(url_for('memorias'))
            
            new_memoria = Memoria(0, nombre, anio, relative_file_path, id_directiva)
            result = ModelMemoria.register_memoria(db, new_memoria)
            if result:
                return redirect(url_for('memorias'))
            else:
                flash("Error al registrar la memoria.")
                return redirect(url_for('memorias'))
    return render_template('navs/memorias.html')


@app.route('/memorias/<int:id>', methods=['GET'])
@login_required
def get_memoria(id):
    memoria = ModelMemoria.get_memoria_by_id(db, id)
    if memoria:
        return jsonify({
            'id': memoria.id,
            'nombre': memoria.nombre,
            'anio': memoria.anio,
            'ruta_pdf': memoria.ruta_pdf,
            'id_directiva': memoria.id_directiva
        })
    return jsonify({'error': 'Memoria no encontrada'}), 404

@app.route('/update_Memoria', methods=['POST'])
@login_required
def update_Memoria():
    id = request.form['id']
    nombre = request.form['nombre']
    anio = request.form['anio']
    file = request.files.get('file', None)

    if not id or not nombre or not anio:
        flash("Por favor, complete todos los campos.")
    else:
        memoria = ModelMemoria.get_memoria_by_id(db, id)
        if memoria:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                extension = os.path.splitext(filename)[1]
                new_filename = uuid.uuid4().hex + extension
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                file.save(file_path)
                ruta_pdf = os.path.relpath(file_path, start=os.getcwd())
            else:
                ruta_pdf = memoria.ruta_pdf

            # Obtener la junta directiva vigente
            id_directiva = ModelMemoria.get_vigente_junta_id(db)
            if id_directiva is None:
                flash("No hay una junta directiva vigente.")
                return redirect(url_for('memorias'))
            
            updated_memoria = Memoria(id, nombre, anio, ruta_pdf, id_directiva)
            result = ModelMemoria.update_memoria(db, updated_memoria)
            if result:
                return redirect(url_for('memorias'))
            else:
                flash("Error al actualizar la memoria.")
                return redirect(url_for('memorias'))
    return render_template('navs/memorias.html')


@app.route('/delete_Memoria/<int:id>', methods=['POST'])
@login_required
def delete_Memoria(id):
    result = ModelMemoria.delete_memoria(db, id)
    if result:
        return redirect(url_for('memorias'))
    else:
        flash("Error al eliminar la memoria.")
    return render_template('navs/memorias.html')


@app.route('/download_memoria/<int:id>', methods=['GET'])
@login_required
def download_memoria(id):
    memoria = ModelMemoria.get_memoria_by_id(db, id)
    if memoria:
        file_path = os.path.join(os.getcwd(), memoria.ruta_pdf)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            flash("Archivo no encontrado.")
            return redirect(url_for('memorias'))
    else:
        flash("Memoria no encontrada.")
        return redirect(url_for('memorias'))



@app.route('/noticias', methods=['GET'])
@login_required
def noticias():
    noticias = ModelNoticia.get_all_noticias(db)
    return render_template('navs/noticias.html', noticias=noticias)

@app.route('/register_noticia', methods=['POST'])
@login_required
def register_noticia():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        new_filename = uuid.uuid4().hex + extension
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        file.save(file_path)
        
        relative_file_path = os.path.relpath(file_path, start=os.getcwd())
        
        titulo = request.form['titulo']
        fecha_noticia = request.form['fecha_noticia']
        description = request.form['description']
        information = request.form['information']
        
        if not titulo or not fecha_noticia or not description or not information:
            flash("Por favor, complete todos los campos.")
        else:
            noticia = Noticia(0, titulo, fecha_noticia, relative_file_path, description, information)
            result = ModelNoticia.register_noticia(db, noticia)
            if result:
                return redirect(url_for('noticias'))
            else:
                flash("Error al registrar la noticia.")
                return redirect(url_for('noticias'))
    return render_template('navs/noticias.html')

@app.route('/noticias/<int:id>', methods=['GET'])
@login_required
def get_noticia(id):
    noticia = ModelNoticia.get_noticia_by_id(db, id)
    if noticia:
        return jsonify({
            'id': noticia.id,
            'titulo': noticia.titulo,
            'fecha_noticia': noticia.fecha_noticia.isoformat(),
            'ruta_foto': noticia.ruta_foto,
            'description': noticia.description,
            'information': noticia.information
        })
    return jsonify({'error': 'Noticia no encontrada'}), 404

@app.route('/update_noticia', methods=['POST'])
@login_required
def update_noticia():
    id = request.form['id']
    titulo = request.form['titulo']
    fecha_noticia = request.form['fecha_noticia']
    description = request.form['description']
    information = request.form['information']
    file = request.files.get('file', None)

    if not id or not titulo or not fecha_noticia or not description or not information:
        flash("Por favor, complete todos los campos.")
    else:
        noticia = ModelNoticia.get_noticia_by_id(db, id)
        if noticia:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                extension = os.path.splitext(filename)[1]
                new_filename = uuid.uuid4().hex + extension
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                file.save(file_path)
                ruta_foto = os.path.relpath(file_path, start=os.getcwd())
            else:
                ruta_foto = noticia.ruta_foto
            
            updated_noticia = Noticia(id, titulo, fecha_noticia, ruta_foto, description, information)
            result = ModelNoticia.update_noticia(db, updated_noticia)
            if result:
                return redirect(url_for('noticias'))
            else:
                flash("Error al actualizar la noticia.")
                return redirect(url_for('noticias'))                
    return render_template('navs/noticias.html')

@app.route('/delete_noticia/<int:id>', methods=['POST'])
@login_required
def delete_noticia(id):
    result = ModelNoticia.delete_noticia(db, id)
    if result:
        return redirect(url_for('noticias'))
    else:
        flash("Error al eliminar la noticia.")
    return render_template('navs/noticias.html')


@app.route('/profile', methods=['GET'])
@login_required
def profile():
    user = ModelUser.get_by_id(db, current_user.id)
    return render_template('navs/profile.html', user=user)

@app.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    username = request.form['username']
    fullname = request.form['fullname']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if not username or not fullname:
        flash("Por favor, complete todos los campos obligatorios.")
        return redirect(url_for('profile'))
    
    if password and password != confirm_password:
        flash("Las contraseñas no coinciden.")
        return redirect(url_for('profile'))

    user = User(current_user.id, username, password, fullname)
    result = ModelUser.update_profile(db, user)

    if result:
        flash("Perfil actualizado con éxito.")
        return redirect(url_for('profile'))

    else:
        flash("Error al actualizar el perfil.")

    return redirect(url_for('profile'))

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

app.config.from_object(config['development'])

if __name__ == '__main__':
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
