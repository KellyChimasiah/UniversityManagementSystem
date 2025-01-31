from django.contrib import admin
from .models import FeeType, Fee, Payment

# Register your models here.

@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'fee_type', 'amount', 'due_date', 'paid', 'paid_date')
    list_filter = ('fee_type', 'paid')
    search_fields = ('student__first_name', 'student__last_name', 'fee_type__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('fee', 'amount_paid', 'payment_date')
    list_filter = ('fee__fee_type',)
    search_fields = ('fee__student__first_name', 'fee__student__last_name')