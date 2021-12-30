# .\Flask\env\Scripts\activate 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:pw@localhost/name_of_db'

db = SQLAlchemy(app)

# class offer extends the class db.model. 
class Offers(db.Model):
    __tablename__ = 'offers'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200))
    price=db.Column(db.Numeric(5,2))
    price_before=db.Column(db.Numeric(5,2))
    from_date=db.Column(db.DateTime())
    to_date=db.Column(db.DateTime())
    image_url=db.Column(db.String(200))
    product_page_url=db.Column(db.String(200))
    company=db.Column(db.String(20))

    # Constructor of the object
    def __init__(self, name, price, price_before, from_date, to_date, image_url, product_page_url, company):
        self.name = name
        self.price = price
        self.price_before = price_before
        self.from_date = from_date
        self.to_date = to_date
        self.image_url = image_url
        self.product_page_url = product_page_url
        self.company = company
    

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', offers = Offers.query.all())

# Route to display prices in ascending order
@app.route('/sorted-price', methods=['GET'])
def price():
    return render_template('index.html', offers = Offers.query.order_by(Offers.price.asc()))

if __name__ == '__main__':
    app.run(debug=True)