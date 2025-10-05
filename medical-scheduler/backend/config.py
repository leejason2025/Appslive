# backend/config.py

class Config:
    # Base URL for the existing medical examination scheduling website
    BASE_URL = "https://appslive.com/Client_View_Status.aspx"
    
    # Credentials for logging into the existing site
    USERNAME = "your_username_here"
    PASSWORD = "your_password_here"
    
    # Other configuration settings can be added here
    TIMEOUT = 10  # Timeout for web scraping requests
    DEBUG = True  # Set to False in production environment

# You can extend this class for different environments (development, testing, production) if needed.