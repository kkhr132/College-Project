const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 5000;

let users = []; // In-memory array for users
let nextId = 1;

app.use(cors());
app.use(bodyParser.json());

// CRUD Routes
app.get('/users', (req, res) => {
  res.json(users);
});

app.post('/users', (req, res) => {
  const user = { id: nextId++, ...req.body };
  users.push(user);
  res.json(user);
});

app.put('/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = users.findIndex(u => u.id === id);
  if (index !== -1) {
    users[index] = { ...users[index], ...req.body };
    res.json(users[index]);
  } else {
    res.status(404).json({ error: 'User not found' });
  }
});

app.delete('/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = users.findIndex(u => u.id === id);
  if (index !== -1) {
    users.splice(index, 1);
    res.json({ message: 'User deleted' });
  } else {
    res.status(404).json({ error: 'User not found' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
