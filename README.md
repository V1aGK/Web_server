# Web_server

This Python script leverages the Flask web framework to create a simple web form for collecting user input and saving it to both a text file (database.txt) and a CSV file (database.csv). The application consists of routes for rendering HTML templates, handling form submissions, and writing data to files.
Features:

    Web Form: Implements a web form with fields for email, subject, and message input.

    Data Storage: Saves user-submitted data to both a text file (database.txt) and a CSV file (database.csv).

    Error Handling: Includes error handling to ensure data is saved properly, providing feedback to the user.

    Template Rendering: Uses Flask's render_template to display HTML templates, enhancing the user experience.

How it Works:

    The Flask application is initiated, and routes are defined for rendering HTML pages and handling form submissions.

    The html_page route dynamically renders HTML templates based on the provided page name.

    Two functions, write_to_file and write_to_csv, are defined to write user-submitted data to text and CSV files, respectively.

    The /submit_form route processes form submissions using the request object. If the submission is successful, the data is written to the files, and the user is redirected to a thank-you page (/thankyou.html). Otherwise, an error message is displayed.

Usage:

    Run the Flask application, and navigate to the provided routes to access the web form and submit data.

bash

python app.py

Note:

This Flask application serves as a foundational example for building web forms and handling user input. It can be extended and customized for various use cases, such as contact forms, surveys, or data collection.
