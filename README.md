# 📦 Repo-Archi-Graph

> **AI-Powered Architecture Intelligence Platform**  
> Visualize, analyze, and audit your codebase with deep architectural reasoning powered by IBM Bob AI.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128+-green.svg)](https://fastapi.tiangolo.com/)
[![IBM Bob](https://img.shields.io/badge/IBM%20Bob-AI%20Powered-purple.svg)](https://www.ibm.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎯 Concept

**Repo-Archi-Graph** is an enterprise-grade, fullstack AI application that transforms static codebases into **interactive architectural intelligence networks**. By leveraging IBM Bob's advanced contextual reasoning capabilities, it generates real-time insights into:

- **Blast Radius Analysis** - Quantify the impact of modifying each file
- **Technical Debt Auditing** - AI-driven critique of architectural weaknesses
- **Dependency Mapping** - Visual relationship graphs between system components
- **Risk Scoring** - Predictive metrics for maintenance complexity

This project showcases a **decoupled, production-ready architecture** combining Python backend intelligence with modern frontend visualization.

---

## ✨ Key Features

### 🔍 Interactive Architecture Graph
- **Force-directed network visualization** using Vis.js
- Real-time node inspection with contextual metrics
- Color-coded layers (Python, Frontend, Data, Documentation)
- Smooth physics-based layout with professional styling

### 🎯 AI-Powered Blast Radius Score
- **1-10 risk scoring system** for each file
- Predicts cascading effects of code modifications
- Identifies high-impact architectural components
- Enables proactive risk mitigation strategies

### ⚠️ Architectural Debt Audit
- **Brutally honest AI critique** of code quality
- Identifies violations of SOLID principles
- Detects security vulnerabilities and anti-patterns
- Provides actionable refactoring recommendations

### 📊 Advanced Metrics Dashboard
- Lines of Code (LOC) analysis
- Layer/Group classification
- Dependency relationship mapping
- Real-time data streaming from backend API

---

## 🛠️ Tech Stack

### Backend (Intelligence Layer)
- **FastAPI** - High-performance async Python web framework
- **Uvicorn** - Lightning-fast ASGI server
- **IBM Bob AI** - Advanced contextual reasoning engine
- **Python 3.11+** - Modern language features

### Frontend (Visualization Layer)
- **Vis.js** - Network graph rendering engine
- **Vanilla JavaScript** - Zero-dependency, lightweight
- **HTML5/CSS3** - Modern responsive design
- **Catppuccin Color Palette** - Professional dark theme

### Data Layer
- **JSON Schema** - Structured architectural metadata
- **CORS-enabled API** - Secure cross-origin communication

---

## 🏗️ Architecture Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     IBM Bob AI Engine                        │
│            (Contextual Reasoning & Analysis)                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              FastAPI Backend (Port 8080)                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  GET /api/analyze                                     │   │
│  │  • Reads output/architecture.json                     │   │
│  │  • Validates JSON schema                              │   │
│  │  • Returns structured data with CORS headers          │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/JSON
                       ▼
┌─────────────────────────────────────────────────────────────┐
│           Vis.js Frontend (template/index.html)              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  • Fetches data via fetch() API                       │   │
│  │  • Renders interactive force-directed graph           │   │
│  │  • Displays metrics on node click                     │   │
│  │  • Real-time blast radius & debt visualization        │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Edge)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/NHZ-DS/Repo-Archi-Graph.git
cd Repo-Archi-Graph
```

2. **Install Python dependencies**
```bash
python -m pip install fastapi uvicorn
```

3. **Start the FastAPI backend**
```bash
python core/scanner.py
```

The server will start at `http://127.0.0.1:8080`

4. **Open the visualization**
- Open `template/index.html` in your browser
- Or navigate to `http://127.0.0.1:8080` (if serving static files)

---

## 🤖 IBM Bob Integration

### How IBM Bob Powers the Intelligence

**Repo-Archi-Graph** leverages IBM Bob's advanced AI capabilities to transform raw code into actionable architectural intelligence:

#### 1. **Contextual Code Analysis**
IBM Bob analyzes the entire codebase context, understanding:
- Import relationships and dependency chains
- Function signatures and call hierarchies
- Design patterns and architectural styles
- Cross-file coupling and cohesion metrics

#### 2. **Blast Radius Calculation**
Using deep reasoning, Bob predicts:
- Which files are most critical to system stability
- Cascading effects of modifications
- Risk propagation through dependency graphs
- Impact scoring on a 1-10 scale

#### 3. **Technical Debt Detection**
Bob identifies architectural anti-patterns:
- SOLID principle violations
- Code smells and maintainability issues
- Security vulnerabilities
- Performance bottlenecks
- Missing documentation and tests

#### 4. **Intelligent Recommendations**
Bob provides actionable insights:
- Refactoring strategies
- Modularization opportunities
- Dependency injection patterns
- Test coverage improvements

### AI-Generated Metadata Schema

```json
{
  "nodes": [
    {
      "id": "file/path.py",
      "label": "filename",
      "group": "python|frontend|data|documentation",
      "summary": "AI-generated architectural role description",
      "metrics": {
        "blast_radius_score": 1-10,
        "lines_of_code": 123,
        "architectural_debt": "AI critique and recommendations"
      }
    }
  ],
  "edges": [
    {
      "from": "source.py",
      "to": "target.py",
      "label": "semantic relationship description"
    }
  ]
}
```

---

## 📁 Project Structure

```
Repo-Archi-Graph/
├── core/
│   └── scanner.py          # FastAPI backend server
├── template/
│   └── index.html          # Vis.js frontend visualization
├── output/
│   └── architecture.json   # AI-generated architectural data
├── .gitignore              # Security exclusions
├── HOW_TO_RUN.md          # Quick start guide
└── README.md              # This file
```

---

## 🎨 Features Showcase

### Interactive Node Inspection
Click any node in the graph to reveal:
- **File name and layer classification**
- **Blast radius risk score** (color-coded: green=safe, red=critical)
- **Lines of code metrics**
- **AI-generated architectural debt audit**

### Professional Visualization
- Dark theme optimized for developer workflows
- Color-coded by technology layer
- Smooth physics-based animations
- Responsive sidebar with real-time metrics

---

## 🔒 Security & Best Practices

- ✅ CORS properly configured for secure API access
- ✅ Input validation and error handling
- ✅ No hardcoded credentials or API keys
- ✅ Comprehensive .gitignore for sensitive files
- ✅ Async/await patterns for optimal performance
- ✅ Type hints and documentation throughout

---

## 🏆 IBM Bob Hackathon Submission

This project demonstrates:
- **Advanced AI Integration** - Leveraging IBM Bob's reasoning capabilities
- **Fullstack Architecture** - Decoupled backend/frontend design
- **Production-Ready Code** - Error handling, CORS, async patterns
- **Real-World Value** - Solves actual developer pain points
- **Scalability** - Extensible to any codebase size
- **Professional Polish** - Enterprise-grade UI/UX

---

## 📝 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Author

**Built with IBM Bob AI** - Showcasing the power of AI-assisted fullstack development

*Transforming code analysis into architectural intelligence* 🚀