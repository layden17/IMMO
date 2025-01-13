import React, { useState } from 'react';
import axios from 'axios';

const SignUp = () => {
  const [user, setUser] = useState({ name: '', email: '', password: '' });
  const [responseMessage, setResponseMessage] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUser((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSignUp = () => {
    console.log('Données envoyées :', user);
    axios.post('http://localhost:5001/signup', user) 
      .then((response) => {
        setResponseMessage(response.data.message);
      })
      .catch((error) => {
        console.error('Erreur lors de l\'inscription :', error);
      });
  };

  return (
    <div className="max-w-md w-full bg-white p-8 shadow-md rounded-lg">
      <h1 className="text-2xl font-bold text-blue-600 mb-6">Créer un compte</h1>

      <div className="mb-4">
        <input
          type="text"
          name="name"
          value={user.name}
          onChange={handleInputChange}
          placeholder="Nom"
          className="w-full p-3 border border-gray-300 rounded-md"
        />
      </div>

      <div className="mb-4">
        <input
          type="email"
          name="email"
          value={user.email}
          onChange={handleInputChange}
          placeholder="Email"
          className="w-full p-3 border border-gray-300 rounded-md"
        />
      </div>

      <div className="mb-4">
        <input
          type="password"
          name="password"
          value={user.password}
          onChange={handleInputChange}
          placeholder="Mot de passe"
          className="w-full p-3 border border-gray-300 rounded-md"
        />
      </div>

      <button
        onClick={handleSignUp}
        className="w-full bg-blue-500 text-white p-3 rounded-md"
      >
        S'inscrire
      </button>

      <p className="mt-4 font-bold text-green-400">{responseMessage}</p>
    </div>
  );
};

export default SignUp;
