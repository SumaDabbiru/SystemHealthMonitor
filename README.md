<<<<<<< HEAD
# SystemHealthMonitor
Python web API that checks the health of a system that comprise of a multi-level correlated components in a Directed Acyclic Graph (DAG) form

# System Health Monitor 🚀

The **System Health Monitor** is a FastAPI-based web application that visualizes the health status of system components structured as a Directed Acyclic Graph (DAG). The application offers both a JSON API endpoint and a visual web interface for health status representation.

---

## 📖 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Sample JSON Structure](#sample-json-structure)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🟢 Overview
The project is designed to:
- Simulate the health status of interconnected components.
- Generate a DAG graph visualizing healthy/unhealthy nodes.
- Provide a REST API for system health checks.
- Offer a UI-based visualization for a detailed overview.

---

## ✨ Features
✅ FastAPI-based architecture  
✅ JSON API for data exchange  
✅ HTML UI for visualization  
✅ Automated tests using `pytest`  
✅ Docker support for easy deployment  
✅ Fully documented code with comments  

---

## 📂 Project Structure
```
SystemHealthMonitor/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── endpoints/
│   │   ├── __init__.py
│   │   ├── healthcheck.py
│   │   ├── healthcheck_ui.py
│   │   └── root.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── dag_service.py
│   │   ├── graph_service.py
│   └── dag_graph.json
├── tests/
│   ├── __init__.py
│   ├── test_healthcheck.py
│   ├── test_healthcheck_ui.py
│   ├── test_root.py
├── .env
├── dag_json_generator.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Prerequisites
- **Python 3.10+**
- `venv` for virtual environment management
- `pip` package manager

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd SystemHealthMonitor
```

### Step 2: Create and Activate Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate     # Windows
source venv/bin/activate    # MacOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Generate the DAG graph for the input
```bash
python .\dag_json_generator.py     # Windows
python ./dag_json_generator.py    # MacOS/Linux
```

### Step 5: Run the Application
```bash
python -m uvicorn app.main:app --reload
```

---

## 🚀 Usage
### JSON API via `curl` (Recommended for CLI)
```bash
curl -X GET "http://localhost:8000/healthcheck/?dag_file=dag_graph.json"
```

```PowerShell
Invoke-RestMethod -Uri "http://localhost:8000/healthcheck/?dag_file=dag_graph.json" -Method Get
```

### Visual UI
1. Open your browser.
2. Go to **`http://localhost:8000/healthcheckui`** for visual results.

### Root Endpoint
Navigate to:
```
http://localhost:8000
```

This shows instructions and guidance to explore the API.

---

## 🌐 Endpoints
| Endpoint        | Method | Description |
|-----------------|---------|-------------|
| `/`              | GET     | Home page with instructions |
| `/healthcheck`   | POST    | JSON-based health check for DAG input |
| `/healthcheckui` | GET     | UI-based health visualization |

---

## 🟨 Sample JSON Structure

### Example `dag_graph.json` for API Testing
```json
{
    "components": [
        {"id": "Step 1", "dependencies": ["Step 2", "Step 3"]},
        {"id": "Step 2", "dependencies": ["Step 4"]},
        {"id": "Step 3", "dependencies": ["Step 5", "Step 6"]},
        {"id": "Step 4", "dependencies": []},
        {"id": "Step 5", "dependencies": []},
        {"id": "Step 6", "dependencies": []}
    ]
}
```

---

## ✅ Testing
Run the tests using `pytest`:

```bash
pytest -v
```

**Common Test Scenarios**
1. `/healthcheck` returns correct JSON format
2. `/healthcheckui` generates a proper UI page with table and graph
3. `/` endpoint displays the correct instructions page
>>>>>>> d41339c (Initial Commit)
