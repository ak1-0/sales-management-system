from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import Product, Customer, Sale
from datetime import datetime

def init_routes(app):
    @app.route('/')
    def index():
        products = Product.query.all()
        customers = Customer.query.all()
        sales = Sale.query.all()
        return render_template('index.html', products=products, customers=customers, sales=sales)

    @app.route('/add_product', methods=['POST'])
    def add_product():
        name = request.form.get('name')
        price = request.form.get('price')
        if not name or not price:
            flash('Name and price are required!', 'error')
            return redirect(url_for('index'))
        
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        
        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))

    @app.route('/add_customer', methods=['POST'])
    def add_customer():
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        if not first_name or not last_name or not email:
            flash('First name, last name, and email are required!', 'error')
            return redirect(url_for('index'))
        
        new_customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone)
        db.session.add(new_customer)
        db.session.commit()
        
        flash('Customer added successfully!', 'success')
        return redirect(url_for('index'))

    @app.route('/make_sale', methods=['POST'])
    def make_sale():
        product_id = request.form.get('product_id')
        customer_id = request.form.get('customer_id')
        quantity = request.form.get('quantity')
        if not product_id or not customer_id or not quantity:
            flash('Product, customer, and quantity are required!', 'error')
            return redirect(url_for('index'))
        
        product = Product.query.get(product_id)
        if not product:
            flash('Product not found!', 'error')
            return redirect(url_for('index'))
        
        total_price = product.price * int(quantity)
        new_sale = Sale(product_id=product_id, customer_id=customer_id, sale_date=datetime.utcnow(), quantity=quantity, total_price=total_price)
        db.session.add(new_sale)
        db.session.commit()
        
        flash('Sale made successfully!', 'success')
        return redirect(url_for('index'))