# 💬 Chat Message History Manager

A lightweight and modular **Chat Message History Manager** built in Python.

🧠 It uses classic data structures to simulate chat operations:

- **Queue** → Incoming message processing (FIFO)
- **Stacks** → Undo and Redo actions (LIFO)
- **Timestamps** → Log every message accurately

---

## 🚀 Features

- 📥 **Incoming Message Queue** – Maintain order of received messages
- 📤 **Sent Message Stack** – Track outgoing messages
- ⏪ **Undo/Redo** – Easy retract and re-send of messages
- 🕒 **Timestamp Tracking** – UTC-based timestamps for all actions
- 🖥️ **Console-based UI** – Neat and readable output

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Data Structures**:
  - `Queue` for incoming messages
  - `Stack` for undo/redo
  - `@dataclass` to model messages

---

## 📂 Project Structure

```
chat-message-history-manager/
┣ 📜 chat_manager.py         # Core logic
┣ 📂 screenshots/            # Terminal demo outputs
┣ 📜 README.md               # This file
┣ 📜 .gitignore              # (optional)
```

---

## ⚡ How to Run

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/chat-message-history-manager.git
cd chat-message-history-manager
```

2. **Run the program**  
```bash
python chat_manager.py
```

---

## 🖼️ Screenshots

> Add screenshots like this:

**Message Processing**
![Screenshot](screenshots/queue_demo.png)

**Undo/Redo Demo**
![Screenshot](screenshots/undo_redo.png)

---

## 🎯 Future Enhancements

- Menu-driven CLI
- Persistent chat log file
- GUI with Tkinter or PyQt
- Multi-user support

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

---
