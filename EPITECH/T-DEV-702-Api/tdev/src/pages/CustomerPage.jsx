import React, { useEffect, useState } from 'react';
import { fetchCustomers } from '../services/apiService';
import CustomerForm from '../Components/CustomerForm';

const CustomerPage = () => {
  const [customers, setCustomers] = useState([]);

  const loadCustomers = async () => {
    const data = await fetchCustomers();
    setCustomers(data);
  };

  useEffect(() => {
    loadCustomers();
  }, []);

  return (
    <div>
      <h1>Customers</h1>
      <CustomerForm onCustomerAdded={loadCustomers} />
      <ul>
        {customers.map((customer) => (
          <li key={customer._id}>
            {customer.firstName} {customer.lastName} - {customer.billingDetails.city}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CustomerPage;
