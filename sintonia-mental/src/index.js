import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
// arquvivos de estilo
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from './navbar/navbar';




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
  <NavBar />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
