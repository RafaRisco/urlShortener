# URL Shortener

This project provides a REST API for generating short strings for URLs and redirecting to the original URLs using those short strings.

## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine
2. Navigate to the project directory:
    shortenerapi
3. Create a virtual enviroment and activete it.
3. Install the dependencies using pip:
    - pip install -r requirements.txt
4. Apply database migrations:
    - python manage.py makemigrations
    - python manage.py migrate
5. Start the server:
    - python manage.py runserver


### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /core/shorturls/ | Retrieve all short URLs. |
| GET | /core/optout/:short_string/ | Redirect to the original URL using a short string. |
| POST | /core/shorturls/:url | Generate a short string for a given URL. Provide a JSON payload with the URL. |


