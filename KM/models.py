from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from datetime import date
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q

from USER.models import *



class Sekolah(models.Model):
    KATEGORI_CHOICES = (
        ('SMA', 'SMA'),

        ('Diploma 1', 'D1'),
        ('Diploma 2', 'D2'),
        ('Diploma 3', 'D3'),

        ('Strata 1', 'S1'),
        ('Strata 2', 'S2'),
        ('Strata 3', 'S3')
    )

    jenjang = models.CharField(max_length=15, choices=KATEGORI_CHOICES)
    nama_sekolah = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.jenjang +' '+self.nama_sekolah

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
    KATEGORI_CHOICES = (
        ('SMA', 'SMA'),

        ('Diploma 1', 'D1'),
        ('Diploma 2', 'D2'),
        ('Diploma 3', 'D3'),

        ('Strata 1', 'S1'),
        ('Strata 2', 'S2'),
        ('Strata 3', 'S3')
    )

    id_username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=50)
    slug = models.SlugField(default='', editable=False, max_length=140)
    NIK = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    email2= models.EmailField(null=True, blank=True)
    tanggal_bergabung = models.DateField(null=True, blank=True)
    alamat = models.TextField(blank=True, null=True)
    pendidikan_terakhir = models.CharField(max_length=10, choices=KATEGORI_CHOICES, default= 'Strata 1', blank=True, null=True)
    Institusi_pendidikan = models.OneToOneField(Sekolah, on_delete=models.CASCADE, default=True, blank=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    posisi = models.CharField(max_length=150, default=True, blank=True, null=True)
    golongan_peneliti = models.CharField(max_length=20, blank=True, null=True)
    jabatan_struktural = models.CharField(max_length=20, blank=True, null=True)
    kepakaran = models.CharField(max_length=80, blank=True, null=True)
    peminatan = models.CharField(max_length=80, blank=True, null=True)
    Tempat_Lahir = models.CharField(max_length=50, blank=True)
    Tanggal_Lahir = models.CharField(max_length=50, blank=True)
    foto = models.ImageField(upload_to="images/web/staff/", height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cv = models.FileField(upload_to="km/staff/cv/", blank=True, null=True)
    deskripsi_singkat= models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
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

class Publikasi (models.Model):
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
    
    TEMA_CHOICES = (
        ('HIV AIDS', 'HIV AIDS'),
        ('Publikasi', 'Publikasi'),
        ('Regulasi', 'Regulasi'),
        ('Lain-lain', 'Lain-lain')
    )

    project  = models.ForeignKey(Donor, on_delete=models.CASCADE, blank=True, null=True)
    tema = models.CharField(max_length=15, choices=TEMA_CHOICES, default='HIV AIDS', blank=True, null=True)
    judul  = models.CharField(max_length=50)
    slug = models.SlugField(default='', editable=False, max_length=140)
    penulis = models.ForeignKey(Staff, on_delete=models.CASCADE, default=True)
    tanggal = models.DateField(default=date.today)
    kategori  = models.CharField(max_length=30, choices = KATEGORI_CHOICES)
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
    gambar = models.ImageField(upload_to='document/KM/Inventaris')
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
    gambar = models.ImageField(upload_to='document/KM/Kontak')

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
    principal_investigator = models.ForeignKey(Staff, related_name='Principal_investigator', verbose_name="Principal Investigator", on_delete=models.CASCADE, default=True)
    PIC = models.ForeignKey(Staff, related_name='PIC_penelitian', verbose_name="PIC Penelitian", on_delete=models.CASCADE)
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

    penelitian = models.ForeignKey(Penelitian, on_delete=models.CASCADE)
    Kategori = models.CharField(max_length= 60, choices= KATEGORI_CHOICES)
    Judul = models.TextField(blank=True)
    dokumen = models.FileField(upload_to='KM/dokumenpenelitian')
    date_created = models.DateField(default=date.today)

    class Meta:
        verbose_name = ("Dokumen Penelitian")
        verbose_name_plural = ("Dokumen Penelitian")

    def __str__(self):
        return self.Kategori + str(self.penelitian)

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
    peran = models.CharField(max_length=10, choices=PERAN_CHOICES, null=True)
    laporan_kegiatan = models.FileField(upload_to='KM/peningkatan/laporan/', null=True, blank=True)
    materi = models.FileField(upload_to='KM/peningkatan/materi/')


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
    Judul = models.ForeignKey(PeningkatanKapasitas, on_delete=models.CASCADE)
    dokumen = models.FileField(upload_to='KM/peningkatankapasitas')
    date_created = models.DateField(default=date.today)

    class Meta:
        verbose_name = ("Dokumen Peningkatan")
        verbose_name_plural = ("Dokumen Peningkatan")

    def __str__(self):
        return self.Judul

    @property
    def tanggal(self):
        return self.date_created.strftime('%d %B %Y')

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
    judul = models.TextField()
    slug = models.SlugField(default='', editable=False, max_length=140)
    penulis = models.ForeignKey(Staff, on_delete=models.CASCADE, default=True)
    kategori = models.CharField(max_length=20, choices = KATEGORI_CHOICES)
    peran = models.CharField(max_length=20, choices = PERAN_CHOICES)
    tingkat = models.CharField(max_length=20, choices = TINGKAT_CHOICES)
    link = models.URLField(blank=True, null=True)

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