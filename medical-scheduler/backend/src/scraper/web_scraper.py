def login_to_site(browser, username, password):
    # Navigate to the login page
    browser.goto("https://appslive.com/Client_View_Status.aspx")
    
    # Fill in the login form
    browser.fill("input[name='username']", username)
    browser.fill("input[name='password']", password)
    
    # Submit the login form
    browser.click("button[type='submit']")
    
    # Wait for navigation after login
    browser.wait_for_navigation()

def scrape_case_data(browser, search_params):
    # Fill in the search form with provided parameters
    browser.fill("input[name='last_name']", search_params.get('last_name', ''))
    browser.fill("input[name='first_name']", search_params.get('first_name', ''))
    browser.fill("input[name='case_number']", search_params.get('case_number', ''))
    browser.fill("input[name='policy_number']", search_params.get('policy_number', ''))
    browser.fill("input[name='applicant_dob']", search_params.get('applicant_dob', ''))
    
    # Submit the search form
    browser.click("button[type='submit']")
    
    # Wait for results to load
    browser.wait_for_selector(".results")

    # Scrape the case data
    case_data = []
    results = browser.query_selector_all(".results .case")
    for result in results:
        case_info = {
            "applicant_name": result.query_selector(".applicant-name").inner_text(),
            "insurance_company": result.query_selector(".insurance-company").inner_text(),
            "agent_name": result.query_selector(".agent-name").inner_text(),
            "status_description": result.query_selector(".status-description").inner_text(),
            "case_number": result.query_selector(".case-number").inner_text(),
            "appointment_date": result.query_selector(".appointment-date").inner_text(),
            "image_available": result.query_selector(".image-available").inner_text(),
            "packet_available": result.query_selector(".packet-available").inner_text(),
            "quick_update": result.query_selector(".quick-update").inner_text(),
            "applicant_zip_code": result.query_selector(".applicant-zip-code").inner_text(),
        }
        case_data.append(case_info)
    
    return case_data

# Example usage:
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     login_to_site(page, "your_username", "your_password")
#     search_params = {
#         "last_name": "Doe",
#         "first_name": "John",
#         "case_number": "",
#         "policy_number": "",
#         "applicant_dob": "01/01/1990"
#     }
#     case_data = scrape_case_data(page, search_params)
#     print(case_data)
#     browser.close()