BarangElektronik = []
pilihan = 0

while pilihan != 7:
    print('''opsi:
    1.menambahkan barang
    2.menghapus salah satu barang
    3.mngedit salah satu barang
    4.menampilkan semua barang
    5.mengecek barang
    6.menampilkan index barang
    7.exit''')

    pilihan = int(input('masukkan opsi yang dipilih:'))

    if pilihan == 1:
        tambah = str(input('masukkan nama barang yang ingin ditambahkan:'))
        BarangElektronik.extend(tambah.split(','))

    elif pilihan == 2:
        hapus = int(input('masukkan index barang yang ingin di hapus:'))
        BarangElektronik.pop(hapus)

        lanjut = str(input('ketik y jika ingin melanjutkan program, selain itu stop:')).lower()
        if lanjut != 'y':
            break

    elif pilihan == 3:
        while True:
            edit = int(input('masukkan index yang ingin di edit:'))
            if edit > len(BarangElektronik):
                print('index ke-', edit, 'tdak terdapat dalam list')
            else:
                BarangElektronik [edit] = str(input('masukkan barang baru:'))

                lanjut = str(input('ketik y jika ingin melanjutkan program, selain itu stop:')).lower()
                if lanjut != 'y':
                    break

    elif pilihan == 4:
        for b in BarangElektronik:
            print(b)

    elif pilihan == 5:
        cek = str(input('masukkan nama barang yang ingin di cek:'))
        if cek in BarangElektronik:
            print('nama barang dengan nama', cek, 'tersedia dalam list')
        else:
            print('tidak tersedia dalam list')

    elif pilihan == 6:
        tampil = str(input('masukkan nama barang yang ingin dicek indexnya:'))
        if tampil in BarangElektronik:
            print(tampil, 'berada pada index ke-',BarangElektronik.index(tampil))
        else:
            print('masukkan nama barang dengan teliti')

print(BarangElektronik)


