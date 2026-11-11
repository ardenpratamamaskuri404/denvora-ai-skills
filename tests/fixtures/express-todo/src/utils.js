/**
 * Utility helpers for the todo API.
 * Follows CommonJS style to match the rest of the project.
 */

function generateId(items) {
  if (items.length === 0) return 1
  return Math.max(...items.map((item) => item.id)) + 1
}

function formatDate(date) {
  return new Date(date).toISOString().split('T')[0]
}

module.exports = { generateId, formatDate }
