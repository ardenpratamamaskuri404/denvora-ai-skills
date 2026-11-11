const express = require('express')
const router = express.Router()

let todos = [
  { id: 1, title: 'Learn Express', completed: false },
  { id: 2, title: 'Build an API', completed: true },
]

router.get('/', (req, res) => {
  res.json(todos)
})

router.post('/', (req, res) => {
  const todo = {
    id: todos.length + 1,
    title: req.body.title,
    completed: false,
  }
  todos.push(todo)
  res.status(201).json(todo)
})

router.delete('/:id', (req, res) => {
  const id = parseInt(req.params.id)
  todos = todos.filter((t) => t.id !== id)
  res.status(204).end()
})

module.exports = router
