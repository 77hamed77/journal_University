from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings # لاستخدام User model

class User(AbstractUser):
    # AbstractUser يحتوي بالفعل على username, password, email, first_name, last_name
    ROLE_CHOICES = (
        ('researcher', 'Researcher'),
        ('approver', 'Approver'), # مسؤول الموافقة
    )
    # سيتم استخدام is_staff لحساب مسؤول الموافقة الرئيسي مبدئياً
    # يمكن إضافة حقل role إذا أردت أكثر من مسؤول موافقة أو أدوار أخرى لاحقاً
    # is_active سيتحكم به مسؤول الموافقة للباحثين الجدد
    # True = تم الموافقة عليه، False = معلق أو مرفوض

    # يمكنك إضافة حقول أخرى هنا إذا احتجت
    # مثلاً: department, university_id, etc.

    def __str__(self):
        return self.username

class ResearchPaper(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='papers')
    # ملف البحث (PDF, DOCX, etc.)
    document = models.FileField(upload_to='research_papers/')
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # من وافق أو رفض (اختياري، يمكن أن يكون مسؤول الموافقة الوحيد)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_papers')
    review_date = models.DateTimeField(null=True, blank=True)
    review_comments = models.TextField(blank=True, null=True) # ملاحظات المسؤول عند الرفض مثلا

    def __str__(self):
        return f"{self.title} by {self.author.username}"