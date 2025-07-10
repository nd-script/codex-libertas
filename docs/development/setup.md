# 🛠️ Development Environment Setup

## Prerequisites

- Python 3.10 or newer
- Git
- pip (Python package manager)

## Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/nd-script/codex-libertas.git
   cd codex-libertas
   ```

2. Create and activate a virtual environment:
   ```bash
   # For Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # For Linux/Mac
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) For documentation development:
   ```bash
   pip install -r requirements-docs.txt
   ```

## Project Structure

```
codex-libertas/
├── docs/               # Documentation files
├── src/                # Source code
│   ├── archives/       # System archives
│   ├── artifacts/      # System artifacts
│   ├── core/           # Core components
│   ├── engines/        # System engines
│   ├── monitors/       # Monitoring systems
│   └── rituals/        # System rituals
├── tests/              # Test files
├── .gitignore          # Git ignored files
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE            # License file
├── README.md          # Project overview
└── requirements.txt   # Dependencies
```

## Running Tests

```bash
# Install test requirements
pip install -r requirements-test.txt

# Run all tests
pytest
```

## Building Documentation

```bash
# Install documentation requirements
pip install -r requirements-docs.txt

# Run documentation server locally
mkdocs serve
```

Then open your browser to:
`http://127.0.0.1:8000`

---

[Back to Home](../index.md)
