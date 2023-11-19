// This page will display the story
import React from 'react';
import { Link} from "react-router-dom";


export default function TextShow(props) {  
    return (
      <div>
        <h1>TextShow Component</h1>
          <div>
            <h2>Received Image</h2>
          </div>
        <Link to="/">Go to home</Link>
      </div>
    );
}