# 🤖 Discord Gemini Bot 🚀

🌟 A powerful **Discord bot** that integrates **Google Vertex AI's Gemini models** to generate AI-powered responses! ✨

---

## ✨ Features 🎉

- ✅ **AI-powered responses**: generate text using **Gemini AI** models.  
- ✅ **Model selection**: choose between **🚀 Gemini 1.5 Flash**, **✨ Gemini 1.5 Pro**, or **🌌 Gemini-Exp-1206**.  
- ✅ **Interactive UI**: uses Discord's interactive UI components (buttons, modals, and dropdowns).  
- ✅ **Text-based & file-based prompting**: supports both **direct text input** and **file uploads**.  
- ✅ **Session management**: each user gets their **own AI chat session**.  

---

## 📌 Dependencies 📦

- 🛠 **py-cord**: Discord API wrapper for bot development.
- ✨ **google-cloud-aiplatform** & **vertexai**: Google Cloud Vertex integration and platform API.
- 🔑 **python-dotenv**: loads environment variables from ```.env``` file.

---

## ⚙️ Installation 🛠

### 1️⃣ Clone the repository 🏗️
```sh
git clone https://github.com/Braun-Alex/discord-gemini-bot.git
cd discord-gemini-bot
```

### 2️⃣ Create a virtual environment 🐍
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies 📦
```pip3 install -r requirements.txt```

### 4️⃣ Set up Google Cloud authorization 🔑
The bot uses **Google Vertex AI API** to generate responses. You must authenticate with **Google Cloud**.

### 5️⃣ Set up environment variables 🌍
Create a ```env``` file in the root directory and add:
```env
DISCORD_BOT_API_TOKEN=your_discord_bot_token
GOOGLE_CLOUD_API_KEY=your_google_cloud_project_id
```

### 6️⃣ Run the bot 🚀
```python3 bot.py```

---

## ⚡ Usage 🔄

### 1️⃣ Start the bot 🎬

Once the bot is running, use ```/prompt``` in your Discord server.
### 2️⃣ Select a Gemini model 🏆

A dropdown will appear, allowing you to select one of the following AI models:

- **🚀 Gemini 1.5 Flash**: fast but less powerful.
- **✨ Gemini 1.5 Pro**: balanced speed and intelligence.
- **🌌 Gemini-Exp-1206**: experimental and most advanced.

Once selected, your **AI chat session starts**.

### 3️⃣ Choose a prompt type 📜

You will be given **two options** to submit a prompt:

- **📘 Long prompt**: upload a ```.txt``` file containing the prompt.
- **📝 Short prompt**: directly enter a text prompt.

### 4️⃣ AI processing & response 🤖

The bot will process your prompt using **Google Vertex AI** and respond in the Discord chat.

### 5️⃣ Continue chatting 💬

You can **continue the conversation** with Gemini AI until you close the session.

---

## 🤝 Contributing

⭐ Want to improve this bot? Fork the repository and submit a **pull request**!

1. Fork the repository.
2. Create a feature branch ```git checkout -b feature-name```.
3. Commit changes ```git commit -m "Add feature"```.
4. Push to GitHub ```git push origin feature-name```.
5. Open a **pull request** 🚀.

---

## 📄 License 📜

📜 **MIT license**: free to modify and distribute. See the repository LICENSE file for details.
