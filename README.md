This project implements a RESTful API backend for a blogging platform. Users can create, read, update, and delete posts. The API also provides endpoints for filtering posts by author or creation date, pagination, authentication, and authorization mechanisms.

Endpoints
  1. Retrieve All Posts
  URL: /posts/
  Method: GET
  Description: Retrieve a list of all posts.
  Authentication: Not required
  2. Retrieve Single Post
  URL: /posts/{post_id}/
  Method: GET
  Description: Retrieve a single post by its ID.
  Authentication: Not required
  3. Create Post
  URL: /posts/
  Method: POST
  Description: Create a new post.
  Authentication: Required
  Request Body:
json
Copy code
{
  "title": "string",
  "content": "string"
}
4. Update Post
URL: /posts/{post_id}/
Method: PUT
Description: Update an existing post.
Authentication: Required
Request Body:
json
Copy code
{
  "title": "string",
  "content": "string"
}
5. Delete Post
URL: /posts/{post_id}/
Method: DELETE
Description: Delete a post by its ID.
Authentication: Required
6. Filter Posts
URL: /posts/?author={author_id}&date={yyyy-mm-dd}
Method: GET
Description: Filter posts by author ID and/or creation date.
Authentication: Not required
Authentication
The API uses token-based authentication.
Users can obtain an authentication token by logging in with their username and password.
Authentication tokens are included in the request headers for authenticated endpoints.
Pagination
Pagination is implemented for retrieving a large number of posts.
The default page size is 10 posts per page.
How to Run the Project
Clone the repository:
git clone https://github.com/your-username/blogging-platform.git
Navigate to the project directory:
cd blog
Install dependencies:
pip install -r requirements.txt
Apply database migrations:
python manage.py makemigrations
python manage.py migrate
Run the development server:
python manage.py runserver
The API will be accessible at http://localhost:8000/.
Testing
Unit tests are provided to validate the functionality of the application.
Run the tests using the following command:
python manage.py test

