# [Hidden Irish Travels](xx)

## site mock Up
## link to live site

Paragraph about document: testing

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

- Error pages should be in place. 405

- Regular logged in user should not be able to do the following
  - View logged out menu bar
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

| 	| Tests Performed | Results |
|------ | ----| ---- |
| Understand the main purpose of the   site.| | |
|View recommended places in Ireland  <br> and Northern Ireland. | View recommendations section. Scroll through to view all| |
| Find out how to submit a recommendation | | |
| Register as a user  | | |
| Be able to view the site on mobile/<br> desktop/tablet. | User can view the site on mobile/tablet/laptop/desktop screensizes without issues. | |
| Be able to access all pages and navigate <br> without confusion, without too many clicks. | | |

#### As a returning user, I want to

| 	| Tests Performed | Results |
|------ | ----|---- |
| View recommended places in Ireland  <br> and Northern Ireland.| View recommedations section, when logged in and out| |
| Log In|Select log in from nav bar access the site.<br> Logged out of site and use log in button to access | |
| Submit a recommendation |Select Add new recommendations and submit. <br> View new on the recommendations section. |
|			  | Repeated test with button on home page.| |
| Edit a previously submitted recommendation | | |
| Delete negative / misleading  user <br> recommendations  | | |
| Delete Users | | |
| Be able to view the site on mobile/<br> desktop/tablet. | | |
| Be able to access all pages and navigate <br> without confusion, without too many clicks. |A clear navbar with links to all areas of the site is provided on all pages.<br> This is fixed to the top of the page for easy access.
|											    |Recommendations and search options are clearly avilable when logged in
|											    |Easy to use "go to top" button to avoid user having to scroll | |								

#### As site owner I want to

| 	| Tests Performed | Results |
|------ | ----| ---- |
| Provide a place for users to recommend <br>unusual and unknown places to see on the island of Ireland.| | |
| Manage Categories | | |
| Update/add own personal recommendations | | |
| Delete negative and misleading recommendations | |
| Delete users| | |

[Back to table of contents](#table-of-contents)

### Issues during development


[Back to table of contents](#table-of-contents)

### Bugs


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