# 🌌 **DREAMFORGE — Generative World Builder**

**DREAMFORGE** is an AI-powered **fictional universe generator** that transforms short seed prompts into fully developed worlds — including **lore, geography, species, cultures, factions, histories, and story hooks**.

Built on top of **`google/flan-t5-xl`**, DREAMFORGE provides a streamlined way for writers, game designers, and worldbuilding enthusiasts to bootstrap creative content using a lightweight Python pipeline and an optional Streamlit UI.



## ✨ **Features**

- 🧠 **AI-Generated Worlds**  
  Convert a single sentence into a complete fictional setting.

- 🌍 **World Components**  
  DREAMFORGE outputs:
  - 🔸 World name  
  - 🔸 Geography & regions  
  - 🔸 Species & races  
  - 🔸 Factions & organizations  
  - 🔸 Cultural elements  
  - 🔸 Technologies or magic systems  
  - 🔸 Story hooks / plot seeds  

- ⚡ **Lightweight Pipeline**  
  Built using **Hugging Face Transformers** for local inference.

- 🖥️ **Streamlit UI**  
  A clean interface for interactively generating worlds.

- 📚 **Examples & Notebooks**  
  Includes sample prompts and a demonstration notebook.



## 📦 **Installation**

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/dreamforge.git
cd dreamforge
```

### 2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Install the model  
DREAMFORGE uses the **FLAN-T5-XL** model:

```bash
pip install transformers accelerate sentencepiece
```



## 🚀 **Usage**

### 🧪 **Python Pipeline**

```python
from dreamforge.pipeline import DreamForgeWorldBuilder

builder = DreamForgeWorldBuilder(model_name="dreamforge")

prompt = "A dying star empire on the edge of the galaxy."

world = builder.generate_world(prompt)
print(world)
```


## 🖥️ **Streamlit Interface**

Run the local UI:

```bash
streamlit run ui/app.py
```

Then open your browser at:

```
http://localhost:8501
```

You'll be able to enter prompts and explore generated universes interactively.



## 📁 **Project Structure**

```
dreamforge/
│
├── pipeline/              # World generation pipeline
├── ui/                    # Streamlit interface
├── examples/              # Sample prompts + outputs
├── notebooks/             # Demo Jupyter notebooks
├── model/                 # Model loading utilities
└── README.md
```



## 📝 **Example Prompt**

**Prompt:**  
> “A floating archipelago ruled by dream-eating spirits.”

**Output Includes:**  
✨ World Name  
🗺️ Geography (floating islands, dream rifts)  
👁️ Species (spirit lords, skyborn tribes)  
🏛️ Factions (The Sleepwatchers, The Hollow Court)  
📖 History (The Shattering Dream)  
🔥 Story Hooks (the awakening of the First Sleeper)

