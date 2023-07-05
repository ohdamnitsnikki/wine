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
| Site Name | Redirects to home page | Click site name | Redirects to home page | Pass |
| My Account | Show dropdown menu for login and register | Click my account | Show dropdown menu for login and register | Pass |
| My Account (as a logged in user) | Show dropdown menu for my profile and logout | Click my account | Show dropdown menu for my profile and logout | Pass |
| My Account (as a logged in admin) | Show dropdown menu for login,register and product management | Click my account | Show dropdown menu for login,register and product management | Pass |
| Shopping Bag | Redirects to bag page | Click site name | Redirects to bag page | Pass |
| Searchbar | Give option to write in the textfield | Click searchbar | Give option to write in the textfield | Pass |
| All Products | Show dropdown menu for all products | Click all producst | Show dropdown menu for all products | Pass |
| Region | Show dropdown menu for region | Click region | Show dropdown menu for region | Pass |
| Colour | Show dropdown menu for colour | Click colour | Show dropdown menu for colour | Pass |
| Pairings | Show dropdown menu for pairings | Click pairings | Show dropdown menu for pairings | Pass |
| `Home Page` |
| Shop now button | Redirects to all product page | Click button | Redirects to all product page | Pass |
| `Login Page` |
| Sign Up link | Redirects user to sign up page | Click link | Redirected to sign up page | Pass |
| Input field for username | Activates text area | Click textfield | Activates text area | Pass |
| Input field for password | Activates text area | Click textfield | Activates text area | Pass |
| Radio button for remeber me | Fills in button | Click radio button | Fills in button | Pass |
| Home button | Redirects user to home page | Click link | Redirected to sign home page | Pass |
| Sign in button | Redirects user to home page | Click link | Redirected to home page | Pass |
| Forgot password link | Redirects user to reset password page | Click link | Redirects user to reset password page | Pass |
| `Register Page` |
| Sign in link | Redirects user to sign in page | Click link | Redirects user to sign in page | Pass |
| Input field for email address | Activates text area | Click textfield | Activates text area | Pass |
| Input field for email confirmation | Activates text area | Click textfield | Activates text area | Pass |
| Input field for username | Activates text area | Click textfield | Activates text area | Pass |
| Input field for password | Activates text area | Click textfield | Activates text area | Pass |
| Input field for password confirmation | Activates text area | Click textfield | Activates text area | Pass |
| Back to login button | Redirect user to sign in page | Click button | Redirect user to sign in page | Pass |
| Sign up button | Redirects user to home page | Click button | Redirects user to home page | Pass |
| `Logout page` |
| Cancel button | Redirect user to home page | Click button | Redirect user to home page | Pass |
| Sign out button | Redirects user to home page | Click button | Redirects user to home page | Pass |
| `My profile Page` |
| Input field for Phone number | Activates text area | Click textfield | Activates text area | Pass |
| Input field for address 1 | Activates text area | Click textfield | Activates text area | Pass |
| Input field for address 2 | Activates text area | Click textfield | Activates text area | Pass |
| Input field for Town | Activates text area | Click textfield | Activates text area | Pass |
| Input field for Conty, State, Locality | Activates text area | Click textfield | Activates text area | Pass |
| Input field for Postal Code | Activates text area | Click textfield | Activates text area | Pass |
| Input field for Country| Activates text area | Click textfield | Activates text area | Pass |
| Update Information button | Update users information | Click button | Update users information | Pass |
| `Product Management` |
| Dropdown menu for Category | Shows menu | Click menu | Shows menu | Pass |
| Input field for Sku | Activates text area | Click textfield | Activates text area | Pass |
| Input field for Name | Activates text area | Click textfield | Activates text area | Pass |
| Input field for Description | Activates text area | Click textfield | Activates text area | Pass |
| Input field for Price| Activates text area and increase and decrease number| Click textfield | Activates text area and increase and decrease number | Pass |
| Input field for Rating | Activates text area and increase and decrease number | Click textfield | Activates text area and increase and decrease number | Pass |
| Input field for Image Url | Activates text area | Click textfield | Activates text area | Pass |
| Button for Select Image | Opens iamge folder | Click button | Opens iamge folder | Pass |
| Button for Cancel | Cancel product adding | Click button | Cancel product adding | Pass |
| Button for Add Product| Adds product | Click button | Adds product | Pass |


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
