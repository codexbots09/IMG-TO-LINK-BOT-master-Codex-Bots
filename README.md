&lt;p align="center"&gt;
  &lt;img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=6A5ACD&center=true&vCenter=true&random=false&width=600&lines=Telegraph+Cloud+Uploader;Fast+%26+Secure+Media+Hosting;Catbox.moe+Integration;Telegram+Bot+Solution" alt="Typing Animation" /&gt;
&lt;/p&gt;

&lt;p align="center"&gt;
  &lt;img src="https://files.catbox.moe/qs361h.jpg" width="800px" alt="Telegraph Cloud Uploader Banner" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" /&gt;
&lt;/p&gt;

&lt;p align="center"&gt;
  &lt;b&gt;⚡ A Powerful Telegram Bot to Upload Media to Catbox.moe with Lightning Speed&lt;/b&gt;
&lt;/p&gt;

&lt;p align="center"&gt;
  &lt;a href="https://t.me/CodeVoultX_Bots"&gt;
    &lt;img src="https://img.shields.io/badge/Channel-CodeVoultX_Bots-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&labelColor=1a1a1a" alt="Telegram Channel"&gt;
  &lt;/a&gt;
  &lt;a href="https://t.me/codesXSupport"&gt;
    &lt;img src="https://img.shields.io/badge/Support-@codesXSupport-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&labelColor=1a1a1a" alt="Support Group"&gt;
  &lt;/a&gt;
  &lt;img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a1a" alt="Python"&gt;
  &lt;img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&labelColor=1a1a1a" alt="License"&gt;
&lt;/p&gt;

---

## ✨ Features

&lt;div align="center"&gt;

| Feature | Description |
|---------|-------------|
| ⚡ **Fast Uploads** | Direct integration with Catbox.moe for instant hosting |
| 🔗 **Permanent Links** | No expiry - Your files stay forever |
| 🗂️ **User History** | Track all uploads with `/history` command |
| 📊 **Statistics** | Detailed usage analytics for admins |
| 🛡️ **Admin Controls** | Ban/Unban users & Broadcast messages |
| 📢 **Log Channel** | Automatic logging of all uploads |
| 🐳 **Docker Ready** | One-click Docker deployment |

&lt;/div&gt;

## 🚀 Deployment Methods

### 💜 Heroku (One-Click Deploy)
&lt;p&gt;
  &lt;a href="https://heroku.com/deploy?template=https://github.com/CodeVoultX-Bots/imgtolink"&gt;
    &lt;img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" height="40"&gt;
  &lt;/a&gt;
&lt;/p&gt;

&lt;details&gt;
&lt;summary&gt;&lt;b&gt;Manual Heroku Setup&lt;/b&gt;&lt;/summary&gt;

1. 🍴 Fork this repository
2. 🆕 Create new app on [Heroku](https://heroku.com)
3. 🔗 Connect GitHub repository
4. ⚙️ Add Config Vars (see below)
5. ▶️ Deploy `worker` dyno

&lt;/details&gt;

### ☁️ Render (Free Tier)
&lt;details&gt;
&lt;summary&gt;&lt;b&gt;Click to Expand Steps&lt;/b&gt;&lt;/summary&gt;

1. 🍴 Fork this repo
2. 🆕 Create **Web Service** on [Render](https://render.com)
3. 🔗 Connect GitHub repository
4. ⚙️ Add Environment Variables
5. 🚀 Deploy! *(Runs 24/7 on free tier)*

&lt;/details&gt;

### 🐳 Docker Deployment
```bash
# Clone repository
git clone https://github.com/CodeVoultX-Bots/imgtolink.git
cd imgtolink

# Build Docker image
docker build -t telegraph-uploader .

# Run container
docker run -d --env-file .env --name telegraph-bot telegraph-uploader
