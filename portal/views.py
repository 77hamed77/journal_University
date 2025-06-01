from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ResearcherRegistrationForm, CustomAuthenticationForm, ResearchPaperForm
from .models import User, ResearchPaper
from django.conf import settings


# --- مساعدات (Helpers) للتحقق من دور المستخدم ---
def is_researcher(user):
    return user.is_authenticated and not user.is_staff # باحث وليس مسؤول

def is_approver(user):
    return user.is_authenticated and user.is_staff # نفترض أن المسؤول هو staff member

# --- عروض الصفحات العامة ---
def index_view(request):
    # يمكنك تمرير أي بيانات تحتاجها صفحة index هنا
    return render(request, 'index.html')

def archef_view(request):
    approved_papers = ResearchPaper.objects.filter(status='approved').order_by('-submission_date')
    context = {'papers': approved_papers}
    return render(request, 'archef.html', context)

def contact_view(request):
    return render(request, 'contact.html')

def roles_view(request):
    return render(request, 'roles.html')

def team_university_view(request):
    return render(request, 'teamUniversity.html')

# --- عروض المصادقة ---
def register_researcher_view(request):
    if request.user.is_authenticated:
        return redirect('portal:index') # أو لوحة التحكم المناسبة
    if request.method == 'POST':
        form = ResearcherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'تم تسجيل حسابك بنجاح. سيتم مراجعته من قبل المسؤول للموافقة.')
            # يمكنك إرسال إشعار للمسؤول هنا
            return redirect('portal:login')
        else:
            messages.error(request, 'يرجى تصحيح الأخطاء الموجودة.')
    else:
        form = ResearcherRegistrationForm()
    return render(request, 'registration/register_researcher.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        if is_approver(request.user):
            return redirect('portal:approver_dashboard')
        else:
            return redirect('portal:researcher_dashboard')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active: # فقط المستخدمون النشطون يمكنهم تسجيل الدخول
                    login(request, user)
                    if is_approver(user):
                        return redirect('portal:approver_dashboard')
                    elif is_researcher(user): # تأكد من أنه باحث معتمد
                        return redirect('portal:researcher_dashboard')
                    else: # مستخدم عادي بدون دور محدد (إذا سمحت بذلك)
                        return redirect('portal:index')
                else:
                    messages.error(request, 'حسابك غير نشط أو معلق للمراجعة.')
            else:
                messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'تم تسجيل خروجك بنجاح.')
    return redirect('portal:index')

# --- عروض لوحة تحكم الباحث ---
@login_required
@user_passes_test(is_researcher, login_url='portal:login') # تأكد أنه باحث
def researcher_dashboard_view(request):
    papers = ResearchPaper.objects.filter(author=request.user).order_by('-submission_date')
    form = ResearchPaperForm() # لإظهار فورم التقديم مباشرة في الداشبورد
    context = {
        'papers': papers,
        'form': form,
    }
    return render(request, 'researcher/researcher_dashboard.html', context)

@login_required
@user_passes_test(is_researcher)
def submit_research_view(request):
    if request.method == 'POST':
        form = ResearchPaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.author = request.user
            paper.save()
            messages.success(request, 'تم تقديم بحثك بنجاح للمراجعة.')
            return redirect('portal:researcher_dashboard')
        else:
            messages.error(request, 'يرجى تصحيح الأخطاء في النموذج.')
    else: # في حال الوصول للرابط مباشرة (GET) أو خطأ في الفورم
        # عادةً ما يتم تضمين الفورم في الداشبورد، لكن يمكن عمل صفحة منفصلة
        # إذا كان الفورم معقدًا
        # form = ResearchPaperForm()
        return redirect('portal:researcher_dashboard') # أو عرض الفورم في صفحة منفصلة
    # إذا فشل الفورم، ارجع إلى الداشبورد مع الأخطاء (سيتم هذا تلقائيًا إذا كان الفورم في الداشبورد)
    papers = ResearchPaper.objects.filter(author=request.user).order_by('-submission_date')
    context = {
        'papers': papers,
        'form': form, # مرر الفورم مع الأخطاء
    }
    return render(request, 'researcher/researcher_dashboard.html', context)


# --- عروض لوحة تحكم مسؤول الموافقة ---
@login_required
@user_passes_test(is_approver, login_url='portal:login') # تأكد أنه مسؤول
def approver_dashboard_view(request):
    pending_users = User.objects.filter(is_active=False, is_staff=False).order_by('date_joined')
    pending_papers = ResearchPaper.objects.filter(status='pending').order_by('submission_date')
    # يمكنك إضافة قوائم أخرى مثل الأبحاث الموافق عليها/المرفوضة، كل المستخدمين، إلخ.
    all_researchers = User.objects.filter(is_staff=False, is_superuser=False).order_by('username') # كل الباحثين (نشط وغير نشط)

    context = {
        'pending_users': pending_users,
        'pending_papers': pending_papers,
        'all_researchers': all_researchers,
    }
    return render(request, 'approver/approver_dashboard.html', context)

@login_required
@user_passes_test(is_approver)
def approve_user_view(request, user_id):
    user_to_approve = get_object_or_404(User, id=user_id, is_staff=False)
    if request.method == 'POST': # تأكد أن الطلب POST للأمان
        user_to_approve.is_active = True
        user_to_approve.save()
        messages.success(request, f'تمت الموافقة على الباحث {user_to_approve.username}.')
        # يمكنك إرسال إيميل للباحث هنا
    return redirect('portal:approver_dashboard')

@login_required
@user_passes_test(is_approver)
def reject_user_view(request, user_id):
    user_to_reject = get_object_or_404(User, id=user_id, is_staff=False)
    if request.method == 'POST':
        # يمكنك حذف المستخدم أو فقط تركه is_active=False مع سبب للرفض
        # هنا سنقوم بحذفه كمثال، ولكن الأفضل تركه غير نشط مع سبب
        username = user_to_reject.username
        user_to_reject.delete()
        messages.info(request, f'تم رفض وحذف طلب الباحث {username}.')
        # يمكنك إرسال إيميل للباحث هنا
    return redirect('portal:approver_dashboard')

@login_required
@user_passes_test(is_approver)
def approve_paper_view(request, paper_id):
    paper_to_approve = get_object_or_404(ResearchPaper, id=paper_id)
    if request.method == 'POST':
        paper_to_approve.status = 'approved'
        paper_to_approve.reviewed_by = request.user
        paper_to_approve.review_date = timezone.now() # from django.utils import timezone
        paper_to_approve.save()
        messages.success(request, f'تمت الموافقة على البحث "{paper_to_approve.title}".')
        # يمكنك إرسال إيميل للباحث هنا
    return redirect('portal:approver_dashboard')

@login_required
@user_passes_test(is_approver)
def reject_paper_view(request, paper_id):
    paper_to_reject = get_object_or_404(ResearchPaper, id=paper_id)
    if request.method == 'POST':
        paper_to_reject.status = 'rejected'
        paper_to_reject.reviewed_by = request.user
        paper_to_reject.review_date = timezone.now() # from django.utils import timezone
        # يمكنك إضافة حقل لملاحظات الرفض في الفورم
        # paper_to_reject.review_comments = request.POST.get('comments', '')
        paper_to_reject.save()
        messages.info(request, f'تم رفض البحث "{paper_to_reject.title}".')
        # يمكنك إرسال إيميل للباحث هنا
    return redirect('portal:approver_dashboard')

# لا تنسَ استيراد timezone إذا استخدمته
from django.utils import timezone