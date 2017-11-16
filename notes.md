# Notes 

```
mkvirtualenv blog_project 
pip install django 
django-admin startproject blog_project
cd blog_project
git init
./manage.py startapp posts 
```

- update `settings.py:
  * add `posts`  to `INSTALLED_APPS` 
  * configure `dirs` to accept project level directory 

- create `/templates` folder and `templates/_layout.html`

```
./manage.py migrate
./manage.py runserver
```

- update `models.py`
```
./manage.py makemigrations posts 
./manage.py migrate posts
```

- create superuser and add posts content in admin
```
./manage.py createsuperuser
```

- update `admin.py`

- update `blog_project/urls.py`
- create `posts/urls.py` file 
- create `posts/views.py` file 

- create folders for `posts/templates/posts/`
- add files for `post_delete.html`, `post_detail.html`, `post_edit.html`, `post_list.html`, `post_new.html`