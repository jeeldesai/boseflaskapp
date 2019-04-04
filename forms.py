from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class AddProduct(FlaskForm):
    productname = StringField('Product Name')
    productdescription = StringField('Description')
    productprice = StringField('Price')
    productimage = StringField('Image File Name')
    category = StringField('Category (Enter Integer)')
    submit = SubmitField('Submit')