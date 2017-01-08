export CELLAR_HOME="/usr/local/Cellar"
export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_111.jdk/Contents/Home"
export PATH="/usr/local/firework-0.2.0/bin:$CELLAR_HOME/protobuf/3.1.0/bin:$CELLAR_    HOME/redis/3.2.5/bin:$CELLAR_HOME/vim/8.0.0094/bin:/usr/local/bin:/usr/bin:/bin:/us    r/sbin:/sbin"

virtualenv --distribute django-blog 
source django-blog/bin/activate
pip install -r requirements.txt
python manage.py test
