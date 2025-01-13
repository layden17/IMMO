import React, { useState } from 'react';
import { createCustomer } from '../services/apiService';

const CustomerForm = ({ onCustomerAdded }) => {
  const [form, setForm] = useState({
    firstName: '',
    lastName: '',
    phoneNumber: '',
    billingDetails: {
      address: '',
      zipCode: '',
      city: '',
      country: ''
    }
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    if (name.startsWith('billingDetails.')) {
      const field = name.split('.')[1];
      setForm({
        ...form,
        billingDetails: {
          ...form.billingDetails,
          [field]: value
        }
      });
    } else {
      setForm({ ...form, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createCustomer(form);
    onCustomerAdded();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="firstName" placeholder="First Name" onChange={handleChange} required />
      <input name="lastName" placeholder="Last Name" onChange={handleChange} required />
      <input name="phoneNumber" placeholder="Phone Number" onChange={handleChange} required />
      <input name="billingDetails.address" placeholder="Address" onChange={handleChange} required />
      <input name="billingDetails.zipCode" placeholder="Zip Code" onChange={handleChange} required />
      <input name="billingDetails.city" placeholder="City" onChange={handleChange} required />
      <input name="billingDetails.country" placeholder="Country" onChange={handleChange} required />
      <button type="submit">Add Customer</button>
    </form>
  );
};

export default CustomerForm;
