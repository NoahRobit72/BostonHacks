// This page will get the picture of the user
import { Link, useParams} from "react-router-dom";
import React, { useRef, useEffect} from 'react';

import {storage} from "../firebase_setup/firebase";
import {ref, uploadString} from "firebase/storage";

import '../css/ImageGet.css'; // Adjust the filename accordingly


export default function ImagerGet() {
    const { imageNumber } = useParams();

    const videoRef = useRef();

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
        // eslint-disable-next-line
        if (videoRef.current) {
          // eslint-disable-next-line
          const stream = videoRef.current.srcObject;
          if (stream) {
            const tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
          }
        }
      };
      // eslint-disable-next-line
    }, []); // Empty dependency array ensures that useEffect runs only once on component mount

      function convertDataUrl(dataUrl) {
        // Split the input data URL into MIME type and base64-encoded data
        const [, data] = dataUrl.split(',');
      
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
          const pathToSend = `images/Canvas${imageNumber}`;
          const imageRef = ref(storage,pathToSend);
          //
          uploadString(imageRef, newUrl, 'data_url').then(() => {
            console.log('finished');
          })

          const fetchString = `http://127.0.0.1:5000/getImage?imageName=Canvas${imageNumber}`;

          // Fetch code
          var requestOptions = {
            method: 'POST',
            redirect: 'follow'
          };

          fetch(fetchString, requestOptions)
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
              }
      };
    return (
      <div className="container">
      <h1>Canvas Chronicles</h1>
      <div>
        <video ref={videoRef} autoPlay />
      </div>
      <Link to={`/textshow/${imageNumber}`} className="capture-button" onClick={captureImage}>
        Capture
      </Link>
      <div className="link-container">
        <Link to="/" className="goBack-link">
          Go back
        </Link>
      </div>
    </div>
  );
}