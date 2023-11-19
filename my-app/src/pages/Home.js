import React, { useState } from 'react';
import { Link} from 'react-router-dom';
import '../css/Home.css'; // Adjust the filename accordingly



export default function Home() {
    // State to store the random number
    const [randomNumber, setRandomNumber] = useState(generateRandomNumber());

    // Function to generate a random number between 0 and 1000
    function generateRandomNumber() {
        // return Math.floor(Math.random() * 1001);
        return 2;
    }

    // Function to update the random number when the link is clicked
    const handleLinkClick = () => {
        setRandomNumber(generateRandomNumber());
    };

    return (
        <div className="container">
            <h1>Hi! This is Canvas Chronicles!</h1>
                <Link to={`/imageget/${randomNumber}`} onClick={handleLinkClick}>
                Click here to turn a simple drawing or illustration into a captivating full story for kids.
            </Link>
        </div>
    );
}
