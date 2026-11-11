# Stack version pitfalls

Load this reference when working on a project that uses one of these stacks. Check the installed version first, then find the matching section.

## Next.js

| Installed version | Watch out for |
|---|---|
| 13.4+ (App Router default) | `app/` uses React Server Components by default. `"use client"` required for hooks, state, and browser APIs. |
| < 13.4 (Pages Router) | `pages/` directory, `getServerSideProps` / `getStaticProps`, no server components. |
| 15+ | `next.config.ts` supported. `headers()`, `cookies()`, `params`, and `searchParams` are async (`Promise`-based) and must be `await`ed. Turbopack is the default dev bundler — some Webpack plugins won't work. |

## Tailwind CSS

| Installed version | Watch out for |
|---|---|
| v3.x | Config in `tailwind.config.js` / `.ts`. `content` array required. Color palette in `theme.extend.colors`. |
| v4.x | Config moved to CSS with `@theme` directive. No `tailwind.config.js` by default. `@tailwind` directives replaced by `@import "tailwindcss"`. PostCSS plugin name changed to `@tailwindcss/postcss`. |

## React

| Installed version | Watch out for |
|---|---|
| 17 | Introduced the optional `react-jsx` transform, though older setups still require `import React`. No `useId` or `useTransition`. `ReactDOM.render()` is the entry point. |
| 18 | `createRoot()` replaces `ReactDOM.render()`. Strict Mode double-renders in dev. `useId`, `useTransition`, `useDeferredValue` added. |
| 19 | `use()` hook for promises/context. `ref` is a regular prop (no `forwardRef` needed). `<form>` actions and `useFormStatus` / `useActionState` added. `forwardRef` is deprecated. |

## Laravel

| Installed version | Watch out for |
|---|---|
| 9 | Requires PHP 8.0+. Vite not default (uses Mix). Route model binding in `RouteServiceProvider`. |
| 10 | Requires PHP 8.1+. Vite is default. `Process` facade added. `$casts` is a property on models. |
| 11+ | Requires PHP 8.2+. Slim skeleton — no `app/Http/Kernel.php` or `RouteServiceProvider`. Routing/middleware live in `bootstrap/app.php`. `$casts` changed to a `casts()` method on new models. Health endpoint at `/up`. |

## Python

| Detail | Watch out for |
|---|---|
| `python` vs `python3` | On many Linux/macOS systems, `python` is Python 2 or missing. Always use `python3` and `pip3`, or check `python --version` first. |
| Virtual environments | Use `python3 -m venv .venv` (not `virtualenv`). Activate: `source .venv/bin/activate` (Unix) or `.venv\Scripts\Activate.ps1` (Windows PowerShell). |
| Type hints | `list[str]`, `dict[str, int]` built-in generics require Python 3.9+. Use `from __future__ import annotations` or `typing.List` for 3.7/3.8. `X | Y` union syntax requires 3.10+. |

## Flutter / Dart

| Installed version | Watch out for |
|---|---|
| Dart 2.x / Flutter 2.x | Sound null safety added mid-cycle — older packages may not support it. `dart pub` replaces `pub`. |
| Dart 3.x / Flutter 3.x | Null safety is enforced — no opt-out. Class modifiers (`sealed`, `final`, `interface`) added. Records and patterns syntax. `switch` expressions. Dart 3 requires Flutter 3.10+. |

## General

| Situation | What to do |
|---|---|
| Not sure which version is installed | Run `node -v`, `npx next --version`, `php artisan --version`, `python3 --version`, `flutter --version`, or check `package.json` / lockfile. |
| Docs say one thing, installed version does another | Trust the installed version. Read `node_modules/<pkg>/README.md`, `.d.ts` files, or `vendor/<pkg>` source. |
| Upgrading across major versions | Read the official migration guide before changing code. Check for breaking changes in the changelog. |
