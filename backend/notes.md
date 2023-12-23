## Task 1A: The Network

> [YT session by DevClub](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjJUdHFvUVlCTU5YazNxS09PUVhUZGpOZk5oZ3xBQ3Jtc0tsQk94eGVYcDc0SU5sMUkzX0hsaEVPaGkwYkFzSkY0dmtyUXh1czNQZ3pJak1pTGtCemJKVXdoUGJZeXRtZGpaUEdSLVZneGk4S0QwX1NXQUFIckFjcFFEVXdkOHVudGw0d0w1RG13QmNiMkNDWHJCWQ&q=https%3A%2F%2Fdocs.google.com%2Fpresentation%2Fd%2Fe%2F2PACX-1vQbtDDGQonkIoGu68VrINL2s3sQcfiH5XVnk-iU26nk16DFBGsDabichsqhdtBvowPvpxaIbFLAV2h3%2Fpub%3Fslide%3Did.p&v=T4o1oxfz02w)
### Need of backend
- Dynamic webpages use user info, cookies, and sessions to render data. Servers run programs taking parameters from clients.
- Three tier architecture:  
    - Client
    - Server
    - Database
### Databases:
  - json/csv good for small data,
  - SQL for big relational data (check sqlite docs), sql injection
  - Store data based on queries required.
  - eg. can also store how many times people change questions in moodle quiz!

### Networks:
  > Mozilla MDN is a good reference
  - cookies and sessions: client store user id, share to server to identify user, session cookie identifies anonymous users.
  - auth. systems: username-password-CSRF sent to server, post auth server sends auth token to client for further communication by client also, read session hijacking.  
  The client uses auth token in every request from now on, omitting repeated use of credentials.
  - server stores user data during sessions. like session id, cart items, items clicked...

### VirtualEnv
  - Helps to maintain different versions if needed, less messy
  - python -m venv env_name

### Django
- SETUP DJANGO USING POWERSHELL
- Project vs app
- views takes parameters and passes to templates. html dynamic to servers' reqmts.
- GRADING DEMO
- models: interface to SQL queries  
<img width="327" alt="image" src="https://github.com/kohinoor23/summer-of-code-2023/assets/61497490/4b8fac3c-130b-4417-a494-16dcb2c3039a">
  
  - foreign key
  - migrations (still not clear how this works @todo)
      - makemigrations: create SQL commands for defined models
      - migrate: run the SQL commands
        REMINDER: play a lot with the documentation


> Devtools: Inspect
- analyse resources downloaded, throttle the network, block resources
- [For more info](https://developer.chrome.com/docs/devtools/)

 
 - BONUS: telnet/SSH establish connection to a remote server. use wget to send get requests to server using cmd, nc/curl for similar communication.   
    JWTs are alternate method for authorization. They use public/private key pairs, usualy to connect two systems.

## Task 1B : URL Shortener  
### Django Refresher
- Learning Django again. Just cant remember it in one go.
```powershell
python -m venv env_name
.\env_name\Scripts\activate
```
- all the databases stored in _db.sqlite3_
- A basic flow: the user types a URL in the browser, and the client sends a HttpRequest to the server. The server takes that URL and maps to a view function. This function gives the HttpResponse, to be sent back to the client. HttpResponse is just a wrapper for the protocol formalities and the webpage.
- templates folders should be added to TEMPLATES in settings.
- define variables as {'va_name': source_var}, access as {{ va_name }}
- For models, see [this](https://docs.djangoproject.com/en/5.0/topics/db/models/).  
  - model ~ objects ~ tables ~ each instance a row in table
  - when defining new model, makemigrations creates a verbose intermediate of table creation command
  - The migrate command creates SQL commands and executes them.

### Simple http.server
```powershell 
python -m http.server 8000
```
[YT Video](https://www.youtube.com/watch?v=DeFST8tvtuI)

- The assignment is just a play with the path during GET/POST requests. 
- GET request is like (on powershell)
  ```powershell
  curl http://localhost:8000/url
  ```
- POST request is like
  ```powershell
  Invoke-WebRequest -Uri http://localhost:8000/url -Method POST
  ```
- Usage of URL shortener:
  - run the http server
  - write a post request in cmd, with required url and shortcode
  - use get request by typing the url in the browser. (curl isnt working for now)
  
---

## Task 2: Django
- See notes in week 2, covers pretty much of the thinking while creating. Extensive use of copilot bot also.

