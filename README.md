<div align="center">

# ✨ Sham Journal | مجلة شام ✨

**منصة أكاديمية متكاملة لنشر وإدارة الأبحاث العلمية، مبنية باستخدام Django مع دعم متعدد اللغات وتخزين سحابي.**

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="Django" src="https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img alt="Supabase" src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white"/>
  <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge"/>
</p>
[<img src="https://img.shields.io/badge/زيارة_الموقع-Live_Demo-28a745?style=for-the-badge&logo=render" />](https://shamjournal.onrender.com/)

</div>

---

## 📸 معرض المشروع (Project Showcase)

للحصول على أفضل انطباع، يرجى زيارة النسخة الحية من المشروع. يمكنك أيضاً مشاهدة هذه اللقطة للواجهة الرئيسية:

[![Sham Journal Demo](https://i.imgur.com/cWbYp4L.png)](https://shamjournal.onrender.com/)


---

## 🚀 الميزات الرئيسية (Key Features)

تقدم مجلة شام نظاماً متكاملاً لإدارة المحتوى الأكاديمي والبحثي:

*   **🔐 نظام أدوار متقدم (Advanced Role System):**
    *   **الباحث (Researcher):** يمكنه تسجيل حساب، رفع الأبحاث، ومتابعة حالتها (قيد المراجعة، مقبول، مرفوض).
    *   **الموافق (Approver):** يمتلك لوحة تحكم لمراجعة الأبحاث المقدمة، قبولها، رفضها، أو طلب تعديلات.
    *   **المدير (Superuser):** يمتلك صلاحيات كاملة على الموقع من خلال لوحة تحكم Django.

*   **⚙️ دورة حياة كاملة للأبحاث (Full Research Lifecycle):**
    *   نظام رفع ملفات آمن ومنظم لكل باحث.
    *   تتبع حالة البحث في كل مرحلة من مراحل المراجعة والنشر.
    *   إشعارات ورسائل للمستخدمين عند تحديث حالة أبحاثهم.

*   **🌍 دعم متعدد اللغات (Multilingual Support):**
    *   واجهة مستخدم تدعم اللغات **العربية، الإنجليزية، والتركية**.
    *   نظام ترجمة من جانب العميل (Client-Side) باستخدام JavaScript لتجربة استخدام سريعة وسلسة دون إعادة تحميل الصفحة.

*   **☁️ بنية تحتية سحابية حديثة (Modern Cloud Infrastructure):**
    *   نشر المشروع بالكامل على منصة **Render** مع عمليات بناء ونشر تلقائية.
    *   استخدام قاعدة بيانات **PostgreSQL** مُدارة عبر **Supabase**.
    *   تخزين سحابي آمن للملفات (الأبحاث) باستخدام **Supabase Storage** المتوافق مع S3.

---

## 🛠️ التقنيات المستخدمة (Tech Stack)

تم بناء هذا المشروع باستخدام مجموعة من التقنيات الحديثة والقوية:

| الفئة | التقنية |
|---|---|
| **الواجهة الخلفية (Backend)** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white) ![Gunicorn](https://img.shields.io/badge/-Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white) |
| **الواجهة الأمامية (Frontend)** | ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |
| **قاعدة البيانات** | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Supabase](https://img.shields.io/badge/-Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white) |
| **تخزين الملفات** | ![Supabase Storage](https://img.shields.io/badge/-Supabase_Storage-3ECF8E?style=flat-square&logo=supabase&logoColor=white) |
| **النشر (Deployment)** | ![Render](https://img.shields.io/badge/-Render-46E3B7?style=flat-square&logo=render&logoColor=white) ![WhiteNoise](https://img.shields.io/badge/-WhiteNoise-FFFFFF?style=flat-square) |
| **مكتبات أساسية** | `django-storages`, `dj-database-url`, `psycopg2-binary` |

---

## ⚙️ التشغيل محلياً (Local Setup)

لتشغيل المشروع على جهازك المحلي، اتبع الخطوات التالية:

1.  **نسخ المستودع (Clone the repository):**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **إنشاء وتفعيل البيئة الافتراضية (Create and activate virtual environment):**
    ```bash
    python -m venv venv
    # For Windows
    venv\Scripts\activate
    # For macOS/Linux
    source venv/bin/activate
    ```

3.  **تثبيت المكتبات (Install dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **إعداد متغيرات البيئة (Set up environment variables):**
    *   أنشئ ملفاً باسم `.env` في جذر المشروع.
    *   أضف المتغيرات التالية إلى الملف مع قيمك الخاصة من Supabase:
    ```env
    SECRET_KEY='your_django_secret_key'
    DEBUG=True
    DATABASE_URL='your_supabase_postgres_connection_url'
    AWS_ACCESS_KEY_ID='your_supabase_project_anon_public_key'
    AWS_SECRET_ACCESS_KEY='your_supabase_project_service_role_secret_key'
    AWS_STORAGE_BUCKET_NAME='your_supabase_bucket_name'
    AWS_S3_ENDPOINT_URL='your_supabase_storage_endpoint_url'
    AWS_S3_REGION_NAME='your_supabase_project_region'
    ```

5.  **تطبيق التحديثات على قاعدة البيانات (Apply migrations):**
    ```bash
    python manage.py migrate
    ```

6.  **إنشاء حساب مدير (Create a superuser):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **تشغيل الخادم (Run the server):**
    ```bash
    python manage.py runserver
    ```
    الآن يمكنك زيارة الموقع على `http://127.0.0.1:8000`.

---

## 📜 الترخيص (License)

هذا المشروع مرخص تحت رخصة MIT. انظر ملف `LICENSE` للمزيد من التفاصيل.

---

## 👨‍💻 المؤلف (Author)

**حامد محمد المرعي**

<p>
    <a href="https://github.com/77hamed77" target="_blank">
        <img alt="Github" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
    </a>
    <a href="https://www.linkedin.com/in/hamidmuhammad/" target="_blank">
        <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
    </a>
</p>