from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    block_number = models.CharField(max_length=32)
    flat_number = models.CharField(max_length=32, null=True)
    post_code = models.CharField(max_length=16)


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)


class Phone(models.Model):
    phone_number = models.CharField(max_length=32)
    phone_type = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


class Email(models.Model):
    email = models.EmailField()
    email_type = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


class Group(models.Model):
    name = models.CharField(max_length=64)
    persons = models.ManyToManyField(Person)
