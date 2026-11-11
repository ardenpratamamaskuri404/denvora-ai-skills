const express = require('express')
const todosRouter = require('./routes/todos')

const app = express()
const PORT = process.env.PORT || 3000

app.use(express.json())
app.use('/api/todos', todosRouter)

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})

module.exports = app
