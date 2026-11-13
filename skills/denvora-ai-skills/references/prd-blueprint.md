# PRD & Architecture Blueprint

Read this when a task involves building a new application, a major subsystem, or a vague request (e.g., *"build an invoice app"*, *"bikin sistem auth"*, *"make my project better"*).

Before writing code for large tasks, formulate a concise **Product Requirements Document (PRD) & Technical Blueprint**. Getting user alignment on the spec first prevents wasted tokens, architectural dead-ends, and unverified rewrites.

---

## 1. When to Use

| Task Type | Action |
|---|---|
| **Tiny task** (one-line fix, rename, small styling) | Skip PRD. Answer directly. |
| **Normal task** (add an endpoint, fix an existing bug) | Skip PRD. Follow normal 3–7 slice plan in chat. |
| **Big or vague task** (new app, new module, major refactor) | **Draft this PRD Blueprint first.** Present it, wait for user confirmation, then build in slices. |

---

## 2. Standard PRD Blueprint Format

Present this concise document to the user before scaffolding or modifying code:

```markdown
# [Project / Feature Name] Blueprint

## 1. Overview & Problem Statement
- **What it does:** <1-2 sentences in plain language>
- **Target user:** <who will use this — beginner, admin, public user>
- **Core problem solved:** <why this needs to be built>

## 2. Scope & Explicit Non-Goals
### In Scope (v1)
- [ ] <Core feature 1>
- [ ] <Core feature 2>
- [ ] <Core feature 3>

### Non-Goals (Omit for now - YAGNI)
- ❌ <Feature to postpone, e.g. complex microservices, OAuth if email/pass suffices>
- ❌ <Unneeded complexity, e.g. third-party analytics before MVP works>

## 3. Tech Stack & Architecture
- **Language / Framework:** <e.g. Next.js 15 (App Router), Tailwind CSS v4, SQLite>
- **Data Model:**
  ```text
  Entity: <e.g. User (id, email, password_hash, created_at)>
  Entity: <e.g. Invoice (id, user_id, amount, status, due_date)>
  ```
- **Key API / Route Contracts:**
  - `POST /api/invoices` -> creates new invoice
  - `GET /api/invoices` -> lists invoices for authenticated user

## 4. Slice Implementation Plan (Sequential & Independent)
1. **Slice 1: Scaffolding & Verification** — Setup directory, dependencies, and verify blank app runs.
2. **Slice 2: Data Model & Storage** — Setup database schema, migrations, or local storage.
3. **Slice 3: Core Business Logic & Endpoints** — Implement routes/services with automated tests.
4. **Slice 4: User Interface** — Build interactive forms and views connecting to the core logic.
5. **Slice 5: Edge Cases & Polish** — Error states, loading states, empty lists, and input validation.

## 5. Verification & Acceptance Criteria
- [ ] Build command succeeds with 0 errors (`npm run build`, `cargo check`, etc.)
- [ ] Core happy path tested end-to-end (manual command or automated test)
- [ ] Clean project state (no temporary files, `.bak` files, or unneeded dependencies)
- [ ] Secrets check: Zero `.env` variables or keys committed or exposed

## 6. Assumptions & Defaults
- <e.g. Using SQLite locally for zero-configuration setup>
- <e.g. English UI text by default, customizable later>
```

---

## 3. Format Blueprint untuk Pengguna Bahasa Indonesia

Jika pengguna berkomunikasi dalam Bahasa Indonesia, gunakan template berikut:

```markdown
# Cetak Biru: [Nama Aplikasi / Fitur]

## 1. Ringkasan & Masalah
- **Fungsi utama:** <1-2 kalimat ringkas bahasa santai/jelas>
- **Pengguna:** <siapa yang menggunakan, misal: kasir, admin, pengguna umum>
- **Masalah yang diselesaikan:** <kenapa fitur/aplikasi ini penting dibuat>

## 2. Cakupan Fitur & Batasan (Scope & Non-Goals)
### Fitur yang Dibuat Sekarang (v1)
- [ ] <Fitur utama 1>
- [ ] <Fitur utama 2>
- [ ] <Fitur utama 3>

### Yang Ditunda Dulu (Hindari Over-Engineering)
- ❌ <Fitur rumit yang belum dibutuhkan, misal payment gateway jika belum ada produk>
- ❌ <Library berat yang tidak penting>

## 3. Struktur Teknis & Model Data
- **Stack:** <Framework, bahasa, dan database yang dipakai>
- **Model Data:**
  ```text
  Tabel/Objek: <misal Produk (id, nama, harga, stok)>
  ```
- **Rute / Alur:**
  - `GET /produk` -> menampilkan daftar produk
  - `POST /produk` -> menambah produk baru

## 4. Rencana Pengerjaan Bertahap (Slices)
1. **Langkah 1: Setup & Tes Awal** — Pastikan fondasi project berjalan tanpa error.
2. **Langkah 2: Model & Database** — Siapkan tabel atau struktur penyimpanan data.
3. **Langkah 3: Logika Utama** — Buat fungsi simpan, ambil, dan edit data.
4. **Langkah 4: Tampilan (UI)** — Buat halaman interaktif yang terhubung ke data.
5. **Langkah 5: Penanganan Error & Finishing** — Cek validasi input dan rapikan tampilan.

## 5. Bukti Selesai (Kriteria Verifikasi)
- [ ] Perintah build berhasil dengan 0 error (`npm run build`, dll.)
- [ ] Alur utama sudah dicoba dan terbukti jalan
- [ ] Tidak ada file sampah, file backup `.bak`, atau log debug tertinggal
- [ ] Rahasia aman: Tidak ada API key atau file `.env` yang bocor

## 6. Asumsi yang Dipilih
- <misal: Menggunakan penyimpanan lokal sementara sebelum menghubungkan ke server hosting>
```

---

## 4. Spec-Driven Development (SDD) Guidelines

1. **Wait for Approval:** Present the blueprint and ask: *"Does this scope and plan match what you want?"* Do not start editing files until the user gives confirmation.
2. **Never Over-Engineer:** A beginner's todo app does not need microservices, Kubernetes manifests, or complex state machines. Choose the simplest reliable architecture.
3. **Keep Slices Small:** Each slice must be independently verifiable. Never combine data modeling, API creation, and complete UI into a single unreviewed turn.
4. **Preserve Compatibility:** This blueprint integrates seamlessly with Spec-Driven IDEs and agents such as **Kiro**, **Claude Code**, **Cursor**, and **Antigravity**.
