# Devon Decks & Dice Board Games Cafe by Tom Cowen


![devon decks & dice responsive screenshot](/docs/images/screenshots/am_i_responsive.png)

This is a full-stack framework project built using Django, Python, HTML and CSS. My goal is to create a functioning and responsive website for an imagined board games cafe. This project has been built for educational purposes.

**[Visit my website](https://devon-decks-n-dice-5055496812fd.herokuapp.com/)**  
  
SUPERUSER CREDENTIALS:  
username - admin  
password - cowchickensheep  
  
These will be needed to access some features of the site.

# Overview

Devon Decks & Dice, is a full stack website for an imagined board games cafe in the imaginary town of Torrington Vale. It encourages user sign up by offering extra features if someone is logged in, such as leaving comments on events (with full CRUD functionality), registering interest in said events, booking tables at the cafe and viewing the cafe's current board game library. It also offers the site admin a feature to search for new games using the board game geek website's API then using it to populate DD&D's own board games database, displaying the game automatically in the site's games library.

# Table of Contents

1. [UX](#ux)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Site Features](#site-features)
    - [Future Features](#future-features)

3. [Wireframes](#wireframes)

4. [Database schema](#database-schema)

5. [Structure](#structure)
    - [Models](#models)

6. [Surface](#surface)
    - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Fonts](#fonts)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)


# UX

Starting with strategy, guided by core UX principles, I considered the target audience and the features that would benefit them.

The target audience for Devon Decks & Dice are:

- trendy young adults and professionals looking to socialise in a different way.
- families who want to spend time together at the weekends.
- anyone who likes playing board games!

The users will be looking for:

- An informative, intuitive website with information that is easy to find.
- The ability to sign up to interact with site content.
- the ability to book a table at the cafe.
- the ability to comment and register interest in upcoming events.
- the ability to see an up to date list of board games available to play at the cafe.

The site admin will be looking for:

- an easy and intuitive way of managing content on the website.
- an easy way to keep the board games library up to date.


## User Stories

**Epic: Admin**

- As a Site Admin, I will be able to manage table bookings.
- As a Site Admin, I can search for games I want to add to the games library using the board games geek API. The games I choose will automatically populate the games library.
- As a Site Admin, I can create, read, update and delete events so that I can manage my events calendar.
- As a Site Admin, I can manage games available at the cafe in the games library.
- As a Site Admin, I can create draft events so that I can finish writing the content later.
- As a Site Admin, I can approve or disapprove comments so that I can filter out objectionable comments.
- As a Site Admin, I can review suggested games so I can decide whether to add them to the games library or not.


**Epic: User Interaction**

- As a Site User, I can make a table booking request.
- As a Site User / Admin I can view comments on an individual event so that I can read the conversation.
- As a Site User I can modify or delete my comment on an event so that I can be involved in the conversation.


**Epic: Navigation**

- As a Site User, I can view a paginated list of events so that I can select which event to view.
- As a Site User, I can click on an event from the events page and view it in more detail.
- As a Site User, I will see a home page so I will know what services are offered on the site and at the Cafe.
- As a Site User, I can see what games are available to play at the Cafe so I can see if there is one I want to play.


**Epic: Login/Register**

- As a Site User, I can register an account so that I can comment on an event, create a profile and suggest games for the library.
- As a Site User, I can log in/out off my account if I wish so that I can connect or disconnect from the website.
- As a Site User, I can create a custom profile so that I can display information about myself and games I like.


![ddnd project board](/docs/images/screenshots/kanban.png)
*Project kanban board*

#
# Scope

## **Site Features**

1. **Navigation Bar**
- The navigation bar appears on every page so users can easily navigate through the site. It adds an active class to the current url for better UX.
- Navigation bar has links for "Home", "Book a Table", "Events", "Games Library" and 'Account'. An 'Add Games to Library" link will be shown to super users from the "Games Library" dropdown. 
- If the user is logged in then their username will appear on the right hand side of the nav bar and the dropdown will show a link to log out.
- If the user is not logged in then they will see "Account" with a dropdown offering sign up and log in links.
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size.

![Navbar when logged out](/docs/images/screenshots/navbar_loggedout.png)

![Navbar when admin logged in](/docs/images/screenshots/navbar_admin.png)

2. **Footer**
The footer, present on all pages, comprises of copyright information on the left hand side, and social links on the right. On smaller screens, the copyright information is hidden.

![footer](/docs/images/screenshots/footer.png)

3. **Landing Page**
The landing page offers a background image of the cafe (generated by AI), a call to action with a short description of the website and some of it's features and also opening hours for the Cafe. A message appears below the navbar to confirm a successful login attempt.

![landing page](/docs/images/screenshots/landing.png)

4. **Book a Table Page**
The booking page will show a booking form to logged in users and a request to log in if the user is unregistered or not logged in. The form invites the user to book a table using their user name. It asks for an email address, offers a choice of party size, session length, date and time and will provide clear feedback in the shape of messages below the nav bar if the booking form has not been filled out correctly. The user will then be assigned the smallest available table in the cafe that meets their party size requirement. This can only be seen from the admin panel however, so when the customer turns up for their booking, the cafe staff will know which table they have assigned to them. Double booking and booking over capacity is not possible. The admin can amend tables available in the admin panel.

![booking page](/docs/images/screenshots/booking.png)

5. **Events Page**
The Events page provides a paginated list of upcoming events. It provides an image of the event along with a title, an excerpt, the time and date and the number of people attending. I have used banners with transparent backgrounds in the styling for improved UX. The example events have been generated using AI, including the images.

![event listings page](/docs/images/screenshots/event_list.png)

When the user clicks on the event they are interested in, they see a more detailed version of the event with a full description. They can leave comments, update or delete them and register their attendance at the event. When commenting, confirmation messages or error messages are provided under the navbar for improved UX.

![event detail head of page](/docs/images/screenshots/event_detail_head.png)

![event detail foot of page](/docs/images/screenshots/event_detail_foot.png)

6. **Games Library**
The Games Library provides a list of all the available board games at the cafe in alphabetical order along with all the information they might need about the game to make their choice. The list is paginated with 6 items per page. They are also invited to get in touch to suggest new games. The data is provided from the sites Board Games database, though generated using the Board Games Geek API, more on that on the page below.

![games library](/docs/images/screenshots/library.png)

7. **Add Games to Library**
The site admin has an extra feature on the website. This page is not available to regular users. On this page, there is a search bar which will fetch data from the Board Games Geek database. the data is returned and parsed before being displayed on the page. While the admin is waiting for the results to load, there is a message explaining that the data is being fetched, this has been implemented as it can take a while for the data to be returned, this way the admin knows that the results are on their way. I have used JavaScript to add loading dots to the message.

![game search loading message](/docs/images/screenshots/fetch_message.png)

Once the results are returned, the admin has the option of adding the chosen game to the sites own Board Games database, where it is automatically displayed in the Games Library. If the searched game is already in the library, it will say so below the returned search result.

![game search results](/docs/images/screenshots/search_results.png)

8. **Register Page**
- The register page allows users to create a new account by providing necessary information such as username, email, password. It is generated by allauth and styled using crispy forms. There is some custom text welcoming the user back to the site.

![sign up page](/docs/images/screenshots/signup.png)

9. **Login Page**
- The Login page allows users to log in. It is also generated by allauth and styled using crispy forms.

![sign in page](/docs/images/screenshots/signin.png)

10. **Logout Page**
- The Login page asks users to confirm they wish to log out. It is also generated by allauth and styled using crispy forms.

![sign out page](/docs/images/screenshots/signout.png)


## **Future Features**

In the wireframes and user stories I had planned for the users to have a profile page where they could write about themselves, upload an avatar, view the events they have said they will attend, list their top 5 games available at the cafe and view, update or delete any future bookings.

I had also planned to include a form in the Game Library, allowing users to suggest new games for the cafe.

I would also like to add a custom 404 page.

I ran out of time to implement these features, but they could be implemented in a future deployment of the site.


# **Wireframes**

Wireframes were created immediately after the project's inception along with the entity relationship diagrams. Although the structure of the site has changed and evolved to a degree, a lot of the layout of the site was based as closely as possilbe on these images.

Please note, there is no wireframe for the game search page. This is because initially, I thought this page would be too difficult to implement in the time that I had to build the site. I later changed my mind on this and went ahead with the page.

All wireframes were created using [Balsamiq](https://balsamiq.com/).

![landing page wireframe](/docs/images/wireframes/wireframes_3.png)
*The landing page*

![table booking wireframe](/docs/images/wireframes/wireframes_5.png)
*The book a table page*

![event listings wireframe](/docs/images/wireframes/wireframes_1.png)
*The event listings page*

![event detail wireframe](/docs/images/wireframes/wireframes_2.png)
*The event detail page*

![games library wireframe](/docs/images/wireframes/wireframes_7.png)
*The games library page*

![user profile wireframe](/docs/images/wireframes/wireframes_6.png)
*The un-implemented user profile page - see future features*

![sign up wireframe](/docs/images/wireframes/wireframes_8.png)
*The sign up page*

![log in wireframe](/docs/images/wireframes/wireframes_4.png)
*The log in page*


# **Database Schema**

Before I set to migrating any models to my database, I created an entity relationship diagram to help me see how the models would link together. I didn't end up using the user profile model in the end as this wasn't implemented in the current version of the website and is down as a future feature.

I also hadn't planned on using the Board Games Geek API initially so the board game diagram doesn't show the bgg_id field.

The entity relationship diagrams were created using [Lucidchart](https://www.lucidchart.com/).

<p align="center">
<img src="/docs/images/wireframes/erdiagrams.jpeg" width="600" height="100%">
</p>


# **Structure**

As the Devon Decks & Dice website is mainly targeted towards customers who intend on coming to the actual cafe, I kept the the structure simple and intuitive with the intention of users being able to quickly and easily access the services they require. I also wanted it to be as easy as possible for the site admin to maintain the website and update the Board Games library.

The website is made from three apps:

- bookings - for the table booking page.
- events - for the events list and event detail pages.
- library - to display the board games library and provide an easy way for the admin to add games to the library.

## **Models**

### **Event Model**

Both the event and the comment models were influenced by the Code Institute, I think therefore I blog walkthrough project.

<p align="center">
<img src="/docs/images/screenshots/event_model.png" width="600" height="100%">
</p>

### **Comment Model**

<p align="center">
<img src="/docs/images/screenshots/comment_model.png" width="600" height="100%">
</p>

### **Booking Model**

The booking model was my most complex model and had to contain various methods to validate the data being submitted by the user. This was done in order to display detailed error messages using the django messages framework, for better UX.

There are five error messages built into the model for if:

- The user tries tries to book a table, but all tables have been assigned and the cafe is fully booked.
- The user tries to book in the past.
- The user tries to book a 4 hour time slot after 6pm, as the cafe closes at 10pm.
- The user tries to book on a Monday as the cafe is closed.
- The user tries to book on a Tuesday as the cafe is closed.

When building the model I tried to add a sixth error message for if the user has already booked a table on the selected date, but encountered an issue with the model searching for a primary key for the booking that had not yet been created. In the end I added this feature to the view instead.

<p align="center">
<img src="/docs/images/screenshots/booking_choices.png" width="600" height="100%">
</p>

<p align="center">
<img src="/docs/images/screenshots/booking_model.png" width="600" height="100%">
</p>

### **Table Model**

The table model was designed to prevent double booking or overbooking at the cafe by assigning each table in the cafe a unique identifier along with a capacity. This way, once a table is assigned to a booking, it cannot be assigned to another booking on the same date at the same time.

<p align="center">
<img src="/docs/images/screenshots/table_model.png" width="600" height="100%">
</p>

### **BoardGame Model**

The board game model has been designed with fields to match those found in the Board Games Geek database in order to make populating and displaying games in the library easier for the site admin.

<p align="center">
<img src="/docs/images/screenshots/boardgame_model.png" width="600" height="100%">
</p>

# **Surface**

## **Design**

I wanted the website to have a clean and functional design. I didn't want to overcomplicate any of the pages. I wanted the role and function of each page to be clear and intuitive to the user so I kept the design as simple as possible.

## **Colour Scheme**

The colour scheme of the website evolved naturally as I was building it. I wanted clean and inviting colours with a good contrast. After a lot of playing around with colour schemes to find one I liked, I ended up with the below.

<p align="center">
<img src="/docs/images/screenshots/colour_scheme.png" width="600" height="100%">
</p>

- **#DD2700** - Used as the navbar background color. It goes nicely with the hero image on the landing page.
- **#FFA552** - This colour was used to highlight and complement the navbar background colour. It is used for active links amongst other things.
- **#FAF9F6** - Used for the background colour of the body. It gives a nice clean look while being easier on the eye than pure white.
- **#381D2A** - This colour was used for text as it provides good contrast with the other colours.
- **#28A745** - The colour I used for buttons and pagination. It is the bootstrap success colour which simplified styling while being a good fit with the rest of the palette.

## **Fonts** 

I chose two custom fonts with free licenses from [Fontfabric](https://www.fontfabric.com/) then added them to the static file.
The fonts I chose were:

- [Gagalin](https://www.fontfabric.com/fonts/gagalin/) - Great for headings and grabbing attention.
- [Aleo](https://www.fontfabric.com/fonts/aleo/) - I chose this font as it fitted nicely with the board games theme, evoking thoughts of books and games.

In the end, I decided against using the Gagalin font as the clarity wasn't very good on smaller screens. I went with the Aleo font for everything although the Gagalin font can still be seen in the static/fonts folder.


# **Technologies Used**

## **Languages**
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

## **Frameworks, Libraries and Programs**

- [GitHub](https://github.com/) - GitHub is a web-based platform for version control using Git, enabling collaborative software development and hosting of code repositories. GitHub connects to GitPod and Heroku.

- [GitPod](https://gitpod.io/workspaces) - Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository.

- [Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilized/tested.

- [Django](https://www.djangoproject.com/) - Django is a high-level web framework for building web applications rapidly with a clean and pragmatic design.

- [ElephantSQL](https://api.elephantsql.com) - ElephantSQL is a hosted PostgreSQL database service that can be seamlessly integrated with Django applications, providing scalable and reliable database solutions.

- [Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

- [Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework for developing responsive and mobile-first websites quickly and efficiently.

- [Cloudinary](https://cloudinary.com) - Cloudinary is a cloud-based media management platform that offers solutions for storing, optimizing, and delivering images and videos for web and mobile applications.

- [Summernote](https://summernote.org/) - Summernote is a Django app that enables users to easily integrate a rich text editor into their web applications, enhancing event creation and description functionality.

- [Django-allauth](https://www.intenct.nl/projects/django-allall/) - A comprehensive authentication app for Django, supporting social authentication, registration, and account management.

- [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Django Crispy Forms is a Django app that provides a better way to generate forms in your Django application.

- [Whitenoise](http://whitenoise.evans.io/en/stable/) - WhiteNoise allows your web app to serve its own static files, making it simpler to deploy on services like Heroku.

- [TinyPNG](https://tinypng.com/) - TinyPNG is a website that offers image compression services to optimize image files for faster loading on webpages while maintaining visual quality.

- [Font Awesome](https://fontawesome.com/) - Font Awesome is a library of scalable vector icons that can be easily customized and used to enhance the visual appeal of websites and applications.

- [Balsamiq](https://balsamiq.com/) - Balsamiq is a wireframing tool used for creating low-fidelity mockups of user interfaces, allowing for quick and easy visualization of design ideas.

- [Lucidchart](https://lucid.app) - Lucidchart is a web-based diagramming tool that allows users to create and collaborate on flowcharts, ERDs, and other visual representations of data and processes.

- [Am I Responsive](http://ami.responsivedesign.is/) - Am I Responsive is a web tool that allows users to quickly preview how their website appears on various devices and screen sizes, helping to ensure responsiveness and compatibility across platforms.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - The W3C CSS Validator is a tool used to check the validity and syntax of CSS code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).

- [W3C Markup Validator](https://validator.w3.org/#validate_by_input) - The W3C Markup Validator is a tool used to check the validity and syntax of HTML code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).

- [JSHint](https://jshint.com/) - JSHint is a static code analysis tool used for checking JavaScript code for errors, potential problems, and stylistic inconsistencies.

- [Pep8ci](https://pep8ci.herokuapp.com/) - Pep8ci provides Python developers with a tool to check their code against the PEP 8 style guide for adherence to coding standards.

- [Lighthouse](https://developer.chrome.com/docs/lighthouse) - Lighthouse is an open-source tool used for auditing web page quality, including performance, accessibility, SEO, and cross-browser testing.

The full list of requirements for the project along with versions can be seen below.
  
asgiref==3.7.2  
cloudinary==1.36.0  
crispy-bootstrap5==0.7  
dj-database-url==0.5.0  
dj3-cloudinary-storage==0.0.6  
Django==4.2.11  
django-allauth==0.57.2  
django-bootstrap-v5==1.0.11  
django-crispy-forms==2.1  
django-summernote==0.8.20.0  
gunicorn==20.1.0  
oauthlib==3.2.2  
psycopg2==2.9.9  
PyJWT==2.8.0  
python3-openid==3.2.0  
requests-oauthlib==1.4.0  
sqlparse==0.4.4  
urllib3==1.26.18  
whitenoise==5.3.0  

# **Testing**

[TESTING.md](TESTING.md)

# **Deployment**

The site was deployed on Heroku and connected to GitHub for version control. This was done by following the below steps:

- Log in to GitHub and create a new repository, using the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template).
- Sign up for Heroku and create a new account.
- Create a new app and choose a suitable region for deployment.
- In the app settings, go to config vars and click "reveal config vars".
- The app requires configuration for the following variables: SECRET_KEY, DATABASE_URL, CLOUDINARY_URL. Assign the corresponding values from your project's env.py to these variables.
- Integrate Heroku with your GitHub by choosing the GitHub integration option in Heroku.
- Locate and select the GitHub repository you created earlier from the CI template.
- Choose manual deployment from the selected branch of your GitHub repository.
- Deploy by clicking the manual deploy button.
- Once deployed, the site is accessible through the live link provided at the top of the document.

# **Credits**

## **Tech Support**

- [W3Schools](https://www.w3schools.com/) - Used to help understanding with certain features.

- [Stack Overflow](https://stackoverflow.com/) - Used to inspire me when trying to picture how to implement certain features.

- [Slack](https://app.slack.com/)

- [ChatGPT](https://openai.com/gpt) - Used to check my code when I had gone code blind looking for bugs.

- [Code Institute](https://codeinstitute.net/) - I think therefore I blog walkthrough project inspired the events page on my site. I have also learned everything I needed to build this site whilst undertaking the 16 week Full Stack skills bootcamp over the last 4 months.

## **API**

- [Board Games Geek API](https://boardgamegeek.com/wiki/page/BGG_XML_API2) - I used the BGG API for one of the sites main features.

- [Taylor A. Liss](https://www.tayloraliss.com/bggapi/) - It was after reading Taylor's how to guide for the BGG API that I decided it wasn't out of my reach to implement the search feature on my site.

## **Media**

- [Fontfabric](https://www.fontfabric.com/) - I got the fonts for the site from Fontfabric.

- [DALL-E 3](https://openai.com/) - DALL-E 3 was to generate all of the artwork used on the site.

- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) - Photoshop was used to edit some of the artwork on the site.

- [EZgif](https://ezgif.com/) - EZ gif was used to resize the gifs I have used on the testing page.

- [ShareX](https://getsharex.com/) - I used ShareX to take screen recordings to demonstrate responsivity of pages on the site for testing purposes.

### **Acknowledgements**

- Thanks to everyone in my cohort for supporting me through the bootcamp!
- Thanks to my friend Jonathan for helping me think through certain features and user-testing the site for me upon completion.