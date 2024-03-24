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