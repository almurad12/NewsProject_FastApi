***Project Name: News project with authentication using FastApi
1.	Clone github repository
2.	Activate virtual environment (myenv) then install requirments.txt
3.	Then go to news_api_app and run this project uvicorn app.main:app --reload using this command
4.	You can get full swagger documentation http://127.0.0.1:8000/docs this url



*Login
POST /login
Description: Authenticates a user and returns a token.
Request Body (JSON):
{
  "username": "user1",
  "password": "yourpassword"
}
Response (JSON):
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}



*Registration
Description: Registers a new user.
Request Body (JSON):
{
  "username": "newuser",
  "password": "securepassword",
  "email": "user@example.com"
}


*GET /users/me
Description: Retrieves the currently authenticated user.
Authorization: Bearer Token (JWT) required.
Response (JSON): {
  "id": 1,
  "username": "user1",
  "email": "user@example.com"
}
*GET /news
Description: Fetch all news articles from your data source or database.
Response (JSON):

{
  "status": "ok",
  "articles": [
    {
      "title": "Example News",
      "description": "Summary",
      "source": "Source Name"
    }
  ]
}



*POST /news/save-latest
Description: Fetches the latest news from an external API and saves it to the database.
Response (JSON):
201 created

*GET /top-headlines/country/{country_code}
Description: Get top headlines by country.
Path Parameter:

country_code (string) — e.g., us

Response (JSON):

{
  "status": "ok",
  "articles": [...]
}

*GET /news/headlines/source/{source_id}
Description: Get top headlines from a specific news source.
Path Parameter:

source_id (string) — e.g., bbc-news,

Response (JSON):
{
  "status": "ok",
  "articles": [...]
}

*GET /news/headlines/filter
Description: Get top headlines from a specific news source.
Path Parameter:
source_id (string) — e.g., bbc-news
country(string)  — e.g., bbc-news
Response (JSON):
{
  "status": "ok",
  "totalResults": 33,
  "articles": [...],
}
**Testing
First news_api_app/test
There is 2 test file 1. test_auth.py 2.test_news.py
For run test using commandd pytest test_news.py






