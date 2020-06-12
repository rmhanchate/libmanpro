# libmanpro
IT Minor Project

### Import database
`mysql -u root -p` <br>
mysql> `source ~/libmanpro/library.sql` <br>
mysql> `exit;` <br>

### Make migrations
`python manage.py makemigrations` <br>
`python manage.py migrate` <br>
`python manage.py rebuild_index` <br>

### Run server
`python manage.py runserver`
