# Testing for Wine O'Clock

![Found in Translation site shown on multiple screen sizes](static/images/site-responsive.png)

Visit the deployed site: [Found in Translation](https://foundintranslationsodaci.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [JavaScript Validator](#JavaScript-Validator)
  * [Python Validator](#Python-Validator)
  * [Lighthouse](#Lighthouse)
* [MANUAL TESTING](#MANUAL-TESTING)
  * [Testing User Stories](#Testing-User-Stories)
  * [Full Testing](#Full-Testing)

Through out the entire building of the application Wine O'Clock functions where being tested. Mainly by opening the page in the Web browser Chrome but also by using the inspect tool and reading from the console. 

---------------
Each page has been inspected using google chrome developer tools & Firefox inspector tool to ensure that each page is fully responsive on a variety of different screen sizes and devices. We have also physically tested the responsiveness of the site on a number of different devices.
---------------------------
- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.


* [Index Page W3C HTML Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffoundintranslationsodaci.herokuapp.com%2F) - Pass

* [Login Page W3C HTML Validation](documentation/testing/login-user.png) - Pass
* [Register Page W3C HTML Validation]
* [Log out Page W3C HTML Validation](documentation/testing/admin-validation.png) - Pass

* [All products Page W3C HTML Validation](documentation/testing/admin-validation.png) - Pass
* [Add product Page W3C HTML Validation](documentation/testing/allthreads-validation.png) - Pass
* [Edit product Page W3C HTML Validation](documentation/testing/allthreads-validation.png) - Pass
* [Product details Page W3C HTML Validation](documentation/testing/allthreads-validation.png) - Pass

* [The bag Page W3C HTML Validation](documentation/testing/allthreads-validation.png) - Pass

* [The Checkout Page W3C HTML Validation](documentation/testing/allthreads-validation.png) - Pass
* [Checkout Success Page W3C HTML Validation](documentation/testing/allthreads-validation.png) - Pass

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [dropdown.js](documentation/testing/dropdownjs-validation.png)
* [form_validation.js](documentation/testing/form-validation-js.png)
* [language_codes.js](documentation/testing/language-list-js.png)

- - -

### Python Validator

[PEP8](http://pep8online.com/)was used to validate the python files.

* [translate.py](documentation/testing/translate-validation.png)

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

* Index Page
  ![Index Page lighthouse testing desktop](documentation/lighthouse/index-lh-desk.png)

* Login Page
  ![Login Page Lighthouse testing desktop](documentation/lighthouse/login-lh-desk.png)
  
* Register Page
  ![Sign Up Page Lighthouse testing desktop](documentation/lighthouse/signup-lh-desk.png)
  
* All Products Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* Add Product Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* Edit Product Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* Product Detail Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* The Shoppinng Bag Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* The Checkout Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* The Checkout Success Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

### Mobile Results

* Index Page
  ![Index Page lighthouse testing desktop](documentation/lighthouse/index-lh-desk.png)

* Login Page
  ![Login Page Lighthouse testing desktop](documentation/lighthouse/login-lh-desk.png)
  
* Register Page
  ![Sign Up Page Lighthouse testing desktop](documentation/lighthouse/signup-lh-desk.png)
  
* All Products Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* Add Product Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* Edit Product Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* Product Detail Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* The Shoppinng Bag Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* The Checkout Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

* The Checkout Success Page
  ![All threads page lighthouse testing desktop](documentation/lighthouse/allthreads-lh-desk.png)

- - -

## MANUAL TESTING

### Testing User Stories

`First Time Visitors`

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| As a first time user, I want to easily understand the page I'm on | To achieve good UX the page uses animations to lead the user to the purpose of the site | ![Shop now button](documentation/navbar-desktop.png) |
| As a first time user, I want to easily navigate through out the page | To make a userfriendly page the navbar includes standardized icons | ![Navbar](documentation/navbar-desktop.png) |
| As a first time user, I want to be able to sign up to the site and create a profile | Users can create their own profile for the site by using the sign up page. Links to the sign up page are included on the navbar, and there is also a button to redirect users to the sign up page on the 404 page if they are not logged into an account on the site | ![sign up link](documentation/testing/signup-user.png) |
| As a first time user, I want to be able to being able to save my profile information | Users can choose to save their billing information while making their first purchase | ![sign up link](documentation/testing/signup-user.png) |

`Registered/Returning Visitors`

|  Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| As a returning/registered user, I want to be able to log in to my account | The Navbar has a login link | ![Login user link](documentation/testing/login-user.png) |
| As a returning/registered user, I want to be able to see my history | From the navbar I can access my profile and see my order history | ![Order History](documentation/testing/login-user.png) |
| As a returning/registered user, I want to be able to have products saved in my shopping bag | Users shopping bag is saved in the shopping bag reached from the navbar | ![Order History](documentation/testing/login-user.png) |
| As a returning/registered user, I want to be able to change my billing information | Users can change and add their information under their profile | ![Billing Information](documentation/testing/login-user.png) |
| As a returning/registered user, I want to be able to like a product | Users can like a product on the product dettail | ![Like](documentation/testing/login-user.png) |
| As a returning/registered user, I want to be able to comment a product | Users can comment a product on the product dettail | ![Comment](documentation/testing/login-user.png) |

`Admin User`

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| As an admin user, I want to be able to add a product | Admin can easily add a product when signed in | ![Add product](documentation/testing/login-user.png) |
| As an admin user, I want to be able to edit a product | Admin can easily edit a product when signed in | ![Edit product](documentation/testing/login-user.png) |
| As an admin user, I want to be able to delete a product | Admin can easily delete a product when signed in | ![Delete product](documentation/testing/login-user.png) |

- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 14 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Phone X.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes.  

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Navbar` |
| Site logo | Redirects to the home page | Click logo |  Redirects to home page | Pass |
| Site Name | Redirects to home page | Click site name | Redirects to home page | Pass |
| Home Link | Redirects to home page | Click home link | Redirects to home page | Pass |
| Login Link (user not logged in) | Redirect to Login page | Click log in link | Redirected to log in page | Pass |
| Sign up Link (user not logged in)  | Redirect to Sign up page | Click sign up link | Redirected to sign up page | Pass |
| View all posts link | Redirects the user to the all threads page | Click view all posts link | Redirected to all posts page | Pass |
| Admin View | Redirects to the admin view page | Click admin view link | Redirected to admin view page | Pass |
| Logout link (user logged in) | User will be logged out | Click log out link| Redirected to home page - login link available | Pass |
| `Home Page` |
| View threads button | Redirects to the threads page | Click button | Redirected to the thread | Pass |
| Start a new thread button | Modal popup to create new thread | Click button | New thread modal popped up | Pass |
| `Login Page` |
| Form - link to sign up page | Redirects user to sign in page | Click link | Redirected to sign up page | Pass |
| Form - Submission with no information | User prompted to fill in information | clicked submit button with no fields filled out | Form highlighted first empty field | Pass |
| `Signup Page` |
| Form - Submission with no information | User prompted to fill in information | clicked submit button with no fields filled out | Form highlighted first empty field | Pass |
| `New Post Page` |
| --- | --- | --- | --- | --- |
| `New Thread Page` |
| --- | --- | --- | --- | --- |
| `Threads Page` |
| --- | --- | --- | --- | --- |
| `Admin Posts Page` |
| --- | --- | --- | --- | --- |
| `Privacy Policy Page` |
| Link to Terms & Conditions Page | Redirects user to the Terms & Conditions page | Click link | Redirected to the terms & conditions page | Pass |
| Get Safe Online link | Redirects the user to the get safe online website in a new browser tab | Click link | site opens, but in same browser tab | Fail |
| Link to Rocket Lawyer site in Attribution section | User is taken to the Rocket Lawyer site in a new browser tab | Click link | Rocket Lawyer site opens, but in same tab | Fail |
| `Terms and Conditions Page` |
| Link to Rocket Lawyer site in Attribution section | User is taken to the Rocket Lawyer site in a new browser tab | Click link | 404 page opens | Fail |
| `404 Page` |
| (User Logged in) Home Button | User will be redirected to the home page | Click home button | Redirected to the home page | Pass |
| (Guest User) Login Button | User redirected to the login page | Click login button | Redirected to the login page | Pass |
| (Guest User) Sign Up Button | User redirected to the sign up page | Click sign up button | Redirected to sign up page | Pass |
| `Footer` |
| Footer - Join now button | Redirects user to the sign up page | Click button | Redirected to sign up page | Pass |
| Footer - Social media links | Opens new tab to the social media site | Clicked each icon | New tabs opened for each site | Pass |
| Footer - Privacy Policy link | Redirects to the privacy policy page | Clicked link | Redirected to privacy policy page | Pass |
| footer - Terms and conditions link | Redirects to the terms and conditions page | Clicked link | Redirected to terms and conditions page | Pass |

Back to [README.md](README.md)
