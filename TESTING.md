# **Testing**

This is the TESTING file for the [Devon Decks & Dice Website](https://devon-decks-n-dice-5055496812fd.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## **Testing Contents**
  
- [Testing](#testing)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Lighthouse Scores](#lighthouse-scores)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Site Responsivity](#site-responsivity)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)

## **Validation**

### HTML Validation

To validate my HTML code, I used the [HTML W3C Validator](https://validator.w3.org).

As every page on the site has been rendered using Jinja syntax, the validator would throw up errors if I tried to validate it using the page's URL. For this reason, from the deployed site, I had to directly input the code rendered on each page by right clicking and viewing page source.

The only page that threw up an error was the landing page, see below:

![HTML validation error for landing page](/docs/testing/validation/HTML_validation_error.png)

Once I had resolved the issues on the list, validation passed on every page. I will address the error fixes in the [bugs](#bugs) section below.
I was given the all clear for every page with 'No errors or warnings to show', as seen here.

![HTML validation pass](/docs/testing/validation/HTML_validation.png)

---

### CSS Validation

I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate my custom CSS file. I did not test bootstrap CSS.
The result came back with no errors found as can be seen here.

![CSS validation pass](/docs/testing/validation/CSS_validation.png)

---

### Javascript Validation

To test my javascript, I used [JSHint](https://jshint.com/). In spite of some advisory warnings about syntax available in ES6 being displayed, the code passed with no errors as seen below.

![comments.js file validation](/docs/testing/validation/comments_js_validation.png)
*JS file for comments on events*

![gamesearch.js file validation](/docs/testing/validation/gamesearch_js_validation.png)
*JS file for the game search page*

---

### Python Validation

I used the [CI Python Linter](https://pep8ci.herokuapp.com/#) to validate my python code and make sure it was pep8 compliant. The majority of my python code needed tweaking to make it compliant and my results are in the below table.

| App/directory | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| bookings | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant |
| ddnd  | na | na | na | :white_check_mark: compliant | na |
| events | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant |
| library | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant | :white_check_mark: compliant | :x: not compliant |

In the table above, it is seen that the library app's views.py is not pep8 compliant. This is because there were seven lines of code that I couldn't write in 79 characters or under. When I tried I broke the code and would need more time to figure out how to refactor the code to make it pep8 compliant. I to leave it as it is for the moment as for the purposes of this project, working code is more impotant to me that pep8 compliance.

Here is the library views.py result:

![Linter result for library views.py](/docs/testing/validation/search_view_linter.png)

And here is what happened when I tried to contract the code:

![Broken game search page](/docs/testing/bugs/search_view_bug.png)

Here is an example of the feedback I received for the rest of the tests:

![Pep8 compliant result](/docs/testing/validation/pep8_compliant.png)

---

### Lighthouse Scores

Lighthouse testing was carried out in Google Chrome incognito mode for best results. The results are listed below. The lowest scores come in for performace on the pages where I have used large images. Despite running the images through [TinyPNG](https://tinypng.com/), they could still be reduced in size for better performance and given more time, this is something I would do. The results are all well within acceptable limits.

---

![lighthouse score for the landing page](/docs/testing/validation/lighthouse_landing.png)  
*The Landing Page*

---

![lighthouse score for the bookings page](/docs/testing/validation/lighthouse_bookings.png)  
*The Bookings Page*

---

![lighthouse score for the event listings page](/docs/testing/validation/lighthouse_eventlist.png)  
*The Event Listings Page*

---

![lighthouse score for the event details page](/docs/testing/validation/lighthouse_eventdetail.png)  
*The Event Details Page*

---

![lighthouse score for the games library page](/docs/testing/validation/lighthouse_library.png)  
*The Games Library Page*

---

![lighthouse score for the games search page](/docs/testing/validation/lighthouse_gamesearch.png)  
*The Games Search Page*

---

## **Manual Testing**

### Functional Testing

| Page | Feature | Tested? | Input Required | User Feedback Provided | Pass/Fail | Fix |
|---------|----------|----------|-----------|---------|----------|-----------|
| Landing | Navbar logo and icons | yes | click | Logo takes the user home, and the icons take the user to the indicated site locations. Nav links have the active class assigned to them. | :white_check_mark: pass | - |
| Landing | Footer icons | yes | click | Icons take the user to the indicated social links in a new window. | :white_check_mark: pass | - |
| Landing | Sign up link in hero text. | yes | click | Link takes the user to the sign up page if unregistered and will do nothing if the user is already logged in. | :white_check_mark: pass | User could be given a message saying that they are already logged in. - Future feature |
| Book a Table | Log in link | yes | click | If logged out, the user will be prompted to log in so that they can use the booking form. link takes user to the log in page. | :white_check_mark: pass | - |
| Book a Table | Form Submit | yes | text input / click | If the email field or start time field are left blank or filled out incorrectly on the form, the user is prompted to fill them out or fill them out correctly. When the user has filled out the form correctly they will click submit to submit the form. | :white_check_mark: pass | - |
| Book a Table | Success/Error messages | yes | text input | If the user successfully submits the form, they receive feedback in the form of a message below the header. There are six possible messages - all have been successfully displayed. | :white_check_mark: pass | - |
| Event Listings | Pagination next | yes | click | Another six events are displayed to the user. | :white_check_mark: pass | - |
| Event Listings | Pagination previous | yes | click | The previous six events are displayed to the user and the pagination bar indicates the page number. | :white_check_mark: pass | - |
| Event Listings | Pagination page number | yes | click | The six events assigned on a specific page are displayed to the user and the pagination bar indicates the page number. | :white_check_mark: pass | - |
| Event Listings | View an event in more detail | yes | click | If the user clicks on an event, they will be able to view it in more detail. | :white_check_mark: pass | - |
| Event Details | Register interest in attending an event | yes | click on 'I'll be there!' button. | The number attending increases and the 'I can't attend' button is displayed.  | :white_check_mark: pass | - |
| Event Details | Revoke interest in attending an event | yes | click on 'I can't attend' button. | The number attending decreases and the 'I'll be there!' button is displayed.  | :white_check_mark: pass | - |
| Event Details | Submit a comment | yes | text input and click. | The comment is displayed in the comments section with the option to edit it or delete it.  | :white_check_mark: pass | - |
| Event Details | Edit a comment | yes | click | The user's comment appears in the leave a comment text field and the update button is displayed.  | :white_check_mark: pass | - |
| Event Details | Delete a comment | yes | click | A modal is displayed to the user confirming they wish to delete their comment. Close and Delete buttons are displayed. | :white_check_mark: pass | - |
| Event Details | Delete comment modal | yes | click | If the user clicks the delete button, the modal disappears and their comment is no longer displayed. If they click close then the modal disappears and their comment is still visible. | :white_check_mark: pass | - |
| Games Library | View game description | yes | scroll | The user is able to continue reading the game description by scrolling down through its test box. | :white_check_mark: pass | - |
| Games Library | Pagination next | yes | click | Another six entries are displayed to the user. | :white_check_mark: pass | - |
| Games Library | Pagination previous | yes | click | The previous six events are displayed to the user and the pagination bar indicates the page number. | :white_check_mark: pass | - |
| Games Library | Pagination page number | yes | click | The six events assigned on a specific page are displayed to the user and the pagination bar indicates the page number. | :white_check_mark: pass | - |
| Add to Games Library | Search Games | yes | text input | Upon submitting a search, a wait message is displayed to the user before the search results are returned. The results either have an 'Add to Library' button or an 'Added to Library message below them.  | :white_check_mark: pass | - |
| Add to Games Library | Add Game to Library | yes | click | A user clicks on the game of choice from the search results and its details are added to the Games Library. The user is taken back to an empty search page. | :white_check_mark: pass | - |
| Sign Up | Sign Up Form | yes | text input | If the user fills out the form incorrectly, they are prompted on how to fix it. Once the form is successfully submitted, the user is returned to the landing page and a success message is displayed. | :white_check_mark: pass | - |
| Sign In | Sign In Form | yes | text input | If the user fills in their details incorrectly, an error message is displayed. If they fill in their details correctly and click sign in, they are returned to the landing page and a success message is displayed. Their username is also displayed on the right of the navbar if not collapsed. | :white_check_mark: pass | - |
| Log Out | Log Out | yes | click | If the user clicks sign out, they are signed out, returned to the landing page and an succes message is displayed. | :white_check_mark: pass | - |