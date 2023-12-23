The app layout is as follows:
    - Home page : signup/login
    - Post login auth: catalogue
When the user accesses the empty URL, we check if the user is logged in, if yes, they are redirected to catalogue, otherwise login page. This page also has a link to the signup page. The user can signup, and get redirected to the login page.
Updates: 
- Now, the catalogue is available to all. So the catalogue page will have a login option if not logged in. If logged in, there will be a add product option as well. 
  - Home page : ~~signup/login~~ catalogue as guest