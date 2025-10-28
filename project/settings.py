from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 🌟🌟 แก้ไข NameError: ใช้ _file_ อย่างถูกต้อง 🌟🌟
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-3r3d+@d5p+r6v8%#*p1d0o*1qj#v#7-i%j(p52r*a+k*d9d$'

# 🌟🌟 ตั้งค่าสำหรับการโฮสต์: เปลี่ยนเป็น False เมื่อขึ้น Production 🌟🌟
DEBUG = True 

# 🌟🌟 ตั้งค่าสำหรับการโฮสต์: อนุญาตให้ IP สาธารณะเข้าถึงได้ (ต้องมีสำหรับ ngrok/Hosting) 🌟🌟
ALLOWED_HOSTS = ['*'] 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🌟🌟 ตั้งค่า WSGI สำหรับการรัน Gunicorn (โฮสติ้ง) 🌟🌟
WSGI_APPLICATION = 'project.wsgi.application'


# Database (ใช้ SQLite3 เหมือนเดิม)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ... (ส่วน Password validation, Internationalization, Time Zone คงเดิม) ...


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/' 

# ตั้งค่าให้ Django ค้นหาไฟล์ Static ในโฟลเดอร์ 'restaurant/static/' 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'restaurant/static/'),
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'