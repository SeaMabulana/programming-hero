from pathlib import Path # created by defualt
BASE_DIR = Path(__file__).resolve().parent.parent # create by default

# user code bellow to config your static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR,
    'static',
]