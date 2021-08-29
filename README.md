# [Hidden Irish Travels](xx)

![site-mockup](xxx)

Irish Hidden Travels is a site where users can share/view information/recommendations on places on the island of Ireland that others may not have heard of, but the user recommends visiting. Site was inspired by stories of friends and families about places they have accidently ‘found’, or discovered through word of mouth, while on day trips, or longer holidays around the island of Ireland.

The aim is to highlight and share information on places/things to do, that do not always appear on those “top10 places to visit lists” or get hidden way down the bottom of a google search. Site is aiming to encourage people living and visiting the Island of Ireland, to experience, discover and tell others about these places in a positive and helpful way. 


## **To open any links in a new tab, please press Ctrl + click**

## Table of Contents

- [UX](#ux)
  - [External User Goals](#external-user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [Strategy and Scope](#strategy-and-scope)
  - [Structure](#structure-of-the-website)
  - [Wireframes](#wireframes)
  - [Surface](#surface)
    - [Colors](#colors)
    - [Typography](#typography)
    - [Images](#images)
    - [Features](#features)
- [Technologies](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - [SetUp](#set-up)
    - [Heroku Deployment](#deployment-to-heroku)
    - [Run repo locally](#download-and-run-repo-locally)
    - [Cloning the repo](#cloning-the-repo)
    - [Forking the repo](#forking-the-repo)
- [Credits](#credits)

---



## UX

### External User goals

#### As a first-time user, I want to

- Understand the main purpose of the site.
- View recommended places in Ireland and Northern Ireland.
- Register as a user
- Find out how to submit a recommendation
- Be able to view the site on mobile/desktop/tablet.
- Be able to access all pages and navigate without confusion, without too many clicks.

#### As a returning user, I want to

- View recommended places in Ireland and Northern Ireland.
- Log-In
- Submit a new recommendation
- Edit a previously submitted recommendation
- Delete a previous recommendation
- Be able to view the site on mobile/desktop/tablet.
- Be able to access all pages and navigate without confusion, without too many clicks.
- Search based on a key word

### Site Owner goals

#### As site owner I want to

- Provide a place for users to recommend unusual and unknown places to see on the island of Ireland.
- Manage categories
- Update/add own personal recommendations
- Delete negative and misleading recommendations.
- Delete Users.

### Strategy and scope

The main goal of the site is to provide user with a site where they can find recommendations from others, on unusual or unknown places on the island of Ireland. Eg places the user may not have been aware. Users will not need to be registered to view the recommendations but will have to do so, in order to upload a review.<br>
To convert a visitor, and draw them in, there will be a short explanation of the site with some examples of unique and interesting places to visit.<br> Emphasis is on positivity on the site, this is a place for users to let others know about places they have perhaps stumbled that they have enjoyed and found interesting, but maybe had never heard of before.

####       ADD SCREENSHOT OF SCOPE TABLES ###

[Strategy and scope tables](xx)

### Structure of the website

The basic structure of the site is designed around making it easy for the user to navigate and view/upload recommendations. A user will land on the home page where they can view recommendations and use a simple process to register/login in order to manage their recommendations. Recommendation form will have 4 Fields for the user to update, 2 of which will be dropdown boxes. Username will be updated from the user profile.

Standard form will be used for new reviews/editing/deleting for all users and admin. Login and registration forms will be as simple and clear as possible to make it easy for the user to use the site
Admin user will also have a small form to find a user and option to delete.
Logout button will also be provided


[Structure Plan](xx)

### Wireframes

[Wireframe Mobile](xx)
[Wireframe Tablet](xx)
[Wireframe Desktop](xx)
These were built using balsamiq.

### Surface

[Surface Plane](xx)

#### Colors

I wanted to use green colour associate with Ireland so chose the hex value of the green on the irish flag. Use a dark colour for text, making it easily accessible and a light calming blue colour. All colours will be tested for accessibility/contrast/

Simple colour scheme containing 3 main colours:
	- 172a3a/169b62/edf6f9			
    | Irish green for small elements / A dark color for txt / light blue colour for overall visual |



![Final Colours Used](xx)

#### Typography

There will be two fonts used throughout the website. The titles font will be Hind, and the accompanying body font will be Poppins. Fallback fonts for both are san-serif
I feel these fonts are easy for user to read on screen and are visually appealing.


#### Images

[Back to table of contents](#table-of-contents)

## Features

**_Website has the following features_**

### Features which are accessible on all pages with the exception of error pages.

#### Navigation Menu. 

- Contains links to:

| Logged Out | Logged In	|
|------------|-----------------	|
|  Home	     | Home       	|
|  Log In    | Recommendations  |
|  Register  | Search 		|
|  	     | Admin *  	| 
|  	     | Log Out  	|
|  	     |   		|

| Recommendations Menu| 
|---------------------|
|  Add New	      | 
|  Edit  	      | 
|  Delete	      | 

** Admin option will bring the user to the overall Admin  page, where user can access the admin functionality
** The Admin option is restricted and regular user will not have access

- Navbar is collapsible icon on medium and small screens, and will display as vertical menu when clicked
- Search will display as an icon on desktop

#### Search

- search box to be displayed

#### Footer

- Contains copyright and site policy info


### Features on individual pages

#### Home Page

Contains the following:

- Logged Out User 
	- Navigation Menu
	
	- Button to Log in
	- Button to register  Modal Pop Up for instructions on registering
	- Recommendations section
	- Button to click to go to top of page.
	- Footer

- Logged In User (Regular and Admin)
	- Navigation Menu
	
	- Add/Edit button
	- Recommendations section
	- Button to click to go to top of page.
	- Footer

#### Registration Page

Contains the following:

- Navigation Menu
- Header and quick note on how to register
- Registration Form with 3 input fields and submit button
	- username
	- password
	- password confirmation
	- Submit button to register
- Footer

#### Log In Page

Contains the following:

- Navigation Menu
- Log In Form with 2 input fields and submit button
	- username
	- password
	- Log In button
- Footer

#### Recommendation Page

Contains the following:

- Navigation Menu
- If Add New Option was selected : Blank Recommendation form.
- If Edit Option was selected: Prepopulated form is shown with Edit button. **Restrict to username
- If Delete Option was selected: Prepopulated form is shown with delete button.    **Restrict to username and show confirmation btn

- Recommendation Form:
	- Image to select from
	- 2 user input fields: title and details.
		On Edit, fields user can click on fields to edit
	- 2 fields for user to select from dropdown
	- Created_by field updated from username
	- Submit Button/Edit Button/Delete Button (dependant on option selected)
- Footer

#### Admin Overview Page

Contains the following:

- Navigation Menu
- Manage Form fields Button
- Delete a user recommendation button
- Delete user button
- Footer

#### Admin Delete User Page

Contains the following:

- Navigation Menu
- Admin Username as heading
- Form with the following fields:
	- Find username
	- User details
	- Reason for deletion (admin could keep screenshots as back up to confirm reasons)
- Delete button
- Cancel button
- Footer

#### Admin Add/Edit Fields Page

Contains the following:

** warning on how these actions affect active recommendation **

- Navigation Menu
- Admin Username as heading
- Recommendation Form:
	- current fields on display
- Add New button
	- will display form with key:value details to be input and button confirmation
- Edit button: allow Admin user to click on a field to edit
- Cancel button
- Footer

#### Admin Delete Recommendation Page

** Note: Admin should only be able to delete a users recommendation, not edit it.
Contains the following:

- Navigation Menu
- Admin Username as heading
- Form with the following fields:
	- Find recommendation (*using _id or how??)
	- Details
	- Reason for deletion (admin could keep screenshots as back up to confirm reasons)
- Delete button
- Cancel button
- Footer

#### Logout Page

Contains the following:

- Navigation Menu
- Confirm logout button. 
- Footer

#### Logout confirmation

Contains the following:

- Message to user 
- Option to return to home page

## Future Features

[Back to table of contents](#table-of-contents)

## Technologies Used

- [Github](https://github.com/)- software hosting platform to keep project in a remote location
- [Gitpod](https://gitpod.io/) - a development hosting platform
- Git - used for version-control.
- [Google fonts](https://fonts.google.com/) -used to select and provide typography.
- [Online kanban tool for plan and management of project tasks](https://kanbantool.com/)
- [Balsamiq](https://balsamiq.com/) - used to build wireframes. Downloaded software to use.
- [Markdown table convert](https://tableconvert.com/) - I am using this to turn data on excel into markdown table syntax
- Microsoft word and excel: to assis in organising planning for project
- [Flow chart](https://app.diagrams.net/) - Used to create a flow chart for planning of project
- [site for creating DB schema diagrams](dbdiagram.io)
- [site to enable me to edit pdfS](https://www.ilovepdf.com/) - I needed a tool to allow me to edit pdfs of diagrams 
- 






[Back to table of contents](#table-of-contents)

## Testing

[Testing Documentation](https://github.com/LisaHackett97/HiddenIrishTravels/blob/main/TESTING.md)


- Issues during development and bugs are covered in this document, in addition to the planned testing.

## Deployment

### Set up
### Deployment to Heroku
### Download and run repo locally
### Cloning the repo
### Forking the repository:



## Credits

### Media

#### Images Used

#### Other

### Content

### Colours


### Code

### Acknowledgements

I referred to the following to add to my knowledge and for help.

[Back to table of contents](#table-of-contents)

This site was developed for Educational purposes
