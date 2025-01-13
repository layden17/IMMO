/*
import React, { useState } from 'react';
import SignUp from './components/SignUp';
import SignIn from './components/SignIn';

function App() {
  const [showSignUp, setShowSignUp] = useState(true);

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-300 via-blue-500 to-blue-700">
      <div className="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
        <div className="flex justify-center mb-6">
          <button
            onClick={() => setShowSignUp(true)}
            className={`p-2 px-6 text-sm font-medium transition-colors duration-300 rounded-l-lg ${
              showSignUp
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-100 hover:bg-gray-200 text-gray-600'
            }`}
          >
            S'inscrire
          </button>
          <button
            onClick={() => setShowSignUp(false)}
            className={`p-2 px-6 text-sm font-medium transition-colors duration-300 rounded-r-lg ${
              !showSignUp
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-100 hover:bg-gray-200 text-gray-600'
            }`}
          >
            Se connecter
          </button>
        </div>
        <div className="transition-all duration-500 ease-in-out">
          {showSignUp ? <SignUp /> : <SignIn />}
        </div>
      </div>
    </div>
  );
}

export default App;
*/

import React from 'react';
import CustomerInfoForm from './Components/customer_info_form'; // Import du composant à afficher directement
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Ajout des imports nécessaires
import CustomerPage from './pages/CustomerPage'; // Import du composant CustomerPage

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/customers" element={<CustomerPage />} />
      </Routes>
    </Router>
  );
}

export default App;
