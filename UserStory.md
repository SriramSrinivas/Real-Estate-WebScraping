#UserStory

1. As a user, I want to login to the website
Acceptance criteria :- User can login and logout
Mis User stories :- User information can be stolen, and malicious user can steal the data.
Mitigation Criteria:- Django admin will keep users info same, should kick the user out after 45 minutes of login and force them to change the password every 90 days.
2. As a user, I want to browse and navigate to the website
Acceptance criteria :-Website should be responsive, easy to navigate and mobile friendly
Mis User stories:- User can access information which should be only avilable to user
Mitigation Criteria:- Secure Rest End points
3. As a user, I can define my search criteria and get data
Acceptance criteria :-User can enter search criteria and get results back
Mis User stories:- Can delete ES index accidentaly or do adhoc ES search
Mitigation Criteria:- Restrict user access to ES
4. As a user, I can sort the data and make comments on the data
5. As a user, I can Logout from the application
6. As a user, I can send email or forward data as an attachment
7. As a user, I can send text message to any phone numbers
8. As an administrator, I can run the web scrapping script to fetch data and store in ES
9. As an administrator, I can delete/add data from ES
