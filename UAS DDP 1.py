## Nama kelas : orang
## properties : Nama, Tempat Lahir, Gendre
## Method     : _get()-->untuk mengambil nilai dari properties
##              _get()-->untuk memberikan nilai pada properties
class _orang():
    def _init_(self, nama, tmp_lahir, tgl_lahir, gender) :
       self.nama = nama
       self.tmp_lahir = tmp_lahir
       self.tgl_lahir = tgl_lahir
       self.gender = gender
    def _set(self, nama, tmp_lahir, tgl_lahir, gender):
       self.nama = nama
       self.tmp_lahir = tmp_lahir
       self.tgl_lahir = tgl_lahir
       self.gender = gender
    def _get(self):
      pass

## Memanggil kelas
p1 = _orang ()

arr_nama = []
arr_tmp = []
arr_tgl = []
arr_gend = []

print('======================================================')
print('                        DATA ORANG                    ')
print('======================================================')
print('Menu utama:')
print('[C]reate Data')
print('[R]ead Data')
print('[U]pdate Data')
print('[D]elete Data')
print('[V]iew Data')

lagi = True
while lagi:
    pilih = input('Input Pilihan [C/R/U/D/v] : ')
    if pilih in ('Cc'):
        _nama       = input('Nama Lengkap               : ')
        _tmpLahir   = input('Tempat Lahir               : ')
        _tglLahir   = input('Tanggal Lahir [dd/mm/yyyy] : ')
        _gender     = input('Gender [L/P]               : ')

        p1._set(_nama, _tmpLahir, _tglLahir, _gender)

        arr_nama.append(p1.nama)
        arr_tmp.append(p1.tmp_lahir)
        arr_tgl.append(p1.tgl_lahir)
        arr_gend.append(p1.gender)
    elif pilih in ('Rr'):
         _nama       = input('Nama Lengkap               : ')
         if arr_nama.count(_nama) > 0:
             _idx = arr_nama.index(_nama)
             p1._get()
             p1.tmp_lahir = arr_tmp[_idx]
             p1.tgl_lahir = arr_tgl[_idx]
             p1.gender = arr_gend[_idx]

             print('Tempat Lahir               :', p1.tmp_lahir)
             print('Tanggal Lahir [dd/mm/yyyy] :', p1.tgl_lahir)
             print('Gender [L/P]               :', p1.gender)
         else:
             print('Data tidak ditemukan.')
    elif pilih in ('Uu'):
        _nama        = input('Nama lengkap          : ')
        if arr_nama.count(_nama) > 0:
            _idx = arr_nama.index(_nama)
            _tmpLahir = input('Tempat Lahir                  : ')
            _tglLahir = input('Tempat Lahir [dd/mm/yyyy]     : ')
            _gender   = input('Gender [L/P]                  : ')

            p1._set(_nama, _tmpLahir, _tglLahir, _gender)
            arr_tmp[_idx] = p1.tmp_lahir
            arr_tgl[_idx] = p1.tgl_lahir
            arr_gend[_idx]= p1.gender
        else:
            print('Data tidak ditemukan.')

    elif pilih in('Dd'):
        _nama       = input('Nama Lengkap               : ')
        if arr_nama.count(_nama) > 0:
           _idx = arr_nama.index(_nama)
           arr_nama.pop(_idx)
           arr_tmp.pop(_idx)
           arr_tgl.pop(_idx)
           arr_gend.pop(_idx)
        else:
           print('Data tidak ditemukan.')
    elif pilih in('Vv'):
       print('===========================================================')
       print('         NAMA          |            TTL        | GENDER    ')
       print('===========================================================')
       for x in range(len(arr_nama)):
          print ('%-25s%-25s%3s' % (arr_nama[x], arr_tmp[x] + ', ' + arr_tgl[x], arr_gend[x]))
       print('===========================================================')
    else:
             print('Pilihan Salah, Silakan pilih lagi [C/R/U/D/V] |')

    print ()
    lagi = input('Input Data Lagi [Y/T] :')
    while lagi not in ('YyTt') :
             lagi = input('Input Data Lagi [Y/T] : ')

    if lagi in ('Tt'):
             lagi = False
