# medical-scheduler/README.md

# Medical Scheduler

This project is a proof-of-concept automated scheduling system designed to act as an overlay on top of an existing medical examination scheduling website. The system is built with a backend in Python using Flask or FastAPI and a frontend in React or vanilla JavaScript.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

- **src/app.py**: Entry point of the backend application, initializes the Flask or FastAPI app.
- **src/auth/**: Contains authentication-related modules.
  - **session_manager.py**: Manages user sessions, including login and session persistence.
- **src/scraper/**: Implements web scraping logic.
  - **web_scraper.py**: Uses Playwright or Selenium to log in and scrape case data.
- **src/api/**: Defines API routes for handling requests.
  - **routes.py**: Handles requests related to case data and user authentication.
- **requirements.txt**: Lists Python dependencies required for the backend.
- **config.py**: Contains configuration settings for the backend application.

### Frontend

- **src/index.html**: Main HTML file for the frontend application.
- **src/js/**: Contains JavaScript files for the frontend.
  - **app.js**: Entry point for the frontend JavaScript application.
  - **api.js**: Functions for making API calls to the backend.
  - **components/**: Contains React components.
    - **SearchForm.js**: Component for inputting search criteria.
    - **CaseResults.js**: Component for displaying search results.
- **src/css/styles.css**: Styles for the frontend application.
- **package.json**: Configuration file for npm, listing dependencies and scripts.

## Features

- Real-time querying of the existing medical examination scheduling website.
- User authentication and session management.
- Web scraping to retrieve case data.
- Clean and modern user interface.

## Future Enhancements

- Integration of Twilio for client communication.
- Additional functionality for updating case statuses and adding notes.

## Getting Started

1. Clone the repository.
2. Navigate to the `backend` directory and install the required dependencies using `pip install -r requirements.txt`.
3. Start the backend server.
4. Navigate to the `frontend` directory and install the required npm packages using `npm install`.
5. Start the frontend application.

## License

This project is licensed under the MIT License.