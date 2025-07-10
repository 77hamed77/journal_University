# portal/models.py (النسخة الكاملة والمعدلة)

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # AbstractUser يحتوي بالفعل على الحقول الأساسية

    # --- الخطوة 2: حل تعارض العلاقات العكسية ---
    # قمنا بإعادة تعريف الحقول مع إضافة related_name فريد
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="portal_user_set",  # اسم فريد لحل التعارض
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="portal_user_permissions_set", # اسم فريد آخر لحل التعارض
        related_query_name="user",
    )

    def __str__(self):
        return self.username

# --- دالة مساعدة لتحديد مسار الرفع الديناميكي ---
def user_directory_path(instance, filename):
    """
    سيتم رفع الملف إلى المسار: user_<id>/<filename>
    """
    return f'user_{instance.author.id}/{filename}'

class ResearchPaper(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('needs_revision', 'Needs Revision'),
    )
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='papers')
    document = models.FileField(upload_to=user_directory_path)
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='reviewed_papers'
    )
    review_date = models.DateTimeField(null=True, blank=True)
    review_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"