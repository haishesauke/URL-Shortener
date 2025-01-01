# URL Shortener

A simple URL shortener web application built with Flask and SQLite. This application allows users to convert long URLs into short, easily shareable links.

## Features

- Convert long URLs into short, unique URLs
- Persistent storage using SQLite database
- Simple and clean web interface
- Automatic redirection from short URLs to original URLs

## Technologies Used

- Python 3.x
- Flask
- SQLAlchemy
- Hashids
- SQLite

## Project Structure
url-shortener/
├── app.py
├── urls.db
└── templates/
└── index.html

## How It Works

1. When a user submits a URL, it's stored in the SQLite database
2. A unique identifier is generated using Hashids
3. The short URL is created by combining the host URL and the unique identifier
4. When someone visits the short URL, they are automatically redirected to the original URL

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Hashids](https://hashids.org/)
