from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from datetime import date
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q
from KM.models import Staff, Donor, Publikasi
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from taggit.models import TagBase, GenericTaggedItemBase
from django.utils.translation import ugettext_lazy as _

from django.core.validators import RegexValidator

#berita 
class BeritaQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(judul__icontains=query) |
                         Q(isi__icontains=query)
                         )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class BeritaManager(models.Manager):
    def get_queryset(self):
        return BeritaQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)


class Author(TagBase):
    ket = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Peneliti")
        verbose_name_plural = _("Peneliti")

class TaggedAuthor(GenericTaggedItemBase):
    tag = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_items",
    )
    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Author")

class Berita (models.Model):
    KATEGORI_CHOICES = (
        ('Artikel','Artikel'),
        ('Dokumentasi', 'Dokumentasi'),
        ('Newsletter', 'Newsletter'),
    )
    AGENDA_CHOICES = (
        ('Penelitian', 'Penelitian'),
        ('Advokasi', 'Advokasi'),
        ('Peningkatan Kapasitas', 'Peningkatan Kapasitas'),
        ('Pelayanan Komunitas', 'Pelayanan Komunitas'),
        ('Newsletter', 'Newsletter'),
    )

    Kategori = models.CharField(max_length=25, choices=KATEGORI_CHOICES, default= 'Dokumentasi')
    Agenda = models.CharField(max_length=25, choices=AGENDA_CHOICES, default='Penelitian')
    judul = models.CharField(max_length=150)
    penulis = models.ForeignKey(Staff, on_delete=models.PROTECT, default=True, blank=True, null=True)
    penulis_luar = TaggableManager(through=TaggedAuthor, related_name='abstracts', verbose_name='Penulis Lain', blank=True)
    slug = models.SlugField(default='', editable=False, max_length=140)
    tanggal = models.DateField()
    isi = RichTextField()
    sumber = models.CharField(max_length=50, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    gambar = models.ImageField( upload_to='images/web/berita', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    ket_gambar = models.CharField(max_length=100, blank=True, null=True)
    download = models.FileField(upload_to='document/web/berita', blank = True, null = True)
    dibuat = models.DateTimeField(auto_now_add=True)
    dirubah = models.DateTimeField(auto_now=True )
    tags = TaggableManager()

    objects = BeritaManager()

    class Meta:
        verbose_name = ("Berita")
        verbose_name_plural = ("Berita")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    _metadata = {
        'title': 'judul',
        'image': 'get_meta_image',
    }
    def get_meta_image(self):
        if self.gambar:
            return self.gambar.url

    @property
    def thn(self):
        return self.tanggal.strftime('%d %B %Y')

    @property
    def bln(self):
        return self.tanggal.strftime('%b')

    @property
    def tgl(self):
        return self.tanggal.strftime('%d')


#Acara
class AcaraQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(judul__icontains=query) |
                         Q(isi__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class AcaraManager(models.Manager):
    def get_queryset(self):
        return AcaraQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Acara (models.Model):
    AGENDA_CHOICES = (
        ('Penelitian', 'Penelitian'),
        ('Advokasi', 'Advokasi'),
        ('Peningkatan Kapasitas', 'Peningkatan Kapasitas'),
        ('Pelayanan Komunitas', 'Pelayanan Komunitas'),

    )
    Agenda = models.CharField(max_length=25, choices=AGENDA_CHOICES, default='Penelitian')
    judul = models.CharField(max_length=150)
    slug = models.SlugField(default='', editable=False, max_length=140)
    subjudul = models.CharField(max_length=200, blank=True, null=True)
    isi = RichTextField()
    lokasi = models.CharField( max_length=200)
    waktu_mulai = models.DateTimeField()
    waktu_selesai = models.DateTimeField()
    link = models.URLField( blank=True)
    gambar = models.ImageField(upload_to='images/web/acara/', blank=True, null=True)
    ket_gambar = models.CharField(max_length=50, blank=True)
    download = models.FileField(upload_to='document/web/acara/', blank=True, null=True)
    dibuat = models.DateTimeField(auto_now_add=True)
    dirubah = models.DateTimeField(auto_now=True )
    tags = TaggableManager()

    objects = AcaraManager()

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Event")

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def thn(self):
        return self.waktu_mulai.strftime('%Y')
    
    @property
    def thnlgkp(self):
        return self.waktu_mulai.strftime('%d %B %Y')

    @property
    def bln(self):
        return self.waktu_mulai.strftime('%b')

    @property
    def tgl(self):
        return self.waktu_mulai.strftime('%d')

    @property
    def sls(self):
        return self.waktu_selesai.strftime('%d')

    @property
    def wktmly(self):
        return self.waktu_mulai.strftime('%H' '.' '%M')

    @property
    def wktsls(self):
        return self.waktu_selesai.strftime('%H' '.' '%M')

    @property
    def jam(self):
        return self.waktu_selesai.strftime('%X')

class TentangKami (models.Model):
    tanggal = models.DateField(auto_now_add=True)
    sejarah = RichTextField()
    history = RichTextField()
    visi = models.TextField()
    vison = models.TextField()
    misi = models.TextField()
    mission =models.TextField()

    class Meta:
        verbose_name = ("Tentang Kami")
        verbose_name_plural = ("tentang Kami")

    def __str__(self):
        return str(self.tanggal)
   
class HomeSLide (models.Model):
    tanggal = models.DateField()
    slide1_img = models.ImageField(upload_to='images/web/homepage')
    Slide1_desc = models.CharField(max_length=30)
    Slide1_link = models.TextField(default="#")
    slide2_img = models.ImageField(upload_to='images/web/homepage')
    Slide2_desc = models.CharField(max_length=30)
    Slide2_link = models.TextField(default="#")
    slide3_img = models.ImageField(upload_to='images/web/homepage')
    Slide3_desc = models.CharField(max_length=30)
    Slide3_link = models.TextField(default="#")
    tentang_kami = models.ImageField(upload_to='images/web/homepage', default=True)
    pustaka = models.ImageField(upload_to='images/web/homepage', default=True)
    kesehatan = models.ImageField(upload_to='images/web/homepage', default=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    kesjiw_banner=RichTextField(null=True)
    kesjiw_history=RichTextField(null=True)
    kesjiw_history_highlight = RichTextField(null=True)
    pustaka_desc = models.CharField(max_length=300, blank=True, null=True)
    pustaka_HIV_judul = models.CharField(max_length=100, blank=True, null=True)
    pustaka_HIV_ket = models.CharField(max_length=250, blank=True, null=True)
    pustaka_publikasi_judul = models.CharField(max_length=100,blank=True, null=True)
    pustaka_publikasi_ket = models.CharField(max_length=250,blank=True, null=True)
    pustaka_regulasi_judul = models.CharField(max_length=100,blank=True, null=True)
    pustaka_regulasi_ket = models.CharField(max_length=250,blank=True, null=True)
    about_desc = RichTextField(null=True)
    about_desc_en = RichTextField(null=True)
    cop = RichTextField(null=True)
    about_cop = RichTextField(null=True)


    class Meta:
        verbose_name = ("Web Settings")
        verbose_name_plural = ("Web Settings")

    def __str__(self):
        return str(self.tanggal)

class Kontak (models.Model):
    nama_kntk = models.CharField(max_length=50, null=True)
    email_kntk = models.EmailField(blank=True, null=True)
    telp_kntk = models.CharField(max_length=15, null=True, blank=True)
    org_kntk = models.CharField(max_length=150, null=True, blank=True)
    pesan_kntk = models.TextField(blank=True, null=True)
    tanggal_kntk = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Kontak")
        verbose_name_plural = ("Kontak")

    def __str__(self):
        return self.nama_kntk

class downloadForm(models.Model):
    nama = models.CharField(max_length = 50)
    email = models.EmailField(blank=True, null=True)
    organisasi = models.TextField(blank=True)
    dokumen = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField( auto_now_add=True )
    url = models.TextField(blank=True, null=True)
    

    class Meta:
        verbose_name = ("Download")
        verbose_name_plural = ("Download")

    def __str__(self):
        return self.nama

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class TagAnotated(TagBase):
    class Meta:
        verbose_name = _("Annotated Tags")
        verbose_name_plural = _("Annotated Tags")

class TaggedAnnotated(GenericTaggedItemBase):
    tag = models.ForeignKey(
        TagAnotated,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_items",
    )
    class Meta:
        verbose_name = _("Annotate Tags")
        verbose_name_plural = _("Annotate Tags")

class anotatedQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(judul__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class anotatedManager(models.Manager):
    def get_queryset(self):
        return anotatedQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class AnotatedCOP(models.Model):
    judul = models.CharField(max_length=300)
    slug = models.SlugField(default='', editable=False, max_length=140)
    tanggal = models.DateField()
    Author = TaggableManager(through=TaggedAuthor, related_name='+', verbose_name='Author')
    sumber = models.CharField(max_length=120, blank=True)
    volume = models.CharField(max_length=10, blank=True)
    DOI_number = models.CharField(max_length=120, blank=True)
    DOI_URL = models.URLField(blank=True)
    doctype = models.CharField(max_length=4, blank=True)
    url = models.URLField(blank=True)
    download = models.FileField(upload_to='anotated/', blank=True)
    bibliografi = RichTextField(blank=True)
    anotated = RichTextField(blank=True)
    visit_num = models.PositiveIntegerField(default=0)

    tags = TaggableManager(through=TaggedAnnotated, related_name='tagannotated', verbose_name='Annotated Tags')

    objects = anotatedManager()

    class Meta:
        verbose_name = ("Anotated COP")
        verbose_name_plural = ("Anotated COP")

    def __str__(self):
        return self.judul

    def get_absolute_url(self):
        return reverse('books:detail', args=[self.id])

    def save(self, *args, **kwargs):
        value = self.judul
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


    @property
    def tgl(self):
        return self.tanggal.strftime('%d %B %Y')

class LayananKeswa(models.Model):
    KATEGORI_CHOICES = (
        ('RSUD/RSJ', 'RSUD/RSJ'),
        ('Puskesmas', 'Puskesmas'),
        ('Klinik/Layanan Swasta', 'Klinik/Layanan Swasta'),
    )
    PROVINSI_CHOICES = (
        ('Aceh', 'Aceh'),
        ('Sumatera Utara', 'Sumatera Utara'),
        ('Sumatera Barat', 'Sumatera Barat'),
        ('Riau', 'Riau'),
        ('Kepulauan Riau', 'Kepulauan Riau'),
        ('Jambi', 'Jambi'),
        ('Bengkulu', 'Bengkulu'),
        ('Sumatera Selatan', 'Sumatera Selatan'),
        ('Kepulauan bangka Belitung', 'Kepulauan bangka Belitung'),
        ('lampung', 'lampung'),
        ('Banten', 'Banten'),
        ('Jawa Barat', 'Jawa Barat'),
        ('Jakarta', 'Jakarta'),
        ('Jawa Tengah', 'Jawa Tengah'),
        ('Yogyakarta', 'Yogyakarta'),
        ('Jawa Timur', 'Jawa Timur'),
        ('Bali', 'Bali'),
        ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'),
        ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'),
        ('Kalimantan Barat', 'Kalimantan Barat'),
        ('Kalimantan Selatan', 'Kalimantan Selatan'),
        ('Kalimantan Tengah', 'Kalimantan Tengah'),
        ('Kalimantan Timur', 'Kalimantan Timur'),
        ('kalimantan Utara', 'kalimantan Utara'),
        ('Gorontalo', 'Gorontalo'),
        ('Sulawesi Barat', 'Sulawesi Barat'),
        ('Sulawesi Selatan', 'Sulawesi Selatan'),
        ('Sulawesi Tengah', 'Sulawesi Tengah'),
        ('Sulawesi Tenggara', 'Sulawesi Tenggara'),
        ('Sulawesi Utara', 'Sulawesi Utara'),
        ('Maluku', 'Maluku'),
        ('Maluku Utara', 'Maluku Utara'),
        ('Papua Barat', 'Papua Barat'),
        ('Papua', 'Papua'),
    )

    nama = models.CharField(max_length=150)
    provinsi = models.CharField(max_length=30, choices=PROVINSI_CHOICES)
    kota = models.CharField(max_length=50)
    kategori = models.CharField(max_length=25, choices=KATEGORI_CHOICES)
    alamat = models.TextField(blank=True)
    deskripsi = RichTextField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Nomor Hp menggunakan format: '+999999999'. maksimal nomor hp yaitu 15 karakter.")
    telpon = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        verbose_name = ("layanan Kesehatan Jiwa")
        verbose_name_plural = ("layanan Kesehatan Jiwa")

    def __str__(self):
        return self.nama