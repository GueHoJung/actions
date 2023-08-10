"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from environ import Env
from datetime import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env(
    # set casting, default value
    DEBUG=(bool, False)
)

CRM_HOST_IP = env('CRM_HOST_IP')
CRM_HOST_NAME = env('CRM_HOST_NAME')
CRM_HOST_PORT = env('CRM_HOST_PORT')

HRM_HOST_IP = env('HRM_HOST_IP')
HRM_HOST_NAME = env('HRM_HOST_NAME')
HRM_HOST_PORT = env('HRM_HOST_PORT')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used _in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on _in production!
DEBUG = bool(os.environ.get("DEBUG", default=False))

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # requirements.txt에 작성 된 djangorestframework
    'rest_framework',
    # yet another swagger,
    'drf_yasg',
    # django-cors-headers
    'corsheaders',
    # django-admin startproject 으로 생성한 config
    'config',
    # django-admin startapp 으로 생성 apps
    # 분석
    'analysis',
    # 고객
    'customer',
    # 로그인
    'designer_server',
    # 인사
    'employ',
    # ITSR
    'itsr',
    # 주문
    'order',
    # 예약
    'reservation',
    # 통계
    'stats',
    # view template 처리
    'web',
    # startapp 에 대해 사용 할 template
    'hexagonal_archi_template',
]

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    # CUSTOM EXCEPTION HANDLER 추가
    'EXCEPTION_HANDLER': 'config.utils.exceptions.custom_exception_handler',
}

# django admin화면 접속 시도시 Site matching query does not exist. 발생
# /adim/ 화면 안뜨는 문제 해결 위해 추가
# SITE_ID=1

#  Forbidden (Origin checking failed - https://app.junobiz.com does not match any trusted origins.)
CSRF_TRUSTED_ORIGINS = [os.environ.get("CSRF_TRUSTED_ORIGINS")]

# CORS Error 대응 https://dzone.com/articles/how-to-fix-django-cors-error
# CORS_ORIGIN_WHITELIST = [] 설정도 가능, 하지만 CORS_ORIGIN_ALLOW_ALL = True 설정으로 모든 도메인 허용
CORS_ORIGIN_ALLOW_ALL = bool(os.environ.get("CORS_ORIGIN_ALLOW_ALL", default=False))
CORS_ALLOW_CREDENTIALS = bool(os.environ.get("CORS_ALLOW_CREDENTIALS", default=False))
CORS_ALLOW_HEADERS = [os.environ.get("CORS_ALLOW_HEADERS")]
CORS_ALLOWED_ORIGINS = [os.environ.get("CORS_ALLOWED_ORIGINS")]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS Error 대응
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': os.environ.get("POSTGRES_PORT"),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = os.path.dirname(BASE_DIR)

STATIC_URL = 'static/'

STATIC_ROOT = './.static_root/'

MEDIA_URL = 'media/'

MEDIA_ROOT = './.media_root/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 로그 형식 추가
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # True일경우 이미 존재하는 로거들을 비활성화
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',  # DEBUG가 True일 때 레코드를 전달합니다 뭔소린지
        },
    },
    # 로그텍스트 형식정의
    'formatters': {
        'formatNormal': {'format': '%(levelname)s %(message)s [%(name)s:%(lineno)s]'},
        'formatTime': {'format': '[%(asctime)s] %(levelname)s %(message)s', 'datefmt': "%Y-%m-%d %H:%M:%S"},
    },
    'handlers': {
        # 파일 저장방식
        'file': {
            'level': 'INFO',  # 설정한 레벨이상의 로그만 동작합니다.
            'class': 'logging.handlers.RotatingFileHandler',  # 파일처리 핸들러로 파일저장
            'filename': "./api_logs/admin_log"+datetime.now().strftime('%Y-%m-%d')+".log",
            'encoding': 'UTF-8',  # 인코딩 깨지지 말라고
            'maxBytes': 1024 * 1024 * 5,  # 5 MB  /
            'backupCount': 5,
            'formatter': 'formatTime',
        },
        # 콘솔(터미널)에 출력
        'console': {
            'level': 'DEBUG',  # 설정한 레벨이상의 로그만 동작합니다.
            'class': 'logging.StreamHandler',  # stream으로 로깅출력
            'formatter': 'formatTime',
        },
    },
    # 설정한 레벨이상의 로그만 동작합니다.  DEBUG < INFO < WARNING < ERROR < CRITICAL
    'loggers': {
        # 종류
        'django.server': {
            'handlers': ['file', 'console'],
            'propagate': False,
            'level': 'DEBUG',  # 설정한 레벨이상의 로그만 동작합니다.
        },
        # 'django.server': {
        #     'handlers': ['file', 'console'],
        #     'propagate': False,
        #     'level': 'CRITICAL',
        # },
        # 'django.request': {
        #     'handlers': ['file', 'console'],
        #     'propagate': False,
        #     'level': 'DEBUG',
        # },

    },
}
