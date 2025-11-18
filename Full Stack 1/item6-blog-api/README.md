# Item 6: Blog REST API

This is a REST API for a blog application using Node.js and Express.

## Features

- CRUD operations for blog posts.
- Uses MongoDB for data storage.

## Installation

1. Ensure Node.js and npm are installed.
2. Run `npm install` in the project directory.

## Running the Application

Run `node server.js` to start the server. The API will be available at http://localhost:5001.

## Endpoints

- GET /posts - Get all posts
- GET /posts/:id - Get single post
- POST /posts - Create new post
- PUT /posts/:id - Update post
- DELETE /posts/:id - Delete post

## Description

- Uses Express for routing.
- Mongoose for MongoDB interaction.
- CORS enabled for cross-origin requests.
