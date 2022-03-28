nama = []
pilihan = 0

while pilihan != 7:
    print('''opsi:
    1.menambahkan nama
    2.menghapus salah satu nama
    3.mengedit salah satu nama
    4.mengecek nama dalam list
    5.menampilkan semua nama
    6.menampilkan index barang
    7.exit
    ''')

    pilihan = int(input('masukkan opsi yang dipilih:'))
    if pilihan == 1:
        tambah = str(input('masukkan nama yang ingin ditambahkan:'))
        nama.extend(tambah.split(','))

    elif pilihan == 2:
        hapus = int(input('masukkan index yang ingin di hapus:'))
        nama.pop(hapus)

        lanjut = str(input('ketik y jika ingin melanjutkan, selain itu stop:')).lower()
        if lanjut != 'y':
            break

    elif pilihan == 3:
        while True:
            edit = int(input('masukkan index yang ingin di edit:'))
            if edit > len(nama):
                print('index ke-', edit, 'tidak dapat di edit karena index tersebut tidak ada dalam list')
            else:
                nama [edit] = str(input('masukkan nama baru:'))

                lanjut = str(input('ketik y jika ingin melanjutkan, selain itu stop:')).lower()
                if lanjut != 'y':
                    break

    elif pilihan == 4:
        cek = str(input('masukkan nama yang ingin di cek:'))
        if cek in nama:
            print('nama', cek, 'tersedia dalam list')
        else:
            print(cek, 'tidak tersedia dalam list')

    elif pilihan == 5:
        for i in nama:
            print(i)

    elif pilihan ==6:
        tampil = str(input('masukkan nama barang yang ingin ditampilkan indexnya:'))
        if tampil in nama:
            print(tampil, 'berada pada index ke-', nama.index(tampil))
        else:
            print('masukkan nama dengan benar')

print(nama)    