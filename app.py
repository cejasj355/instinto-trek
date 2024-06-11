from flask import Flask, url_for, render_template, request

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proximas_salidas')
def proximas_salidas():
    return render_template('proximas_salidas.html')

@app.route('/proximas_salidas/cerro_champaqui')
def cerro_champaqui():
    return render_template('/salidas/cerro_champaqui.html')

@app.route('/proximas_salidas/cumbrecita')
def cumbrecita():
    return render_template('/salidas/cumbrecita.html')

@app.route('/proximas_salidas/gigantes')
def gigantes():
    return render_template('/salidas/gigantes.html')

@app.route('/proximas_salidas/peersonalizado')
def personalizado():
    return render_template('/salidas/personalizado.html')

@app.route('/proximas_salidas/sierras_chicas')
def sierras_chicas():
    return render_template('/salidas/sierras_chicas.html')

@app.route('/proximas_salidas/yuspe')
def yuspe():
    return render_template('/salidas/yuspe.html')


#RUTA HACIA LA PAGINA NOSOTROS
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


#registro
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class contacto(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    mensaje = StringField('mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar:')

@app.route("/#contacto", methods = ['GET', 'POST'])
@app.route("/proximas_salidas#contacto", methods = ['GET', 'POST'])
@app.route("/experiencias#contacto", methods = ['GET', 'POST'])
@app.route("/nosotros#contacto", methods = ['GET', 'POST'])

def contactarse():
    form = contacto()
    if form.validate_on_submit():
        nombre = form.nombre.data
        telefono = form.telefono.data
        email = form.email.data
        mensaje = form.mensaje.data
        
        return f'Nombre: {nombre}, Telefono: {telefono}, Email: {email}, Mensaje: {mensaje}'
        
    return render_template('base.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)