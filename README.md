# drf-pandas
A Django boilerplate to serve content of tabular files through a REST API with Django, Django Rest Framework (DRF), Django Rest Pandas (DRP) and of course, pandas.

The idea behind this project was to build a system that can serve csv files, manipulate them through pandas, serve them to a React frontend through REST API.

## Getting Started

Clone the repo, create a virtualenv, and install dependencies:

```
pip install -r requirements.txt
```

Instantiate database and apply migrations:

```
./manage.py migrate
```

Launch the Django development server:

```
./mangage.py runserver
```

## Retrieving Data

A sample data file (`data/movies.csv`) is hard-coded. The list of attributes and their data types can be retrieved:

```
http://localhost:8000/movies/attributes?format=json
```

The data file can be queried by providing a list of attributes to be retrieved:

```
http://localhost:8000/movies/items?format=json&attributes=Name,ReleaseDate,AvgRating
```

This will return JSON that includes the selected fields:

```
[{"Name":"Toy Story (1995)","ReleaseDate":1995,"AvgRating":4.15},{"Name":"Jumanji (1995)","ReleaseDate":1995,"AvgRating":3.2},{"Name":"Grumpier Old Men (1995)","ReleaseDate":1995,"AvgRating":3.02},{"Name":"Waiting to Exhale (1995)","ReleaseDate":1995,"AvgRating":2.73}, ...]
```

Other formats such as CSV can be retrieved as well:

```
http://localhost:8000/movies/items?format=csv&attributes=Name,ReleaseDate,AvgRating
```

Details about possible formats are included in the [django-rest-pandas](https://github.com/wq/django-rest-pandas) documentation.

## Future
In the next iteration I will serve this content to a React frontend. So stay tuned.
