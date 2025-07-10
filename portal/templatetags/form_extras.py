# templatetags\form_extras.py
from django import template
register = template.Library()

@register.filter(name='get_field_label')
def get_field_label(form, field_name):
    if field_name == '__all__': # __all__ يستخدم للأخطاء التي لا تتعلق بحقل معين
        return "" 
    try:
        # محاولة الحصول على التسمية من كائن الحقل في النموذج
        return form.fields[field_name].label
    except KeyError:
        # كحل احتياطي إذا لم يتم العثور على الحقل
        # أو لتحسين مظهر اسم الحقل الافتراضي إذا لم يكن له label
        # يمكنك استخدام هذا السطر لجعل الاسم أكثر قابلية للقراءة
        return field_name.replace('_', ' ').capitalize() 
        # أو إذا كنت تريد فقط اسم الحقل كما هو:
        # return field_name