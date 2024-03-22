<h1 align="center">Devon Decks & Dice Board Games Cafe by Tom Cowen</h1>

<p align="center">
<img src="/static/screenshots/images_readme/multi-screen-screenshot.png" width="600" height="100%">
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

## **Features**

### **Home Page**

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
   - The footer, present on all pages, comprises of copyright information on the left hand side, and social links on the right. On smaller screens, the copyright information is hidden.

<p align="center">
<img src="/static/images_readme/screenshots/footer.png" width="100%" height="100%">
</p>

3. **Landing Page**
   - The landing page offers a background image of the cafe (generated by AI), a call to action with a short description of the website and some of it's features and also opening hours for the Cafe.

