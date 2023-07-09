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
| My Account (as a logged in user) | Show dropdown menu for my profile, contact us and logout | Click my account | Show dropdown menu for my profile,contact us and logout | Pass |
| My Account (as a logged in admin) | Show dropdown menu for login,register, contact us and product management | Click my account | Show dropdown menu for login,register, contact us and product management | Pass |
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
| `Contact Us` |
| Textfield for product name | Activates textarea | Click field | Activates textarea | Pass |
| Dropdown menu for Countries | Shows menu | Click menu | Shows menu | Pass |
| Dropdown menu for Category | Shows menu | Click menu | Shows menu | Pass |
| Textfield for Description | Activates textarea | Click field | Activates textarea | Pass |
| Send button | Sends message to the admin panel | Click button | Sends message to the admin panel | Pass |
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
| `Product Page` |
| Product link | Redirects user to product detail page | Click link | Redirects user to product detail page | Pass |
| Dropdown menu for sorting | Gives user option on how to sort products on page | Click menu| Gives user option on how to sort products on page | Pass |
| Category link on product | Redirects user to that category | Click link | Redirects user to that category | Pass |
| Category button (if user is on category) | Redirects user to that category | Click button | Redirects user to that category | Pass |
| Products Home link (if user is on category) | Redirects user to all products page | Click link | Redirects user to all products page | Pass |
| Edit and Delete link (if user is superuser) | Edit link opens product management page and delete link deletes product | Click link | Edit link opens product management page and delete link deletes product | Pass |
| `Product Detail Page` |
| Product link | Opens product image in a new window | Click link | Opens product image in a new window | Pass |
| Category link | Redirects user to specific category page | Click link | Redirects user to specific category page | Pass |
| Like button (if user is logged in) | Increase number of likes | Click button | Increase number of likes | Pass |
| Dropdown Menu | Gives user option to buy bottle or box | Click button | Gives user option to buy bottle or box | Pass |
| Textfield with buttons | Activates textfield and buttons increase or decrease number | Click button | Activates textfield and buttons increase or decrease number | Pass |
| Keep Shopping button | Redirects users to all products page | Click button | Redirects users to all products page | Pass |
| Add To Bag button | Adds product to bag | Click button | Adds product to bag | Pass |
| Comment form (if user is logged in) | Make a comment | Click form | Make a comment | Pass |
| Written comment (if user is author) | Edit and delete comment | Click edit or delete button | Edit and delete comment | Pass |
| Edit and Delete link (if user is superuser) | Edit link opens product management page and delete link deletes product | Click link | Edit link opens product management page and delete link deletes product | Pass |
| `Shopping Bag page` |
| Decrease Amount button | Decrease amount of product choosen | Click button | Decrease amount of product choosen | Pass |
| Increase Amount button | Increase amount of product choosen | Click button | Increase amount of product choosen | Pass |
| Update link | Update to new amount choosen | Click button | Update to new amount choosen | Pass |
| Remove link | Remove products from shopping bag | Click button | Remove products from shopping bag | Pass |
| Keep Shopping button | Redirects user to all products page | Click button | Redirects user to all products page | Pass |
| Secure Checkout button | Redirects user to secure checkout | Click button | Redirects user to secure checkout | Pass |


| `Secure Scheckout Page` |
| Secure Checkout button | Redirects user to secure checkout | Click button | Redirects user to secure checkout | Pass |
| Secure Checkout button | Redirects user to secure checkout | Click button | Redirects user to secure checkout | Pass |
| Secure Checkout button | Redirects user to secure checkout | Click button | Redirects user to secure checkout | Pass |
| Secure Checkout button | Redirects user to secure checkout | Click button | Redirects user to secure checkout | Pass |
| Secure Checkout button | Redirects user to secure checkout | Click button | Redirects user to secure checkout | Pass |

| `404 Page` |
| (User Logged in) Home Button | User will be redirected to the home page | Click home button | Redirected to the home page | Pass |
| (Guest User) Login Button | User redirected to the login page | Click login button | Redirected to the login page | Pass |
| (Guest User) Sign Up Button | User redirected to the sign up page | Click sign up button | Redirected to sign up page | Pass |
| `Footer` |
| Facebook link | Redirects user to the sign up page | Click button | Redirected to sign up page | Pass |
| Instagram link - Social media links | Opens new tab to the social media site | Clicked each icon | New tabs opened for each site | Pass |
| Subsribe link - Privacy Policy link | Redirects to the privacy policy page | Clicked link | Redirected to privacy policy page | Pass |


Back to [README.md](README.md)
