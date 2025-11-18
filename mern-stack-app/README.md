# MERN Stack App

This is a full-stack MERN (MongoDB, Express.js, React, Node.js) application demonstrating user authentication with JSON Web Tokens (JWT), component integration, and a Movie Review user interface with state management.

## Tasks Covered
- Implement user authentication in a MERN stack application using JSON Web Tokens (JWT).
- Demonstrate the ability to install and configure the MERN stack components and ensure they work together correctly.
- Create a functional web application demonstrating the integration of all four technologies.
- Develop a user interface for a "Movie Review" application using React.js, including components for displaying a list of movies, adding new reviews, and filtering by genre, with state management.

## Features
- **User Authentication**: JWT-based login and registration.
- **Movie Reviews**: List movies, add reviews, filter by genre.
- **State Management**: React state for managing UI and data.
- **Full-Stack Integration**: Seamless connection between frontend and backend.

## Prerequisites
- Node.js (v14 or higher)
- MongoDB (running locally or cloud instance)
- npm or yarn

## Installation
1. Navigate to the project directory:
   ```
   cd mern-stack-app
   ```
2. Install dependencies for both client and server (assuming standard MERN structure):
   ```
   npm install
   ```
   If separate client/server folders exist, install in each.

## Usage
1. Configure MongoDB connection and JWT secret in environment variables.
2. Start the backend server:
   ```
   npm run server
   ```
3. Start the React frontend:
   ```
   npm start
   ```
4. Access the app at `http://localhost:3000`.

## Components
- **Authentication**: Login/Register forms with JWT.
- **Movie List**: Display movies with reviews.
- **Add Review**: Form to submit new reviews.
- **Filter**: Filter movies by genre.

## Technologies
- **Frontend**: React.js
- **Backend**: Express.js, Node.js
- **Database**: MongoDB
- **Authentication**: JWT

## Notes
- Ensure all MERN components are properly configured and communicating.
- This is a demonstration app; enhance with validation, security, and testing for production use.
