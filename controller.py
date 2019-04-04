from flask import Flask, flash, url_for, redirect, render_template, request, session, abort
import models
from config import Config
from flask_sqlalchemy import SQLAlchemy
#from forms import AddQuoteForm,SearchForm
from forms import AddProduct


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#By default, address points to /productlist
@app.route("/")
def soextra():
    return redirect('/productlist')

#Fetches all items from database
@app.route("/productlist", methods=['GET', 'POST'])
def hello():
    query = models.Product.query.all()
    return render_template(
        'prodlist.html',**locals())

#Displays product details in a new page
@app.route("/detail/<int:prodid>")
def detail(prodid):
    query = models.Product.query.filter_by(id=prodid)
    return render_template('detail.html',**locals())

#Displays a Form imported from W3Schools
@app.route("/contact")
def contact():
    return render_template('contact.html',**locals())

#Adds produsct to database
@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    theform = AddProduct()
    if theform.validate_on_submit():
        p = models.Product(productname=theform.productname.data,productdescription=theform.productdescription.data,
                           productimage=theform.productimage.data, productprice=theform.productprice.data)
        db.session.add(p)
        db.session.commit()
        flash("Added new product")
        return redirect('/productlist')
    return render_template('addproduct.html', title='Added a new Bose Product!', form=theform)


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
