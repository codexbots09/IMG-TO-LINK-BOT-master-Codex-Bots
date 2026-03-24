<div align="center">

<img src="https://files.catbox.moe/qs361h.jpg" alt="Telegraph Cloud Uploader Bot" width="100%" style="border-radius: 15px;" />

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&lines=Telegraph+Cloud+Uploader+Bot;Upload+Media+to+Catbox.moe;Fast+%E2%80%A2+Permanent+%E2%80%A2+Reliable;Open+Source+%26+Free+to+Deploy!" alt="Typing Animation" />

<br><br>

<a href="https://t.me/CodeVoultX_Bots">
  <img src="https://img.shields.io/badge/Channel-CodeVoultX__Bots-6C63FF?style=for-the-badge&logo=telegram&logoColor=white" />
</a>
<a href="https://t.me/codesXSupport">
  <img src="https://img.shields.io/badge/Support-@codesXSupport-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" />
</a>
<a href="https://github.com/CodeVoultX-Bots/imgtolink/stargazers">
  <img src="https://img.shields.io/github/stars/CodeVoultX-Bots/imgtolink?style=for-the-badge&color=FFD700&logo=github" />
</a>
<a href="https://github.com/CodeVoultX-Bots/imgtolink/fork">
  <img src="https://img.shields.io/github/forks/CodeVoultX-Bots/imgtolink?style=for-the-badge&color=00C9A7&logo=github" />
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Pyrogram-2.0-009EFF?style=flat-square&logo=telegram" />
<img src="https://img.shields.io/badge/MongoDB-Database-47A248?style=flat-square&logo=mongodb&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />

</div>

---

## ✨ What Is This?

> **Telegraph Cloud Uploader Bot** is a powerful, open-source Telegram bot that lets users upload photos, videos, and animations to **Catbox.moe** — giving permanent, no-expiry public links in seconds.

---

## 🚀 Features

<div align="center">

| Feature | Description |
|:-------:|:------------|
| ⚡ **Lightning Fast** | Uploads powered by Catbox.moe CDN |
| 🔗 **Permanent Links** | No expiry — your links live forever |
| 🗂️ **Upload History** | Users can view last 10 uploads via `/history` |
| 📢 **Log Channel** | All uploads tracked in your private channel |
| 🛡️ **Admin Controls** | Ban users, broadcast messages |
| 🐳 **Multi-Platform** | Supports Docker, Heroku & Render |

</div>

---

## 🛠️ Deployment

### ☁️ One-Click Heroku

<div align="center">

<a href="https://heroku.com/deploy?template=https://github.com/CodeVoultX-Bots/imgtolink">
  <img src="https://www.herokuimg.com/deploy/button.svg" alt="Deploy to Heroku" />
</a>

</div>

**Steps:**
1. 🍴 Fork this repository
2. 🆕 Create a new Heroku app
3. 🔗 Connect your GitHub repo
4. ⚙️ Add the Config Vars (see below)
5. ▶️ Deploy the `worker` dyno

---

### 🌐 Render (Free Tier)

1. 🍴 Fork this repository
2. 🆕 Create a new **Web Service** on [Render](https://render.com)
3. 🔗 Connect your GitHub repo
4. ⚙️ Add Environment Variables
5. 🚀 Hit **Deploy** — runs on free tier!

---

### 🐳 Docker

```bash
# Build the image
docker build -t codevoulx-imgtolink .

# Run with your environment file
docker run --env-file .env codevoulx-imgtolink
```

---

## ⚙️ Configuration

Create a `.env` file or set these variables in your platform:

```env
API_ID        = your_api_id          # From my.telegram.org
API_HASH      = your_api_hash        # From my.telegram.org
BOT_TOKEN     = your_bot_token       # From @BotFather
MONGO_URL     = your_mongo_uri       # MongoDB connection string
ADMINS        = your_user_id         # Admin Telegram user ID
LOG_CHANNEL   = -100xxxxxxxxxx       # Channel ID for upload logs
```

<details>
<summary>📌 Where to get these values?</summary>

<br>

- **API_ID & API_HASH** → Go to [my.telegram.org](https://my.telegram.org), log in, and create an app
- **BOT_TOKEN** → Open [@BotFather](https://t.me/BotFather) on Telegram and use `/newbot`
- **MONGO_URL** → Create a free cluster at [mongodb.com](https://mongodb.com)
- **ADMINS** → Your Telegram user ID (use [@userinfobot](https://t.me/userinfobot) to find it)
- **LOG_CHANNEL** → Create a private channel and add your bot as admin

</details>

---

## 🤖 BotFather Commands

Copy and paste this into [@BotFather](https://t.me/BotFather) → `Edit Bot` → `Edit Commands`:

```
start - 🚀 Start the bot
history - 🗂️ View your upload history
users - 👥 (Admin) View user stats
broadcast - 📢 (Admin) Broadcast a message
ban - 🚫 (Admin) Ban a user
unban - ✅ (Admin) Unban a user
```

---

## 📁 Project Structure

```
imgtolink/
├── 📄 bot.py              # Main bot entry point
├── 📄 config.py           # Configuration loader
├── 📄 database.py         # MongoDB handler
├── 📂 plugins/
│   ├── 📄 upload.py       # Upload handler
│   ├── 📄 admin.py        # Admin commands
│   └── 📄 start.py        # Start & history
├── 🐳 Dockerfile
├── 📄 requirements.txt
└── 📄 .env.example
```

---

## 💡 How It Works

```
User sends photo/video
        ↓
Bot downloads media locally
        ↓
Uploads to Catbox.moe API
        ↓
Returns permanent public link
        ↓
Logs upload to channel + DB
```

---

## 👨‍💻 Credits

<div align="center">

| Role | Info |
|------|------|
| 👨‍💻 Developer | [@codesXSupport](https://t.me/codesXSupport) |
| 📢 Channel | [CodeVoultX Bots](https://t.me/CodeVoultX_Bots) |

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1000&color=FF6B6B&center=true&vCenter=true&width=500&lines=⭐+Star+the+repo+if+you+found+it+useful!;🍴+Fork+it+to+build+your+own!;❤️+Don't+copy+without+credit!" alt="Footer Animation" />

<br>

> ⚠️ **Don't copy or redistribute without proper credit!**

</div>
