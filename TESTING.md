# [Hidden Irish Travels](xx)

## site mock Up
## link to live site

This document will cover manual, caompatability and validation testing. Issues found during development and bugs are also detailed.
I have included a section on the defensive design elements of the site I planned.

## **To open any links in a new tab, please press Ctrl + click**

##

## Table of Contents

- [Testing](#testing)
  - [Planning Approach](#testing-plan)
  - [Functionality testing](#functionality-testing)
  - [Compatibility testing](#compatibility-testing)
  - [User stories testing](#user-stories-testing)
  - [Issues found during site development](#issues-during-development)
  - [Bugs](#bugs)
  - [Performance and Accessibility testing](#performance-and-accessibility-testing)
  - [Code Validation](#code-validation)
  - [Defensive design testing](#defensive-design-testing)
  - [Main README File](https://github.com/LisaHackett97/HiddenIrishTravels/blob/main/README.md)
    
---



### Testing Plan

Testing Plan:

For each change/bug resolved, test the feature to ensure working as expected. Test other developed features to ensure no changes

Once main development finished, the following testing should be done.

#### Manual testing will cover the following
  
- Run Functionality/feature tests
- Each feature is tested per plan. Feature, expectation, testing and results are noted.
- Negative and positive cases to be tested
- Tests to be run for each feature on the site. Each will be tested for 3 user types. Logged-out/logged-in/admin.
- If a bug is encountered, work is done to resolve. Noted in bugs section. And testing cycle to start at beginning.
- Check responsiveness for screen sizes
- Do the user story testing. Review each goal of users. Note how this is achieved. Issues noted
- Review already resolved bugs and test again.

#### Non-manual testing

Run code through

- validators
- lighthouse
- WAVE extension

Validation of code re-checked each time a change made, after the main development completed. <br>
If issues occur, resolve and re-run validation tests. <br>
Wave tests help identify issues early so that they could be corrected and feature/functions re-tested.

- Validate css, html and javascript.
- Lighthouse reports
- WAVE accessibility reports
- Cross brower testing

#### Defensive Design

The following are defensive design elements identified in planning. Each will be manually tested

- Non registered User should not be able to do the following:
  - Add/Edit/Delete a recommendation
  - Search site
  - View 'logged in' menu bar
  - View or access any admin options

- Error pages should be in place. 404

- Regular logged in user should not be able to do the following
  - View 'logged out' menu bar
  - View Admin Option in nav bar
  - View Admin Overview page
  - View or action any admin functionality: Edit fields/delete recommendations (other than own)/Delete a user

- Back buttons/Home buttons or other navigation buttons should bring user back to the appropriate page, depending on their logged in/Out status

- Required input fields on forms, give message

- Form validation needs to be in place

----

- Any further changes made, re-run all steps (manual, non-manual and defensive design tests) and note any issues (iterative)

----

### Functionality Testing

[Back to table of contents](#table-of-contents)
### Compatibility Testing
[Back to table of contents](#table-of-contents)
### User stories Testing

#### As a prospective user, I want to

| 	| Tests Performed | 
|------ | ----| 
| Understand the main purpose of the   site.| | 
|View recommended places in Ireland  <br> and Northern Ireland. | | 
| Find out how to submit a recommendation | | 
| Register as a user  | | 
| Be able to view the site on mobile/<br> desktop/tablet. |  | |
| Be able to access all pages and navigate <br> without confusion, without too many clicks. | |

#### As a returning user, I want to

| 	| Tests Performed | 
|------ | ----|
| View recommended places in Ireland  <br> and Northern Ireland.| | 
| Log In| | 
| Submit a recommendation | |
|	
| Delete negative / misleading  user <br> recommendations  | | 
| Delete Users | | 
| Be able to view the site on mobile/<br> desktop/tablet. | | 
| Be able to access all pages and navigate <br> without confusion, without too many clicks. |
|											    |
|											    | | 								

#### As site owner I want to

| 	| Tests Performed |
|------ | ----| 
| Provide a place for users to recommend <br>unusual and unknown places to see on the island of Ireland.| |
| Manage Categories | |
| Update/add own personal recommendations | | 
| Delete negative and misleading recommendations | 
| Delete users| | 

[Back to table of contents](#table-of-contents)

### Issues during development

- Heroku not running after deployment. checked all config variable, versions in requirements etc...
in app.py, I had "main" instead of "__main__"

- On mobile view, on add new, no spacing between buttons. 

- Icon on nav bar too big and was not appearing on all pages. Needed to set the url_for method for img src, and set height and width

- Showing search results, no user name on screen. Needed to pass username into the return function and needed to reset the form and target it by Id not class name in JS




footer on templates is not showing full width. Ok on hime and registration Not ok on login template. cloising div tag missing a >
fixed and commited when finalising page structure




styling divs with card-title. These are on teh card reveal. Top has icon to close and btm has txt also. Needed to give id to text inorder to change font


reduced space for images, so that more details could be viewed on fromnt card But large space, related to card action footer
reveal top border is hidden
needed to 
.card.medium .card-image+.card-content {
   max-height: 55%;
   padding-bottom: 10px;
}
Using dev tools id'd what to be targeted

Was using the root color irish green for card reval, used color picker to change the transparency but then you could see txt on card. used color picker to choose a different shade of the green. could not use any transparency settings


Session user set up on nav bar, cannot access recommendations dropdown. I needed to correct the data target, issue resolved

Closed app while still logged in. When re-opened, was still showing logged in. 
session cookies cleared when full browser window closed but not when tab closed. Timer

Looking at length of text for details and how it appears on small screens!! Need to change to list, decrease font size



[Back to table of contents](#table-of-contents)

### Bugs

- Modal confirm button was causing jsut first item in the list to be deleted. The Id needed to be passed into the function


- Issue with image upload. Resolved by storing in cloudinary, updating url in images collection
- validate on form not working on dropdown lists. Code wasn't inside the doc ready function

- search was not working. 
    - Only returning 1 result, should have multiple. No flash message if no results
    - Needed an else statment on template for no results, needed to drop index and set up so could search on all fields
    - Bug: the hide search container is hiding it but also actually performing a search. Button was needed to hide container and cancel search. 


- Search icon and link was haing when trying to cancel. Needed to add toggle jquery to the search icon.
  - And ensure that syntax was correct. Was previously using the hide on window load and jquery to show for click. Toggle works better   

- Setting admin: 
	Started with checking if session user was called Admin (user I had set up), works fine
	Tried to see if I could set this as a role in MongoDB. couldn't get it to work
	Tried assigning roles, not authorized
		1. used the db.createUser method in cli. Not authorised. also tried using the db.grantRolesToUser
		2. added a role field to document in the collection
		Then use the @roles.required decorator. Error AttributeError: 'Flask' object has no attribute 'user_manager'
	Talk to tutor. No experience with roles in mongodb but advised me to do the following
	have a user_type field in my user collection
	Set that as admin for the user who is admin
	Then do a check for that admin user type field. No route decorator needed, jsut a check if the user_type field contains admin
		I set a type field with normal for stnd user. Giving errors
Now have set is_admin to true/false. and updated code. Tested and no issues

- Admin delete function and user delete recommendation are basically repeats but could not get them to be in one function, with using if/else to redirect to diff pages.
If/else, kept deleting wrg recommendation, then while trying this with just s message, still not working, returning false
Needed to allow admin to be redirected to admin page, not the user page
Indentation corrected


Addin the materialize nav bar, I had a dropdown list under recommendations. Once I got the collpsed mobile menu to work, the dropdown wouldn't work for desktop view.
Needed to add a 2nd UL with id of dropdown2, and match this so the mobile...

card layout: need to standardise size or restrict content?? They are scaling up and down. layout issues when I tried to add margin to cards
headings to show on fromt of card and details to show on reveal. Was trying to make it so a user could click anywhere to close. Doesn't work. Added to cancel buttons
cards with no spacing: If giving margin, cards are not held on same row/colum,n as intened. Needed to wrap each card in its own column


card-reveal not working!. class to be added to correct elements. Cancel symbol added

added jquery for password match on confirmation But when user click on first password field, giving password match mesg
before anything input
Also, need to disable register button until validation complete!



Set up register functinality, working--> users are being insterted into db but allowing same user and password to register again..


Can still register even if passwords do not match. Need to disable submit button until passwords match

- layout of cards on large screen, change font size, number of columns on the div
Navbar fixed not working, disappears on scroll. Resolved by wrapping nav element only, not the header

- User being directed to wrong page after clicking dismiss option. Update the return route

- Image was not updating on the edit page, pass username, image name into the render tempalte, update the 
- Card buttons and reveal not working. Reviewed all code structure. Typos, but also styling and spacing needs to be updated. text hiding and overflowing
- Open-close collections on mage form. Was not opening correctly, Had two collections on the page. Reviewed code and what the materialize collections did and layout. 
Decided layout on a table looked better for this form

Bug with icon: url for method and upate filepath

Search limited, not fully searching. Moved within its own container

Testing registration form when the 'logged in user' functionality discovered was able to register without a username. Required field was missing from form

Search was showing for logged out. Restrict to session user



[Back to table of contents](#table-of-contents)

### Performance and accessibility Testing

#### Lighthouse testing

#### Accessibility

[Click here are the final WAVE reports](xx)

### Code Validation

[These are the final validation reports](xx)

### Defensive Design testing

[Back to table of contents](#table-of-contents)

[Link to README File](https://github.com/LisaHackett97/HiddenIrishTravels/blob/main/README.md)