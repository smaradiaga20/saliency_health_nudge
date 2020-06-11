from os import environ
import os
import dj_database_url


#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

## Static files (CSS, JavaScript, Images)
## https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

#
## Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
#            os.path.join(BASE_DIR, '_static'),
#            )

#django_heroku.settings(locals())

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    #{
    #    'name': 'public_goods',
    #    'display_name': "Public Goods",
    #    'num_demo_participants': 3,
    #    'app_sequence': ['public_goods', 'payment_info'],
    #},
# {
#     'name': 'voly_main_qns',
#     'display_name': "Voly main Qns",
#     'num_demo_participants': 1,
#     'app_sequence': ['volyIntroGame', 'volyMainQn'],
#
# },

]
 

REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False
 

INSTALLED_APPS = ['otree', 'django.contrib.humanize']

ROOMS = [
    {
        'name': 'WBS3005',
        'display_name': 'WBS 3.005 Behavioural Science Lab',
        'participant_label_file': '_rooms/3005.txt',
    },
    ]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'yr29khtiRlA1'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'ac6ea2791ac94d04e733b6b886a080fa  -'

AUTH_LEVEL = 'DEMO'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
ON_HEROKU = os.environ.get('ON_HEROKU')

MIDDLEWARE = [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'otree-mouse-tracking', #'otreetutorial',
         'USER': 'sofia', #'otreetutorial',
         'PASSWORD': '2c51b7b58b55', #'rb3z2Psf6c60',
         'HOST': 'localhost',
         'PORT': '5432',
        } 
   }
