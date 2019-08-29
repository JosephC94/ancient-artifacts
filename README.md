# Ancient Artifacts

[Link to website via GitHUb](https://github.com/JosephC94/ancient-artifacts/)

A website used for browsing, bidding, buying and learning about different ancient artifacts. The website contains a welcome page, registration and login functionality, a page of products listed, detailed info about each product and events they have been involved in, and the option to purchase the product. The website's primary focus is for the user to buy a product. The user must register and account or sign in, in order to navigate to the products.

The website focuses largely on what is for sale, each items journey of events, previous ownership and importance. The goals of the website are to:

* Provide knowledge of each product's journey and significance to entice customer's to purchase
* Allow a user to purchase products
* Excellent use of UX to ensure customers go from visiting the website to leaving the website having purchased a product or products
* Provide enough info of each item to highlight its importance for customers to recognise its true value for purchase
* Allow users to search for a product
* Allow users the option to bid on a product
* Easy navigation
* Simple order process that conforms with modern day online order processes
 
# UX
 
 ## Target audience and customers:
 
 ### Ideal customers for this website
 
 * Collectors of rare and valuable items
 * Customers who have a profound interest in historical artifacts
 * Rich customers with a fondness for history
 * Customers of particular beliefs and religions
 * History students
 * Archeologists
 * Historians


### These customers are looking for:

* Items of such rarity, that only 1 in the world exists of each
* Knowledge of the imortance/significance of the products
* The option to purchase one, or more, of these artifacts
* A story being told of each item and where its journey has led it to today


### The customers are able to achieve the above as:

* The website is simple and focuses primarily on the products listed and their journey of events/description
* There are no adverts on the site promoting any other kind of material - it only focuses on the artifacts
* The site does not contain an overload of JavaScript which would slow it down
* There are few products on the site due to their rarity, making browsing much quicker than having hundreds of products
* The website is easy to navigate as there are only a few links
* Each product has their own descriptive content
* The descriptions of each product provide indepth knowledge about the product and its journey of events and ownership
* A function for adding a product to a cart and naviagting to a checkout menu

### User stories:

1. As a historian, I would like a site that provides the ability to purchase ancient artifacts
2. As a history student, I would like to know more information about some historical artifacts to gain some knowledge and insight about them
3. As a competitive buyer, I would like a site that draws a lot of attention to potential bidders
4. As a person interested in unique historical artifacts, I would like a site that gives me the opportunity to purchase and find out more information about some of them
5. As someone interested in historical events and artifacts, I would like a website that tells of the journey that an item went through for my own fascination
6. As a user of the bidding site, I would like the opportunity to narrow my search to something that directly interests me so I am not searching through each and every product


### Mock Ups

## All mockups found [here](https://github.com/JosephC94/ancient-artifacts/tree/master/mockups)

## Features

Each page of the website contains a navbar with content that alters depending on which page the user is on. The home page contains links for the products page (Artifacts) and the Resgiter/Sign In/Out Model. On the products page, the navbar contents change to Home, View Cart, Resgiter/Sign In/Out modal. View cart changes to Back To Products on the View Cart page and the Checkout page's navbar is the same as the Home page navbar. All contents of the navbar remain in the same position with each page.

The font family, colour and page layout of each page is the same. This is so that the website is easily recognisable and much more user friendly to navigate. Each page also contains a Title so the user can easily recognise where they are.

* Home Page:

This page contains a brief intro to the website in the middle of the page with a title. Beneath the descriptive text, the user is presented with a slideshow of each product, and the name of each product, through a carousel. If the using is viewing the page on smaller screens, the carousel is replaced by hyperlinks for an easier read.

* Products page (Artifacts page)

This page is accessed when a user sign in or registers. It displays a list of all of the products on site with an image, price, 'Buy now and add to cart' option, a link for the user to place a bid on the product, and a brief description of the item. It also includes a search bar for users to narrow their search. When a user adds an item to their cart, using the 'Buy now and add to cart button', the cart icon will display how many items are in their cart.


* View cart page (Shopping Cart)

When a user enters this page they are displayed with the contents of all of the items within their shopping cart. Like the products page, the user is presented with a list of all the products; displaying the image, price, brief description and an amend option for each. If the user enters 0 into the Amend box and clicks the amend button. This will remove the item from the shopping cart. Below the list of products within the cart, the user is displayed with the total cost of all products within the cart and a link for checking out.  


* Checkout

When the user clicks the checkout button, they are brought to a page that lists of all of the items that were in the shopping cart, along with the item's image, description, price as well as a total cost. Beneath all of the porducts, the user is presented with a form in which they must fill out in order to process the order by clicking on the Submit Payment button. Should the user not complete the form fields, the form will not submit and the user is asked to fill in the fields required by a message beneath the required field. Once the user enters the fields in correctly, they will be redirected back to the products page, their cart will empty, and they will be presented with a message indicating that payment was successful.


* Modal

The modal allows the user to Sign In, Register and Logout. Should the user already be signed in, they are only promted with the Logout function. If a user selects to register, they are redrected to the register page.


* Register Page

When the user clicks the register link, or vists the /accounts/register/ url, they are provided with a simple form that asks them for their Email Address, Username, Password and Password Confirmation. Once the user correctly enters all of these fields, they are redirected to the Products page with a message saying that they have been registered to the site.


* Bid Product (Product detail)

Should the user click the 'click here to bid' button on the products page, they are directed to the products detail page that displays the product image, price and description that they have selected. They are also presented with the navbar containing the Artifacts and Modal links/options. The user is also presented with a link that says 'Click here to place bid'. Should the user click this, they are redirected to the place bid page.


* Place Bid

On this page the navbar remains the same as the Bid Product/Product Detail page (above) and the user is presented with a simple form that allows them to place a bid of up to 9 digits. Once the user submits the form by clicking the Place Bid button. They are redirected to the bidding list for that product.


* Bid Detail (Bid list)

The user is presented with the same navbar mentioned above, and is also shown an image of the product, name, brief description and all of the bids that have been placed on it in descending order.


* Product Infomation

The user is able to access more infomation about each product via the links at the bottom of the home page. Each info page's layout is the same, with a navbar, title, x2 images related to the story of the product, paragraphs detailing the product and it's story/events and a footer with a generic piece of info provided to the user about the current state of the product.
 
### Existing Features

* Navbar - exists on every page and allows the user to navigate through the site depending on which page they are on currently.

* Title - each page contains a title other than the checkout and bidding pages - this allows the user to easily discern where they are on the site.

* Search - this feature exists on the Products page and allows the user to search for a product and narrow their results.

* Brief Description - this feature is presented to the user on the products page and through the bidding and adding to cart and buying process.

* Carousel - this feature exists only on the home page, and will be replaced by hyperlinks when the screen has reduced size - anything below 800px.

* Modal - is consistent on every page other than the Product Info pages.

* Products page - displays all available products to the user without overloading them with content

* View cart page - displays the products within the users cart without overloading them with content

* Checkout page - displays the products and the checking out form without overloading the user with content

* Modal - allows the user to sign in/out/register

* Home page - provides the user with an intro to the site and links to the products info

* Product info pages - provides the user with infoamtion about a specific product


### Features Left to Implement

* I would like a feature that makes the product dissapear from the products page when this has been added to the cart and paid for. 

* I would to add more javascript to the site to make it 'come alive' a bit more

* Another feature to implement is once the user has placed a bid, their bid is highlighted in the list of bids, with a message stating whether or not the user is the highest bidder. I would also like to display the time and date and username of the users who have bid on that product. 

* I would like a timing function for the products presented to the user once they sign in. This would be highlighted on anything that they have already placed a bid on, too. Once the time is up, the product would be removed form the page, and the highest bidder would be sent an email stating that they have won the auction. When the user signs in, this product would then be in a separate list on their account labelled 'auctions won'. They would then proceed to payment once this list has been accessed.

* One feature to implement is to provide an 'Overview' and/or 'History' page to the user detailing all of the bids that they have won, and all of the products that they have purchased.

* I would like to add video content to each product info page that broadcasts archeologists/historians talking about that specific product - this would make for a more user friendly experience rather than just plain text for the user to read.

* An option to choose a different language for the website

* An option to select currency.

## Technologies Used

* [JQuery](https://jquery.com)
    - The project uses **JQuery** to provide the site with the carousel on the home page and to accept payments via Stripe.
   
* [Stripe](https://stripe.com/)
    - The project uses **Stripe** to allows users to pay for their products
    
* [Javascript](https://www.javascript.com/)
    - The iste makes use of javascript to allow for Stripe payments through the app

* [Django](https://www.djangoproject.com/)
    - This project uses the **Django** Framework to allow a smoother user experience by providing the developer with the ability to complete the project as quickly as possible. It is secure, and provides a clean and pragmatic desgin. It is a framework used to allow the developer to focus on building their application without the need of re-inventing the wheel.
    
* [Python 3](https://www.python.org/)
    - This project is written using Python to supply the site with the Backend materials to prodive logic and functionality as required
    
* [HTML 5](https://html.com/)
    - HTML 5 is used to employ text, images and pages to the application
    
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS is used to provide styling to the HTML technology for a better user experience
    
* [Bootstrap4](https://getbootstrap.com/)
    - The site makes use of Bootstrao v 3.4 to allow for a better user experience by providing a framework that complies javascript and css for a more professional and intuitive website
    
* [Postgres Database](https://www.postgresql.org/)
    - The site makes use of Postgres to store infomation into a database for access


## Testing


### User story 1: 

* 'As a historian, I would like a site that provides the ability to purchase ancient artifacts'. This is achieved by providing the user with an option to add a product to the cart from the products page once the user has signed in. To do this, the user would select the quantity of the product (only x1 of each product can be selected as these are Ancient Artifacts) and then click on the 'Buy Now and Add To Cart' button beneath and next to the image and description of the product. The page will refresh, and the cart will then display an integer value of how many products have been added to the cart. The user clicks on View Cart link - they are directed to the View Cart webpage where all of their cart items are displayed. The user then clicks the checkout link and enters their details into the forms. If a user does not enter all of their details, the form will not submit and a pop up window provided by django will ask the user to fill in the field. Once the user has successfully enter all of their details, the form will submit, and the user is re-directed back to the Products page and is greeted with a message stating that the payment has been successful. This removes the item from the Cart, too.


### User story 2:

* 'As a history student, I would like to know more information about some historical artifacts to gain some knowledge and insight about them'. This user story is achieved when the user is presented with the home page. The user can click on the product name/hyperlink at the bottom of each slide on the carousel of each product. The user will be directed to that particular product's url page which can be accessed either being logged in or out. This page provides the user with all of the available info on the site about the product available.


### User story 3:

* 'As a competitive buyer, I would like a site that draws a lot of attention to potential bidders' This user story is achieved when the user signs in or registers. They are directed to the products page. From here the user clicks on the 'Click here to bid on this item link'. They are then redirect to the product_detail url. This page provides the user with a single product - the product they intent to bid on - and a "click here to place bid' link. When the user clicks on this link, they are taken to the place_bid url that provides the user with a form that requires an integer as an input - this is the amount the user wishes to bid on the product. When they submit the bid, the user is finally re-directed to a current list of bids on that product. Their bid is displayed in a list in descending order along with other users' bids.


### User story 4:

* 'As a person interested in unique historical artifacts, I would like a site that gives me the opportunity to purchase and find out more information about some of them'. The testing for this userstory is essentially covered in the above for user stories 1 and 2. Visiting this site provides the user with a broad and unique range of historical artifacts that come from all over the world and from differing periods in time; from the Ancient Egyptians to Norse Gods to The Knights Templars. This info is found when the user clicks on the hyperlinks in the carousel, should the screen be larger than 800px, otherwise they can access it with standard hyperlinks at the bottom on the home page. 


### User story 5:

* 'As someone interested in historical events and artifacts, I would like a website that tells of the journey that an item went through for my own fascination'. This user story has been achieved via the urls that direct the user to the individual product info pages through the slideshow hyperlinks found on the home page. These pages provide the user with content that describes the journeys that the items have gone through.


### User story 6:

* 'As a user of the bidding site, I would like the opportunity to narrow my search to something that directly interests me so I am not searching through each and every product'. Once the user has registered or signed in, they are taken to the products page which lists every product available. The user can use the Search box at the top of the page to narrow their search by typing in some content that relates to the products that match it. The list of products is then narrowed, making it easier for the user to browse.


The forms throughout the site must require user input. If the user does not fill in all of the form fields, the submit buttons do not fire and the user is presented with a 'This field is required message' beneath the required field. 

If a user attempts to access the products page without signing in, they will be redirected to the home page.

Once the user logs in, they are directed to the products page. If they do not supply their correct credentials, they will not be signed in and the home page will display a message stating that their username or password is incorrect.

When the user adds an item to the cart, the cart will update with a figure dislpaying how many items are within the cart. If the user attempts to enter more than 1 of any item, they will be displayed with an message stating 'Value must be equal to 1'. The cart will not update unless the user only enters 1 of the item. If, after the user has added 1 item, they can not add this same item to the cart (essentially making it 2 of the same item); the page will simply refresh and the cart will not be updated.

Once the user clicks on the 'click here to place bid' link, the user is directed to that specific products bidding page - all other products become non existent here.

Should the user attempt to make a bid larger than 9 digits, they will be promted to 'ENSURE THAT THERE ARE NO MORE THAN 9 DIGITS IN TOTAL' and the bid will not take place. If the user attempts to type in text into this form, the field does not populate the user input - it behaves as though nothing is happening inside the field - no error messages are displayed. Once the user places a bid, they are successfully redirected to the bid_detail page displaying their bid.

Should a user attempt to amend the cart, they can only enter the value as '0' - since there is only x1 of each product - the user will be presented with an error message stating that the value must be equal to '0' - the user can not amend the cart item unless they do so - neither the cart or the page changes.




## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
