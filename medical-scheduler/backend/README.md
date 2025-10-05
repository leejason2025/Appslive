# backend/README.md

# Medical Scheduler Backend

This is the backend component of the Medical Scheduler project, which serves as a proof-of-concept automated scheduling system. The backend is built using Python and utilizes Flask or FastAPI for handling requests and managing user sessions.

## Project Structure

- **src/**: Contains the source code for the backend application.
  - **app.py**: Entry point of the application, initializes the web framework and sets up routes.
  - **auth/**: Module for handling user authentication and session management.
    - **session_manager.py**: Functions for managing user sessions.
  - **scraper/**: Module for web scraping functionality.
    - **web_scraper.py**: Implements the logic for logging into the existing medical examination scheduling website and scraping case data.
  - **api/**: Module for defining API routes.
    - **routes.py**: Contains the API endpoints for case data and user authentication.

- **requirements.txt**: Lists the Python dependencies required for the backend application.

- **config.py**: Configuration settings for the backend application, including URLs and credentials.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the backend directory:
   ```
   cd medical-scheduler/backend
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the backend application, execute the following command:
```
python src/app.py
```

## Future Development

This project is a proof-of-concept and will be expanded with additional features, including:
- Integration with Twilio for SMS notifications.
- Enhanced user interface for managing case data.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.