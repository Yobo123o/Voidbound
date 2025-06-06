# Voidbound

**Voidbound** is a dark fantasy, text-based roguelike RPG written in Python.  
This repository is in the very early stages of development. Core mechanics are still being prototyped and the codebase is likely to change rapidly.  
You are a soul cursed to die and return, trapped in a decaying world where memory fades, but pain persists. Each cycle brings you deeper into the truth — and closer to the void.

---

## 🌌 The Curse of the Voidbound

> *You awaken in darkness. Again.*  
> The stone beneath you is cold. Wet. You’ve lost count of how many times you've clawed your way out of the black.  
>  
> The world above has crumbled. The sky is cracked. The dead walk not by magic, but by memory.  
>  
> You are Voidbound — branded by the Sigil of Return, tethered to the last ember of a dying flame.  
> Each death rewinds the world. But something always stays.  
>  
> Escape is a lie. But understanding may not be.

---

## 🕹️ Features

- Turn-based combat with randomized enemy encounters  
- Exploration, rest, and risk-reward decisions  
- Death and rebirth mechanic (roguelike loop)  
- Atmospheric writing and lore-rich world  
- Custom GUI using `pygame_gui` over `pygame`  
- Modular codebase designed for expandability  

---

## 🚀 Getting Started

### Requirements

- Python **3.13+**
- See [`requirements.txt`](./requirements.txt)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/voidbound.git
cd voidbound
pip install -r requirements.txt
```

Optionally install in editable mode for development:

```bash
pip install -e .
```

### Run the Game

Run the prototype (once created):

```bash
python -m voidbound
```

---

## 🧱 Project Structure (planned)

```
.
├── LICENSE
├── README.md
├── requirements.txt
└── voidbound/
    ├── __init__.py
    ├── __main__.py         # Game entry point
    ├── engine.py           # Core game loop and scene manager
    ├── player.py           # Player stats, combat, inventory
    ├── enemies.py          # Enemy definitions and AI
    ├── world.py            # Zone/events/procedural logic
    ├── ui.py               # pygame_gui integration
    ├── audio.py            # Sound and music
    ├── lore.py             # Dialogs, intros, item text
    └── utils.py            # Formatting, helpers
```

---

## 📜 License

MIT License — free to use, modify, and build upon.

---

## 💡 Contributing

Pull requests and ideas welcome! This is an experimental solo project with an emphasis on creativity, simplicity, and story-driven design.

---

## 🧠 Inspired By

- Dark Souls / Hollow Knight  
- Dwarf Fortress / Cataclysm DDA  
- Classic roguelikes and MUDs  
