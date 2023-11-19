import { initializeApp } from "firebase/app";
import { getStorage } from "firebase/storage";
import { getDatabase } from "firebase/database";


// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB6fWAiUcIRgRHZeBax2tDFh2h_1rWhdig",
  authDomain: "canvas-chronicles.firebaseapp.com",
  projectId: "canvas-chronicles",
  storageBucket: "canvas-chronicles.appspot.com",
  messagingSenderId: "984043178691",
  appId: "1:984043178691:web:0544f44e7337c98aad7076",
  measurementId: "G-06Y1LN1P9Q"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const storage = getStorage(app);
export const database = getDatabase(app);
