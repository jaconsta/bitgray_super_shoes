# Super Shoes Inventory app

## *Another test for bitgray and Growth Acceleration Partners*

Api: 
* [Django](https://www.djangoproject.com/) for the API construction.
* Urls follows REST syntax for web services. 
* Responses are provided via JSON.

This application can be accessed by two methods. API requests and management interfaces.

API is used for accessing data cross-device.

Admin is used to manage the information stored in the system.

## Instructions

To access the API services:

	/services/

To access the information management:

	/admin/

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

To create the platform database:

    $ python manage.py migrate

Create the default admin user for administration access and management:

	$ pytnon manage.py createsuperuser

To run the server locally:

    $ python manage.py runserver 0.0.0.0:8000

And access [localhost](http://localhost:8000) API from your tester.