from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.safestring import mark_safe
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.forms import ModelForm, TextInput, Textarea


# PRODUCT_CHOICES = (
#     ('laptop', 'LAPTOP'),
#     ('printer', 'PRINTER'),
#     ('accessories', 'ACCESSORIES'),
#     ('phones', 'PHONES'),
#     ('storage', 'STORAGE'),
# )


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def _str_(self):
        return self.user

class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='img')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.name}"

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug',))

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return '/'.join(full_path[::-1])

class Product(models.Model):
    title = models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = RichTextUploadingField()
    # category = models.CharField(choices=PRODUCT_CHOICES, max_length=50)
    image = models.ImageField(upload_to='img')
    slug = models.SlugField(null=False, unique=True)
    update_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def image_tag(self):
            return mark_safe('<img src="/img/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})

class Images(models.Model):
    product=models.ForeignKey(Product, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    
    def _str_(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    tansaction_id = models.CharField(max_length=100, null=True)

    def _str_(self):
        return str(self.id)

    @property
    def delivery(self):
        delivery = False
        orderitems = self.orderitem_set.all()
        # for i in orderitems:
        #     if i .mobiles.digital ==False:
        #         delivery =True
        return delivery

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.mobile

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class DeliveryInformation(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    estate = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.address

class Description_header(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.title
    
class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
            'subject' : TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }
