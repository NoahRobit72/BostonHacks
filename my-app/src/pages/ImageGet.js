// This page will get the picture of the user
import { Link } from "react-router-dom";
import React, { useRef, useEffect, useState} from 'react';

import {storage} from "../firebase_setup/firebase";
import {ref, uploadString} from "firebase/storage";

export default function ImagerGet() {
    const videoRef = useRef();
    const [capturedImageValue, setCapturedImage] = useState(null);

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

      function convertDataUrl(dataUrl) {
        // Split the input data URL into MIME type and base64-encoded data
        const [prefix, data] = dataUrl.split(',');
      
        // Create the new data URL with a different MIME type
        const newTextDataUrl = `data:text/plain;base64,${data}`;
      
        return newTextDataUrl;
      }

      const captureImage = () => {
        if (videoRef.current) {
          const canvas = document.createElement('canvas');
          canvas.width = videoRef.current.videoWidth;
          canvas.height = videoRef.current.videoHeight;
          const context = canvas.getContext('2d');
          context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
      
          // Now, 'canvas.toDataURL()' contains the captured image as a Base64-encoded string
          const imageDataUrl = canvas.toDataURL(); // Do not specify image format
          const newUrl = convertDataUrl(imageDataUrl);
          console.log(newUrl);
          const imageRef = ref(storage,'images/image1');
          uploadString(imageRef, newUrl, 'data_url').then(() => {
            alert("image uploaded")
          })
          setCapturedImage(imageDataUrl);
        }
      };

    return (
        <div>
            <h1>Canvas Chronicles</h1>
            <div>
                <video ref={videoRef} autoPlay />
            </div>
            <Link to="/textshow" onClick={captureImage}>Capture</Link>
            <br></br>
            <Link to="/">go back</Link>
      </div>
  );
}