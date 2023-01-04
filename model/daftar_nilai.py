///tambah_data
elif c.lower() == 't':
i = open('view/database.txt', 'a')
P(" Tambah Kontak")
while (True):
    nama = input(" Nama : ")
    if nama == '':
        P(' Masukan dengan Nama Dengan Benar')
    else:
        break
while (True):
    try:
        nim = int(input(" NIM  : "))
        if nim == '':
            P(' Masukan Nim dengan Angka')
    except ValueError:
        P(' Masukan Nim dengan Angka')
    else:
        break
while (True):
    try:
        tugas = int(input(" TUGAS  : "))
        if tugas == '':
            P(' Masukan TUGAS dengan Angka')
    except ValueError:
        P(' Masukan TUGAS dengan Angka')
    else:
        break
while (True):
    try:
        uts = int(input(" UTS  : "))
        if uts == '':
            P(' Masukan UTS dengan Angka')
    except ValueError:
        P(' Masukan UTS dengan Angka')
    else:
        break
while (True):
    try:
        uas = int(input(" UAS  : "))
        if uas == '':
            P(' Masukan UAS dengan Angka')
    except ValueError:
        P(' Masukan UAS dengan Angka')
    else:
        break
akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
i.write('\nNama : ' + nama + '|Nim : ' + str(nim) + '|Tugas : ' + str(tugas) + '|UTS : ' + str(uts) + '|UAS : ' + str(
    uas) + "|Akhir : " + str(akhir) + '\n')
i.close()
Oc("clear")

///ubah_data
elif c.lower() == 'u':
u = open('view/database.txt', 'r').read().splitlines()
target = input(' Masukan Nama : ')
nm = []
for l in u:
    if l == '':
        pass
    else:
        l1 = l.replace('Nama : ', '').replace('Nim : ', '').replace('Tugas : ', '').replace('UTS : ', '').replace(
            'UAS : ', '').replace('Akhir : ', '')
        na, ni, tu, uts, uas, akhir = l1.strip().split('|')
        if na == target:
            P(' Mengedit Data %s' % (target))
            while (True):
                nama = input(" Nama : ")
                if nama == '':
                    P(' Masukan dengan Nama Dengan Benar')
                else:
                    break
            while (True):
                try:
                    nim = int(input(" NIM  : "))
                    if nim == '':
                        P(' Masukan Nim dengan Angka')
                except ValueError:
                    P(' Masukan Nim dengan Angka')
                else:
                    break
            while (True):
                try:
                    tugas = int(input(" TUGAS  : "))
                    if tugas == '':
                        P(' Masukan TUGAS dengan Angka')
                except ValueError:
                    P(' Masukan TUGAS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uts = int(input(" UTS  : "))
                    if uts == '':
                        P(' Masukan UTS dengan Angka')
                except ValueError:
                    P(' Masukan UTS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uas = int(input(" UAS  : "))
                    if uas == '':
                        P(' Masukan UAS dengan Angka')
                except ValueError:
                    P(' Masukan UAS dengan Angka')
                else:
                    break
            akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
            edit = ('Nama : ' + nama + '|Nim : ' + str(nim) + '|Tugas : ' + str(tugas) + '|UTS : ' + str(
                uts) + '|UAS : ' + str(uas) + "|Akhir : " + str(akhir) + '\n')
            nm.append(edit + '\n')
        else:
            nm.append(str(l) + '\n')
new = open('view/database.txt', 'w')
new.write(str(nm))
new.close()
new = open('view/database.txt', 'r').read().splitlines()
new1 = open('view/database.txt', 'w')
new1.close()
new2 = open('view/database.txt', 'a')
for i in new:
    i2 = i.replace("['", "").replace("\\n', '", "\n").replace("']", "").replace("\\n", "\n")
    new2.write(i2 + '\n')
new2.close()

///hapus_data
elif c.lower() == 'h':
u = open('view/database.txt', 'r').read().splitlines()
target = input(' Masukan Nama : ')
nm = []
for l in u:
    if l == '':
        pass
    else:
        l1 = l.replace('Nama : ', '').replace('Nim : ', '').replace('Tugas : ', '').replace('UTS : ', '').replace(
            'UAS : ', '').replace('Akhir : ', '')
        na, ni, tu, uts, uas, akhir = l1.strip().split('|')
        if str(na) == str(target):
            P('BERHASIL MENGHAPUS Data %s' % (target))
            pass
        else:
            nm.append(str(l) + '\n')
new = open('view/database.txt', 'w')
new.write(str(nm))
new.close()
new = open('view/database.txt', 'r').read().splitlines()
new1 = open('view/database.txt', 'w')
new1.close()
new2 = open('view/database.txt', 'a')
for i in new:
    i2 = i.replace("['", "").replace("\\n', '", "\n").replace("']", "").replace("\\n", '')
    new2.write(i2)
new2.close()

///cari_data
elif c.lower() == 'c':
cari = input(' cari : ')
i = open('view/database.txt', 'r').read().splitlines()
P(" ╔═════════════════════════════════════════════════════════════════════╗")
P(" ╠════════════════════════ DAFTAR DATA MAHASISWA ══════════════════════╣")
P(" ╠══════════════════╦══════════════════╦═══════╦═══════╦═══════╦═══════╣")
P(" ║      NAMA        ║       NIM        ║ TUGAS ║  UTS  ║  UAS  ║ AKHIR ║")
P(" ╠══════════════════╬══════════════════╬═══════╬═══════╬═══════╬═══════╣")
for l in i:
    if l == '':
        pass
    elif cari in l:
        l1 = l.replace('Nama : ', '').replace('Nim : ', '').replace('Tugas : ', '').replace('UTS : ', '').replace(
            'UAS : ', '').replace('Akhir : ', '')
        na, ni, tu, uts, uas, akhir = l1.strip().split('|')
        P((' ║ ') + (na).ljust(17) + ('║ ') + (ni).ljust(17) + ('║ ') + (tu).ljust(6) + ('║ ') + (uts).ljust(6) + (
            '║ ') + (uas).ljust(6) + ('║ ') + (akhir).ljust(6) + ('║'))
P(" ╚══════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")
