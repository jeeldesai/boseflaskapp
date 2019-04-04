from controller import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productdescription = db.Column(db.Text)
    productname = db.Column(db.String(120), index=True)
    productimage = db.Column(db.String(256), index=True)
    productprice = db.Column(db.Float, index=True)
    category = db.Column(db.Integer, index=True)

#    def __init__(self, quote,author,image):
#        self.quote = quote
#        self.author = author
#        self.image = image

    def __repr__(self):
        return '<Contains...%r>' % (self.productname)
