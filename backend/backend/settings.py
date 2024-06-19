ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pract8',
        'USER': 'root',
        'PASSWORD': 'ketchup1234',
        'HOST': 'db',
        'PORT': '3306',
    }
}
