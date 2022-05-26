from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator

# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'account'
    avatar = models.ImageField(upload_to='uploads/%y/%m')

class PersonInfo(models.Model):
    class Meta:
        abstract = True
        ordering = ['-id']

    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    dateOfBirth = models.DateField()
    gender = models.BooleanField()
    address = models.TextField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{8,10}$')])
    idNumber = models.CharField(max_length=12, validators=[RegexValidator(regex=r'^\d{12,12')])
    account = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.firstName

class Employee(PersonInfo):
    class Meta:
        db_table = "employee"
    salary = models.IntegerField(validators=[MinValueValidator(0)])
    avatar = models.ImageField(upload_to='avatar/%Y/%m', blank=True)

class Customer(PersonInfo):
    class Meta:
        db_table = "customer"
    pass

class Category(models.Model):
    class Meta:
        db_table = "category"
        ordering = ["categoryName"]

    categoryName = models.CharField(max_length=255, null=False)
    active = models.BooleanField(default=True)

class TypeJewerly(models.Model):
    class Meta:
        db_table = "typejewerly"
        ordering = ["typeName"]

    typeName = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    active = models.BooleanField(default=True)

class Supplier(models.Model):
    class Meta:
        db_table = "supplier"

    supplierName = models.CharField(max_length=255, null=False)
    phoneNumber = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{8,10}$')])
    address = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=255, null=False)
    active = models.BooleanField(default=True)

class Jewerly(models.Model):
    class Meta:
        db_table = "jewerly"
    jewerlyName = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    jewerlyImage = models.ImageField(upload_to='jewerly/%Y/%m', blank=True)
    typeJewerly = models.ManyToManyField(TypeJewerly, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True)
    active = models.BooleanField(default=True)