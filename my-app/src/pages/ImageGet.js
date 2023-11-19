// This page will get the picture of the user
import { Link } from "react-router-dom";
import React, { useRef, useEffect, useState} from 'react';
import { ref, uploadString } from "firebase/storage";
import { storage } from '../firebase_setup/firebase';

const storageRef = ref(storage, 'some-child');


export default function ImagerGet() {
    const videoRef = useRef();
    const [capturedImage, setCapturedImage] = useState(null);

    useEffect(() => {
        const startWebcam = async () => {
          try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            if (videoRef.current) {
              videoRef.current.srcObject = stream;
            }
          } catch (error) {
            console.error('Error accessing webcam:', error);
          }
        };
    
        startWebcam();
    
        // Cleanup function to stop the webcam when the component unmounts
        return () => {
          if (videoRef.current) {
            const stream = videoRef.current.srcObject;
            if (stream) {
              const tracks = stream.getTracks();
              tracks.forEach(track => track.stop());
            }
          }
        };
      }, []); // Empty dependency array ensures that useEffect runs only once on component mount

      const captureImage = () => {
        if (videoRef.current) {
          const canvas = document.createElement('canvas');
          canvas.width = videoRef.current.videoWidth;
          canvas.height = videoRef.current.videoHeight;
          const context = canvas.getContext('2d');
          context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
      
          // Now, 'canvas.toDataURL()' contains the captured image as a Base64-encoded string
          const imageDataUrl = canvas.toDataURL(); // Do not specify image format
          console.log(imageDataUrl);
          setCapturedImage(imageDataUrl);
        }
      };

      const handleLinkClick = () => {
        captureImage();
        console.log(capturedImage);
        console.log('Link clicked!'); // button clicked

        uploadString(storageRef, capturedImage, 'base64url').then((snapshot) => {
            console.log('Uploaded a base64url string!');
          });
        console.log("send to database"); 
      };
    

    return (
        <div>
            <h1>Canvas Chronicles</h1>
            <div>
                <video ref={videoRef} autoPlay />
            </div>
            <Link to="/textshow" onClick={handleLinkClick}>Capture</Link>
            <br></br>
            <Link to="/">go back</Link>
      </div>
  );
}