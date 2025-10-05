from flask import Blueprint, request, jsonify
from ..auth.session_manager import login_required
from ..scraper.web_scraper import scrape_case_data

api = Blueprint('api', __name__)

@api.route('/cases', methods=['GET'])
@login_required
def get_cases():
    last_name = request.args.get('last_name')
    first_name = request.args.get('first_name')
    case_number = request.args.get('case_number')
    policy_number = request.args.get('policy_number')
    applicant_dob = request.args.get('applicant_dob')

    # Call the scraper function to get case data
    case_data = scrape_case_data(last_name, first_name, case_number, policy_number, applicant_dob)

    return jsonify(case_data) if case_data else jsonify({'message': 'No cases found'}), 404

@api.route('/status/update', methods=['POST'])
@login_required
def update_status():
    # Placeholder for future implementation
    return jsonify({'message': 'Update status functionality coming soon'}), 200

@api.route('/client/text', methods=['POST'])
@login_required
def text_client():
    # Placeholder for future implementation
    return jsonify({'message': 'Text client functionality coming soon'}), 200

@api.route('/note/add', methods=['POST'])
@login_required
def add_note():
    # Placeholder for future implementation
    return jsonify({'message': 'Add note functionality coming soon'}), 200