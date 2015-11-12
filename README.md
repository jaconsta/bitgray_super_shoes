# Super Shoes Inventory app

## *Another test for bitgray and Growth Acceleration Partners*

Api: 
* [Django](https://www.djangoproject.com/) for the API construction.
* Urls follows REST syntax for web services. 
* Responses are provided via JSON.

## Instructions

### API

Set The Virtual environment:

    $ python -m venv myenv
    $ source myenv/bin/activate # If Linux
    or
    $ myenv\Scripts\activate.bat # If Windows

And install from requirements:

	$ pip install  -r requirements.txt # --no-index

In the project directory:

	$ cd bitgray_superShoes/superShoes

Create a database with name *supershoes* and run:

    $ python manage.py migrate

To run the server locally:

    $ python manage.py runserver 0.0.0.0:8000

And access [localhost](http://localhost:8000) API from your tester.