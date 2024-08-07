####################################################
       Project Name : BADAN BARMAN PORTFOLIO
####################################################
date : 01.06.2024
*Start with creating an stanalone environment for the project..
$py -m venv <name_of_environment>
$py -m pip install django
$django-admin startproject <project_name>
$ cd <project_name>
$ django-admin startapp <app_name>
$ py mange.py createsuperuser    =>Username : badan, Passwd : badan@123
   added normal user    => Username : precidingofficer, Password: notanadmin@123
##########################################
FIle Structure >>
	--BadanBarman
	   |________ settings.py
	   |________ urls.py
	   |________ wsgi.py
	   |________ asgi.py
	   |_______ __init__.py
	--PO
	   |________ migrations	  
	   |________ __init__.py
	   |________ admin.py
	   |________ apps.py
	   |________ models.py
	   |________ urls.py
	   |________ views.py
	   |________ tests.py
	--static
	--templates
	   |________ base.html
	   |________ index.html
	   |________ login.html
	   |________ povo_home.html
	   |________ preciding_officer.html
	   |________ voter.html
	   |________ voter_show_BadanBarman.html
	--db
	--manage
#############################################
# BADAN BARMAN

This is the Personal Portfolio Designed for Dr Badan Barman.
<div style="align:center">
 <img src="BadanBarman/static/images/main_logo.png" alt="django-image">
</div>
 

_______________________________________________________________________________________________________________________________________________________________________
# Software Used
<div>
 <img src="./screenshots/Django.png" alt="django-image">
 </div>

The project is build with Django. The Database is the ~Sqlite3 which comes in built with the Django Framework,since the amount of data we are dealing with is very small so no external database is implemented.  

It uses GSAP for animations.

Tailwind CSS is used for the styles.




_______________________________________________________________________________________________________________________________________________________________________
# Usage

#### To get it up and running quickly:
Make sure you have python@latest or above installed on your machine.


### The easier method :


> Download the zip file by selecting the branch as master.


> Unzip it and move inside the BadanBarman folder.


> You have to create the environment by typing the below command.

```javascript
$.\env\Scripts\activate
```


> Again move inside the BadanBarman folder.Once you are inside the first BadanBarman folder ,again move into the next BadanBarman folder.


> Now open the powershell or command prompt with the current BadanBarman folder and type the bellow command.


```javascript
$ python3 manage.py runserver
```
This will start the server on 8000
> vist the below link in browser 
```javascript 
$ http://127.0.0.1:8000
 ```

And you are good to go.




### or (other method)
> Copy the Below command if you have git bash installed on your computer.
```javascript
$ git clone https://github.com/Hungryfoxz/BadanBarman.git
```
This will create a folder named Django_poll into your current working directory.
> Now cd into the directory 
```javascript
$ cd BadanBarman
```
Now you will see a directory tree something like this.
>##### BadanBarman


>######    |+..../BadanBarman


>######    |+..../setup


>######    |+..../jstoolchain


>######    |+..../static


>######    |+..../templates


>######    |+..../db


>######    |+..../input.css


>######    |+..../manage.py


>##### env


>##### screenshots


>##### README.md


>##### requirements.txt


> You have to create the environment by typing the below command.

```javascript
$.\env\Scripts\activate
```

> Now cd into the BadanBarman folder 

```javascript
$ cd BadanBarman
```
> Now cd again into the BadanBarman folder 

```javascript
$ cd BadanBarman
```

Now once you are inside the BadanBarman directory just type in the bellow command to start the development server.
> By default it will run on http://127.0.0.1:8000
```javascript
$ python3 manage.py runserver
```


### Default Credentials

Login to the admin panel with this url : 
### http://127.0.0.1:8000/admin



```username :```
> ##### badan


```password :```
> ##### badan@123


After you are successfully logged in , Go to the users table and add New user and select the previledges. Add new admin and password as your choice and give him the 'super-user' access and after the new 'super-user' is created remove the default superuser.






# Working :

#### ```Home/Index page```


> On successfull Completion of the Server setup , You will be greeted with this page.



<div style="align:center">
 <img src="./screenshots/hero.png" alt="django-image">
</div>


> Some sample images from the site are given below :

<div style="align: start">
 <img src="./screenshots/menu.png" alt="menu-image" width="30%"></img>
 <img src="./screenshots/lectures.png" alt="lectures-image" width="30%"></img>
 <img src="./screenshots/contact.png" alt="contact-image" width="30%"></img>
 <img src="./screenshots/ppts.png" alt="ppts-image" width="30%"></img>
 <img src="./screenshots/publications.png" alt="publicaitons-image" width="30%"></img>
 <img src="./screenshots/booksbuy.png" alt="booksbuy-image" width="30%"></img>
 <img src="./screenshots/scholar.png" alt="scholar-image" width="30%"></img>
 <img src="./screenshots/books.png" alt="books-image" width="30%"></img>
 <img src="./screenshots/footer.png" alt="footer-image" width="30%"></img>
</div>



### ``` Database area```Websites,Research_Scholars, Invited_Lectures, Projects, Awards, Presentation, Articles_In_Journals, Chapters_In_Edited_Books, Books, Periodicals
> The Databse to control all the Tables from adding usrs to creating BadanBarman.

>```Websites``` --- It is the table that shows the websites created by BadanBarman.
>```Research_Scholars``` --- It is the table that shows the Research_Scholars under BadanBarman.
>```Invited_Lectures``` --- It is the table that shows the Invited_Lectures attended by BadanBarman.
>```Projects``` --- It is the table that shows the Projects completed by BadanBarman.
>```Awards``` --- It is the table that shows the Awards achived by BadanBarman.
>```Presentation``` --- It is the table that shows the Presentation created by BadanBarman.
>```Articles_In_Journals``` --- It is the table that shows the Articles_In_Journals created by BadanBarman.
>```Chapters_In_Edited_Books``` --- It is the table that shows the Chapters_In_Edited_Books created by BadanBarman.
>```Books``` --- It is the table that shows the Books created by BadanBarman.
>```Periodicals``` --- It is the table that shows the Periodicals created by BadanBarman.



_______________________________________________________________________________________________________________________________________________________________________
## Acknowledgments
 Many diificulties faced during the projects were tackled thanks to the open source community and stackoverflow.

## See Also

- [`Django Documentation`](https://github.com/noffle/common-readme)
- [`StackOverflow`](https://stackoverflow.com)
- [`GSAP`](https://gsap.com)
- [`Tailwind`](https://tailwindcss.com)

## License

Not Licenced.