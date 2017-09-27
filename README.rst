# dju-menuzen
A attempt to build a simple breadcrumb/menu system for Django-CMS

::

 export D=$(pwd)

::

 cd $D
 virtualenv env -p $(which python3)
 source env/bin/activate
 pip install djangocms-installer==0.9.7
 djangocms mysite

:: 

 cd $D/mysite
 cat >> mysite/settings.py << EOF
 INSTALLED_APPS += ('dju_menuzen',)
 CMS_TEMPLATES += (('page-menuzen-b3.html', 'Menuzen B3'),)
 EOF

::
   
 pip install ipython
 pip install -e git+https://github.com/fp4code/dju-menuzen.git#egg=dju_menuzen

::
  
 cd $D/mysite/templates
 ln -s ../../../env/src/dju-menuzen/demos/page-menuzen-b3.html .
 ln -s ../../../env/src/dju-menuzen/demos/menu-b3.html 
 ln -s ../../../env/src/dju-menuzen/demos/menuzen-b3.html 
 ln -s ../../../env/src/dju-menuzen/demos/page-menuzen-f6_4.html .
 ln -s ../../../env/src/dju-menuzen/demos/menu-f6_4.html 
 ln -s ../../../env/src/dju-menuzen/demos/menuzen-f6_4.html 

::

 cd $D
 git clone https://github.com/fp4code/foundation-zurb-template.git
 cd foundation-zurb-template
 npm install
 npm start

::

 cd $D/mysite/mysite/static
 ln -s ../../../foundation-zurb-template/dist/assets
 mkdir Z
 cd Z
 wget http://zurb.com/playground/uploads/upload/upload/288/foundation-icons.zip
 unzip foundation-icons.zip
 mv foundation-icons ..
 cd ..
 rm -rf Z

::

 cd $D/mysite
 ./manage.py shell

::
 
 from cms import models
 from cms import api
 from cms.constants import TEMPLATE_INHERITANCE_MAGIC
 from django.contrib.auth.models import User

 
 def page(parent, title, template=TEMPLATE_INHERITANCE_MAGIC):
     user = User.objects.all()[0]
     id = "id_home" if parent == None else None
     p = api.create_page(title, template, "en",
                         parent=parent,
                         in_navigation=True,
			 reverse_id = id,
                         published=True)
     api.publish_page(p, user , "en")
     return p

 home = page(None, "home")
 b = page(home, "Bootstrap 3", "page-menuzen-b3.html")
 f = page(home, "Foundation 6.4", "page-menuzen-f6_4.html")
 b1 = page(b, "1")
 b2 = page(b, "2")
 b3 = page(b, "3")
 f1 = page(f, "1")
 f2 = page(f, "2")
 f3 = page(f, "3")
 b2a = page(b2, "a")
 b2b = page(b2, "b")
 b2b1 = page(b2b, "1")
 b2b2 = page(b2b, "2")
 f2a = page(f2, "a")
 f2b = page(f2, "b")
 f2b1 = page(f2b, "1")
 f2b2 = page(f2b, "2")

Launch server
 
::

 ./manage.py runserver 8005

and open http://localhost:8005/en/bootstrap-3/
