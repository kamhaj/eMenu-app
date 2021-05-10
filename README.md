# Application using API calls <br/> to display/create/edit/delete restaurant menus online. </br></br>

<br/><br/>
# Deployed on Heroku (look at navbar for possible further steps): 
## **https://kamhaj-emenu-app.herokuapp.com**

<br/><br/>
## Django + DRF utilized. <br/>
## Celery + Redis used for running periodic tasks
(sending emails everyday at 10 a.m.) <br/>
(no third party email service specified, requires configuration) <br/><br/>
## Documentation in Swagger:
<br/> https://github.com/axnsan12/drf-yasg

<br/><br/><br/><br/>
## API usage:
https://kamhaj-emenu-app.herokuapp.com/swagger/

model Dish:<br/>
GET methods - no authorization <br/>
POST, PUT, DELETE - Token authorization <br/>

1.  GET    - to get Dish details  </br></br>
2.  GET    - to get Dishes list  </br></br>
3.  POST   - to create Dish object, ImageField included, Django Parsers used </br></br>
4.  PUT    - to update Dish fields, ImageField included, Django Parsers used </br></br>
5.  DELETE - to delete Dish </br></br>

model Menu: <br/>
GET methods - no authorization <br/>
POST, PUT, DELETE - Token authorization <br/>

1.  GET    - to get Menu details </br></br>
2.  GET    - to get Menus list (non empty, meaning - with at least one Dish) </br></br>
3.  POST   - to create Menu object, Dish objects added by specifying a list of their IDs </br> 
	(e.g. dishes: [{"pk":1}, {"pk": 3}, {"pk": 7}]   </br></br>
4.  PUT    - to update Menu fields, Dish objects added by specifying a list of their IDs </br> 
	(e.g. dishes: [{"pk":1}, {"pk": 3}, {"pk": 7}]. Old dishes will be removed.  </br></br>
5.  DELETE - to delete Menu </br></br>

<br/><br/><br/><br/>
## Swagger authorization
1. Click "Authorize" button
2. Provide "Token <token_value>"

<br/><br/><br/><br/>
## Run project locally
1. Clone repo
2. Set up virtual environment (venv) and activate it
```console
	virtualenv venv
```
```console
	venv\Scripts\activate     (Windows)
```
4. Install required libraries
```console
	pip install -r requirements.txt
```
5. Run Redis service (in CMD) to store/process tasks (download from here: https://github.com/ServiceStack/redis-windows)
```console
	redis-server.exe redis.windows.conf
```
7. Run a Celery worker (in separate CMD) to pick up tasks (sample task invoked every minute was provided for testing purposes)
```console
	celery -A restaurant worker -l INFO
```
9. Run app on localhost and access it in a broswer (localhost:8000)
```console
	python manage.py runserver
```




<br/><br/><br/><br/>
## Running tests:
```console
	coverage run --source='.' manage.py test 
```
## Getting tests coverage report:
```console
	coverage report --omit=venv/*
```


<br/><br/><br/><br/>
## Additional info:
1. Periodic task (emails sending) can be run on demand (as Django custom command)
```bash
	python manage.py email-report
``` 
2. API only: listing Dishes and Menus can be sorted <br/>(by adding parameters to URL, <br/> e.g. https://kamhaj-emenu-app.herokuapp.com/api/eMenu/dish/list_dishes/?sort=name )
3. Sqlite3 db was used.

<br/><br/><br/><br/>
## TODO
- add pagination
