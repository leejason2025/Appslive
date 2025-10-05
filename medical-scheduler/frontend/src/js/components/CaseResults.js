import React from 'react';

const CaseResults = ({ results }) => {
    return (
        <div className="case-results">
            {results.length === 0 ? (
                <p>No results found.</p>
            ) : (
                <ul>
                    {results.map((caseData, index) => (
                        <li key={index} className="case-card">
                            <h3>{caseData.applicantName}</h3>
                            <p>Insurance Company: {caseData.insuranceCompany}</p>
                            <p>Agent Name: {caseData.agentName}</p>
                            <p>Status: {caseData.statusDescription}</p>
                            <p>Case Number: {caseData.caseNumber}</p>
                            <p>Appointment Date: {caseData.appointmentDate}</p>
                            <p>Image Available: {caseData.imageAvailable ? 'Yes' : 'No'}</p>
                            <p>Packet Available: {caseData.packetAvailable ? 'Yes' : 'No'}</p>
                            <p>Zip Code: {caseData.applicantZipCode}</p>
                            <div className="action-buttons">
                                <button className="update-status">Update Status</button>
                                <button className="text-client">Text Client</button>
                                <button className="add-note">Add Note</button>
                            </div>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default CaseResults;