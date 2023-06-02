from django.db import models

PILIHAN_KATEGORI = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

PILIHAN_LABEL = (
    ('NEW', 'primary'),
    ('SALE', 'info'),
    ('BEST', 'danger',)
)

class ProdukItem(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.FloatField()
    harga_diskon = models.FloatField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='product_pic')
    label = models.CharField(choices=PILIHAN_LABEL, max_length=4)
    kategori = models.CharField(choices=PILIHAN_KATEGORI, max_length=2)
