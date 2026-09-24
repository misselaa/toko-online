# ==========================================
# FITUR LOGIN & REGISTER - TOKO ONLINE
# ==========================================

# Database sementara untuk menyimpan akun (Username : Password)
database_user = {
    "admin": "admin123",  # Akun bawaan
    "user1": "pass123"
}

def tampilkan_menu_awal():
    print("\n=======================================")
    print("      SELAMAT DATANG DI TOKO ONLINE    ")
    print("=======================================")
    print("1. Login")
    print("2. Register (Daftar Akun Baru)")
    print("3. Keluar")

def register():
    print("\n--- REGISTER AKUN BARU ---")
    username_baru = input("Buat username : ").strip()
    
    if not username_baru:
        print("❌ Username tidak boleh kosong!")
        return
        
    if username_baru in database_user:
        print("❌ Username sudah terdaftar! Gunakan username lain.")
        return

    password_baru = input("Buat password : ").strip()
    if not password_baru:
        print("❌ Password tidak boleh kosong!")
        return

    # Simpan ke database
    database_user[username_baru] = password_baru
    print(f"✅ Registrasi berhasil! Akun '{username_baru}' telah dibuat. Silakan login.")

def login():
    print("\n--- SILAKAN LOGIN ---")
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    # Cek apakah username ada dan passwordnya cocok
    if username in database_user and database_user[username] == password:
        print(f"\n🎉 Berhasil Login! Selamat datang, {username}!")
        return True  # Menandakan login sukses
    else:
        print("\n❌ Gagal Login: Username atau password salah.")
        return False

# Program Utama
def main():
    while True:
        tampilkan_menu_awal()
        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            status_login = login()
            if status_login:
                # Jika login berhasil, Anda bisa mengarahkan ke menu utama toko di sini
                print(">> Anda sekarang bisa mengakses fitur toko online.")
                break # Keluar dari menu login dan masuk aplikasi utama
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("\nTerima kasih! Keluar dari program.")
            break
        else:
            print("❌ Pilihan tidak valid, silakan pilih angka 1, 2, atau 3.")

if __name__ == "__main__":
    main()