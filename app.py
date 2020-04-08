from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.Integer, primary_key=True)
    starring = db.Column(db.Integer, primary_key=True)

    def __init__(self, title, year, rating, genre, starring)
      self.title = title
      self.year = year
      self.rating = rating
      self.genre = genre
      self.starring = starring
    
    class MovieSchema(ma.Schema):
        class Meta:
            fields = ("id", "title", "year","rating", "genre", "starring")
    
    movie_schema = MovieSchema()
    movies_schema = MovieSchema(many=True)

    @app.route("/", methods=["GET"])
    def home():
        return "<h1>Movie Database</h1>"