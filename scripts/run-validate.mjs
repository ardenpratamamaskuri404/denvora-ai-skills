#!/usr/bin/env node
/**
 * Cross-platform launcher for scripts/validate-skill.py.
 * Finds python3, python, py, or Laragon's Python on Windows so `npm run validate` works everywhere.
 */
import { spawnSync } from 'node:child_process';
import { existsSync, readdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const validator = join(root, 'scripts', 'validate-skill.py');

const candidates = [
  ['python3', []],
  ['python', []],
  ['py', ['-3']],
];

if (process.platform === 'win32' && existsSync('C:\\laragon\\bin\\python')) {
  for (const dir of readdirSync('C:\\laragon\\bin\\python')) {
    const exe = join('C:\\laragon\\bin\\python', dir, 'python.exe');
    if (existsSync(exe)) candidates.push([exe, []]);
  }
}

for (const [cmd, prefixArgs] of candidates) {
  const probe = spawnSync(cmd, [...prefixArgs, '--version'], { encoding: 'utf8' });
  if (!probe.error && probe.status === 0) {
    const res = spawnSync(cmd, [...prefixArgs, validator], { stdio: 'inherit', cwd: root });
    process.exit(res.status ?? 1);
  }
}

console.error('Error: Python 3 not found. Install Python 3 or run `python scripts/validate-skill.py` directly.');
process.exit(1);
