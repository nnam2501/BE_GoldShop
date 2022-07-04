from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator

# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'account'
    is_staff = models.BooleanField(default=False)

class PersonInfo(models.Model):
    class Meta:
        abstract = True
        ordering = ['-id']

    fullName = models.CharField(max_length=255, null=False)
    dateOfBirth = models.DateField()
    gender = models.BooleanField()
    address = models.TextField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{8,10}$')])
    idNumber = models.CharField(max_length=12, validators=[RegexValidator(regex=r'^\d{9,12}$')])
    account = models.ForeignKey(User, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullName

class Employee(PersonInfo):
    class Meta:
        db_table = "employee"
    salary = models.IntegerField(validators=[MinValueValidator(0)])

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

    def __str__(self):
        return self.categoryName

class TypeJewerly(models.Model):
    class Meta:
        db_table = "typejewerly"
        ordering = ["typeName"]

    typeName = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.typeName

class Supplier(models.Model):
    class Meta:
        db_table = "supplier"

    supplierName = models.CharField(max_length=255, null=False)
    phoneNumber = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{8,10}$')])
    address = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=255, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.supplierName

class Jewerly(models.Model):
    class Meta:
        db_table = "jewerly"
    jewerlyName = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    jewerlyImage = models.ImageField(upload_to='jewerly/%Y/%m', null=True)
    typeJewerly = models.ManyToManyField(TypeJewerly, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.jewerlyName

class Order(models.Model):
    class Meta:
        db_table = "order"
        ordering = ["-id"]
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False)
    orderDate = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class OrderDetail(models.Model):
    class Meta:
        db_table = "orderdetail"
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null = False)
    jewerly = models.ForeignKey(Jewerly, on_delete=models.PROTECT, null = False)
    unitPrice = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])


class Invoice(models.Model):
    class Meta:
        db_table = "invoice"
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False)
    invoiceDate = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)
    total = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    active = models.BooleanField(default=True)
