# OverBoard
![(https://image.ibb.co/juiQtS/overboard2.png)](https://image.ibb.co/juiQtS/overboard2.png)

Requires [Django](https://tutorial.djangogirls.org/en/django_installation/). Reccomended for database management - [SQLiteStudio](https://sqlitestudio.pl/index.rvt?act=download).

### Run
Run at localhost:8000
```sh
$ cd overboard/overboard
$ python manage.py makemigrations overboardapp
$ python manage.py migrate
$ python manage.py runserver
```

With virtual environment (1. Windows / 2. Linux):
```sh
$ cd overboard
$ virtualenv env
$ 1. env\Scripts\activate 2. source myvenv/bin/activate
(env) $ pip install django
(env) $ cd overboard
(env) $ python manage.py makemigrations overboardapp
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

```sh
python manage.py migrate --run-syncdb
```