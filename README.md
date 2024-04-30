# StockTradingApp

# need to install Mysqlclient
# need to create database "stockapp'
# need to make changes in setting.py 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stockapp',
        'USER': 'root',
        'PASSWORD':'root@123',
        'HOST':'localhost',
        'PORT':3306,
    }
}


# after doing these step we have thw use "python manage.py makemigration" to access dabase by django app
# if it shows no changes then execute 'python manage.py migrate' 