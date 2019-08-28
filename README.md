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
 
## UX
 
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

1 As a historian, I would like a site that provides the ability to purchase ancient artifacts
2 As a history student, I would like to know more information about some historical artifacts to gain some knowledge and insight about them
3 As a collector of rare and valuable items, I would like a site that allows me the opportunity to purchase more rare items to add to my collection
4 As a competitive buyer, I would like a site that draws a lot of attention to potential bidders
5 As a person interested in unique historical artifacts, I would like a site that gives me the opportunity to purchase and find out more information about some of them
6 As someone interested in historical events and artifacts, I would like a website that tells of the journey that an item went through for my own fascination
7 As a user of the bidding site, I would like the opportunity to narrow my search to something that directly interests me so I am not searching through each and every product


### Mock Ups

## All mockups found [here](https://github.com/JosephC94/ancient-artifacts/tree/master/mockups)

## Features

Each page of the website contains a navbar with content that alters depending on which page the user is on. The home page contains links for the products page (Artifacts) and the Resgiter/Sign In/Out Model. On the products page, the navbar contents change to Home, View Cart, Resgiter/Sign In/Out modal. View cart changes to Back To Products on the View Cart page and the Checkout page's navbar is the same as the Home page navbar. All contents of the navbar remain in the same position with each page.

The font family, colour and page layout of each page is the same. This is so that the website is easily recognisable and much more user friendly to navigate. Each page also contains a Title so the user can easily recognise where they are.

* Home Page:

This page contains a a brief intro to the website in the middle of the page with a title. Beneath the descriptive text, the user is presented with a slideshow of each product, and the name of each product, through a carousel.

* Products page (Artifacts page)

This page is accessed when a user sign in or registers. It displays a list of all of the products on site with an image, price, 'Buy now and add to cart' option, a link for the user to place a bid on the product, and a brief description.

* 

 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing


### User story 1: 

* 'As a historian, I would like a site that provides the ability to purchase ancient artifacts'. This is achieved by providing the user with an option to add a product to the cart from the products page once the user has signed in. To do this, the user would select the quantity of the product (only x1 of each product can be selected as these are Ancient Artifacts) and then click on the 'Buy Now and Add To Cart' button beneath and next to the image and description of the product. The page will refresh, and the cart will then display an integer value of how many products have been added to the cart. The user clicks on View Cart link - they are directed to the View Cart webpage where all of their cart items are displayed. The user then clicks the checkout link and enters their details into the forms. If a user does not enter all of their details, the form will not submit and a pop up window provided by django will ask the user to fill in the field. Once the user has successfully enter all of their details, the form will submit, and the user is re-directed back to the Products page and is greeted with a message stating that the payment has been successful. This removes the item from the Cart, too.


### User story 2:

* 'As a history student, I would like to know more information about some historical artifacts to gain some knowledge and insight about them'. This user story is achieved when the user - once registered - enters the Products page. This is done automatically when the user registers or signs in, or clicks on the Artifacts or Back to Products links as well as typing in /products/ into the url bar. This page is only accessible if the user has registered, otherwise they are redirected to the home page should they try accessing the Products page outside of being logged in. The user can then 



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
