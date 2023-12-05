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
  - auth. systems: username-password-CSRF sent to server, post auth server sends auth token to client for further communication by client also, read session hijacking

### VirtualEnv
  - Helps to maintain different versions if needed, less messy
  - python -m venv env_name

## Django
- SETUP DJANGO USING POWERSHELL
- Project vs app
- views takes parameters and passes to templates. html dynamic to servers' reqmts.
- GRADING DEMO
- models: interface to SQL queries
  - foreign key
  - migrations




 
