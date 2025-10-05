# frontend/README.md

# Medical Scheduler Frontend

This is the frontend part of the Medical Scheduler project, which serves as a proof-of-concept automated scheduling system. The frontend is built using JavaScript and interacts with the backend to provide a seamless user experience for searching and managing medical examination cases.

## Project Structure

- `src/`
  - `index.html`: The main HTML file for the application.
  - `js/`: Contains JavaScript files for application logic.
    - `app.js`: Entry point for the frontend application.
    - `api.js`: Functions for making API calls to the backend.
    - `components/`: Contains React components.
      - `SearchForm.js`: Component for inputting search criteria.
      - `CaseResults.js`: Component for displaying search results.
  - `css/`: Contains styles for the application.
    - `styles.css`: Main stylesheet for the frontend.

## Getting Started

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the frontend directory:
   ```
   cd medical-scheduler/frontend
   ```

3. Install dependencies:
   ```
   npm install
   ```

4. Start the development server:
   ```
   npm start
   ```

## Usage

- Open `index.html` in your browser to access the application.
- Use the search form to input criteria and view case results.

## Future Enhancements

- Implement functionality for the action buttons in the case results.
- Integrate Twilio for client communication.
- Improve UI/UX with additional styling and components.

## License

This project is licensed under the MIT License. See the LICENSE file for details.