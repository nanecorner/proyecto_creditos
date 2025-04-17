from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# -------------------------------
# Modelo
# -------------------------------

class Credito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.String(10), nullable=False)


# Crear la base de datos si no existe
with app.app_context():
    db.create_all()


# -------------------------------
# Rutas
# -------------------------------

# Página principal: lista de créditos
@app.route('/')
def index():
    total_creditos = db.session.query(db.func.count(Credito.id)).scalar() or 0
    total_monto = db.session.query(db.func.sum(Credito.monto)).scalar() or 0
    creditos = Credito.query.all()

    # Obtener número de créditos por cliente (para la gráfica)
    creditos_por_cliente = db.session.query(
        Credito.cliente,
        db.func.count(Credito.id)
    ).group_by(Credito.cliente).all()

    clientes = [c[0] for c in creditos_por_cliente]
    montos = [c[1] for c in creditos_por_cliente]

    return render_template('index.html', creditos=creditos, total_creditos=total_creditos,
                           clientes=clientes, montos=montos, total_monto=total_monto)


# Registrar nuevo crédito
@app.route('/registro', methods=['POST'])
def registrar_credito():
    cliente = request.form['cliente']
    monto = request.form['monto']
    tasa_interes = request.form['tasa_interes']
    plazo = request.form['plazo']
    fecha_otorgamiento = request.form['fecha_otorgamiento']

    nuevo_credito = Credito(
        cliente=cliente,
        monto=monto,
        tasa_interes=tasa_interes,
        plazo=plazo,
        fecha_otorgamiento=fecha_otorgamiento
    )

    db.session.add(nuevo_credito)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error al registrar crédito: {e}")

    return redirect(url_for('index'))


# Eliminar crédito
@app.route('/eliminar/<int:id>')
def eliminar_credito(id):
    credito = Credito.query.get_or_404(id)
    db.session.delete(credito)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error al eliminar crédito: {e}")
    return redirect(url_for('index'))


# Editar crédito
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_credito(id):
    credito = Credito.query.get_or_404(id)

    if request.method == 'POST':
        credito.cliente = request.form['cliente']
        credito.monto = float(request.form['monto'])
        credito.tasa_interes = float(request.form['tasa_interes'])
        credito.plazo = int(request.form['plazo'])
        credito.fecha_otorgamiento = request.form['fecha_otorgamiento']

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error al editar crédito: {e}")
        return redirect(url_for('index'))

    return render_template('editar.html', credito=credito)


# -------------------------------
# Ejecutar app
# -------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800, debug=True)
