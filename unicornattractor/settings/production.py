import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# stripe keys
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET')

ALLOWED_HOSTS = [
    'milestone-5.herokuapp.com',
] 

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }


STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
 

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl':'max-age=9453485',
}
AWS_STORAGE_BUCKET_NAME = 'shanes-milestone-5'
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_DEFAULT_ACL = None


# EMAIL
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_POST = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_MAIN = 'Unicorn Attractor Support'