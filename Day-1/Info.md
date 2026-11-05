# Day 1: Python Setup & Environment Configuration

## 🎯 Learning Objectives
- Install and configure Python for machine learning development
- Set up a proper development environment (IDE/editor)
- Write and execute first Python program

---

## 📦 Python Installation

### Version Installed
- **Python 3.x** (latest stable version)
- Downloaded from [python.org](https://www.python.org/downloads/)

### Installation Notes
- ✅ Added Python to PATH during installation
- ✅ Verified installation with `python --version` and `pip --version`
- ✅ Installed `pip` (package manager) for dependency management

---

## 🛠️ Code Editor Evaluation

| Editor | Pros | Cons | Decision |
|--------|------|------|----------|
| **VS Code** | Lightweight, excellent Python extension, integrated terminal, Git support, debugging, free | Can be overwhelming initially | ✅ **Selected** |
| PyCharm Community | Full-featured Python IDE, smart code completion | Heavier, slower startup | Considered |
| Jupyter Notebook | Great for exploratory analysis, visualization | Not ideal for full scripts/projects | For later use |
| Sublime Text | Fast, minimal | Limited Python-specific features out of box | Not selected |

### VS Code Extensions Installed
- **Python** (Microsoft) — core language support
- **Pylance** — fast, feature-rich language server
- **Jupyter** — notebook support within VS Code
- **GitLens** — enhanced Git integration
- **Error Lens** — inline error highlighting

---

## ⚙️ VS Code Configuration

### Key Settings (`settings.json`)
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
  },
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
}
```

### Workspace Setup
- Created project folder: `machine-learning-mastery`
- Initialized Git repository
- Created virtual environment (recommended practice)

---

## 🐍 First Python Program: `first.py`

### Code
```python
# first.py - My first Python program for ML journey
print("Hello, Machine Learning World!")
print("Day 1: Python environment setup complete ✅")
```

### Execution
```bash
python first.py
```

### Output
```
Hello, Machine Learning World!
Day 1: Python environment setup complete ✅
```

---

## 📚 Key Concepts Learned

| Concept | Description |
|---------|-------------|
| **Interpreter vs Compiler** | Python is interpreted — code executes line by line |
| **Virtual Environments** | Isolated environments for project dependencies (`venv`, `conda`) |
| **Package Management** | `pip` for installing libraries (`numpy`, `pandas`, `scikit-learn`, etc.) |
| **IDE vs Editor** | IDE = batteries included; Editor = lightweight + extensions |

---

## ✅ Day 1 Checklist

- [x] Python installed and verified
- [x] VS Code installed and configured
- [x] Python extension + Pylance installed
- [x] Virtual environment created
- [x] First Python script written and executed
- [x] Git repository initialized
- [x] This documentation created

---

## 🎯 Next Steps (Day 2 Preview)
- Python fundamentals: variables, data types, control flow
- Introduction to Jupyter Notebooks
- Basic NumPy arrays and operations
- Reading/writing data with pandas

---

## 📝 Reflection

> **Time spent:** ~2 hours  
> **Biggest win:** Clean, reproducible dev environment ready for ML work  
> **Challenge:** Choosing between editors — VS Code won for flexibility  
> **Mindset:** "Environment setup is not wasted time — it's the foundation for everything that follows."

---

*Last updated: 2026-11-05*  
*Part of: [Machine Learning Mastery Journey](../README.md)*