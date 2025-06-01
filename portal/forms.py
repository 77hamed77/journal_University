from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, ResearchPaper

class ResearcherRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name') # أضف الحقول التي تريدها

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False # الباحث الجديد غير نشط حتى تتم الموافقة عليه
        # user.role = 'researcher' # إذا أضفت حقل role
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    # يمكنك تخصيص نموذج تسجيل الدخول هنا إذا أردت
    pass

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['title', 'abstract', 'document'] # الحقول التي يملؤها الباحث
        # widgets = {
        #     'abstract': forms.Textarea(attrs={'rows': 5}),
        # }