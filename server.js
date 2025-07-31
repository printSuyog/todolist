const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

let todos = [];
let nextId = 1;

app.get('/todos', (req, res) => {
  res.json(todos);
});

app.post('/todos', (req, res) => {
  const { text } = req.body;
  if (!text) return res.status(400).json({ error: 'Text is required' });

  const newTodo = { id: nextId++, text, completed: false };
  todos.push(newTodo);
  res.status(201).json(newTodo);
});

app.put('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todo = todos.find(t => t.id === id);
  if (!todo) return res.status(404).json({ error: 'Todo not found' });

  const { text, completed } = req.body;
  if (text !== undefined) todo.text = text;
  if (completed !== undefined) todo.completed = completed;

  res.json(todo);
});

app.delete('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  todos = todos.filter(t => t.id !== id);
  res.json({ message: 'Todo deleted' });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

