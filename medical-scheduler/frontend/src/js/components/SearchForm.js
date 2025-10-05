import React, { useState } from 'react';

const SearchForm = ({ onSearch }) => {
    const [lastName, setLastName] = useState('');
    const [firstName, setFirstName] = useState('');
    const [caseNumber, setCaseNumber] = useState('');
    const [policyNumber, setPolicyNumber] = useState('');
    const [applicantDOB, setApplicantDOB] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch({ lastName, firstName, caseNumber, policyNumber, applicantDOB });
    };

    return (
        <form onSubmit={handleSubmit} className="search-form">
            <input
                type="text"
                placeholder="Last Name"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
            />
            <input
                type="text"
                placeholder="First Name"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
            />
            <input
                type="text"
                placeholder="Case Number"
                value={caseNumber}
                onChange={(e) => setCaseNumber(e.target.value)}
            />
            <input
                type="text"
                placeholder="Policy Number"
                value={policyNumber}
                onChange={(e) => setPolicyNumber(e.target.value)}
            />
            <input
                type="date"
                placeholder="Applicant DOB"
                value={applicantDOB}
                onChange={(e) => setApplicantDOB(e.target.value)}
            />
            <button type="submit">Search</button>
        </form>
    );
};

export default SearchForm;