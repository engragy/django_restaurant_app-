# Retuarant website
[![LOGO|Django](https://codecondo.com/wp-content/uploads/2014/02/Django-Framework-Logo.png)]()
*** Powered By ***
##### Great implmentation of a Store with ordering web app.
### consists of a couple of pages!
> Main page with pictures of menu items, and odering form on the left.
> ![main_page](https://codecondo.com/wp-content/uploads/2014/02/Django-Framework-Logo.png)
> Order summary with Total amount, before placing the order.
> ![register_page](https://codecondo.com/wp-content/uploads/2014/02/Django-Framework-Logo.png)

### Features:
* Elegant restaurant website with nice Custom CSS effects (no styling framework is used)
* Relaying on JS to handle the ordering forms for better user experience.
* After logging in, users can make orders and track thier progress.
* using sqlite3 DataBase for development.

### Used Django extensions/packages/libraries including:
* [Django] -- web framework
* [django-widget-tweaks] -- ease form's manibulations
* [Pillow] -- handles images inside the website 

### Installation
```sh
just use a virtual environment for the app
$ pip3 install virtualenv
make a new folder for the app
$ mkdir ~/pizza_restaurant
$ cd pizza_restaurant
$ virtualenv .env
$ git clone
$ source .env/bin/activate 
$ pip -r install requirements
$ python manage.py runserver
```
[//]: # (reference links)

[django]: <https://docs.djangoproject.com/en/3.0/>
[django-widget-tweaks]: <https://github.com/jazzband/django-widget-tweaks/>
[Pillow]: <https://pillow.readthedocs.io/en/stable/>
