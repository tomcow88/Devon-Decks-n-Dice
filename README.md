<h1 align="center">Devon Decks & Dice Board Games Cafe by Tom Cowen</h1>

<p align="center">
<img src="/static/images_readme/screenshots/multi-screen-screenshot.png" width="600" height="100%">
</p>

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
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)

4. [Wireframes](#wireframes)

5. [Database schema](#database-schema)

6. [Surface](#surface)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)

#
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

#
# User Stories

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


<p align="center">
<img src="/static/images_readme/screenshots/kanban.png" width="600" height="100%">
</p>

#
# Scope

## **Site Features**

1. **Navigation Bar**
- The navigation bar appears on every page so users can easily navigate through the site. It adds an active class to the current url for better UX.
- Navigation bar has links for "Home", "Book a Table", "Events", "Games Library" and 'Account'. An 'Add Games to Library" link will be shown to super users from the "Games Library" dropdown. 
- If the user is logged in then their username will appear on the right hand side of the nav bar and the dropdown will show a link to log out.
- If the user is not logged in then they will see "Account" with a dropdown offering sign up and log in links.
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size.

<p align="center">
<img src="/static/images_readme/screenshots/navbar_loggedout.png" width="100%" height="100%">
</p>

<p align="center">
<img src="/static/images_readme/screenshots/navbar_admin.png" width="100%" height="100%">
</p>

2. **Footer**
The footer, present on all pages, comprises of copyright information on the left hand side, and social links on the right. On smaller screens, the copyright information is hidden.

<p align="center">
<img src="/static/images_readme/screenshots/footer.png" width="100%" height="100%">
</p>

3. **Landing Page**
The landing page offers a background image of the cafe (generated by AI), a call to action with a short description of the website and some of it's features and also opening hours for the Cafe. A message appears below the navbar to confirm a successful login attempt.

<p align="center">
<img src="/static/images_readme/screenshots/landing.png" width="600" height="100%">
</p>

4. **Book a Table Page**
The booking page will show a booking form to logged in users and a request to log in if the user is unregistered or not logged in. The form invites the user to book a table using their user name. It asks for an email address, offers a choice of party size, session length, date and time and will provide clear feedback in the shape of messages below the nav bar if the booking form has not been filled out correctly. The user will then be assigned the smallest available table in the cafe that meets their party size requirement. This can only be seen from the admin panel however, so when the customer turns up for their booking, the cafe staff will know which table they have assigned to them. Double booking and booking over capacity is not possible. The admin can amend tables available in the admin panel.

<p align="center">
<img src="/static/images_readme/screenshots/booking.png" width="600" height="100%">
</p>

5. **Events Page**
The Events page provides a paginated list of upcoming events. It provides an image of the event along with a title, an excerpt, the time and date and the number of people attending. I have used banners with transparent backgrounds in the styling for improved UX. The example events have been generated using AI, including the images.

<p align="center">
<img src="/static/images_readme/screenshots/event_list.png" width="600" height="100%">
</p>

When the user clicks on the event they are interested in, they see a more detailed version of the event with a full description. They can leave comments, update or delete them and register their attendance at the event. When commenting, confirmation messages or error messages are provided under the navbar for improved UX.

<p align="center">
<img src="/static/images_readme/screenshots/event_detail_head.png" width="600" height="100%">
</p>

<p align="center">
<img src="/static/images_readme/screenshots/event_detail_foot.png" width="600" height="100%">
</p>

6. **Games Library**
The Games Library provides a list of all the available board games at the cafe in alphabetical order along with all the information they might need about the game to make their choice. The list is paginated with 6 items per page. They are also invited to get in touch to suggest new games. The data is provided from the sites Board Games database, though generated using the Board Games Geek API, more on that on the page below.

<p align="center">
<img src="/static/images_readme/screenshots/library.png" width="600" height="100%">
</p>

7. **Add Games to Library**
The site admin has an extra feature on the website. This page is not available to regular users. On this page, there is a search bar which will fetch data from the Board Games Geek database. the data is returned and parsed before being displayed on the page. While the admin is waiting for the results to load, there is a message explaining that the data is being fetched, this has been implemented as it can take a while for the data to be returned, this way the admin knows that the results are on their way. I have used JavaScript to add loading dots to the message.

<p align="center">
<img src="/static/images_readme/screenshots/fetch_message.png" width="600" height="100%">
</p>

Once the results are returned, the admin has the option of adding the chosen game to the sites own Board Games database, where it is automatically displayed in the Games Library. If the searched game is already in the library, it will say so below the returned search result.

<p align="center">
<img src="/static/images_readme/screenshots/search_results.png" width="600" height="100%">
</p>

8. **Register Page**
- The register page allows users to create a new account by providing necessary information such as username, email, password. It is generated by allauth and styled using crispy forms. There is some custom text welcoming the user back to the site.

<p align="center">
<img src="/static/images_readme/screenshots/signup.png" width="600" height="100%">
</p>

9. **Login Page**
- The Login page allows users to log in. It is also generated by allauth and styled using crispy forms.

<p align="center">
<img src="/static/images_readme/screenshots/signin.png" width="600" height="100%">
</p>

10. **Logout Page**
- The Login page asks users to confirm they wish to log out. It is also generated by allauth and styled using crispy forms.

<p align="center">
<img src="/static/images_readme/screenshots/signout.png" width="600" height="100%">
</p>


## **Future Features**

In the wireframes and user stories I had planned for the users to have a profile page where they could write about themselves, upload an avatar, view the events they have said they will attend, list their top 5 games available at the cafe and view, update or delete any future bookings.

I had also planned to include a form in the Game Library, allowing users to suggest new games for the cafe.

I would also like to add a custom 404 page.

I ran out of time to implement these features, but they could be implemented in a future deployment of the site.

### **Structure**

As the Devon Decks & Dice website is mainly targeted towards customers who intend on coming to the actual cafe, I kept the the structure simple and intuitive with the intention of users being able to quickly and easily access the services they require. I also wanted it to be as easy as possible for the site admin to maintain the website and update the Board Games library.

The website is made from three apps:

- bookings - for the table booking page.
- events - for the events list and event detail pages.
- library - to display the board games library and provide an easy way for the admin to add games to the library.

### **Wireframes**

Wireframes were created immediately after the project's inception along with the entity relationship diagrams. Although the structure of the site has changed and evolved to a degree, a lot of the layout of the site was based as closely as possilbe on these images.

All wireframes were created using [Balsamiq](https://balsamiq.com/)

<p>
<img src="/static/images_readme/wireframes/wireframes_1.jpeg" width="600" height="100%">
</p>

<p>
<img src="/static/images_readme/wireframes/wireframes_2.jpeg" width="600" height="100%">
</p>

<p>
<img src="/static/images_readme/wireframes/wireframes_3.jpeg" width="600" height="100%">
</p>

<p>
<img src="/static/images_readme/wireframes/wireframes_4.jpeg" width="600" height="100%">
</p>

<p>
<img src="/static/images_readme/wireframes/wireframes_5.jpeg" width="600" height="100%">
</p>

<p>
<img src="/static/images_readme/wireframes/wireframes_6.jpeg" width="600" height="100%">
</p>

<p>
<img src="/static/images_readme/wireframes/wireframes_7.jpeg" width="600" height="100%">
</p>

<p>
<img src="/static/images_readme/wireframes/wireframes_8.jpeg" width="600" height="100%">
</p>

### **Database Schema**

Before I set to migrating any models to my database, I created an entity relationship diagram to help me see how the models would link together. I didn't end up using the user profile model in the end as this wasn't implemented in the current version of the website and is down as a future feature.

I also hadn't planned on using the Board Games Geek API initially so the board game diagram doesn't show the bgg_id field.

<p align="center">
<img src="/static/images_readme/wireframes/erdiagrams.jpeg" width="600" height="100%">
</p>

### **Models**

# **Event Model**

Both the event and the comment models were influenced by the Code Institute, I think therefore I blog walkthrough project.

<p align="center">
<img src="/static/images_readme/screenshots/event_model.png" width="600" height="100%">
</p>

# **Comment Model**

<p align="center">
<img src="/static/images_readme/screenshots/comment_model.png" width="600" height="100%">
</p>

# **Booking Model**

The booking model was my most complex model and had to contain various methods to validate the data being submitted by the user. This was done in order to display detailed error messages using the django messages framework, for better UX.

There are five error messages built into the model for if:

- The user tries tries to book a table, but all tables have been assigned and the cafe is fully booked.
- The user tries to book in the past.
- The user tries to book a 4 hour time slot after 6pm, as the cafe closes at 10pm.
- The user tries to book on a Monday as the cafe is closed.
- The user tries to book on a Tuesday as the cafe is closed.

When building the model I tried to add a sixth error message for if the user has already booked a table on the selected date, but encountered an issue with the model searching for a primary key for the booking that had not yet been created. In the end I added this feature to the view instead.

<p align="center">
<img src="/static/images_readme/screenshots/booking_choices.png" width="600" height="100%">
</p>

<p align="center">
<img src="/static/images_readme/screenshots/booking_model.png" width="600" height="100%">
</p>

# **Table Model**

The table model was designed to prevent double booking or overbooking at the cafe by assigning each table in the cafe a unique identifier along with a capacity. This way, once a table is assigned to a booking, it cannot be assigned to another booking on the same date at the same time.

<p align="center">
<img src="/static/images_readme/screenshots/table_model.png" width="600" height="100%">
</p>

# **BoardGame Model**

The board game model has been designed with fields to match those found in the Board Games Geek database in order to make populating and displaying games in the library easier for the site admin.

<p align="center">
<img src="/static/images_readme/screenshots/boardgame_model.png" width="600" height="100%">
</p>