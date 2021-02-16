#from my_app import ap
from flask import Blueprint, render_template, request, redirect, flash
from my_app.productos.model.products import PRODUCTOS
from my_app.productos.model.product import Producto
from flask import abort
from my_app import db
from datetime import datetime
import time

productos = Blueprint('productos',__name__)

@productos.route('/')
@productos.route('/home')
def index():
    mostrar_producto = Producto.query.all()
    return render_template('index.html',  mostrar_producto = mostrar_producto )
    

@productos.route('/mostrar/<int:id>')
def mostrar(id):
    productos=  Producto.query.get_or_404(id)
    return render_template('show.html', productos=productos)


    
@productos.route('/filtro/<int:id>')
def filtrar(id):
    productos=  PRODUCTOS.get(id)
    return render_template('filtro.html', productos=productos)
    

@productos.route("/crear", methods=["POST"])
def crear_plato():
    
    name = request.form.get("name")
    price = request.form.get("price")
    productos = Producto(name=name, price=price)
    db.session.add(productos)
    db.session.commit()
    success_mesagge = 'Se ha agregado con exito!!'
    flash (success_mesagge)
    return redirect("/")
    


@productos.route("/borrar/<int:id>")
def borrar(id):
    producto =  Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect("/")

@productos.route('/editar/<int:id>')
def editar(id):
    productos =  Producto.query.get_or_404(id)
    return render_template('editar.html')

# ? Aqui estaran las vistas reetornando los templates
# ? Aqui estaran las vistas reetornando los templates