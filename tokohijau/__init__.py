from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tokoijo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Hubungkan db dengan app
    db.init_app(app)

    # Import models agar dikenali
    from . import models

    # Membuat tabel jika belum ada
    with app.app_context():
        db.create_all()

    # Tambahkan route dasar
    @app.route('/')
    def home():
        return render_template('index.html')

    return app