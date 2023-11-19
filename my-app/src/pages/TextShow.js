import React, { useState, useEffect, useCallback } from 'react';

const YourComponent = () => {
  const [pollingInProgress, setPollingInProgress] = useState(true);
  const [status, setStatus] = useState(''); // State to store the status received from the server

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
    // Your logic for handling success, e.g., calling another function
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
    <div>
      <h1>Your Component</h1>
      <p>Status: {status}</p>
      <p>{(() => {
          if (status === '0') {
            return 'Loading...';
          } else {
            return 'Finished!';
          }
        })()}
      </p>
    </div>
  );
};

export default YourComponent;
