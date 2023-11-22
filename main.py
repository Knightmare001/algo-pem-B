import pandas as pd

fileExcel = "daftar_nama.xlsx"
fileCsv = "daftar_nama.csv"


def membaca(extensi):
    data = ""
    if extensi == "excel":
        data = pd.read_excel(fileExcel)
    elif extensi == "csv":
        data = pd.read_csv(fileCsv, sep=";")
    return data


def menambahkanData(extensi):
    if extensi == "excel":
        nama = input("Masukkan nama : ")
        npm = input("Masukkan npm : ")
        dataLama = membaca("excel")
        dataBaru = {"Nama": [nama], "NPM": [npm]}
        dataGabungan = pd.concat([dataLama, pd.DataFrame(dataBaru)])
        dataGabungan.to_excel(fileExcel, index=False)


def menghapusData():
    print("\033c", end="")
    print(membaca("excel"))
    cari = int(input("Masukkan NPM yang ingin dihapus : "))
    data = membaca("excel")
    find = mencariData(cari)

    try:
        data.drop(find.name, inplace=True)
        data.to_excel(fileExcel, index=False)
    except:
        print(find)
    else:
        print("Data berhhasil dihapus")


def mencariData(user):
    data = membaca("excel")
    found = False
    for baris in range(len(data.NPM)):
        if data.NPM[baris] == user:
            found = True
            # print(data.Nama[baris], data.NPM[baris])
            return data.iloc[baris]
    if found != True:
        return "data tidak ditemukan"


def menu_excel():
    while True:
        print("\033c", end="")
        print("========== Apa yang ingin Anda lakukan ============")
        print("1. Membaca file excel")
        print("2. Mencari data")
        print("3. Menambahkan data ke dalam file excel")
        print("4. Menghapus data file excel")
        try:
            pilihan = int(input("Masukkan pilihan anda : "))
        except ValueError:
            print("pilihan tidak valid")
            input("tekan enter untuk lanjut....")
        else:
            if pilihan == 1:
                print(membaca("excel"))
            elif pilihan == 2:
                cari = int(input("Masukkan NPM yang ingin dicari : "))
                print(mencariData(cari))
            elif pilihan == 3:
                menambahkanData("excel")
                print(membaca("excel"))
                print("Data berhasil ditambahkan")
            elif pilihan == 4:
                menghapusData()
                print(membaca("excel"))
            else:
                print("pilihan tidak valid")

            lagi = input("Ingin melakukannya lagi(y/Y)? : ")
            if lagi.lower() == "y":
                menu_excel()
            else:
                break


menu_excel()
