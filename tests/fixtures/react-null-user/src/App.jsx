import { useState, useEffect } from 'react'

export default function App() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    // Simulate an API call that takes 1 second
    setTimeout(() => {
      setUser({ name: 'Arden', email: 'arden@example.com' })
    }, 1000)
  }, [])

  // BUG: user is null on first render, causing TypeError
  return (
    <div>
      <h1>Profile</h1>
      <p>Name: {user.name}</p>
      <p>Email: {user.email}</p>
    </div>
  )
}
