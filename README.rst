# dju-menuzen
A attempt to build a simple breadcrumb/menu system for Django-CMS

::

 virtualenv env -p $(which python3)
 source env/bin/activate
 pip install djangocms-installer==0.9.7
 djangocms mysite
 cd mysite

:: 
 
 cat >> mysite/settings.py << EOF
 INSTALLED_APPS += ('dju-menuzen',)
 CMS_TEMPLATES += (('page-menuzen-b3', 'Menuzen B3'),)
 EOF

::
   
 pip install ipython
  pip install -e git+https://github.com/fp4code/dju-menuzen.git#egg=dju_menuzen
 cd mysite/templates
 ln -s ../../../env/src/dju-menuzen/demos/page-menuzen-b3.html .
 ln -s ../../../env/src/dju-menuzen/demos/menu-b3.html 
 ln -s ../../../env/src/dju-menuzen/demos/menuzen-b3.html 

::

 ./manage.py shell

::
 
 from cms import models
 from cms import api
 from django.contrib.auth.models import User
 
 def page(parent, title):
     template = 'page-menuzen-b3.html'
     user = User.objects.all()[0]
     p = api.create_page(title, template, "en",
                         created_by='python-api',
                         parent=parent,
                         in_navigation=True,
                         published=True,
                         position="last-child")
     api.publish_page(p, user , "en")
     return p

 home = page(None, "home")
 a = page(home, "A")
 b = page(home, "B")
 c = page(home, "C")
 b1 = page(b, "1")
 b2 = page(b, "2")
 b3 = page(b, "3")
 b2a = page(b2, "a")
 b2b = page(b2, "b")
 b2b1 = page(b2b, "1")
 b2b2 = page(b2b, "2")
