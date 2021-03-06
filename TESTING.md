# [Hidden Irish Travels](https://hiddenirishtravels.herokuapp.com/)

![site-mockup](README-assets/site-mockup.PNG)

## [Link to live site](https://hiddenirishtravels.herokuapp.com/)

This document will cover manual, compatability and validation testing. Issues found during development and bugs are also detailed.
I have included a section on the defensive design elements of the site I planned.

## **To open any links in a new tab, please press Ctrl + click**



## Table of Contents

- [Testing](#testing)
  - [Planning Approach](#testing-plan)
  - [Defensive Design](#Defensive-design)
  - [Functionality testing](#functionality-testing)
  - [Compatibility testing](#compatibility-testing)
  - [User stories testing](#user-stories-testing)
  - [Issues found during site development](#issues-during-development)
  - [Bugs](#bugs)
  - [Performance and Accessibility testing](#performance-and-accessibility-testing)
  - [Code Validation](#code-validation)
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


[Back to table of contents](#table-of-contents)

#### Defensive Design

The following are defensive design elements identified in planning. Each will be manually tested

- Non registered User should not be able to do the following:
  - Add/Edit/Delete a recommendation
  - Search site
  - View 'logged in' menu bar
  - View or access any admin options

As an non registered/logged out user, I manually viewed and tries to type urls to access the above. I did not get any issues and could not access menu/pages I wasn't authorised to.

- Error pages should be in place. 404. This and 500 page is in place, giving user a link back to the home page.

Pages in place, 404 pages are working

- Regular logged in user should not be able to do the following
  - View 'logged out' menu bar
  - View Admin Option in nav bar
  - View Admin Overview page
  - View or action any admin functionality: Edit fields/delete recommendations (other than own)/Delete a user

As an non admin/logged in user, I manually viewed and tried to type urls to access the above. I did not get any issues and could not access menu/pages I wasn't authorised to.
Was redirected back to home page with a message

- Back buttons/Home buttons or other navigation buttons should bring user back to the appropriate page, depending on their logged in/Out status

Each button clicked and brought user back to the expected page. Back buttons also checked that this didn't cause issues

- Required input fields on forms, gives message, through form field validation. 

This in place, user will get a message/feedback

- If Admin deletes a user, how does this affect active recommendations.	

Recommendation remains on the Home page as displayed. Data held in a deperate collection on the DB. Cannot be edited
		
- If Admin deletes/edits/adds fields, how does this affect active recommendations.
  - Data remains on the active card, until a user tries to edit.
  - If admin changes or deletes a field in error, this will not affect the displayed recommendations.
  - Part of future features would be that admin could have an option to change a field, and it would auto update the recommendations displayed to users.


[Back to table of contents](#table-of-contents)

### Functionality Testing

#### Features accessible across all pages 

| Feature:                        	|  Nav Bar                                                                                                                                       	|
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected:                       	|  Users can view and access menu items   according to their user status. <br>      Logged out can only view login/register/home links<br>      	|
| 	                        	| Logged in can view all recommendations options, home, search and logout.<br>     Admin user also has access to Admin option.                    	|
| Testing:                        	| View nav bar as each type of user. Attempt to manually type url for an option user shouldn't have access to, logged in options when user is logged out <br> |
|		                    	| Admin options for standard user
| Results:                        	|                                                                                                                                                  	|
| Home Page:                      	| As expected. User gets 404 message if they try to access a page not authorized by typing in url. Logged in user will get a flashed message        |
| Recommendations Page            	| As expected.                                                                                                                                           	|
| Admin Pages                     	| As expected.                                                                                                                                             	|
| Add Recommendation Page         	| As expected.                                                                                                                                             	|
| Edit/Delete Recommendation Page 	| As expected.                                                                                                                                            	|

| Feature:                        |  Nav Bar- Recommendations menu																|
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected:                       |  Users can view lower level menu for   recommendations.<br>     They can select add new/edit/delete<br>     Not available to logged out users.|  
| Testing:                        | click on Recommendations menu,   check 3 options are available.<br>     Click on each option on lower menu.<br>     Add new should open a blank recommendation form<br>     
|				  |Edit & delete should open prepopulated forms with relevant   buttons,<br>     and be restricted by username of logged in user.<br>     Cancel action buttons should also be available on forms |   
| Results:                        |                                                                                                                                                                                                                                                                                                                                                                            |   |
| Home Page:                      | As expected. |
| Recommendations Page            |As expected. |
| Admin Pages                     | As expected. |
| Add Recommendation Page         | As expected. |
| Edit/Delete Recommendation Page | As expected. |

| Feature:  | Modals                                                                                                  										|   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected: | Modals are in place across site: Registration info, add new recommendations, info for Admin page and confirmation of deletions for user and admin |
| Testing:  | Click on each modal to check info displays as expected. And for delete confirmations, actions completes  or cancels as expected. |   
| Results:                        |    Works as expected  |


| Feature:  | Footer                                                                                                  										|   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected: | All Users can view footer and content across all pages                                                  |   
| Testing:  | View nav bar menu on small, medium   and large screen sizes. <br>     (Same content for each user type). Viewed each page on small, medium and large screen sizes |   
| Results:                        |     |
| Home Page:                      | Footer displaying as expected |
| Recommendations Page            | Footer displaying as expected|
| Admin Pages                     | Footer displaying as expected|
| Add Recommendation Page         | Footer displaying as expected|
| Edit/Delete Recommendation Page | Footer displaying as expected|



| Feature:  | Flash Messages										|   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected: |Display under nav bar. Cancel icon to clear it, will fade out so that user will not have to refresh pg                                                
| Testing:  | Perform action on each page that prompts a flash message, eg login, search etc |   
| Results:              Performs as expected across all pages          |     


| Feature:  | go to top of page function |
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected: | All Users can view arrow icon once they have scrolled down the page, and click to bring to top of page                                                  |   
| Testing:  |View and click on each page where it is possible to scroll down. Test for 3 user types|   
| Results:                        |     |
| Home Page:                      | As expected.|
| Recommendations Page            | As expected. |
| Admin Pages                     | As expected. |
| Add Recommendation Page         | As expected.|
| Edit/Delete Recommendation Page | As expected. |

#### Log in Page
- Features only available to a logged out user

| Feature:  | LogIn form                                                                                                 |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Log In Form with 2 input fields and submit button                                                          |
| Testing:  | Update form with previously   created test user and press login button.<br>     Login should be successful |
| Results:  | Worked as expected                                                                                                      |

- There is also a link to registration page included. Clicked to test it beings user to page as expected. No issues |

#### Home   Page 

| Feature:    | Log In Button accessed through nav bar, with a link on registration page                                                                                                   |   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected:   | Logged out user click button, Log   in page should Open.<br>     Option not available for logged in/admin user 									|   
| Testing:    | Click button, view page which opens                                                                            									|   
| Results:    | Works as expected                                                                                                           									|   



| Feature:    | Register Button  accessed through nav bar, with a link on the login page                                                                                                								|   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected:   | Logged out user click button, Log   in page should Open.<br>     Option not available for logged in/admin user 									|   
| Testing:    | Click button, view page which opens                                                                            									|   
| Results:    |  Works as expected                                                                                                         									|  


| Feature:    | Log Out Button  accessed through nav bar                                                                                                									|   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected:   | "Logged in user clicks button, message is flashed and can then only view logged out options <br> 								|   
| Testing:    | Click button, view page which opens                                                                            									|   
| Results:    |    Works as expected                                                                                                          								| 
 

| Feature:    | Search                                                                                                								|   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected:   | User click search icon, types search details and clicks search button. Search results are displayed. User has option to clear search results. same as clearing a filter <br>     Option not available for loggedout user								|   
| Testing:    | Click button, perform a seach                                                                            									|   
| Results:    | Works as expected. Search result displayed, or messaged given when no result. clear search button resets the page                                                                                                        									| 

| Feature:  | Recommendations section                                                                                 |
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected: | Recommendations from all users,   image and content should be easy to view, <br>     with no ability to edit those for another user                                                     |
| Testing:  | View recommendations, try click   on another users recommendations.<br>     Test for 3 user types. Should be no difference. Admin would have to go   admin page to access functionality |
| Results:  |       Works as expected                                                                                                                                                                                   |   

| Feature:  | Add Recommendation button                                                                          |
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected: | Click on the + icon or select from nav bar. When selected, Blank   recommendation form opens.<br>     Option not available for logged out user |
| Testing:  | Click button, view page which opens. Add details. Test for user and admin user                                  |
| Results:  |  Works as expected. A new recommendation added can be viewed on the page.                                                                                                  |


#### Registration Page
- Features only available to a logged out user


| Feature:  | Registration  Form                                                                                                                                                          |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Form with 3 input fields and   submit button<br>     User can add username/password and register                                                                            |
| Testing:  | Form with 3 input fields and   submit button<br>     Review form is showing as expected.<br>     Update a test user and register.<br>     Registration should be successful |
| Results:  | view page and register a user with no issues. Password validation working                                                                                                                                                                       |

| Feature:    |Modal Pop up for instruction                                                                                    |   
|---------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------	|
| Expected:   | Info icon displayed which user can click and get instructions |   
| Testing:    | View icon, click and check details. Close modal                                                                           |   
| Results:    |    Works as expected                                                                                                            |   
 
- There is also a link to login page included. Clicked to test it beings user to page as expected. No issues


#### Users Page
- only accessible to logged in user

| Feature:  |          Recommendations Section                                                                                                  |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Recommendations which user previously uploaded, displaying with all details or a message is none |
| Testing:  | View page. Check created by on each recommendation: check are only for the logged in user. Add a new recommendation and check display updates      |
| Results:  | Works as expected                                                                                                                          |
 

| Feature:  | Add New Recommendation                                                                                                                                                                                                           |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | If Add New Option was selected :   Blank Recommendation form is presented to user.<br>User can select image, update 2 user input fields, select from 2 dropdown fields and click submit.<br> Action is successful |
| Testing:  | Select Add new from nav   menu/button.<br>     Form opens as expected, add details for a new recommendation. <br>     Click submit button<br>     New recommendation successful and appears in the recommendations section   |
| Results:  | Works as expected. Also tested by clicking on the add new button. Recommendations display on home and user page with details showing                                                                                                                                                                                                                        |

| Feature:  | Edit Recommendation                                                                                                                                                                                                                                       |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Edit Option under recommedation allows access to change a field. Only for recommendations uploaded by the logged in user <br> |
|         |Prepopulated form is shown with Edit button or cancel options. Once edit done or cancel selected, brought back to user page. <br>     Form opens with user details. User can click on a field to update details.   <br>  Click button to confirm edits. Updated details appear in recommendations   section |
| Testing:  | Select Edit option beside a recommendations,   change some details on form. Select submit. <br>  Review recommendations section on home page. Open edit page and check cancel option returns user to thier page                                                                                                                           |
| Results:  | Works as expected                                                                                                                                                              |

| Feature:  | Delete Recommendations                                                                                                         |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Delete Option button under each of the users recommendations. <br>  Modal opens asking user to confirm or dismiss. If confirm selected, recommendation is deleted and does not appear on user or home page. |
| Testing:  | Select Delete under a user recommendation, click dismiss. REcommendations still on page. Repeat but choose confirm. Recommendation is no longer accessible.      |
| Results:  | Works as expected                                                                                                                            |
 

#### Admin Overview Page
- Only accessible to admin user

Test that only the user set with is_admin true in db can access. Logged in as a standard user. Cannot view admin pages. Manually type url for admin.
User is redirected to home page with a Not authorized message.

| Feature:  | Upload   Button                                                                                      |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Button on admin page. When pressed, displays page with cloudinary widget for uploading images to cloud. URL displays on page                                            |
| Testing:  | Press button, Review widget displays on screen.<br> Check url displayed matches the upload image. |
| Results:  | Works as expected                                                                                                       |

| Feature:  | Manage Form fields Button                                                                                 |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Button on page. When pressed, displays Add/edit fields page                                               |
| Testing:  | Press button, Review details shown on screen, and the back to admin page, brings user back to the overall admin pg.<br> Press + and - for visitor and locations, and can view all.|
| Results:  | Works as expected                                                                                                        |


| Feature:  | Delete a user recommendation button                                                                       |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Button on page. When pressed, displays admin delete user page                                             |
| Testing:  | Press button, Review form shown   on screen.<br>     Press cancel. Check back to admin button brings admin back |
| Results:  | Works as expected                                                                                                       |

| Feature:  | Delete user button                                                                                        |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Button on page. When pressed, displays admin delete user page  with list of currently active users                                            |
| Testing:  | Press button, Review form shown   on screen.<br>    Check back to admin button brings admin back  |
| Results:  | Works as expected                                                                                                        |

#### Admin Delete User Page
- Only accessible to admin user

| Feature:  | Delete User form                                                                                                                                                                                               |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Table with list of users and time registered, delete button beside each user. Search/filter button, where user can type text or dates to narrow user list on view. Confirm deletion modal opens |
| Testing:  | Open page, check displays with user list.<br>  Find a user, either by time or user name. <br>     Press delete button on a user. Check dismiss take no action. Repeat and choose delete. Confirm user deleted as expected                                          |
| Results:  | Works as expected                                                                                                                                                                                                             |

-- Users recommendations remain on the home page only, but with no access to edit.                                                                                                                  |

#### Admin Add/Edit Fields Page
- Only accessible to admin user

| Feature:  | Option button to add new details                                                 |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | When pressed, displays 2 simple forms, for visitor type and location. Under each type, there is an add new and also a clear form option|
| Testing:  | Add a new visitor type, press add. Check new type is available to users on the recommendation dropdown form. <br> 
User redirected to the same page. Repeat for Locations. For both types, try add a detail you know already exists. Ensure it doesn't get duplicated and message displayed to user                                                                                                    |
| Results:  | Works as expected                                                                                                                    |


#### Admin Delete Recommendation Page
- Only accessible to admin user

| Feature:  | Delete Recommendation form                                                                                                                                   |
|---------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Expected: | Press button. Page appears with search and all user recommendations. Delete option beneath each. <br>Press delete button, modal appears. Check dismiss returns user to page. Repeat and confirm deletion. check receommendation no longer appears on page andhome page. |
| Testing:  | Open page, review form appears   as expected. <br>     Find a recommendation.                                                                                |
| Results:  | Works as expected                                                                                                                                                             |



[Back to table of contents](#table-of-contents)
### Compatibility Testing

- Site was manually tested on google chrome,microsoft edge, firefox and opera. No issues.

- I have access to IE10. Site has limited functionaility as site uses ES6. Recommended to use Microsoft edge rather than IE for best viewing experience
Recommended do not use IE10 to view site, please use Microsoft edge for best viewing experience

[Back to table of contents](#table-of-contents)
### User stories Testing

#### As a prospective user, I want to

| 	| Tests Performed | 
|------ | ----| 
| Understand the main purpose of the   site.| Paragraph on home and user pages explaing the site. Easy to see the recommendations on both pages | 
|View recommended places in Ireland  <br> and Northern Ireland. | Recommendations are displayed on home and users own page. Cards can be clicked on to see more details if provided | 
| Find out how to submit a recommendation | Information provided on a pop up modal | 
| Register as a user  | Easy to use registration form | 
| Be able to view the site on mobile/<br> desktop/tablet. | Site can be viewed on small/medium/large/extra large.  Layout and some headings are adjuted for different screen sizes.| |
| Be able to access all pages and navigate <br> without confusion, without too many clicks. | Clear options on home page and nav bar. Once user is registered and logged in, options are provided in the nav bar as well as some links on the page |

#### As a returning user, I want to

| 	| Tests Performed | 
|------ | ----|
| View recommended places in Ireland  <br> and Northern Ireland.| Recommendations are displayed on home and users own page. Cards can be clicked on to see more details if provided | 
| Log In| Easy to use login form provided | 
| Submit a recommendation | Add recommendation form provided in nav bar and on logged in users page. Hints and instructions included |
| Delete negative own recommendations  | User can view their own recommendations on their user page, where they can edit or delete previously uploaded | 
| Be able to view the site on mobile<br> desktop/tablet. | Site can be viewed on small/medium/large/extra large.  Layout and some headings are adjuted for different screen sizes | 
| Be able to access all pages and navigate <br> without confusion, without too many clicks. | Clear options on home page and nav bar. Once user is registered and logged in, options are provided in the nav bar as well as some links on the page |

							

#### As site owner I want to

| 	| Tests Performed |
|------ | ----| 
| Provide a place for users to recommend <br>unusual and unknown places to see on the island of Ireland. | Users can access site, and once register/loggedin can add a recommendation with location, visitory type and details. Drop down images are provided for user to choose from |
| Manage Categories | On the admin page, link to a manage fields form/page. Here admin user can view all current user and visitor types. Otions are provided to edit each of these, with an option at top of page to add new details |
| Update/add own personal recommendations | Admin or site owner functionality works same as standard user for updating and adding own recommendations| 
| Delete negative and misleading recommendations | On the admin page, link to a manage user recommendation page. Here admin user can view all current and can dlete if appropriate. Other business controls would need to be in place to manage the adminisatration of this process. Admin cannot edit another usrs recommendations.
| Delete users| On the admin page, link to a delete user page, where the admin is provided with a list of current users and option to search and delete.| 

[Back to table of contents](#table-of-contents)

### Issues during development

- Heroku not running after deployment. I checked all config variable, versions in requirements etc... Contacted tutorResolved. In app.py, I had "main" instead of "__main__"

- On mobile view, on add new, no spacing between buttons. Changed line height on the row to give mroe space to the materialze buttons 

- Icon on nav bar too big and was not appearing on all pages. Needed to set the url_for method for img src, and set height and width

- When showing search results, no user name on screen. Needed to pass username into the return function and needed to reset the form 
and target it by Id not class name in JS

- The footer on templates was not showing full width on all pages, specificially on the login template. Issue was that a closing div tag was missing. Resolved

- Issues with styling divs with card-title, on the card reveal. Top has icon to close and footer close has txt also. 
I needed to give id to the text in order to change font

- I needed to reduce space for recommendation images, so that more details could be viewed on front card, but large space was showing. 
This was related to card action footer and reveal top border is hidden. I needed to be more specific in targeting with css.
Using dev tools identified what to be targeted

- I was Was using the root color irish green for card reval, used color picker to change the transparency but then you could see txt on card. used color picker to choose a different shade of the green. Could not use any transparency settings

- Session user was set up on nav bar,but could not access recommendations dropdown. I needed to correct the data target, issue resolved

- Closed app while still logged in. When re-opened, was still showing logged in. 
session cookies cleared when full browser window closed but not when tab closed. Timer

- Looking at length of text for details and how it appears on small screens!! I needed to change to list, decrease font size.

- I wanted to give users the option to either upload own images or have a choice of default images. I was using cloudinary to do this but did not have the knowledge/time to implement functionality for user to upload own images. 
	- Images are stored in Cloudinary, where Admin user with the account details, can upload further images.
	- Image URL from Cloudinary is manually updated on the images collection in the DB.
	- Functionality is set up, so user can view and select image name, and this is the linked to the field for the image URL in mongo.
  - Instruction are on the admin upload page. It is assumed that an admin user would have access to the cloudinary and mongo accounts for the site.
  - Details of the uploaded image are accessed through an input field on the upload page or through cloudinary account.

- After testing and getting user feedback, some images were showing stretched on different screen sizes, along with the 2 images on home and user pages.
I needed to resize all, and set the height and width, as well as the object cover properties (home/user pg imgs) so images displayed for a better user experience. Some images may still need to be compressed further. Will work through this in order to show increased lighthouse scores.

[Back to table of contents](#table-of-contents)

### Bugs

- Modal confirm button was causing just the first item in the list to be deleted. The Id needed to be passed into the function and issues resolved

- Issue with image upload. Resolved by storing in cloudinary, updating url in images collection on the DB. Resolved

- Validate on form not working on dropdown lists. Code wasn't inside the doc ready function. Resolved

- search was not working. 
    - Only returning 1 result, should have multiple. No flash message if no results
    - Needed an else statment on template for no results, needed to drop index and set up so could search on all fields
    - Bug: the hide search container is hiding it but also actually performing a search. Button was needed to hide container and cancel search. Resolved

- Search icon and link was showing display issues when trying to cancel. Needed to add toggle jquery to the search icon.
  - And ensure that syntax was correct. Was previously using the hide on window load and jquery to show for click. Toggle works better  Resolved 

- Setting admin: 
	Started with checking if session user was called Admin (user I had set up), works fine
	Tried to see if I could set this as a role in MongoDB. couldn't get it to work
	Tried assigning roles, not authorized
		1. used the db.createUser method in cli. Not authorised. also tried using the db.grantRolesToUser
		2. added a role field to document in the collection
		Then use the @roles.required decorator. Error AttributeError: 'Flask' object has no attribute 'user_manager'
	  - Talk to tutor. No experience with roles in mongodb but advised me to do the following
	    - have a user_type field in my user collection
	    - Set that as admin for the user who is admin
	Then do a check for that admin user type field. No route decorator needed, jsut a check if the user_type field contains admin
		I set a type field with normal for stnd user. Giving errors
Now have set is_admin to true/false. and updated code. Tested and no issues. Resolved

- Admin delete function and user delete recommendation are basically repeats but could not get them to be in one function, with using if/else to redirect to diff pages.
If/else, kept deleting wrg recommendation, then while trying this with just a message, still not working, returning false
I needed to allow admin to be redirected to admin page, not the user page
Indentation was corrected. Resolved

- Adding the materialize nav bar, I had a dropdown list under recommendations. Once I got the collpsed mobile menu to work, the dropdown wouldn't work for desktop view.
Needed to add a 2nd UL with id of dropdown2, and match this so the mobile navbar displays correctly. Resolved

- On card layout: issue with deciding to standardise size or restrict content. Cards were scaling up and down. Layout issues when I tried to add margin to card
headings to show on front of card and details to show on reveal. Was trying to make it so a user could click anywhere to close. Doesn't work. Added to cancel buttons
cards with no spacing: If giving margin, cards are not held on same row/column as intened. Needed to wrap each card in its own column. To close the reveal I have a cancel icon at top and bottom of card. Resolved

- The card-reveal was not working. To resolve, the class added needed to be added to correct elements. Cancel symbol also added.

- I added jquery for password match on confirmation But when user clicked on first password field, giving password match mesg
before anything input. Resolved, password check doesn't happen and display message until a user has input first password field

- Set up register functinality, working--> users are being insterted into db but allowing same user and password to register again. Resolved, function updated.

- Can still register even if passwords do not match. Need to disable submit button until passwords match. Resolved. Validation/functions checks working as planned now.

- Layout of cards on large screen, change font size, number of columns on the div, Resolved

- Navbar fixed not working, disappears on scroll. Resolved by wrapping nav element only, not the header. Resolved

- User being directed to wrong page after clicking dismiss option. Update the return route. Resolved

- Image was not updating on the edit page, pass username, image name into the render template. Resolved

- Card buttons and reveal not working. Reviewed all code structure. Typos, but also styling and spacing needs to be updated. Resolved.

- Open-close collections on manage form. Was not opening correctly, Had two collections on the page. Used jquery, toggle to resolve.
Reviewed code and what the materialize collections did and layout. Decided layout on a table looked better for this form. Resolved

- Bug with icon: Resolved by adding url for method and upate filepath. Resolved

- Search functionality was limited, not fully searching. Moved within its own container and set up index to search on all fields. Resolved

- When testing registration form, for the 'registration' functionality, I discovered was able to register without a username. Required field was missing from form. This resolved the issue.

- Search was showing for logged out. Restrict to session user. Resolved

- After fixing bugs, user page edit/delete btns had floated out of the card
Use compare site to id where difference in last few commits. Needed to update the id'S on title and details, that I removed when fixing validation. 
Also changed the columns for large screen. Resolved.

- When testing the recommendation forms, discovered that the Add new allowed 500 chars on the details. But edit form was restirected to 200. Causes issues for users when trying to update details. Resolved by updating the restriction on the edit form.

#### Bug/issue not fully resolved

Cloudinary is used for the admin to upload images. Result data was being console logged where admin can access the info. But I found a resolution, where this data can be updated to an input field on the upload page. Tested and no issues. Though admin has to copy the data before refreshing page
I did not have the time to pass the url info to a form in order to upload info directly to DB, instead of having to manually update these image details.

- Cloudinary not defined message shows in the console if user is on any page other than the upload page. Tried various things to resolve. Included the script tags in base template and also in individual templates. But this caused further errors to show in the console. Due to time constraints, decided to leave the script on the uplaod page. Not causing any other issues

[Back to table of contents](#table-of-contents)

### Performance and accessibility Testing

#### Lighthouse testing

When code finished, ran lighthouse reports on mobile and desktop
Version one score across the site on mobile were as follows:
- Performance 76 to 94
- Accessibility 77 to 93
- Best Practices 67 to 87
- SEO 96 TO 100 

Review worst score first: 67 on Home Page
Most of scores on this page/type relate to images. Bulk resize images and compress, which has improved scores.
Aria labels updated improved scores for accessibility]

Version two score across the site on mobile were as follows:
- Performance 77 to 95
- Accessibility 89 to 97
- Best Practices 87 to 93
- SEO 96 TO 100 

Desktop score across the site were as follows:
- Performance 92 to 100
- Accessibility 89 to 97
- Best Practices 87 to 93 (Improved after cloudinary url function update)
- SEO 100 

To try and improve scores, I resized images and corrected the aspect ratios. The aspect ratio correction improved the best practice scores.

After running the attached reports, I found a resolution to displaying cloudinary url on the page, rather than in the console. This has improved all the nest practice scores to over 90. Many of the other things bringing down score were related to materialize and cdns.

[Reports for Mobile](README-assets/Lighthouse-mobile.pdf)
[Reports for Desktop](README-assets/Lighthouse-desktop.pdf)

#### Accessibility

I had a number of contrast issues.
  Changed colour of text on navbar, text on cards to the root main text colour. 
  Used the color picker to choose darker colors for footer icons and inoput labels. This cleared all the contrast errors

- Errors relating to empty links and buttons. Aria labels needed to be updated across the site

- Some warnings showing on each pge
  - Links: due to having code for navbar and mobiel side nav bar
  - Alt attributes on images repeating. This is due to the fact that images are uploading from db, with a standard alt text


### Code Validation
Ran code through all validatiors for python, js, html and css once miost of the coding was complete.
Errors in relation to some stray tags within code. Updated these and ran through again

JS:
Cloudinary undefined.Console error when on any other page that the upload

3 unused vars. Associated with onclick assigned to elements

Unexpected use of ~. But this is required in order for the search functionm to work

Pep8:
continuation line over indented for visual indent. If I tried to change this indent, just created an over indent message. code is related to line above

CSS:
No errors

HTML: I first validated by text only on each page. I cleared up error with stray and unclosed tags. remiang errors relate to jinja templating.
To validate by uri method
Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections. TO BE REVIEWED
Duplicate IDs are the remaining warnings

recommend-title id was repeated across, add new and edit. Change add new pg is to recommend-title1. Updated on the edit route. Tested ok
Change is on the admin delete page to recommend-tt#itle3.
Change is on the user delete page to recommend-tt#itle4.
all working as expected.
Ran through validator again. Still error warning as they are being picked up frm the new recommendations added/held. all have the same id. 
Needed to remove the ID from User page and home page for title and details. Not needed for display. On the reveal-close, changed it to a class, needed for styling


When all feature, user story testing etc fully completed. Rerun though validators. Any changes would be noted here

[HTML](README-assets/html-validator.PNG)
[CSS](README-assets/css-validator.PNG)
[JS](README-assets/js-validator.PNG)
[PEP8](README-assets/pep8-validator.PNG)

[Back to table of contents](#table-of-contents)

[Link to README File](https://github.com/LisaHackett97/HiddenIrishTravels/blob/main/README.md)