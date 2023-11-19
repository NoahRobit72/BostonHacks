import React, { useState, useEffect, useCallback } from 'react';
import { Link } from "react-router-dom";
import { getDatabase, ref, child, get } from "firebase/database";
import '../css/TextShow.css'; // Adjust the filename accordingly



const YourComponent = () => {
  const [pollingInProgress, setPollingInProgress] = useState(true);
  const [status, setStatus] = useState(''); // State to store the status received from the server
  const [successData, setSuccessData] = useState(null);


  const pollForImage = useCallback(async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/getStatus');
      const data = await response.text();

      console.log('Received data:', data);
      console.log(status);

      setStatus(data);

      if (data === '1') {
        console.log('Received the desired response: 1');
        setPollingInProgress(false);
        handleSuccess();
      } else {
        setTimeout(pollForImage, 250);
      }
    } catch (error) {
      console.error('Error during polling:', error);
    }
  }, [status]); // Include status as a dependency

  const handleSuccess = () => {
    const dbRef = ref(getDatabase());
    get(child(dbRef, 'Canvas2')).then((snapshot) => {
      if (snapshot.exists()) {
        const data = snapshot.val();
        setSuccessData(data); // Save the data to state
        console.log(data);
      } else {
        console.log("No data available");
      }
    }).catch((error) => {
      console.error(error);
    });
    console.log('Handling success...');
  };

  useEffect(() => {
    if (pollingInProgress) {
      // Start the polling process when the component mounts
      pollForImage();
    }

    // Cleanup function to stop polling when the component unmounts
    return () => {
      setPollingInProgress(false);
    };
  }, [pollingInProgress, pollForImage]);

  return (
    <div className="container">
      <h1>Canvas Chronicles</h1>
      <p className="loading-status">
        {(() => {
          if (status === '0') {
            return 'Loading...';
          } 
        })()}
      </p>
      {successData && <p className="success-data">{successData}</p>}
      <Link to="/" className="goBack-link"> Return to start</Link>
    </div>
  );
};

export default YourComponent;
