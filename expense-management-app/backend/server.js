const express = require('express');
const app = express();

app.use(express.json());

let expenses = [];

app.get('/', (req, res) => {
    res.send('Welcome to the Expense Management Backend!');
});

app.post('/add_expense', (req, res) => {
    const data = req.body;
    expenses.push(data);
    res.json({ message: 'Expense added successfully!' });
});

app.get('/expenses', (req, res) => {
    res.json(expenses);
});

app.listen(5001, () => {
    console.log('Backend server is running on port 5001');
});
