from django.db import models


class Flat(models.Model):
    street = models.CharField(max_length=128, verbose_name="Ulica")
    block_number = models.CharField(max_length=64, verbose_name="Nr domu")
    flat_number = models.CharField(max_length=64, verbose_name="Nr mieszkania", null=True)
    post_code = models.CharField(max_length=16, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=64, verbose_name="Miasto")
    flat_description = models.TextField(verbose_name="Dodatkowe info", null=True)

    def __str__(self):
        if self.flat_number:
            block_flat_number = f"{self.block_number}/{self.flat_number}"
        else:
            block_flat_number = f"{self.block_number}"
        return f"{self.street} {block_flat_number}, {self.post_code} {self.city}"


class Tenant(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko")
    phone = models.CharField(max_length=16, verbose_name="Telefon", null=True)
    email = models.CharField(max_length=64, verbose_name="E-mail", null=True)
    tenant_description = models.TextField(verbose_name="Dodatkowe info", null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agreement(models.Model):
    code = models.CharField(max_length=32, verbose_name="Identyfikator umowy", unique=True)
    agreement_date = models.DateField(verbose_name="Data podpisania umowy")
    date_from = models.DateField(verbose_name="Data początku najmu")
    date_to = models.DateField(verbose_name="Data końca najmu")
    mth_payment_value = models.FloatField(verbose_name="Miesięczny koszt wynajmu")
    mth_payment_deadline = models.SmallIntegerField(verbose_name="Termin miesięcznej opłaty")
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name="Najemca")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name="Wynajmowane mieszkanie")
    agreement_description = models.TextField(verbose_name="Dodatkowe info", null=True)

    def __str__(self):
        return f"{self.code} - {self.flat} - {self.tenant}"
