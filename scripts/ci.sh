virtualenv --distribute django-blog 
source django-blog/bin/activate
pip install -r requirements.txt
python manage.py test
