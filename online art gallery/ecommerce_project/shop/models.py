from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db import models
# from django.contrib.auth.models import User
# from models import Product





class Exhibition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    venue = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    video_url = models.URLField(default="https://res.cloudinary.com/dn7sk8y8y/video/upload/v1720029053/WhatsApp_Video_2024-07-03_at_23.15.49_34d932f7_rx0t8l.mp4 ")
    image_url = models.URLField(default="https://indianartideas.in/articleimages/1575894895Significance-of-Online-Indian-Art-Gallery.jpg")
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review of {self.product.name} by {self.user.username}'


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return f'Payment for Order {self.order.id}'

