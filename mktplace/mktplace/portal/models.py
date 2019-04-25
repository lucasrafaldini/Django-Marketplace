from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True, related_name='cat_child', on_delete=models.SET_NULL)
    order = models.IntegerField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    @property
    def get_products(self):
        return self.categories.filter(status='Active').order_by('-id')[:8]

    def __str__(self):
        if User.is_superuser:
            if self.parent:
                return '%s (%s), Parent: %s' % (self.name, self.slug, self.parent)
            return '%s (%s)' % (self.name, self.slug)
        else:
            return '%s ' % (self.name)

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True, related_name='categories')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    short_description = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Inactive")

    @property
    def questions_no_answer(self):
        return self.productquestion_set.filter(status='Active', productanswer__isnull=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return '%s,  Status: %s. ' % (self.name, self.status)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            super(Product, self).save()
            self.slug = '%s-%i' % (slugify(self.name), self.id)
        super(Product, self).save(*args, **kwargs)



class ProductQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    question = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")

    class Meta:
        verbose_name = 'Product Question'
        verbose_name_plural = 'Product Questions'

    @property
    def get_answers(self):
        return self.productanswer_set.filter(status='Active')

    def __str__(self):
        return 'User: %s, Status: %s. ' % (self.user, self.status)


class ProductAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_question = models.ForeignKey('ProductQuestion', on_delete=models.CASCADE)
    answer = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return '%s, Status: %s' % (self.answer, self.status)


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.PROTECT)
    cpf = models.CharField(max_length=35, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)
    zipcode = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    remote_customer_id = models.CharField(max_length=255, null=True, blank=True, default='')
    remote_receiver_id = models.CharField(max_length=255, null=True, blank=True, default='')



### Model para imagens no S3 da amazon

# class ProductImages(models.Model):
#     product = models.ForeignKey(Product, related_name='prod_images')
#     images = S3DirectField(dest='product_images')
#
#     class Meta:
#         verbose_name_plural = "Images"