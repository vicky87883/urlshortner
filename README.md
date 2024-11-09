URL Shortener
A URL shortener web application built with Django and PostgreSQL, allowing users to shorten long URLs into compact, easy-to-share links. This project includes features like custom short URLs, analytics tracking, and a clean interface for user interaction.

Features
URL Shortening: Quickly generate a short link for any long URL.
Custom Aliases: Option to customize the short URL alias for easy recognition.
Click Tracking: Monitor the number of times each shortened URL is accessed.
Expiration Dates: Set optional expiration dates for short URLs.
Analytics: Track link usage with analytics for better insights.
Technologies Used
Backend: Django
Database: PostgreSQL
Frontend: HTML, CSS, JavaScript (optional)
Getting Started
Prerequisites
Python 3.x
PostgreSQL
Django
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Configure PostgreSQL Database:

Create a PostgreSQL database and user.
Update your settings.py file with the database credentials.
Run Migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000 to see the app in action.

Usage
Create Short URLs: Enter the original URL and, optionally, a custom alias.
Access Shortened Links: Use the generated short link to redirect to the original URL.
Track Analytics: View usage statistics for each link, including the number of clicks.
Screenshots

Contributing
Contributions are welcome! Follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For questions or feedback, feel free to reach out via LinkedIn or create an issue in this repository.

