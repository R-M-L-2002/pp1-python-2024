from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return self.nombre

class Precio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Float)

    def __str__(self):
        return self.nombre

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(30), nullable=False)   
    codigo = db.Column(db.String(30), nullable=False)

    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    precio_id = db.Column(db.Integer, db.ForeignKey('precio.id'), nullable=False)

    marca= db.relationship('Marca', backref=db.backref('producto', lazy=True)) 
    precio = db.relationship('Precio', backref=db.backref('producto', lazy=True))   

    def __str__(self):
        return self.producto

