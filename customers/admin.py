from django.contrib import admin
from .models import Company, User, Order, Client, Plan, Employee, Owner, Note


admin.site.register(Company)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Note)
admin.site.register(Client)
admin.site.register(Plan)
admin.site.register(Employee)
admin.site.register(Owner)


