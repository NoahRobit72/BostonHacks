import './App.css';
// import Home from "./pages/Home"
import Home from './pages/Home'
import ImageGet from './pages/ImageGet'
import TextShow from './pages/TextShow'
import Test from './pages/Test'



import { BrowserRouter, Routes, Route } from "react-router-dom";



function App() {
  return (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/imageget/:imageNumber" element={<ImageGet />} />
      <Route path="/textshow/:imageNumber" element={<TextShow />} />
      <Route path="/test" element={<Test />} />

      
    </Routes>
  </BrowserRouter>
  );
}

export default App;
