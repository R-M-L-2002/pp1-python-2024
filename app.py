from flask import(
    Flask,
    render_template,
    redirect,
    request
    )

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Mercaderia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Precio, Producto


#GET
lista_productos =[
    dict(
        product=dict(
            name='Mayonesa',
            price='1800',
            code='x000001'
            )

    ),
        dict(
        product=dict(
            name='Mostaza',
            price='2000',
            code='x000002'
    )),
        dict(
        product=dict(
            name='Ketchup',
            price='2300',
            code='x000003'
    )),
        dict(
        product=dict(
            name='Mayonesa Vegana',
            price='2100',
            code='x000004'
    ))
]


@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/productos')
def productos():
    listado = lista_productos
    return render_template('productos.html',
    listado = listado)

@app.route('/add_productos', methods=['POST', 'GET'])
def add_productos():
    if request.method == 'POST':
        #peticion formulario
        name = request.form['product']
        price = request.form['price']
        code = request.form['code']

        producto= dict(
        product=dict(
            name=name, 
        price=price,

        code=code
        ))
        lista_productos.append(producto)
    return render_template('add_productos.html')