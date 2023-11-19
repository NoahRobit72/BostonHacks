// This is a homepage to greet the user
import React from 'react';
import { Link } from "react-router-dom";


export default function Home() {
    return (
        <div>
            <h1>Hi! This is Canvas Chronicles!</h1>  

            {/* Alternatively, you can use the Link component */}
            <Link to="/imageget">Click here to turn a simple drawing or illustration into a captivating full story for kids.</Link>
      </div>
  );
}