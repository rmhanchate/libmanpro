# libmanpro
IT Minor Project

# Import database
mysql -u root -p
mysql> source ~/libmanpro/library.sql
mysql> exit;

# Make migrations
python manage.py makemigrations
python manage.py migrate
python manage.py rebuild_index

# Run server
python manage.py runserver
