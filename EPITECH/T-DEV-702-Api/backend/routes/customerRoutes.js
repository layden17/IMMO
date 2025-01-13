const express = require('express');
const { getCustomers, addCustomer } = require('../controllers/customerController');
const router = express.Router();

router.get('/', getCustomers); // Récupérer tous les clients
router.post('/', addCustomer); // Ajouter un nouveau client

module.exports = router;
