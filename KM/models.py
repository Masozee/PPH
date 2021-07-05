from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from taggit.managers import TaggableManager
from datetime import date
from django.db.models import Q
from USER.models import *

class Jabatan(models.Model):
    jabatan = models.CharField(max_length=100)
    keterangan = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("Jabatan")
        verbose_name_plural = ("Jabatan")

    def __str__(self):
        return self.jabatan

class Posisi(models.Model):
    posisi = models.CharField(max_length=100)
    keterangan = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("Posisi")
        verbose_name_plural = ("Posisi")

    def __str__(self):
        return self.posisi

class Kepakaran(models.Model):
    pakar = models.CharField(max_length=100)
    keterangan = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("Kepakaran")
        verbose_name_plural = ("Kepakaran")

    def __str__(self):
        return self.pakar

class Peminatan(models.Model):
    minat = models.CharField(max_length=100)
    keterangan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.minat
        
    class Meta:
        verbose_name = ("Fokus Area")
        verbose_name_plural = ("Fokus Area")

    
# Create your models here
class StaffQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class StaffManager(models.Manager):
    def get_queryset(self):
        return StaffQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Staff (models.Model):
    STATUS_CHOICES = (
        ('Staff Peneliti','Staff Peneliti'),
        ('Staff Manajemen','Staf Manajemen'),
        ('Intern & Fellowship', 'Intern & Fellowship'),
        ('Lainnya', 'Lainnya'),
    )


    KATEGORI_CHOICES = (

        ('Diploma 3', 'D3'),
        ('Strata 1', 'S1'),
        ('Strata 2', 'S2'),
        ('Strata 3', 'S3')
    )

    User = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    nama = models.CharField(max_length=50)
    slug = models.SlugField(default='', editable=False, max_length=140)
    NIK = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    email2= models.EmailField(null=True, blank=True)
    tanggal_bergabung = models.DateField(null=True, blank=True)
    alamat = models.TextField(blank=True, null=True)
    pendidikan_1 = models.CharField(max_length=10, choices=KATEGORI_CHOICES, null=True, blank=True)
    jurusan_1 = models.TextField(null=True, blank=True)
    pendidikan_2 = models.CharField(max_length=10, choices=KATEGORI_CHOICES, null=True, blank=True)
    jurusan_2 = models.TextField(null=True, blank=True)
    pendidikan_3 = models.CharField(max_length=10, choices=KATEGORI_CHOICES,  null=True, blank=True)
    jurusan_3 = models.TextField(null=True, blank=True)
    pendidikan_4 = models.CharField(max_length=10, choices=KATEGORI_CHOICES,  null=True, blank=True)
    jurusan_4 = models.TextField(null=True, blank=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    posisi = models.CharField(max_length=150, default=True, blank=True, null=True)
    golongan_peneliti = models.CharField(max_length=20, blank=True, null=True)
    jabatan_struktural = models.CharField(max_length=20, blank=True, null=True)
    kepakaran = models.ForeignKey(Kepakaran, on_delete=models.PROTECT,blank=True, null=True)
    peminatan = models.ForeignKey(Peminatan, on_delete=models.PROTECT,blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    Tempat_Lahir = models.CharField(max_length=50, blank=True)
    Tanggal_Lahir = models.CharField(max_length=50, blank=True)
    foto = models.ImageField(upload_to="images/web/staff/", height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cv = models.FileField(upload_to="km/staff/cv/", blank=True, null=True)
    deskripsi_singkat= models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    no_urut = models.PositiveIntegerField(null=True)
    edited = models.DateTimeField(auto_now=True)


    objects = StaffManager()

    class Meta:
        verbose_name = ("Staff/Organisansi")
        verbose_name_plural = ("Staff/Organisansi")

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

#Donor----------------------------------------------------------------------------------------------------------------------------------------
class Donor(models.Model):
    nama = models.CharField(max_length= 150,)
    ket = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = ("Donor")
        verbose_name_plural = ("Donor")

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        value = self.nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

#Publikasi -----------------------------------------------------------------------------------------------------
class PublikasiQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(judul__icontains=query) |
                         Q(deskripsi__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class PublikasiManager(models.Manager):
    def get_queryset(self):
        return PublikasiQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Rak(models.Model):
    Nama = models.CharField(max_length=75)
    slug = models.SlugField(default='', editable=False, max_length=75)
    keterangan = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = ("Rak")
        verbose_name_plural = ("Rak")

    def __str__(self):
        return self.Nama

    def save(self, *args, **kwargs):
        value = self.Nama
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Publikasi (models.Model):
    MATERI = '0'
    LAPORAN = '1'
    POLICY = '2'
    MODUL = '3'
    SOP = '4'
    INFOGRAFIS = '5'
    ARTIKEL = '6'
    CONFERENCE = '7'
    REGULASI ='8'
    BUKU = '9'
    LAPORANKOMUNITAS = '10'
    LAIN = '11'
    LECTURE = '12'
    WORKSHOP = '13'
    HIV = '14'
    NAPZA = '15'
    KESWA = '16'
    JURNAS = '17'
    JURINTER = '18'


    KATEGORI_CHOICES = (
        (MATERI, 'Materi Pengetahuan HIV AIDS'),
        (LAPORAN,'Laporan Penelitian'),
        (POLICY, 'Policy Brief'),
        (MODUL,'Modul'),
        (SOP,'SOP'),
        (INFOGRAFIS, 'Infografis'),
        (ARTIKEL, 'Artikel Jurnal Nasional & Internasional'),
        (CONFERENCE, 'Conference'),
        (REGULASI, 'Regulasi'),
        (BUKU, 'buku'),
        (LAPORANKOMUNITAS, 'Laporan Pelayanan Komunitas'),
        (LECTURE, 'Lecture Series'),
        (WORKSHOP, 'Workshop'),
        (HIV, 'HIV - Aids'),
        (KESWA, 'Kesehatan Jiwa'),
        (NAPZA, 'Napza'),
        (JURNAS,'Jurnal Nasional'),
        (JURINTER,'Jurnal Internasional'),
        (LAIN, 'Lainnya')
    )

    INFORMASI = '0'
    PUBLIKASI = '1'
    REGULASI = '2'
    PENELITIAN ='3'
    PELAYANAN = '4'
    PENINGKATAN = '5'


    TEMA_CHOICES = (
        (INFORMASI, 'Informasi HIV AIDS'),
        (PUBLIKASI, 'Publikasi'),
        (REGULASI, 'Regulasi'),
        (PENELITIAN, 'Penelitian'),
        (PELAYANAN, 'Pelayanan Komunitas'),
        (PENINGKATAN, 'Peningkatan Kapasitas'),
    )

    project  = models.ForeignKey(Donor, on_delete=models.PROTECT, blank=True, null=True)
    tema = models.CharField(max_length=1, choices=TEMA_CHOICES, default='HIV AIDS', blank=True, null=True, verbose_name='Rak')
    judul  = models.CharField(max_length=150)
    slug = models.SlugField(default='', editable=False, max_length=140)
    penulis = models.ForeignKey(Staff, on_delete=models.PROTECT, default=True)
    tanggal = models.DateField(default=date.today)
    kategori  = models.CharField(max_length=2, choices = KATEGORI_CHOICES)
    gambar = models.ImageField(upload_to='images/KM/publikasi/', blank=True, null=True)
    deskripsi = RichTextField()
    date_upload = models.DateField( auto_now_add=True)
    download = models.FileField(upload_to='document/KM/publikasi')
    web_content = models.BooleanField(default=False)
    tagging = TaggableManager()

    objects = PublikasiManager()

    class Meta:
        verbose_name = ("Pustaka")
        verbose_name_plural = ("Pustaka")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thn(self):
        return self.tanggal.strftime('%Y')

#inventaris------------------------------------------------------------------------------------------------------
class InventarisQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class InventarisManager(models.Manager):
    def get_queryset(self):
        return InventarisQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Inventaris (models.Model):
    KATEGORI_CHOICES = (
        ('Hardware', 'Hardware'),
        ('Software', 'Software')
    )
    JENIS_CHOICES = (
        ('Tab', 'Tab'),
        ('Recorder', 'Recorder'),
        ('Laptop', 'Laptop'),
        ('Desktop','Desktop'),
        ('Lainnya', 'Lainnya')
    )

    kategori = models.CharField(max_length=8, choices = KATEGORI_CHOICES, default = 'Hardware' )
    jenis_barang = models.CharField(max_length=10, choices=JENIS_CHOICES)
    nama_barang =models.CharField(max_length=100, default=True)
    tahun_pembelian = models.DateField(blank=True, null=True)
    slug = models.SlugField(default='', editable=False, max_length=140)
    deskripsi = models.TextField(blank=True, null=True)
    gambar = models.ImageField(upload_to='document/KM/Inventaris', null=True, blank=True)
    Tersedia = models.BooleanField(default=True)

    objects = InventarisManager()

    class Meta:
        verbose_name = ("Inventory")
        verbose_name_plural = ("Inventory")

    def __str__(self):
        return self.nama_barang

    def save(self, *args, **kwargs):
        value = self.nama_barang
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

#Kontak ------------------------------------------------------------------------------------------------------
class kontakQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama_organisasi__icontains=query) |
                         Q(Kontak__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class kontakManager(models.Manager):
    def get_queryset(self):
        return kontakQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Kontak_PPH (models.Model):
    KATEGORI_CHOICES = (
        ('Pemerintah Implementer', 'Pemerintah Implementer'),
        ('Pemerintah Stakeholder', 'Pemerintah Stakeholder'),
        ('Non Pemerintah Implementer', 'Non Pemerintah Implementer'),
        ('Non Pemerintah Stakeholder','Non Pemerintah Stakeholder'),
    )

    kategori_kontak = models.CharField(choices = KATEGORI_CHOICES, max_length=30 )
    nama_organisasi = models.CharField(max_length=100)
    Kontak = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(default='', editable=False, max_length=140)
    email = models.EmailField(blank=True, null=True)
    no_hp = models.CharField(max_length=13, blank=True, null=True )
    no_telp = models.CharField(max_length=13, blank=True, null=True )

    objects = kontakManager()

    class Meta:
        verbose_name = ("Kontak")
        verbose_name_plural = ("Kontak")

    def __str__(self):
        return self.nama_organisasi

    def save(self, *args, **kwargs):
        value = self.nama_organisasi
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

#Penelitian------------------------------------------------------------------------------------------------------
class PenQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama_kegiatan__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class PenManager(models.Manager):
    def get_queryset(self):
        return PenQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Penelitian(models.Model):
    KATEGORI_CHOICES = (
        ('Kebijakan', 'Kebijakan'),
        ('Sosial Perilaku', 'Sosial Perilaku'),
        ('Bio-medis', 'Bio-medis'),
        ('Operasional', 'Operasional'),
    )
    Status_CHOICES = (
        ('Initiating', 'Initiating'),
        ('Planning', 'Planning'),
        ('Executing', 'Executing'),
        ('Closing', 'Closing'),
        ('Completed', 'Completed')
    )

    nama_kegiatan = models.CharField(max_length=150)
    slug = models.SlugField(default='', editable=False, max_length=140)
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES)
    mulai = models.DateField()
    selesai = models.DateTimeField()
    sumber_dana = models.ManyToManyField(Donor)
    organisasi_mitra = models.TextField(blank=True)
    mata_uang = models.CharField(max_length=10)
    nominal = models.IntegerField()
    principal_investigator = models.ForeignKey(Staff, related_name='Principal_investigator', verbose_name="Principal Investigator", on_delete=models.PROTECT, default=True)
    PIC = models.ForeignKey(Staff, related_name='PIC_penelitian', verbose_name="PIC Penelitian", on_delete=models.PROTECT, blank=True)
    tim = models.ManyToManyField(Staff)
    status = models.CharField(max_length=10, choices=Status_CHOICES)

    objects = PenManager()

    class Meta:
        verbose_name = ("Penelitian")
        verbose_name_plural = ("Penelitian")

    def __str__(self):
        return self.nama_kegiatan

    def save(self, *args, **kwargs):
        value = self.nama_kegiatan
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thnmly(self):
        return self.mulai.strftime('%Y')

    @property
    def thnslsy(self):
        return self.selesai.strftime('%Y')

    @property
    def pmulai(self):
        return self.mulai.strftime('%d %B %Y')

    @property
    def pselesai(self):
        return self.selesai.strftime('%d %B %Y')

    @property
    def thn(self):
        return self.mulai.strftime('%Y')

class DokuPenelitianQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class DokuPenelitianManager(models.Manager):
    def get_queryset(self):
        return DokuPenelitianQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class DokumenPenelitian(models.Model):
    KATEGORI_CHOICES = (
        ('Proposal - Penelitian', 'Proposal Penelitian'),
        ('Proposal - Budget Plan', 'Proposal Budget Plan'),
        ('Proposal - Protokol Penelitian', 'Proposal Protokol Penelitian'),
        ('Referensi - Nasional', 'Referensi Nasional'),
        ('Referensi - Interasional', 'Referensi Interasional'),
        ('Instrumen - Kuantitatif', 'Instrumen Kuantitatif'),
        ('Instrumen - Kualitatif', 'Instrumen Kualitatif'),
        ('Data - Kuantitatif','Data Kuantitatif'),
        ('Data - Kualitatif', 'Data Kualitatif'),
        ('Hasil Analisis - Kuantitatif','Hasil Analisis Kuantitatif'),
        ('Hasil Analisis - Kualitatif', 'Hasil Analisis Kualitatif'),
        ('Laporan Penelitian', 'Laporan Penelitian'),
        ('Diseminasi Penelitian - Kerangka Acuan', 'Diseminasi Penelitian Kerangka Acuan'),
        ('Diseminasi Penelitian - Materi', 'Diseminasi Penelitian Materi'),
        ('Diseminasi Penelitian - Notulensi', 'Diseminasi Penelitian Notulensi'),
        ('Diseminasi Penelitian - Foto', 'Diseminasi Penelitian Foto'),
        ('Diseminasi Penelitian - Daftar Hadir', 'Diseminasi Penelitian Daftar Hadir'),
        ('Administrasi dan Keuangan - Izin Penelitian', 'Administrasi dan Keuangan Izin Penelitian'),
        ('Administrasi dan Keuangan - Ethical Clearance', 'Administrasi dan Keuangan Ethical Clearance'),
        ('Administrasi dan Keuangan - Kontrak atau MoU', 'Administrasi dan Keuangan Kontrak atau MoU'),
        ('Administrasi dan Keuangan - Laporan Keuangan', 'Administrasi dan Keuangan Laporan Keuangan'),
        ('Pertemuan dan rapat - Notulensi', 'Pertemuan dan rapat - Notulensi')
    )

    penelitian = models.ForeignKey(Penelitian, on_delete=models.PROTECT, default=True)
    Kategori = models.CharField(max_length= 60, choices= KATEGORI_CHOICES)
    Judul = models.TextField()
    dokumen = models.FileField(upload_to='KM/dokumenpenelitian')
    date_created = models.DateField(default=date.today)

    objects = DokuPenelitianManager()

    class Meta:
        verbose_name = ("Dokumen Penelitian")
        verbose_name_plural = ("Dokumen Penelitian")

    def __str__(self):
        return str(self.pk)

    @property
    def tanggal(self):
        return self.date_created.strftime('%d %B %Y')

#Peningkatan Kapasitas ------------------------------------------------------------------------------------------------------
class kapasitasQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(judul__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class KapasitasManager(models.Manager):
    def get_queryset(self):
        return kapasitasQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class PeningkatanKapasitas(models.Model):
    KATEGORI_CHOICES = (
        ('Lecture Series', 'Lecture Series'),
        ('Workshop dan Pelatihan', 'Workshop dan Pelatihan'),
        ('Pertemuan dan Seminar', 'Pertemuan dan Seminar'),
        ('Kursus Online', 'Kursus Online'),
        ('Fun Sharing Day', 'Fun Sharing Day'),
        ('Liputan Media', 'Liputan Media'),
        ('Konferensi Nasional', 'Konferensi Nasional'),
        ('Konferensi Internasional', 'Konferensi Internasional')
    )

    PERAN_CHOICES = (
        ('Peserta', 'Peserta'),
        ('Pembicara', 'Pembicara'),
        ('Moderator', 'Moderator'),
        ('Konsultan', 'Konsultan'),
        ('MC', 'MC'),
        ('Presenter', 'Presenter')
    )
    PENYELENGGARA_CHOICES = (
        ('PPH UNIKA Atma Jaya', 'PPH UNIKA Atma Jaya'),
        ('Non PPH', 'Non PPH')
    )
    jenis = models.CharField(max_length=20, choices=PENYELENGGARA_CHOICES, default="PPH UNIKA Atma Jaya")
    kategori = models.CharField(max_length=25, choices=KATEGORI_CHOICES)
    judul = models.CharField(max_length=200)
    slug = models.SlugField(default='', editable=False, max_length=140)
    mulai = models.DateField()
    selesai = models.DateField()
    sumber_dana = models.ManyToManyField(Donor)
    mata_uang = models.CharField(max_length=10,null=True)
    budget = models.IntegerField(null=True)
    pengeluaran = models.IntegerField(null=True)
    lokasi = models.TextField(null=True, blank=True)
    kota = models.CharField(max_length=15, null=True, blank=True)
    negara = models.CharField(max_length=15, null=True, blank=True)
    pembicara = models.ManyToManyField(Staff)
    penyelenggara = models.CharField(max_length=100, default=True)


    objects = KapasitasManager()

    class Meta:
        verbose_name = ("Peningkatan Kapasitas")
        verbose_name_plural = ("Peningkatan Kapasitas")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thnmly(self):
        return self.mulai.strftime('%Y')

    @property
    def thnslsy(self):
        return self.selesai.strftime('%Y')

    @property
    def pmulai(self):
        return self.mulai.strftime('%d %B %Y')

    @property
    def pselesai(self):
        return self.selesai.strftime('%d %B %Y')


class DokuPeningkatanQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class DokuPeningkatanManager(models.Manager):
    def get_queryset(self):
        return DokuPenelitianQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class DokumenPeningkatan(models.Model):
    KATEGORI_CHOICES = (
        ('Substansi - Kerangka Acuan', 'Substansi - Kerangka Acuan'),
        ('Substansi - Budget Plan', 'SUbstansi - Budget Plan'),
        ('Pendukung - Poster', 'Pendukung - Poster'),
        ('Pendukung - Foto', 'Pendukung - Foto'),
        ('Pendukung - Daftar Hadir', 'Pendukung - Daftar Hadir'),
        ('Pendukung - Evaluasi Peserta', 'Pendukung - Evaluasi Peserta'),
        ('Pendukung - Laporan Keuangan', 'Pendukung - Laporan Keuangan')
    )

    kategori = models.CharField(max_length=35, choices=KATEGORI_CHOICES)
    Judul = models.ForeignKey(PeningkatanKapasitas, on_delete=models.PROTECT)
    dokumen = models.FileField(upload_to='KM/peningkatankapasitas')
    date_created = models.DateField(default=date.today)

    objects=DokuPeningkatanManager()

    class Meta:
        verbose_name = ("Dokumen Peningkatan")
        verbose_name_plural = ("Dokumen Peningkatan")

    def __str__(self):
        return str(self.Judul)

    @property
    def tanggal(self):
        return self.date_created.strftime('%d %B %Y')


class MediaAdvQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class MediaAdvManager(models.Manager):
    def get_queryset(self):
        return MediaAdvQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class MediaAdvokasi(models.Model):
    KATEGORI_CHOICES = (
        ('Research Report', 'Research Report'),
        ('Policy Brief', 'Policy Brief'),
        ('Lembar Fakta', 'Lembar Fakta'),
        ('Press release', 'Press release'),
        ('Infografis', 'Infografis'),
        ('HIV AIDS', 'HIV AIDS'),
        ('NAPZA', 'NAPZA'),
        ('Kesehatan Jiwa', 'Kesehatan Jiwa'),
        ('Newsletter', 'Newsletter'),
        ('Annual Report', 'Annual Report'),
        ('Lainnya', 'Lainnya')
    )

    judul = models.CharField(max_length=200)
    slug = models.SlugField(default='', editable=False, max_length=140)
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES)
    sumber = models.CharField(max_length=25, null=True, blank=True)
    tahun = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='km/mediaadvokasi/',null=True, blank=True)
    keterangan = models.TextField(null=True, blank=True)

    objects = MediaAdvManager()

    class Meta:
        verbose_name = ("Media Advokasi")
        verbose_name_plural = ("Media Advokasi")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thn(self):
        return self.tahun.strftime('%Y')

class ManajemenQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class ManajemenManager(models.Manager):
    def get_queryset(self):
        return ManajemenQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Manajemen(models.Model):
    KATEGORI_CHOICES = (
        ('Kontrak/MOU', 'Kontrak/MOU'),
        ('SOP', 'SOP'),
        ('Template', 'Template')
    )
    judul = models.CharField(max_length=200)
    slug = models.SlugField(default='', editable=False, max_length=140)
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES)
    tahun = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='km/manajemen/', null=True, blank=True)
    keterangan = models.TextField(null=True, blank=True)

    objects = ManajemenManager()

    class Meta:
        verbose_name = ("Manajemen")
        verbose_name_plural = ("Manajemen")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thn(self):
        return self.tahun.strftime('%Y')

class PublikasiStaffQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class PublikasiStaffManager(models.Manager):
    def get_queryset(self):
        return PublikasiStaffQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Publikasi_staff(models.Model):
    
    KATEGORI_CHOICES = (
        ('Artikel Ilmiah', 'Artikel Ilmiah'),
        ('Artikel Non-ilmiah', 'Artikel Non-ilmiah'),
        ('Policy Brief', 'Policy Brief'),
        ('Buku/Chapter Buku', 'Buku/Chapter Buku'),
        ('Lainnya', 'Lainnya'),
    )
    
    PERAN_CHOICES = (
        ('Penulis Utama', 'Penulis Utama'),
        ('Penulis Pendamping', 'Penulis Pendamping'),
        ('Editor', 'Editor'),
        ('Lainnya','Lainnya')
    )
    
    TINGKAT_CHOICES = (
        ('Nasional', 'Nasional'),
        ('Internasional', 'Internasional'),
    )
    
    tahun = models.DateField()
    judul = models.CharField(max_length=150, default='Admin.PPH')
    slug = models.SlugField(default='', editable=False, max_length=140)
    peserta = models.CharField(max_length=150, default='Admin.PPH')
    #peserta = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    kategori = models.CharField(max_length=20, choices = KATEGORI_CHOICES)
    peran = models.CharField(max_length=20, choices = PERAN_CHOICES)
    tingkat = models.CharField(max_length=20, choices = TINGKAT_CHOICES)
    link = models.URLField(blank=True, null=True)

    objects = PublikasiStaffManager()

    class Meta:
        verbose_name = ("Publikasi Staff")
        verbose_name_plural = ("Publikasi Staff")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thn(self):
        return self.tahun.strftime('%Y')


class PeningkatanStaffQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(nama__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class PeningkatanStaffManager(models.Manager):
    def get_queryset(self):
        return PeningkatanStaffQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class PeningkatanKapasitasstaff(models.Model):
    KATEGORI_CHOICES = (
        ('Lecture Series', 'Lecture Series'),
        ('Workshop dan Pelatihan', 'Workshop dan Pelatihan'),
        ('Pertemuan dan Seminar', 'Pertemuan dan Seminar'),
        ('Kursus Online', 'Kursus Online'),
        ('Fun Sharing Day', 'Fun Sharing Day'),
        ('Liputan Media', 'Liputan Media'),
        ('Konferensi Nasional', 'Konferensi Nasional'),
        ('Konferensi Internasional', 'Konferensi Internasional')
    )

    PERAN_CHOICES = (
        ('Peserta', 'Peserta'),
        ('Pembicara', 'Pembicara'),
        ('Moderator', 'Moderator'),
        ('Konsultan', 'Konsultan'),
        ('MC', 'MC'),
        ('Presenter', 'Presenter')
    )

    kategori = models.CharField(max_length=25, choices=KATEGORI_CHOICES)
    peserta = models.CharField(max_length=150, default='Admin.PPH')
    #peserta = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    peran =models.CharField(max_length=25, choices=PERAN_CHOICES)
    judul = models.CharField(max_length=200,default='Admin.PPH')
    slug = models.SlugField(default='', editable=False, max_length=140)
    mulai = models.DateField()
    selesai = models.DateField()
    lokasi = models.TextField(null=True, blank=True)
    pembicara = models.TextField(blank=True)
    penyelenggara = models.TextField()
    laporan_kegiatan = models.FileField(upload_to='KM/staff/peningkatan/laporan/', null=True, blank=True)
    materi = models.FileField(upload_to='KM/staff/peningkatan/materi/', null=True, blank=True)

    objects = PeningkatanStaffManager()

    class Meta:
        verbose_name = ("Peningkatan Kapasitas Staff")
        verbose_name_plural = ("Peningkatan Kapasitas Staff")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thn(self):
        return self.mulai.strftime('%Y')

class PersonalEvent(models.Model):
    acara = models.CharField(max_length=250)
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=True)
    mulai = models.DateTimeField()
    selesai = models.DateTimeField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.acara