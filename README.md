# homeScreenNetwork-Assignment
view.py contains get() API 
    for fetching current datetime
    1) Here i make a class throttlerViewset which extends (REST framework class) APIView class.
    2) I override the get() method of APIView class which accepts the incoming request and returns current datetime 
       & status(HTTP_200_OK).

settings.py contains configuration: 
    1) Here i configure two settings for enabling throttle support which is given by REST framework DEFAULT_THROTTLE_CLASSES,
      DEFAULT_THROTTLE_RATES.
    2) using 'DEFAULT_THROTTLE_RATES' setting i achieve throttling rate of 20 request per minute. 
    
url.py contains mapping:
    1) Here i map the url path with method to be called from views.py for this type of request.
    
API URL : "http://127.0.0.1:8000/v1/time/"
