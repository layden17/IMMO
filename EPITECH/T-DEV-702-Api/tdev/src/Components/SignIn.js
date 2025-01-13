import React, { useState } from 'react';
import axios from 'axios';

const SignIn = () => {
  const [credentials, setCredentials] = useState({ email: '', password: '' });
  const [responseMessage, setResponseMessage] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSignIn = () => {
    axios.post('http://localhost:5001/signin', credentials) 
      .then((response) => {
        setResponseMessage(response.data.message);
      })
      .catch((error) => {
        console.error('Erreur lors de la connexion :', error);
      });
  };

  return (
    <div className="max-w-md w-full bg-white p-8 shadow-md rounded-lg">
      <h1 className="text-2xl font-bold text-blue-600 mb-6">Se connecter</h1>

      <div className="mb-4">
        <input
          type="email"
          name="email"
          value={credentials.email}
          onChange={handleInputChange}
          placeholder="Email"
          className="w-full p-3 border border-gray-300 rounded-md"
        />
      </div>

      <div className="mb-4">
        <input
          type="password"
          name="password"
          value={credentials.password}
          onChange={handleInputChange}
          placeholder="Mot de passe"
          className="w-full p-3 border border-gray-300 rounded-md"
        />
      </div>

      <button
        onClick={handleSignIn}
        className="w-full bg-blue-500 text-white p-3 rounded-md"
      >
        Se connecter
      </button>

      <p className="mt-4 font-bold text-green-400">{responseMessage}</p>
    </div>
  );
};

export default SignIn;
