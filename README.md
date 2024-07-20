# Blog App

## Overview

The Blog App is a web application built using Flask and AJAX. It allows users to interact with blog posts, including reading, creating, and commenting on posts. The application leverages AJAX for dynamic content updates without requiring full page reloads.

## Features

- **User Authentication**: Sign up, log in, and manage user sessions.
- **Dynamic Blog Interaction**: Create, read, and comment on blog posts using AJAX for seamless interactions.
- **Profile Management**: View and manage user profiles with an intuitive interface.
- **Responsive Design**: A Linux-themed design for a unique and engaging user experience.

## Technologies

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, AJAX (jQuery)
- **Database**: [Your database solution, e.g., SQLite, PostgreSQL]
- **Form Handling**: Flask-WTF
- **Session Management**: Flask sessions

## Usage

- **Home Page**: Access the blog's home page, which displays recent posts and a login form.
- **Sign Up**: Register a new account using the sign-up form.
- **Log In**: Authenticate and access user-specific features.
- **Create Post**: Use the provided form to create new blog posts.
- **Comment**: Add comments to existing posts via AJAX.
- **Logout**: Clear session and logout

## AJAX Endpoints

- **POST /home/post**: Add a new blog post.
- **POST /home/comment**: Add a comment to a blog post.
- **GET /home/logout**: Log out and clear the session.
- **GET /home/reading_page**: Retrieve and render a blog post page dynamically.
- **PUT /home/update_user**: Updates user information
- 
## API Endpoints(CORS)

- **GET /api/client/number_of_users**: returns the total numbers of users
- **GET /api/client/users**: returns all users
- **GET /api/client/user/<id>**: returns specific user with the given ID
- **GET /api/client/post/<id>**: returns specific post with the given ID
- **GET /api/client/user_comment/id**: returns all comments made by specific user with the given ID
- **GET /api/client/post_comment/id**: returns all comments under specific post with the given ID
