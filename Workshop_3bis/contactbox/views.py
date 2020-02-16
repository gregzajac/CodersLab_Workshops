from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from contactbox.models import *


class PersonList(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, "person_list.html", {"persons": persons})


class PersonDetail(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        phones = Phone.objects.filter(person=person)
        emails = Email.objects.filter(person=person)
        context = {
            "person": person,
            "phones": phones,
            "emails": emails,
        }
        return render(request, "person_detail.html", context)


class ModifyPerson(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        phones = Phone.objects.filter(person=person)
        emails = Email.objects.filter(person=person)
        context = {
            "person": person,
            "phones": phones,
            "emails": emails,
        }
        return render(request, "modify_person.html", context)

    def post(self, request, id):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        description = request.POST.get("description")
        street = request.POST.get("street")
        block_number = request.POST.get("block_number")
        flat_number = request.POST.get("flat_number")
        city = request.POST.get("city")
        post_code = request.POST.get("post_code")

        person = Person.objects.get(pk=id)
        if first_name and last_name:
            person.first_name = first_name
            person.last_name = last_name
            person.description = description
            if person.address:
                address = person.address
                address.street = street
                address.block_number = block_number
                address.flat_number = flat_number
                address.city = city
                address.post_code = post_code
                address.save()
            else:
                if city and street and block_number and post_code:
                    address = Address.objects.create(street=street,
                                                     block_number=block_number,
                                                     flat_number=flat_number,
                                                     city=city,
                                                     post_code=post_code)
                else:
                    address = None
            person.address = address
            person.save()

            return redirect(f"/person/{person.id}")
        else:
            return HttpResponse("modify, brak imienia lub nazwiska")


class DeletePerson(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        return render(request, "delete_person.html", {"person": person})

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.delete()
        return redirect("/")


class NewPerson(View):
    def get(self, request):
        addresses = Address.objects.all()
        return render(request, "new_person.html", {"addresses": addresses})

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        description = request.POST.get("description")
        address_id = request.POST.get("address_id")
        address = Address.objects.get(pk=address_id)

        if first_name and last_name:
            person = Person.objects.create(first_name=first_name,
                                           last_name=last_name,
                                           description=description,
                                           address=address)
            return redirect(f"/person/{person.id}")
        else:
            return HttpResponse("newperson, brak imienia lub nazwiska")


class NewAddress(View):
    def get(self, request):
        return render(request, "new_address.html")

    def post(self, request):
        city = request.POST.get("city")
        street = request.POST.get("street")
        block_number = request.POST.get("block_number")
        flat_number = request.POST.get("flat_number")
        post_code = request.POST.get("post_code")

        if city and street and block_number and post_code:
            Address.objects.create(city=city,
                                   street=street,
                                   block_number=block_number,
                                   flat_number=flat_number,
                                   post_code=post_code)
            return redirect("/new-person/")
        else:
            return HttpResponse("brak wszytkich danych")


class NewPhone(View):
    def get(self, request, id):
        return render(request, "new_phone.html")

    def post(self, request, id):
        phone_number = request.POST.get("phone_number")
        phone_type = request.POST.get("phone_type")

        if phone_number and phone_type:
            person = Person.objects.get(pk=id)
            Phone.objects.create(phone_number=phone_number,
                                 phone_type=phone_type,
                                 person=person)
            return redirect(f"/person/{id}")
        else:
            return HttpResponse("podaj numer i typ telefonu")


class DeletePhone(View):
    def get(self, request, id, id_phone):
        phone = Phone.objects.get(pk=id_phone)
        return render(request, "delete_phone.html", {"phone": phone})

    def post(self, request, id, id_phone):
        phone = Phone.objects.get(pk=id_phone)
        phone.delete()
        return redirect(f"/person/{id}")

class NewEmail(View):
    def get(self, request, id):
        return render(request, "new_email.html")

    def post(self, request, id):
        email_address = request.POST.get("email")
        email_type = request.POST.get("email_type")
        if email_address and email_type:
            person = Person.objects.get(pk=id)
            Email.objects.create(email=email_address,
                                 email_type=email_type,
                                 person=person)
            return redirect(f"/person/{id}")
        else:
            return HttpResponse("podaj numer i typ telefonu")


class DeleteEmail(View):
    def get(self, request, id, id_email):
        email = Email.objects.get(pk=id_email)
        return render(request, "delete_phone.html", {"email": email})

    def post(self, request, id, id_email):
        email = Email.objects.get(pk=id_email)
        email.delete()
        return redirect(f"/person/{id}")


class GroupList(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, "group_list.html", {"groups": groups})


class NewGroup(View):
    def get(self, request):
        return render(request, "new_group.html")

    def post(self, request):
        name = request.POST.get("name")
        if name:
            Group.objects.create(name=name)
            return redirect("/groups/")
        else:
            return HttpResponse("Podaj nazwę grupy!")


class DeleteGroup(View):
    def get(self, request, id):
        group = Group.objects.get(pk=id)
        return render(request, "delete_group.html", {"group": group})

    def post(self, request, id):
        group = Group.objects.get(pk=id)
        group.delete()
        return redirect("/groups/")


class GroupDetail(View):
    def get(self, request, id):
        group = Group.objects.get(pk=id)
        persons = group.persons.all()
        context = {
            "group": group,
            "persons": persons,
        }
        return render(request, "group_detail.html", context)


class NewPersonInGroup(View):
    def get(self, request, id):
        group = Group.objects.get(pk=id)
        persons = Person.objects.all()
        context = {
            "group": group,
            "persons": persons
        }
        return render(request, "new_person_in_group.html", context)

    def post(self, request, id):
        person_id = request.POST.get("person_id")
        person = Person.objects.get(pk=person_id)
        group = Group.objects.get(pk=id)
        group.persons.add(person)
        group.save()
        return redirect(f"/group/{id}")


class DeletePersonFromGroup(View):
    def get(self, request, id, id_person):
        group = Group.objects.get(pk=id)
        person = Person.objects.get(pk=id_person)
        context = {
            "group": group,
            "person": person,
        }
        return render(request, "delete_person_from_group.html", context)

    def post(self, request, id, id_person):
        person = Person.objects.get(pk=id_person)
        group = Group.objects.get(pk=id)
        group.persons.remove(person)
        return redirect(f"/group/{id}")