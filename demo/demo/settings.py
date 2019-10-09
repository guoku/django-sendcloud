import environ

ROOT_DIR = environ.Path(__file__) - 2  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()
env.read_env(str(ROOT_DIR.path(".env")))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="xxxxxxxxxx")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", default=True)  # False if not in os.environ

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sendcloud",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "demo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "demo.wsgi.application"

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default=str(ROOT_DIR.path("db.sqlite3")))
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"

# mail config
EMAIL_BACKEND = "sendcloud.backend.SendCloudBackend"
DEFAULT_FROM_EMAIL = "noreply@example.com"

SEND_CLOUD_KEY = {
    "spark_key": {
        "APP_USER": env("SEND_CLOUD_APP_USER"),
        "APP_KEY": env("SEND_CLOUD_APP_KEY"),
    },
    "batch_key": {
        "APP_USER": env("SEND_CLOUD_EDM_USER"),
        "APP_KEY": env("SEND_CLOUD_EDM_KEY"),
    },
}

##
# logging
##
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            # 'format': '[%(asctime)s.%(msecs)d] %(levelname)s [%(module)s:%(funcName)s:%(lineno)d]- %(message)s',
        },
        "error": {
            "format": "[%(asctime)s.%(msecs)d] [%(module)s:%(funcName)s:%(lineno)d]- %(message)s"
        },
    },
    "handlers": {
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "error",
            "filename": "/tmp/django.log",
            "mode": "a",
        },
    },
    "loggers": {
        "django": {"handlers": ["file", "console"], "propagate": True, "level": "INFO"},
        "sendcloud": {
            "handlers": ["file", "console"],
            "propagate": True,
            "level": "INFO",
        },
        "django.request": {"handlers": ["file"], "level": "ERROR", "propagate": True},
    },
}
