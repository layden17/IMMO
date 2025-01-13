const Customer = require('../models/customerModel');

// Récupérer tous les clients
const getCustomers = async (req, res) => {
  try {
    const customers = await Customer.find();
    res.status(200).json(customers);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Ajouter un nouveau client
const addCustomer = async (req, res) => {
  const { firstName, lastName, phoneNumber, billingDetails } = req.body;

  try {
    const newCustomer = await Customer.create({
      firstName,
      lastName,
      phoneNumber,
      billingDetails
    });
    res.status(201).json(newCustomer);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

module.exports = { getCustomers, addCustomer };
