This project (Assessment 3) for the course Advanced Internet Programming is written by Suhit Sthapit only. 
My Student Student ID is 12673341. 

*****************************************************************************************************************
PickYourLiquor.com

I have used Python's Django Framework for the web application development. 
Django is based on Models, Templates and Views concept.

The name of the website is PickYourLiqour.com
The purpose of this website is that, users can signup, login and logout and they can create, read, update and 
search the data. They can enter data about their favorite liquor, its price, its category and its type (if it 
is available in can or bottle). 
The users can also follow or unfollow other users. They can view the data of the person they follow in their
home page. 

*****************************************************************************************************************
BASIC OVERVIEW OF DJANGO FRAMEWORK

There are all the required files attached in this ZIP file for the program to run. 
The 'requirements.txt' file contains list of all the files necessary for the app to run.

The project folder name is PickYourLiqour.

There are four apps installed in this project for basic functions. They are:
1) liquors
2) profiles
3) api
4) githubapi


1) liquors
In this app, users can add their favorite liqour and they have options to make them public. They can also update
the data they have entered. They can also search for liquors, type of liquors, category of liqours in this app.

2) profiles
This app helps to create a profile for each user. In this profile, we store the followers of the user. In the
newsfeed, users can see the favorite liqour of the friends they follow. They can also unfollow them.

Similarly, when a new user register, they will be provided with activation code to activate their account by
email. Until they activate their account, their user profile will not be created.

3)api 
This app exposes a useful REST api to users. Users can perform get, post, delete and update functions. They can
post data about their favorite liquor and they do not have to login in this app. The users can remain anonymous.
Similarly, they can also perform get function to retrive the data in JSON format as well.

4) githubapi
This app helps to integrate the system to a public web service, i.e., GITHUB.
The users can enter their username of GITHUB in our form, and they will be provided with detailed information
about their account in GITHUB. For this purpose, this app sends requests to GITHUB API and recieves JSON data
in return and displays that information in the website.

 
*****************************************************************************************************************
HOW TO GET STARTED:


In order to start the server, following commands must be executed:

	cd AIPProject\Scripts
	activate
	cd ..
	cd src
	python manage.py runserver

The last command is to run our Django server. 

*****************************************************************************************************************
API SERVICE

The API service provided in this web application has get, post, delete and update methods.

The users can go to following link to post data: 
http://127.0.0.1:8000/liquor

Similarly, the users can go send get request to get data of particular liquor if its 'id' is provided.
For instance,
http://127.0.0.1:8000/liquor/2 
The above request allows the user to get data about liquor "Becks" in JSON format.

*****************************************************************************************************************





























