# run.py

from tokoijo import create_app, db

# Membuat instance aplikasi Flask
app = create_app()

# Perintah untuk membuat tabel database di awal
# Jalankan ini sekali saja atau setiap kali models.py berubah
with app.app_context():
    db.create_all()
    print("Database dan tabel telah dibuat!")

if __name__ == '__main__':
    # Menjalankan server pengembangan Flask
    app.run(debug=True)