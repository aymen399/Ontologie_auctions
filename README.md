# Ontologie_auctions
This is a web semantic project built using Django, it's an online platform which offer the users the possibility to participate in online auctions of sharbale and unsharable products.



# Installation guide :
first you need to have python installed.
Enter in the main folder of the project from either the command line or a IDE, and follow these instructions please:

1- pip install -r requirments.txt 

2- python manage.py makemigrations

3- python manage.py migrate

4- python manage.py runserver
 
After runing the app 
you can enter the super user interface (which is considered too as the products provider) following this URL:
http://127.0.0.1:8000/admin/

To enter the client inferce home follow this URL:
http://127.0.0.1:8000/website/


DONE!! 

# Specifications:

-- The provider(super user): 
* Add a new product by specifying its information such as its nature.
* Add units of a pre-existing product in the application database.
* Create an auction specifying the minimum unit price and its exact start and end date and time.


-- The client:
* Consult his balance.
* View its list of current auctions.
* Consult all the auctions in progress, or display a specific category auctions.
* Participate in one of the auctions whether it is in his list or not under the following conditions: that he pays a * small amount at the time of first access to this auction, that he proposes an offer with at least adding unit price proposed or increase the quantity proposed in the case of products exposed of shareable nature. 

