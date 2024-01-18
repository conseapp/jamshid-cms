# jamshid CMS

#### api to fetch, retrieve, search posts from front-end
#### api to add comment for each posts from front-end
#### need authentication for add comments
#### all data has been stored on postgresql running on main server

### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
* ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Admin

admin panel

* https://cms.api.jamshid.app/admin

## Usage

method = GET

### get all posts

```console
https://cms.api.jamshid.app/blog/posts/
```
* paginated by 5
####  get page query
```console
https://cms.api.jamshid.app/blog/posts/?page=<page_number>
```

### get one post

```console
https://cms.api.jamshid.app/blog/post/<post-slug>
```

### get post comments

```console
https://cms.api.jamshid.app/blog/post/<post-slug>/comments/
```
* paginated by 7
#### get page query
```console
https://cms.api.jamshid.app/blog/post/<post-slug>/comments/?page=<page_number>
```
### get all categories

```console
https://cms.api.jamshid.app/blog/categories/
```
### get one category posts

```console
https://cms.api.jamshid.app/blog/category/<category-slug>/
```
* return all posts in current and sub categories
* if you want to fetch just queried category
* pass "descendants=False" in query kwargs
#### get only queried category posts
```console
https://cms.api.jamshid.app/blog/category/<category-slug>/?descendants=False
```
* paginated by 5
#### get page query
```console
https://cms.api.jamshid.app/blog/category/<category-slug>/?page=<page_number>
```


### search all posts

```console
https://cms.api.jamshid.app/blog/posts/?search=<query>
```
* paginated by 5
#### get page query
```console
https://cms.api.jamshid.app//blog/posts/?search=<query>&page=<page_number>
```

### add post comment

method = POST

```console
https://cms.api.jamshid.app/blog/post/<post-slug>/comments/
```

required headers : token<br>

body example:

```console
{
    "body": "first Comment for post 2 from postman",
    "author": "09123333333"
}
```

## Deploy

### 1. install python environment

```console
sudo apt install python3.10-venv
```

### 2. initialize environment

```console
python3 -m venv venv
```

### 3. activate environment

```console
source venv/bin/activate
```

### 4. install requirements

```console
pip3 install -r requirements.txt
```

### 5. make migrations

```console
python3 manage.py makemigrations
```

### 6. migrate

```console
python3 manage.py migrate
```

### 7. create admin user

```console
python2 manage.py createsuperuser
```

### 8. run

```console
python manage.py runserver
```

Developed By Hexoder
