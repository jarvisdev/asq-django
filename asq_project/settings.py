"""
Django settings for asq_project project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x6gfnl&^5*5884oq%a!f^_$%nt_9#$%s^!x06%+u!#c^*ko)-$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'asq_app.apps.AsqAppConfig',
    'froala_editor',
    'haystack',
    'social_django', # <- Here,
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

ROOT_URLCONF = 'asq_project.urls'

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
                'social_django.context_processors.backends',  # <- Here
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'asq_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            # 'read_default_file': '/path/to/my.cnf',
        },
        # 'NAME': os.path.join(BASE_DIR, 'testdb'),
        'NAME': 'asqdb',
        'USER': 'user',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication

    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/accounts/logout'
LOGIN_REDIRECT_URL = '/'


SOCIAL_AUTH_GITHUB_KEY = 'c3686942062e3b07097a'
SOCIAL_AUTH_GITHUB_SECRET = 'c435e76fd001e14496fab946523c4f04fcc641e7'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '30017717787-bc0nnqfcjh0llp9h15jpbjg0p2nioaus.apps.googleusercontent.com'  # Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'T5MaKwjFahCBujIC9KImgRBz'  # Paste Secret Key


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


# to find static folder in project root
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/q/'
#Redirect to home URL after logout 
LOGOUT_REDIRECT_URL = '/q/'
MEDIA_ROOT = 'media/'
FROALA_UPLOAD_PATH = 'froala_uploads/'
MEDIA_URL = '/media/'
# Log email reset mail on console. Can't send email yet as server is not configured.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
FROALA_UPLOAD_PATH = 'froala_uploads/'
MEDIA_URL = '/media/'


# FROALA_INCLUDE_JQUERY = False

FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier', 'code_view', 'colors', 'draggable', 'emoticons',
                         'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image', 'image_manager', 'inline_style',
                         'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
                         'url', 'video')


FROALA_EDITOR_THIRD_PARTY = ('image_aviary', 'spell_checker')


# Generated array to include all css and js files for Froala in Q and A forms
froala_editor_css = ['code_view.css', 'quick_insert.css', 'emoticons.css', 'colors.min.css', 'video.css', 'draggable.css', 'line_breaker.min.css', 'quick_insert.min.css', 'colors.css', 'table.css', 'image.min.css', 'special_characters.min.css', 'fullscreen.min.css', 'file.min.css', 'emoticons.min.css',
                     'char_counter.min.css', 'code_view.min.css', 'draggable.min.css', 'special_characters.css', 'image_manager.css', 'line_breaker.css', 'table.min.css', 'help.min.css', 'char_counter.css', 'image.css', 'help.css', 'file.css', 'fullscreen.css', 'video.min.css', 'image_manager.min.css']
FROALA_PLUGINS_CSS_FILES = []
for f in froala_editor_css:
    FROALA_PLUGINS_CSS_FILES.append('asq_project/froala_editor/css/plugins/' + f)

froala_editor_js = ['image.min.js', 'link.min.js', 'code_beautifier.min.js', 'help.min.js', 'video.min.js', 'font_family.min.js', 'image_manager.min.js', 'code_view.min.js', 'save.min.js', 'emoticons.min.js', 'forms.min.js', 'line_breaker.min.js', 'quote.min.js', 'font_size.min.js', 'draggable.min.js', 'char_counter.min.js',
                    'url.min.js', 'special_characters.min.js', 'colors.min.js', 'inline_style.min.js', 'fullscreen.min.js', 'print.min.js', 'paragraph_format.min.js', 'table.min.js', 'align.min.js', 'quick_insert.min.js', 'file.min.js', 'paragraph_style.min.js', 'entities.min.js', 'lists.min.js', 'word_paste.min.js']
FROALA_PLUGINS_JS_FILES = []
for f in froala_editor_js:
    FROALA_PLUGINS_JS_FILES.append('asq_project/froala_editor/js/plugins/' + f)


# Haystack using Elastic Search (Java based)
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': 'http://127.0.0.1:9200/',
#         'INDEX_NAME': 'haystack_books',
#     },
# }

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# Haystack using Whoosh (Pyhton based)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'INCLUDE_SPELLING': True
    },
}

# HAYSTACK_FUZZY_MAX_EXPANSIONS = 2
