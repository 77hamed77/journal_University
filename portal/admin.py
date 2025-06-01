from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ResearchPaper

class CustomUserAdmin(UserAdmin):
    # يمكنك إضافة حقول من نموذج User المخصص هنا لتظهر في لوحة التحكم
    # UserAdmin.fieldsets += (('Custom Fields', {'fields': ('role',)}),)
    pass

admin.site.register(User, CustomUserAdmin) # استخدم CustomUserAdmin بدلاً من UserAdmin القياسي
admin.site.register(ResearchPaper)