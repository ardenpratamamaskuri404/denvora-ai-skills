# Prompt templates

Copy-paste prompts that work well with denvora-ai-skills. The skill should trigger by itself on coding tasks, but these make your intent extra clear, and they also work with AIs that do not support skills (see the first section).

Replace anything in `<angle brackets>`.

---

## Activate the rules

**English**

```
Read skills/denvora-ai-skills/SKILL.md and follow it for this whole conversation.
Read the reference files it links to when they are relevant.
```

**Bahasa Indonesia**

```
Baca skills/denvora-ai-skills/SKILL.md dan ikuti aturannya selama percakapan ini.
Baca juga file referensi yang ditautkan kalau relevan.
```

If the skill is installed, you can simply say: `Use the denvora-ai-skills skill.` / `Pakai skill denvora-ai-skills.`

---

## Build something new

**English**

```
I want to build <what>, for <who / what purpose>.
I'm a beginner. Plan it in small steps first and wait for my OK before writing code.
Use <stack> if possible, or suggest the simplest option.
```

**Bahasa Indonesia**

```
Saya mau bikin <apa>, untuk <siapa / tujuan apa>.
Saya masih pemula. Tolong rencanakan dulu dalam langkah kecil dan tunggu persetujuan saya sebelum menulis kode.
Pakai <stack> kalau bisa, atau sarankan pilihan yang paling simpel.
```

---

## Fix an error

**English**

```
I got this error:

<paste the full error message here>

It happens when I <what you did>.
Find the root cause first, explain it simply, then fix it. Tell me how to check the fix.
```

**Bahasa Indonesia**

```
Saya dapat error ini:

<tempel pesan error lengkap di sini>

Error muncul waktu saya <apa yang kamu lakukan>.
Cari dulu penyebab utamanya, jelaskan dengan bahasa sederhana, lalu perbaiki. Kasih tahu cara saya mengecek hasilnya.
```

---

## Add a feature to an existing project

**English**

```
Add <feature> to my project.
First read the project structure and the files related to this feature, and follow the existing style.
Tell me what you verified and what you could not test.
```

**Bahasa Indonesia**

```
Tambahkan fitur <fitur> ke project saya.
Baca dulu struktur project dan file yang berhubungan dengan fitur ini, dan ikuti gaya kode yang sudah ada.
Kasih tahu apa yang sudah kamu cek dan apa yang belum bisa dites.
```

---

## Ask about a library or command

**English**

```
How do I <task> with <library / tool>?
I'm using version <version>. If you're not sure something exists in this version, say so.
```

**Bahasa Indonesia**

```
Bagaimana cara <tugas> pakai <library / tool>?
Saya pakai versi <versi>. Kalau kamu tidak yakin sesuatu ada di versi ini, bilang saja.
```

---

## Before going online

**English**

```
I want to deploy this app. Run through the security checklist in the denvora-ai-skills references and tell me what still needs work.
```

**Bahasa Indonesia**

```
Saya mau online-kan aplikasi ini. Cek pakai security checklist di referensi denvora-ai-skills dan kasih tahu apa saja yang masih perlu diperbaiki.
```

---

## When the AI seems to be guessing

**English**

```
Stop. Which parts of your last answer did you actually verify, and which are guesses?
Label them [Certain], [Likely], or [Unsure].
```

**Bahasa Indonesia**

```
Stop dulu. Bagian mana dari jawabanmu tadi yang benar-benar sudah kamu cek, dan mana yang tebakan?
Kasih label [Pasti], [Kemungkinan], atau [Belum yakin].
```

---

Want templates in another language? Contributions are welcome, see [CONTRIBUTING.md](../CONTRIBUTING.md).
