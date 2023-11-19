import './App.css';
// import Home from "./pages/Home"
import Home from './pages/Home'
import ImageGet from './pages/ImageGet'
import TextShow from './pages/TextShow'

import { BrowserRouter, Routes, Route } from "react-router-dom";



function App() {
  return (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/imageget" element={<ImageGet />} />
      <Route path="/textshow" element={<TextShow />} />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
