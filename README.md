# Wine O'Clock Website

The Wine O'clock website is an e-commerce site where users can buy wine. Besides buying wine, they can also learn more about the products in stock as they all have detailed descriptions. Wine O'Clock is mainly targeted towards an older audience since it contains alcohol, but anyone of legal drinking age is able to enjoy the carefully selected products. Our business model aims to maintain exclusivity for both the wines and our customers.

What does that mean for us and the customers? Well, it means that we never have more than 100 products on our page at a time. We always offer a variety of bottles from each region and in different colors to cater to a wider audience. Additionally, since we have fewer products compared to our competitors, we can purchase larger quantities of each bottle, resulting in lower prices for everyone.

We want everyone to be able to enjoy exceptional wine!

We also use socialmedia to render a bigger audince. Moslty we use our Facebook page.

![We also use socialmedia to render a bigger audience. Moslty we use our Facebook page.](media/facebookpage.png)

[View Wine O'Clock on Heroku Pages](https://wine-oclock-d9434a8420f0.herokuapp.com/)

## CONTENTS

* [User Experience (UX)](#User-Experience-(UX))
  * [Initial Discussion](#Initial-Discussion)
  * [User Stories](#User-Stories)

* [Design](#Design)
  * [Colour Scheme](#Colour-Scheme)
  * [Imagery](#Imagery)
  * [Wireframes](#Wireframes)
  * [Features](#Features)
  * [Accessibility](#Accessibility)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

* [Deployment & Local Development](#Deployment-&-Local-Development)
  * [Deployment](#Deployment)
  * [Local Development](#Local-Development)
    * [How to Fork](#How-to-Fork)
    * [How to Clone](#How-to-Clone)

* [Testing](#Testing)
  * [W3C Validator](#W3C-Validator)
  * [Solved Bugs](#Solved-Bugs)
  * [Known Bugs](#Known-Bugs)
  * [Testing User Stories](#Testing-User-Stories)
  * [Lighthouse](#Lighthouse)
    * [Index Page](#Index-Page)
    * [Books Page](#Books-Page)
    * [Contact Us Page](#Contact-Us-Page)
    * [Thank You Page](#Thank-You-Page)
  * [Full Testing](#Full-Testing)
  
* [Credits](#Credits)
  * [Code Used](#Code-Used)
  * [Content](#Content)
  * [Media](#Media)
  * [Acknowledgments](#Acknowledgments)

- - -

## User Experience (UX)

### Initial Discussion

The owners of Wine O'Clock spend a lot of time searching for the best wines from around the globe to offer their customers an amazing selection. They value their regular customers and aim to constantly have a wide range of wines available. To provide exceptional service, Wine O'Clock is always open, regardless of the customer's location. This means that no matter where you are in the world, Wine O'Clock is ready to serve you.

The company also assists newer wine enthusiasts by offering a curated selection of wines specifically chosen to pair well with different types of foods. This category allows customers to easily find wines that complement specific dishes.

#### Key information for the site

* Exclusive wines from around the globe.
* A wine selection tailored to complement different types of cuisine.
* A subscription form for members to stay updated on new wines.
* The ability for logged-in users to "like" products, showcasing their popularity to others.
* Links to our social media pages.
* An order history for users to easily review their past purchases.

### User Stories

#### Client GoalsHere are the revised descriptions:

#### User Goals

* To have a responsive shopping site that works well on various device sizes.
* To easily create an account and make purchases.
* To have the option to save account information for convenience during future purchases.
* To be able to search for products using a search bar or browse through categories.
* To add and remove products from the shopping bag.
* To "like" products of interest.
* To view pictures of the products.
* To read detailed information about each product.
* To register, log in, and log out with ease.
* To have a one-click option to scroll back up on the page.
* To view the entire available stock of products.

#### Admin Goals

* To easily manage and modify products by editing, adding, or deleting them.
* To view customer orders and product likes.
* To receive user feedback and tips regarding new products.

- - -

## Design

### Colour Scheme

Wine O'Clock utilizes a variety of colors to enhance the page, including the vibrant hues found in the products and the scenic backgrounds of vineyards. To ensure that the focus remains on the products themselves, we have chosen to incorporate predominantly white and pale yellow tones, allowing the products to take center stage without distractions.

### Imagery

All images of the product are taken from [Vivino](https://www.vivino.com/SE/en/) and in the json file each products also renders the specific file.

### Wireframes

Wireframes were created for mobile, tablet and desktop.

[Home Page Wireframe](media/index_page.png)

[Products Wireframe](media/product_page.png)

[Products Description Wireframe](media/description_page.png)

[Shopping Bag Wireframe](media/bag_page.png)

[Checkout Wireframe](media/checkout_page.png)

[Contact Us Wireframe](media/contact_page.png)

### Features

This e-commerce site consists of ten pages, each serving a specific purpose to fulfill its intended potential.

1. The Start Page: This is the initial page users encounter upon entering the application.
2. Product Listing Page: Displays all the products available in stock.
3. Shopping Bag: Allows users to view and manage the items they have added for purchase.
4. Checkout Page: Facilitates the order payment and finalization process.
5. My Profile Page: Provides a record of past orders made by the user and users infomraation
6. Contact Us Page: Offers a means for users to get in touch with the site's administrators.
7. Subscribe Page: Enables users to subscribe to receive updates or newsletters.
8. Register Page: Allows new users to create an account on the site.
9. Login Page: Provides a secure login interface for registered users to access their accounts.
10. Logout Page: Allows users to safely log out and end their current session.

These ten pages work together to provide a comprehensive and seamless e-commerce experience for the site's visitors.

* All pages on the website have:
  * A responsive navigation menu that works on all screen sizes. It gives users the ability to search for products by character in the search bar or by category in the dropdown menus. There's a menu to register for the page, log in, log out, subscribe, and contact us. The options render depending on whether the user is logged in or not. Additionally, the logo of the page takes you back to the start page, and there is a bag icon that takes the user to their shopping bag with the selected products.
  * A footer that contains social media icon links to Instagram and Facebook.

* Home Page:
  * Contains an image of a vineyard to show the user that this e-commerce site is all about grapes of different colors. Besides the background image, we also have our slogan, "Wine a little, Laugh a lot!" and a "Shop Now" button to our products page with effects to make it more exciting.

* Register Page:
  * New customers can easily register for the page.
  * Returning customers can easily sign in.
  * Signed-in users can easily sign out.

* Products Page: On the Products page, the user can either click the wine bottle or the like button to open the product.
  * If the user presses the like button (only if the user is logged in), it will render a like on the product visible to other users. It also opens the description for the product.
  * If users click the bottle, it opens the product's description.
  * From the product description, the user can add the product to the bag, like or unlike the product, and open the image in a new window.
  * On the products page, users have the option to use an up arrow to go back to the top of the page.

* Shopping Bag Page:
  * Customers can easily add, change, and delete products in their bag.
  * Users can use a "Keep Shopping" button to go back to the products page.
  * Users can go to the secure checkout page to proceed with the order.

* Checkout Page:
  * Users can fill out a form with their billing information and choose to save it for future purchases or not. Users can also change this later under "My Profile," where they can also see their order history.

* Contact Us Page:
  * Users can send in tips about wines they think we should add to our site using a form. The form asks for a name, country, description, and what dish it pairs with. The form automatically fills in the user's username and email, and when the user submits the message, it ends up in the admin's inbox.

* Subscribe Page:
  * The Subscribe page is a form that users can fill out to receive news from the site.

* Future Implementations:
  * I would like to add a live chat where users can interact with each other and give tips about products on the page.
  * I would like the like buttons to be part of a rating system.
  * Each product should be possible to review if the user has bought it.
  * I would like to have a blog page where users can submit pictures of themselves enjoying the products.

### Accessibility

I have been mindful during coding to ensure that the website is as accessible friendly as possible. I have achieved this by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Providing information for screen readers where there are icons used and no text - such as the review ratings for books & footer icons.
* Ensuring that there is a sufficient colour contrast throughout the site.
* Ensuring menus are accessible by marking the current page as current for screen readers.

- - -

## Technologies Used

### Languages Used

HTML, JavaScript, Python and CSS were used to create this website.

### Frameworks, Libraries & Programs Used

Balsamiq - Used to create wireframes.

Git - For version control.

Github - To save and store the files for the website.

Bootstrap - Framework and features on the app like the view and dropdown menus.

Stripe - To make payments possible.

Heroku - Deploy of application.

Elephant SQL - For managing PostgresSQL databases.

AWS.Amazon - Used to store data.

Google Fonts - To import the fonts used on the website.

Font Awesome - For the iconography on the website.

Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.

[Favicon.io](https://favicon.io/) To create favicon.

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.

### Rendering trafic by keywords

To drive traffic to the application, I've reused a lot of expressions throughout the website. In the product descriptions, the same flowers, fruits, and fragrances are mentioned to give higher ratings when searching for wine in the search engine.

Besides the description, the app has a catchy name, "Wine O'clock." It's inspired by the phrase "It's happy hour somewhere." The main goal with the name was to find an expression that sticks in people's minds and can also be discovered "by accident," thereby generating traffic. To finish it up, there's also a slogan: "Wine a little, laugh a lot," designed to attract people with humor.

- - -

## Deployment & Local Development

### Deployment

Heroku was used for deployment and here are the steps for deploying.

1. Sign up for a Heroku account: Go to the [Heroku website](https://www.heroku.com) and create a new account if you don't already have one.

2. Install the Heroku CLI: Download and install the Heroku Command Line Interface (CLI) tool for your operating system. The CLI allows you to interact with Heroku from the command line.

3. Prepare your app for deployment: Make sure your app is ready for deployment by ensuring all necessary dependencies and configuration files are in place. This includes setting up a Procfile that specifies how to run your app a requirements.txt file and also a env file.

4. Initialize a Git repository: If your app is not already using Git for version control, initialize a new Git repository in the root directory of your app.

5. Log in to Heroku from the CLI: Open a terminal or command prompt, and log in to Heroku by running the command heroku login. Follow the prompts to enter your Heroku account credentials.

6. Push your code to Heroku: Use the command git push heroku main to deploy your code to Heroku. This will upload your app's code and dependencies to Heroku's servers.

7. Set up environment variables (optional): If your app relies on environment variables for configuration, you can set them using the Heroku CLI. Run heroku config:set VARIABLE_NAME=variable_value for each environment variable you need to set.

Open your app in the browser: Go to setting in Heroku and you'll find a link to your page to see your deployed app there.

### Local Development

#### How to Fork

To fork the Wine O'clock repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, ohdamnitsnikki/Wine O'clock.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the Wine O'clock repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, ohdamnitsnikki/Wine O'clock.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

- - -

## Testing

Testing was ongoing throughout the entire build. I utilised Chrome developer tools while building to pinpoint and troubleshoot any issues as I went along.

The following issues were raised during my mid project meeting with my mentor:

* The Join Us section on the home page was not in alignment with the rest of the page. Padding has now been added to bring it in alignment with the rest of the pages padding.
* There was an issue on smaller devices where the book columns were not displaying properly. This issue is documented under issue 2 in solved bugs.
* The introduction paragraph on the books page was not aligned in style with the rest of the page. The text has now been centered.
* The form could be submitted with only a name filled in. ~ A required attribute has been added to the email input and textarea.

The Following items were brought up when I submitted my site to peer code review on slack.

* Andrew Dempsey suggested to change the layout of the about us section on the index page to make it two rows instead of one, as this would improve the flow of the page on larger screens. I have moved the second two items into a second row and have added a margin bottom in the css to give the items a bit more breathing space.
* Andrew also suggested it would look better if the contact us page inputs had a bit of room each side and were centred on the page, as they were rather long on larger screens. I have adjusted the size of the input fields and centred these on the page for a better viewing experience.

### W3C Validator

The W3C validator was used to validate the HTML on all pages of the website. It was also used to validate CSS in the style.css file.

* [Index Page HTML](docs/testing/w3c/w3cindex.png)
* [Books Page HTML](docs/testing/w3c/w3cbooks.png)
* [Contact Us Page HTML](docs/testing/w3c/w3ccontact.png)
* [Thank You Page HTML](docs/testing/w3c/w3cthankyou.png)
* [404 Page HTML](docs/testing/w3c/w3c404.png)
* [style.css CSS](docs/testing/w3c/w3ccss.png)

### Solved Bugs

1. The navbar would lose its alignment when on smaller devices, with the navbar brand pushing the burger icon down and over to the left underneath the site logo. This did not make for a good user experience, as the sites navigation for other sizes is on the right hand side of the navbar. While searching through the bootstrap documentation for navigation bars it directed me to display properties and hiding elements. Once I added the correct class I was then able to hide the navbar brand on devices smaller than a tablet, allowing the alignment of the navbar items to stay in place where I wanted them.

2. The cards on the books page were very long when on smaller devices, causing the user to scroll for a while before seeing the next book. By using a media query to hide the card body I am able to condense the card for a better viewing experience on smaller devices.

3. Halfway down the books page on small devices the columns would jump from displaying one column to displating two colums. After trying several ways to change this with no effect, I posed the problem to the slack community. Simen Daehlin suggested that I specify on the column class what sizes I would use for the screen sizes. By adding these column size classes it has resolved the problem. ![Column Issue](docs/columnissue.gif)

4. The textarea required attribute wasn't activating when the form was submitted. After searching for an answer, I asked on slack and Dave Horrocks spotted that as I had a message in the textarea it was reading that as a message had been entered in the textarea. By adding the message into a placeholder the issue has been rectified.

5. When viewing the books page which is very long, you would have to scroll all the way back up to the top to reach any navigation links. I thought a scroll to top button that floats on the bottom right would fix this problem, however I do not have any javascript knowledge currently to be able to achieve this. One alternative suggested by Dave Horrocks on slack was to change the top navbar to be fixed to the top, so this would be visable at all times. By adding the bootstrap class fixed-top I was able to achieve this. Then Dave suggested that I could use an anchor with an ID to achieve something that would work to achieve a scroll to top. He shared a codepen on slack showing how this would work I used the example of the codepen to create my return to top, and removed the fixed top class from my navigation bar to allow more space to view the books information.

6. When I removed the fixed-top from my navbars there was a gap between the navbar and the top of the page. I added a class of navbar-top to the navbar and used CSS to positon the navbar to the top and left of the page. I added the width of 100% so the navbar would fill the width of the page.

7. The carousel displayed fine on small screen devices, however when viewed on larger devices you would need to scroll down to see the entire image, which led to a bad user experience. By using media queries I targeted the large screen size and targeted the carousel item image to only take up 85% of the viewport height. This solved the issue by allowing the user to view the image without having to scroll, but the image was now being stretched across the screen. I searched google and stack overflow and it mentioned using object fit. I researched this further on MDN web docs and added object-fit: contain to the css which allows the image to correctly maintain its aspect ratio and view correctly.

8. The footer was displaying at the bottom of the screen as I had used a nav tag within the footer with the class fixed bottom. As I reviewed my code for errors I realised that there was no need for a nav tag to be used within the footer. When I removed this I had to add some additional styling to the style.css file to add a background colour and some padding to the footer.

9. When I asked for peer review on slack Anthony O'Brien pointed out that I was missing the container for the join us section on the home page. I had already added the css to style this section but had missed out putting the container class into the HTML. I have now added the container class to this section.

10. The thank you page on small mobile devices was not displaying correctly as the image was off to one side and the navbar and footer did not reach across the page width. After struggling with this for a few days I reached out to Anthony O'Brien to see if he could point me in the right direction to solve this issue. He told me that it was simply an overflow issue and that by reducing the width of the image it would solve the issue. I have added an id to the issue and targeted the width to be 50% in the css.

### Known Bugs

1. When filling out the form to make a purchase, some of the fields are required in order to proceed. Although the field accepts blank spaces without text as valid for submitting the form, submitting the form with blank spaces will result in a 404 error, and the purchase won't go through. The payment form using Stripe is adapted from the walkthrough project "Boutique Ado," and as long as the user fills out the form with text, it works correctly.

### Testing User Stories

* First Time Visitors
  * I want to find out what is Bully Book Club and how I can take part.
  The about us and join us sections of the home page answer some common questions and explain how to take part.

  ![About us and join us section of website](docs/testing/userstories/userstories1.png)

  * I want to be able to navigate the site easily to find information.
  All site navigation is in the top navigation bar, which consistantly appears on all pages of the site. As you are able to scroll for a long time on the book page, a return to top has been added to make it easy for users to return to the navigation menu.

  ![navigation menu for mobile devices](docs/testing/userstories/userstories2.png)
  ![navigation menu for desktop](docs/testing/userstories/userstories4.png)
  ![return to top](docs/testing/userstories/userstories3.png)

  * I want to be able to find their Instagram profile.  
    The instagram icon and link for Bully Book Club is presented on each page in the footer. This opens a new browser window to instagram for a good user experience.

    ![footer with instagram icon](docs/testing/userstories/userstories10.png)

* Returning Visitors
  * I want to find up to date information on what the book club is reading.
  In the navigation menu there is are links to take you directly to what the book club is currently reading and what they will be reading next. The books also display a badge showing that this book is the current read and reading next.

  ![Books navigation drop down menu](docs/testing/userstories/userstories5.png)
  ![Books currently reading badge](docs/testing/userstories/userstories6.png)
  ![Books reading next badge](docs/testing/userstories/userstories7.png)

  * I want to be able to easily contact the book club with questions I might have.
  A contact us page provides a form that users can fill in to contact the book club with any questions they might have. The use of a text area input allows the user to ask their specific question. The footer also contains an envelope icon which users can click to go to the contact us form from any page.

  ![Contact us form and envelope icon in footer](docs/testing/userstories/userstories8.png)

* Frequent Visitors
  * I want to be able to recommend a book for the book club to read.
  The contact us page allows users to select a checkbox for book recommendations. They are then able to add the books information into the text area.

  ![checkboxes on contact us form](docs/testing/userstories/userstories9.png)

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to allow me to test the performance, accessibility, best practices and SEO of the website.

#### Index Page

Initial lighthouse testing :
[Lighthouse Testing for Desktop Index Page - Test 1](docs/testing/lighthouse/indexdesktop.png) ~
[Lighthouse Testing for Mobile Index Page - Test 1](docs/testing/lighthouse/indexmobile.png)

Suggestions:

1. serve images in next-gen formats. Lighthouse suggests using image formats such as WebP & AVIF to improve compression and lead to faster downloads and less data consumption. I have now converted the logo and slide images to webp format using Birme.

Final lighthouse testing:

![Final Lighthouse Testing for Desktop Index Page](docs/testing/lighthouse/indexdesktop2.png)
![Final Lighthouse Testing for Mobile Index Page](docs/testing/lighthouse/indexmobile2.png)

#### Books Page

Initial lighthouse testing:
[Lighthouse Testing for Desktop Books Page](docs/testing/lighthouse/booksdesktop.png) ~
[Lighthouse Testing for Mobile Books Page](docs/testing/lighthouse/booksmobile.png)

Suggestions:

1. Serve images in next-gen formats. Lighthouse suggests using image formats such as WebP & AVIF to improve compression and lead to faster downloads and less data consumption. I have converted the book cover images and logo to webp format using Birme.

2. Properly sized images to improve load time.

Final lighthouse testing:

![Final Lighthouse Testing for Desktop Books Page](docs/testing/lighthouse/booksdesktop2.png)
![Final Lighthouse Testing for Mobile Books Page](docs/testing/lighthouse/booksmobile2.png)

#### Contact Us Page

Initial lighthouse testing:
[Lighthouse Testing for Desktop Contact Us Page](docs/testing/lighthouse/contactdesktop.png) ~
[Lighthouse Testing for Mobile Contact Us Page](docs/testing/lighthouse/contactmobile.png)

Suggestions:

1. Serve images in next-gen formats. Lighthouse suggests using image formats such as WebP & AVIF to improve compression and lead to faster downloads and less data consumption. I have converted the logo to webp format using Birme.

2. There is not a sufficient contrast on the small tag underneath the email input. I have targeted the text-muted class and changed the color of the text in order to improve the contrast.

Final lighthouse testing:

![Final Lighthouse Testing for Desktop Contact Us Page ](docs/testing/lighthouse/contactdesktop2.png)
![Final Lighthouse Testing for Mobile Contact Us Page](docs/testing/lighthouse/contactmobile2.png)

#### Thank You Page

Initial lighthouse testing:
[Lighthouse Testing for Desktop Thank You Page](docs/testing/lighthouse/thankyoudesktop.png) ~
[Lighthouse Testing for Mobile Thank You Page](docs/testing/lighthouse/thankyoumobile.png)

Suggestions:

1. Serve images in next-gen formats. Lighthouse suggests using image formats such as WebP & AVIF to improve compression and lead to faster downloads and less data consumption. I have converted the logo to webp format using Birme.
  
Final lighthouse testing:

![Final Lighthouse Testing for Desktop Thank You Page](docs/testing/lighthouse/thankyoudesktop2.png)
![Final Lighthouse Testing for Mobile Thank You Page](docs/testing/lighthouse/thankyoumobile2.png)

#### 404 Page

Lighthouse testing:

![Lighthouse Testing for Desktop 404 Error Page](docs/testing/lighthouse/404desktop.png)
![Lighthouse Testing for Moblie 404 Error Page](docs/testing/lighthouse/404mobile.png)

### Full Testing

To fully test my website I performed the following testing using a number of browsers (google chrome, safari, mozilla firefox) and devices (Macbook Pro 14 inch, iPhone 13 pro).

I also went through each page using google chrome developer tools to ensure that they responsive on all different screen sizes.

Links.

1. Test each link on the index page. Each link worked as expected, and any links leading to external pages opened correctly in a seperate browser tab.
2. Test each link on the books page. Each link worked as expected, and any links leading to external pages opened correctly in a seperate browser tab.
3. Test each link on the contact us page. Each link worked as expected, and any links leading to external pages opened correctly in a seperate browser tab.
4. Test each link on the thank you page. Each link worked as expected, and any links leading to external pages opened correctly in a seperate browser tab.
5. Test each link on the 404 page. Each link worked as expected, and any links leading to external pages opened correctly in a seperate tab.

Contact Us Form.

1. Test the contact us form. I tried to submit the form without filling in any input fields. The form worked correctly and directed users to fill in the name field. I then filled in the name field and tried to submit the form. Again the form worked correctly and directed the user to fill out the email field. I filled out the name and email forms and tried to submit the form. The form worked correctly and asked the user to fill in the textarea field. I filled out the name, email and textarea field and tried to submit the form. The form then opens the thank you page in the same browser window.
2. I tried to submit the form with only an email address - the form directs the user to fill in the name field. I filled out the name and email fields and tried to submit the form. The form then directs the user to fill out the textarea field. I filled in the name, email and textarea field and submitted the form. The form then opens the thank you page in the same browser window.
3. I tried to submit the form with just the instagram username field filled in and the form directed me to fill in the name field. I filled in the name and instagram username fields and tried again to submit. The form asks the user to fill in the email field. I filled in the name, instagram username and email field and tried to submit. The form asks the user to fill in the textarea field. I filled out the name, instagram username, email and textarea fields and submitted the form. the form then opens the thank you page in the same browser window.
4. I tried to submit the form with only the textarea field filled in. The form directs the user to fill in the name field. I filled in the name and textarea field and submitted the form. The form directs the user to fill in the email field. I filled in the name, email and textarea fields and submitted the form. The form then opens the thank you page in the same browser window.
5. I selected one of the checkboxes and tried to submit the form. The form directs me to fill in the name field. I filled in the name field and the form directs the user to fill in the email field. I filled in the name and email fields and tried to submit the form. The form directs the user to fill in the textarea field. Once I filled in the name, email and textarea fields with a checkbox selected the form then opens the thank you page in the same browser window.
6. I tried submitting the form without any information filled in. The form directs the user to fill in the name field. It then goes on to ask the user to complete the email and textarea fields if they are not filled out. The form can then be submitted and will open the thank you page in the same browser window.

- - -

## Credits

### Code Used

* [Abi Harrison's Meta Tags webinar and repository](https://github.com/Abibubble/meta-tags-example)
* [Tutorial to change bullet images to emojis](https://daily-dev-tips.com/posts/css-emoji-list-style/)
* [Dave Horrocks Copepen for the scroll to top](https://codepen.io/daveyjh/pen/GRMmqOO)

### Content

Content for the website was written by the owner of Bully Book Club and Kera Cudmore.

### Media

#### Book Cover Images

* Each book cover was taken from the publishers website.

2022 Books

[Taste](https://www.simonandschuster.com/books/Taste/Stanley-Tucci/9781982168018)

2021 Books

[A Pinch of Magic](https://www.simonandschuster.co.uk/books/A-Pinch-of-Magic/Michelle-Harrison/A-Pinch-of-Magic-Adventure/9781471124297) ~
[The Devil Wears Prada](https://harpercollins.co.uk/products/the-devil-wears-prada-loved-the-movie-read-the-book-lauren-weisberger?variant=32555806359630) ~
[A Discovery of Witches](https://www.penguinrandomhouse.com/books/307548/a-discovery-of-witches-movie-tie-in-by-deborah-harkness/) ~
[The Southern Book Clubs Guide to Slaying Vampires](https://www.penguinrandomhouse.com/books/608677/the-southern-book-clubs-guide-to-slaying-vampires-by-grady-hendrix/) ~
[The Last Thing He Told Me](https://www.simonandschuster.com/books/The-Last-Thing-He-Told-Me/Laura-Dave/9781501171345) ~
[A Good Girls Guide to Murder](www.penguinrandomhouse.com/books/607351/a-good-girls-guide-to-murder-by-holly-jackson/) ~
[The Other Black Girl](https://www.bloomsbury.com/uk/other-black-girl-9781526630377/) ~
[The Thursday Murder Club](https://www.penguin.co.uk/books/315/315815/the-thursday-murder-club/9780241988268.html) ~
[The Underground Railway](https://www.hachette.co.uk/titles/colson-whitehead/the-underground-railroad/9780708898406/) ~
[Bridgerton The Duke and I](https://www.harpercollins.com/products/the-duke-and-i-julia-quinn?variant=33097598468130) ~
[The Shadow of the Wind](https://www.penguinrandomhouse.com/books/292766/the-shadow-of-the-wind-by-carlos-ruiz-zafon/) ~
[My Sister the Serial Killer](https://www.penguinrandomhouse.com/books/588860/my-sister-the-serial-killer-by-oyinkan-braithwaite/) ~
[The Midnight Library](https://www.penguinrandomhouse.com/books/575653/the-midnight-library-by-matt-haig/) ~

2020 Books

[Nevermore](https://www.hachette.co.uk/titles/jessica-townsend/nevermoor/9781510104112/) ~
[Good Omens](https://www.harpercollins.com/products/good-omens-neil-gaimanterry-pratchett?variant=32179607535650) ~
[Starfell](https://harpercollins.co.uk/products/starfell-willow-moss-and-the-lost-day-starfell-book-1-dominique-valente?variant=32558089175118) ~
[Circe](https://www.littlebrown.com/titles/madeline-miller/circe/9780316556347/) ~
[Luckiest Girl Alive](https://www.simonandschuster.com/books/Luckiest-Girl-Alive/Jessica-Knoll/9781476789644) ~
[Ballard of Songbirds & Snakes](https://shop.scholastic.com/parent-ecommerce/books/the-ballad-of-songbirds-and-snakes-a-hunger-games-novel-9781338635171.html) ~
[The Martian](https://www.penguinrandomhouse.com/books/234102/the-martian-by-andy-weir/) ~
[Queenie](https://www.simonandschuster.com/books/Queenie/Candice-Carty-Williams/9781501196027#:~:text=Queenie%20%7C%20Book%20by%20Candice%20Carty,Official%20Publisher%20Page%20%7C%20Simon%20%26%20Schuster) ~
[Born a Crime](https://www.penguinrandomhouse.com/books/537515/born-a-crime-by-trevor-noah/) ~
[The Hunting Party](https://www.harpercollins.com/products/the-hunting-party-lucy-foley?variant=32205604978722https://www.harpercollins.com/products/the-hunting-party-lucy-foley?variant=32205604978722) ~
[Boy at the Back of the Class](https://www.penguinrandomhouse.com/books/602100/the-boy-at-the-back-of-the-class-by-onjali-q-rauf/) ~
[This is going to Hurt](https://www.panmacmillan.com/authors/adam-kay/this-is-going-to-hurt/9781509858613) ~

2019 Books

[Hercule Poirot Christmas](https://harpercollins.co.uk/products/hercule-poirots-christmas-agatha-christie?variant=32553530556494) ~
[Crazy Rich Asians](https://www.penguinrandomhouse.com/books/222866/crazy-rich-asians-movie-tie-in-edition-by-kevin-kwan/) ~
[Little Darlings](https://harpercollins.co.uk/products/little-darlings-melanie-golding?variant=32546601893966) ~

#### Other Images

* Bully Book Club Logo - with permission from Yasmin Daly, Creator of Bully Book Club.

* All images used in the carousel on the index page are photos of Bully Book Club members who kindly gave their permission for them to be used in this project.
  * [Slide 1](https://www.instagram.com/harrisonfordbulldog/?hl=en)
  * [Slide 2](https://www.instagram.com/gozerandvigo/?hl=en)
  * [Slide 3](https://www.instagram.com/chubbspetersonthebulldog/?hl=en)
  * [Slide 4 & 6](https://www.instagram.com/basicallybusterspage/?hl=en)
  * [Slide 5](https://www.instagram.com/bookswithbubba/?hl=en)

* Illustration of Harrison Ford used on the thank you page - with kind permission from [Harrison Ford](https://www.instagram.com/harrisonfordbulldog/)

* Image of Milkshake the Bulldog used on the 404 page used with kind permission from [Sir Meatball and Milkshake](https://www.instagram.com/sir.meatball/?hl=en)

### Acknowledgments

I would like to acknowledge the following people who helped me along the way in completing my first milestone project:

* Yasmin Daly, Creator of Bully Book Club, for allowing me to create a website based on the book club.
* [Adegbenga Adeye](https://github.com/deye9), my Code Institute Mentor.
* [Abi Harrison](https://github.com/Abibubble) - For her webinar on meta tags, and taking the time to respond to my peer code review request in slack.
* [Simen Daehlin](https://github.com/Eventyret) - For his help with the columns issue, and for taking the time to respond to my peer code review request in slack.
* [Dave Horrocks](https://github.com/daveyjh) - For his help with the textarea required issue & the return to top on books page.
* [Anthony O'Brien](https://github.com/auxfuse) - For pointing out my missing join us container on the index page & helping me solve the issue of the thank you page overflow.
* [Andrew Dempsey](https://github.com/andrewdempsey2018) - For taking the time to respond to my peer code review request in slack.
