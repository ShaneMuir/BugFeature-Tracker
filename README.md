# Milestone 5

[![Build Status](https://travis-ci.org/ShaneMuir/milestone-5.svg?branch=master)](https://travis-ci.org/ShaneMuir/milestone-5)

### [Demo Here](https://milestone-5.herokuapp.com/)

 What is Unicorn Attractor? It's an app built with Django. 
 In this application I use technologies learnt on my coding journey to demonstrate how a SQL (Structured Query Language) based database can be utilised efficiently and effectively to create scalable apps on the web. The aim of this project is to showcase my skill set learnt throughout the course.
 
Throughout this project I will make use of [Python](https://www.python.org/) a high-end programming language along with [Django](https://www.djangoproject.com/) a Python framework. 

---
#### About
Unicorn Attractor is an Issue tracking web app built on the back of the fictional app **'Wuzzat'** which allows users to request paid featuresto the app or to report bugs they have encountered. 

## UX
I created this app to give my user's the ability to request new features to 'Wuzzat' or to report any bugs found on the app. 
The app is designed to allow for users to create free bugs or request paid features. 
I've developed the app to incorporate user authentication  and authorization, this means anonymous users cannot create bugs or features. 
Within the app there is also more authorization restrictions in place to better protect my database and restricted pages.
Within the application design I have included a profile page, this creates a simple way for the logged user to view any self created bugs or features and manage them in one place. 
To provide each user with some site statistics I have also included a graphical dashboard onto the user profile page to give analytics on the app. 
Within my app I have created a cart to accommodate the process of buying and up voting of features, within this app the user has the ability to manage their purchases within the cart. 
By this the user can remove items from their cart if no wanted or if up voting a feature they can increase or decrease the amount of up votes they want to 
apply to that given feature(s).
I've implemented a password reset functionality to my app, this allows registered users the ability to recovery their account and reset their passwords.
From within the profile page a user has the ability to edit or delete their own bugs or features.
The app was designed mobile first, this was to aid the modern style of usability across all types of devices and screen sizes. 

## User Stories
Reasons why I decided to build Unicorn Attractor.
> Wuzzat email inbox full of users request new features to the app

> Wuzzat users wanting a place to log bugs

> A user has found a bug on the app and wants a place to log these and track the progress

> A user wants to request a new feature to the app

> Unicorn Attractor Users have ability to request new features via a paid checkout features

> A user wants to check if a listed bug or feature has already been requested

> Users want the ability to edit or delete their requests

> A user needs the ability to reset their password

> As a user I want the ability to comment on requested bugs or features

## Wireframes

[wireframes here]

## Functionality
The app's main functionality is that it is capable of communicating and manipulating a SQL based database running on Heroku (PostgreSQL) 
and shows my skill set learnt so far from the course. By using Django I have been able to create an application that can register and login users, 
with the ability to password reset if required. Users can create, read, update and delete bugs or features. 
Requested features are purchased via Stripe which gives the app the ability to take payments from users in order to list features on the app. 
Up-voting of bugs and features but feature up-votes use the stripe app as they cost £5 per up-votes, this allows admin to easily identify the most wanted feature or the 
most identified bug that users want dealing with first.

By allowing users to be able to registered with an account I can track bug and feature requests, restrict certain pages, and implement user authentication and authorisation. 
This means I have the ability to restrict users from user activities and also lock down requests to certain users.

The app uses back-end logic where restrictions are used. This creates a better experience with user data and enables me to add a level of security to my app.

My app is scalable and responsive meaning it will perform well on any device its loaded on.

Within my app functionality there is the ability to search, this was implemented to give the user's the ability to quickly filter the database based on a particular search query.

Password reset gives my users the ability to recovery a lost password if required, by entering the email the user signed up with on the password reset page, 
triggers an email from my apps account to the specified email with a password reset link to their account.

Users have the ability to login via email or username.

Only users who created the bug or feature can edit or delete their own. 

My app uses the Stripe API so that users can make payments in order to request new features, and up votes on already requested features.

My app makes use of the Pygal Python libary to create some analytics of the database data.

Bugs and features page use Django's paginator to create a better user experience for the user not having to scroll down lengthy pages. 

My application is developed with SEO practises in mind and is structured well inline with googles best practises. 

Performance of my website is fast and database queries are performed effifiently. 

The bug and feature pages use the browsers local stroage to better enhance the UX of the notification bar so a user doesnt get the message each and every time they go onto this page. 

My login required returns the user back to the page they came from rather then a standard page. 

## Technology Used
- [Python 3](https://www.python.org/download/releases/3.0/)
- [Django](https://www.djangoproject.com/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CCS3](https://www.w3.org/Style/CSS/)
- [BootStrap](https://getbootstrap.com/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Heroku](https://www.heroku.com/)

### Features to be implemented 
In the future I will implement the below features

- A live chat feature, this would allow users to directly chat with online admins of the app.
- Make use of Python's logging library to log system information, i.e log the user, browser they was using, time/date, request.path etc so that 
  I can better understand when my app crashes or any error are encountered. 
- AJAX functionality on the front-end, for example when a user deletes a bug from their profile page.
- Edit username/password

##### Why I Built Unicorn Attractor
The reasoning behind the project is simple, the 'Wuzzat' app is fictional and I came up with a use case for a real world app so that I can show case all the skill set
I've learnt from the whole of the Code Institute Course. The reason I decided to pick a bug tracker was for the fact that I could easily within the time-frame left
create a app that relied heavily on a back-end database. With this I was able to demonstrate CRUD activity against a SQL database, create user authentication and authorization,implement a admin back-end, password resets functionality, and many of the features outlines above in the functionality section. 

## Testing

*Throughout the whole development process of my app I made use of [Unittest](https://docs.python.org/3/library/unittest.html) via [Django tests](https://docs.djangoproject.com/en/2.2/topics/testing/)*
*and manually testing by selected users or myself. Below I will outline and detail my processes and how these helped me identify issues and bugs within my app and rectify them.*


## Automated testing
### Unittesting
My unittesting consisted of test modules in each app using the unittest framework built into Django and running the coverage report to get a detailed report of how well each Django module was tested.
Where I was not able to automate tests for that particular module I used manually testing thoroughly to ensure my app was tested throughout. More on unittest package can be found on the link above.

[Travis CI](https://travis-ci.org/) was implemented to help continuously test my app through the development process. 
You can click the 'build passing' icon at the top of my repo to check out Travis on this app. More on Travis CI can be found on the link [here.](https://travis-ci.org/)

[Coverage](https://coverage.readthedocs.io/en/v4.5.x/) was used to check how well my automated tests were performing on my app, 
this library was golden to showing how much of code my automated tests were actually testing. Note - for any app that wasn't not showing a good coverage report I reverted to manually testing thoroughly.
More on the coverage package can be found using the link [here.](https://coverage.readthedocs.io/en/v4.5.x/)

By using the above mentioned technology through my development process of my app I was able to quickly check if any tests were failing and why, 
and also get a detailed report of all my tests in a view that was easily digestible and then was able to adapt and adjust the tests to make them cover more or give me detail on where I need to manually
test my apps functionality for further improving my coverage. 

## Manual Testing
**Testing Django** - Within my settings I had Django's debugger set to 
```python
debug = False
```
This is so when ever the app encountered a error then Django would give a detailed report and outline what happened and why the error occurred. 
This was vital during the development process as I would work in small sprints where every step in my development I would ensure my app is still working as expected and where any errors occurred I would debug the source until rectification was a success. Where needed I would document the error and the remediation taking in case of future occurrences. 
Doing this meant that after a while the error codes became more familiar to me. And from debugging each error become less time consuming. 


**Testing Python** - When writing any logic, I would write this is small chunks and do any routine testing from the CLI (Command Line Interface) 
and where needed use the Python Interpreter to test any function or statements.

Built-in [Py Lint](https://www.pylint.org/), AWS Cloud9 implements a very handy Python Linter which outlines and identify possible incorrect python code. Using this helped me easily identify indentation errors or syntax errors along with any undefined class methods or function calls and much more. You can found more info on Py Lint by clicking the link [here.](https://www.pylint.org/)

Django server, Django has a built in httpserver which if there is any error on the source code would result in the server throwing a server error if anything was wrong, this helped identify any run time errors in my app.

**Testing Django Views** - In Django each app has views which are functions that invoked when a user navigate to a certain URL (Uniform Resource Location). 
Throughout the entire development process of my app all my views were tested by automated tests and then by using the coverage report to outline what was not tested. 
My manual testing process for my apps views consisted of me following the logic and perform each step manually in a browser to see if my app works as expected. 
From automated testing and manually testing I was therefore confident that my app views worked. Through out testing within Python I see myself always using the` print()` method to ensure database calls were successfully and also that functions had worked properly. 

**Testing the Database** - Alot of my database models were tested with automated tests and then further expanded on from the coverage report by manual tests. 
Automated tests can be found within the apps source code names `test_models.py` and my manual testing process I will outline below.
When creating models and forms in Django, I would then write the corresponding URL and view so that I can manually test each logic. 
Therefore I would need to run my app and then navigate to it via a browser to perform each step I wrote and ensure that my app was successful based on the logic wrote. 
A lot of the database was covered in the automated tests but manual testing where needed was performed. 
 
 Django makes use of SQLite when first creating a project, this is call a 'development database' I made use of this database throughout the entire development process until close to production where I switched to a PostgreSQL database hosted on Heroku. As most of my database was already tested throughout the development stages I had no issues when switch from SQLite to PostgreSQL.
 
 **Testing CRUD** *(Create, Read, Update, Delete)* - After creation of my models and forms I wanted to ensure the logic within my views was working as expected and further tested this by  manual testing against any forms within my app. Were there was any user input to my app after automated testing was complete I would then go manually test each form and ensure that the logic performed as expected without any errors. 

**CREATE**
This was tested by me manually inputting data into the forms via the front-end and checking the operation was successfull from the admin panel. I tested all types of senarios such as long descritpions fields long titles anything that could potential break my site. 

**EDIT** 
To ensure the edit functionality of the bug and features views work correctly I manually used the front-end to edit some bugs and features I already created for testing purposes. In the process I also tested all the form validations from the logic in the backend. 

**DELETE**
To delete a bug or feature from within my app database the user would need to navigate to their profile page and only be able to delete bugs or features that they had requested.
To prevent any bug or feature being delete by mistake I added some JavaScript to confirm the request to the user before actually making any changes to my database. 
This was a measure I implemented to ensure the user didn't make a miss-click. 

**EDIT**
To protect user request bug or features from being deleted or edited I implemented strict logic so that only the said user can edit or delete their own bug or feature. 
This was achievable by creating a relationship from the bug or feature model to the user model. And if the creator of that bug or feature was the logged in user then the logic was allowed to be performed, 
if not then within my app i implemented a alert message to give the user indication on why such action cant be performed.

**Authenitication and Authorisation** - Django comes built in with this so from using the docs and what I'd learnt front he course and already knew around this I implement a basic user registration and login system with the ability to reset a user's forgotten password. From the course we was taught how to allow user to log in via their email address as well as they're username. From the docs I further expanded on the user model and created custom forms for my login and register views. Password hashing is taken care of in Django so any password submitted to my database are hashed. From implementation of the user authentication and authorization I was able to further add security into my app for users and database protection. In Django I was able to restrict logic by using `request.user.is_authenitaticated` and restricting views with the `@login_required` decorator. 

**Cart App**
My cart was taken from the Code Institute course where we created a mini-project that was a e-commerce application. I further adapted this functionality for the purpose of my app, the cart applys feautre up-votes from the user, a user can up-vote multiple features at once and also increase the amount of up-vote they submit onto each feature (up-votes cost £5 per up-vote). I tested this my manually click upvote on several features and processing the checkout too to ensure the cart was emptied as expected and up-viotes were appied to the correct features, the correct value of times also. I tested all different types of senarios on my cart app such as adding multiple to up-vote then removing one and increase one at the same time, spamming the increase or decrease button anything to try break my app. The cart app makes uses of Django sessions.

**Checkout App**
My checkout app was adapted from the Code Institute course for the purpose of my website. I tested this by using Stripes test card (4242 4242 4242 4242) I tested the forms and ensured all my validation worked as expected and my logic was performing as expected. The checkout app works from the Stripe API. 

**Search Bar**
Within my application there is a search bar in the navigation menu that is accessible at all times when the navbar is present. The search bar searches my app for bugs or features, this was manually tested by entering search terms and checking the expected result. I tried to enter unusual types of search to see if I could break the app. 

**Pagination**
My app makes use of Django's paginator, I created this from their docs but testing was done manually by me imeplemented the code then checking the functionality on the front-end to check if the logic was performing as expected. On the profile's page I found that the paginator would give a 500 server error when trying to access a page for a feature that wasn't availble for bugs aswell. To explain this better let's say on my user profile page I I had 5 bugs, 4 features, where my app only displayed 2 max on the profiles page there would be 3 available pages for bugs and 2 for features if you tried to access the 3rd page for bugs my app would encounter a server error. I rectified this issue by further expanding on Django's paginator and adapted it to suit my app's use case. 

**Password Reset**
This functionality comes built-in to Django but I have further expanded on it to suit the use case of my app. The email sent uses my own domain and I have adapted the reset pages and html email sent to the user. I tested this part of my app through entering clicking the forgot password button and entering my email to ensure the functionality was working as expected. 

**Site Analytics**
My app's profile page make use of Pygal a Python libary for creating interactive graphs on the web. I decided to use this package becuase I do data analyse already and want to further progress my Python skills around data science. The code was developed by using the pygal docs, and tested manually by checking the expected outcome on the profile page. 

**Repsonsiveness**
My app makes use of the Bootstrap CSS framework, when implemented successfully it ensure my website is fully responsive on all devices. Further CSS was added to further enhance the UX of my site. I tested the repsonsiveness of my app by making use of chrome's devtools and applying each device preset which set the width and height to specific values based on mobile and tablet devices of all screen sizes. Further testing on this was perform by me on my mobile and tablet phone. The slack community further helped by riggerously testing my website in peer to peer code review. 

**Browser compatibility** 
My app does not work on IE, although I wanted to have my app backward compatible with all browsers, I couldn't have it on IE due to Materialize and using elements that are not support by old Browsers.

My app will be fully functional across all major modern browsers. I have tested my app on the following browsers.

- [Chrome](https://www.google.com/chrome/)
- [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- [Opera](https://www.opera.com/)
- [IE Edge](https://www.microsoft.com/en-gb/windows/microsoft-edge)
- [Safari](https://support.apple.com/en_GB/downloads/safari)
- [Chrome Mobile](https://chrome.en.softonic.com/)

## Resource Sites Used
- [Django Docs](https://docs.djangoproject.com/en/2.2/)
- [Pygal](http://www.pygal.org/en/stable/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [BootStrap](https://getbootstrap.com/)
- [Stripe API](https://stripe.com/docs/api)
- [Bootswatch LUX](https://bootswatch.com/lux/)
- [AWS S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html)
- [Google Fonts](https://fonts.google.com/)
- [jQuery](https://jquery.com/)
- [GitHub](https://github.com/)
- [Font Awesome](https://fontawesome.com/)
- [Unplsash](https://unsplash.com/)
- [Slack](https://slack.com/intl/en-gb/)
- [Stack Overflow](https://stackoverflow.com/)
- [Google](https://google.com/)
- [YouTube](https://www.youtube.com/)

  
#### Website Performance
Through the entirety of my project website performance is at the forefront of my mind. mark-up has been optimized for website performance along with CSS/JS. All images have been compressed. As the project is on Heroku the server cannot be optimized.

#### Django settings
I split my settings module into 3 files, one for the base settings and two others one for a production enviroment and one for a development enviroment. This ensured Travis CI wasn't affected by Heroku's PostgreSQL database in production. It also allowed me to seperate my settings for my static files. I also don't have to change the debugger. This also ensure when anyone wants to expand on my project there is no requirement to remove all my production ready code in order to have my app work locally for anybody without my database access. 


## Deployment 
Getting my application ready for deployment consisted of the following: - 
1. Removing all my hard-coded environment variables to project my keys and secrets. These were placed in the .bashrc for development and entered into Heroku's Config Vars for production.
2. Ensuring the applications requirements.txt is up-to-date with all the latest packages installed for my app being noted on this file. 
	**The command to update requirements**
		```
		pip3 freeze > requirements.txt
		```
3. Set up the Procfile - *A Procfile is required by Heroku in order to tell the service worker what command to run for my application to start.*
4. Push all static files to S3 Bucket `python3 manage.py collectstatic`
5. Enter all my ENV vars into Heroku's config vars (A list of all my config var is listed below in expanding on my project section)
6. Push all my latest production ready code to GitHub ready for deployment via Heroku's GitHub function where you can deploy from GitHub the production ready app.

**Upon successful deployment Heroku will give you the URL that is hosted your app**

*Upon unsuccessful deployment Heroku will log the cause of the error and this is view able in the 'view log' section on the Heroku website. Here you will find a detailed report of what has cause your application not to be deployed successfully. *

### Heroku Config Var's
| Key | Value |
 --- | ---
AWS_ACCESS_KEY_ID| `<your_access_key_id>`
AWS_SECRET_ACCESS_KEY| `<your_secret_key>`
DATABASE_URL| `<your_data_base_url>`
DEFAULT_FROM_EMAIL| `<your_from_email>`
DISABLE_COLLECTSTATIC| `1`
EMAIL_HOST | `<your_email_host>`
EMAIL_HOST_PASSWORD| `<your-email-password>`
EMAIL_HOST_USER| `<your-email-address>`
SECRET_KEY| `<a_secret_key>`
SERVER_EMAIL| `<your_email_address>`
STRIPE_PUBLISHABLE| `<your_stripe_key>`
STRIPE_SECRET| `<your_stripe_secret>`

## Expanding on my Project
To get set up with a copy of my project you can do these multiple ways. 

**Via GitHub** -  
1. You can manually download locally to your machine and then upload to your preferred IDE. 
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few project settings before we can run the app. Open settings folder and in local.py
	1. `ADD ALLOWED HOST`
	2.  `SET UP EMAIL CONFIG`
	3. `SET UP STRIPE API KEY/SECRET`
4. Once the above steps are complete you can try run the application using `python3 manage.py runserver $IP:$PORT`

*Please note* step 4 may be different depending on the operating system you are running, please refer to the documentation for more details on running the Django server on different OS's 

**Via the CLI** -
1. Clone my repo via Git using the following command `https://github.com/ShaneMuir/Milestone-5.git`
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few project settings before we can run the app. Open settings folder and in local.py
	1. `ADD ALLOWED HOST`
	2.  `SET UP EMAIL CONFIG`
	3. `SET UP STRIPE API KEY/SECRET`
4. Once the above steps are complete you can try run the application using `python3 manage.py runserver $IP:$PORT`

## Credits & Acknowledgments 
Credit is due to the following names. I would like to thank each and every one who has helped or contributed to my project in any way. Please see list of names below:

[HTML5 Mockups](https://github.com/pixelsign/html5-device-mockups) - The device pictures used on the landing page, I want to credit this guys work very handy and plenty of devices to use!
[Django Pagination](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) - This guide helped me implement pagination with ease!
[LUX Bootswatch](https://bootswatch.com/lux/) - This theme took care of most of my applications design!
[Custom 404/500 Pages](https://codepen.io/theyve
) - This guy Dave is awesome!

I would like to write a thank you to **Jorden Vijayaratnam**.

- Youtuber **Pretty Printed**
- Slack Users **johnL3_alumni, RyanCooper, Seán, Jorden**
- Flask Megua Tutorial creator **Miguel Grinberg**
- Head First Python: A Brain-Friendly Guide **Paul Barry**

# LICENSE
This project is release under the **MIT** licence. For more info [here.](https://raw.githubusercontent.com/ShaneMuir/milestone-5/master/LICENSE)
