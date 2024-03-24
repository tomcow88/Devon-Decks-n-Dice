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

# Manual Testing



