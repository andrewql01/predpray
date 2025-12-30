# Predator-Prey Simulation

A predator-prey simulation built with Mesa and visualized using pygame.

## Prerequisites

This project uses:
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver
- **[ty](https://docs.astral.sh/ty/)** - Fast Python type checker

## Installation

### Install uv

Install `uv` using one of the following methods:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Or using pip:**
```bash
pip install uv
```

### Install ty

`ty` is included in the dev dependencies and will be installed automatically. You can also install it globally:

```bash
uv pip install ty
```

Or use it directly with `uvx`:
```bash
uvx ty check
```

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd predpray
```

### 2. Install dependencies

```bash
uv sync
```

This will:
- Create a virtual environment (`.venv`)
- Install all project dependencies
- Install dev dependencies (including `ty`, `ruff`, `pre-commit`)

### 3. Run the simulation

```bash
uv run python main.py
```

### 4. Type checking

Run type checking with `ty`:

```bash
uv run ty check
```

Or use `uvx`:
```bash
uvx ty check
```

## Development Workflow

### Running commands

All Python commands should be run with `uv run`

### Pre-commit hooks

This project uses pre-commit hooks for code quality. Install them:

```bash
uv run pre-commit install
```

The hooks will automatically:
- Run `ruff` for linting and formatting
- Run `ty` for type checking

### Project Structure

```
predpray/
├── agents/          # Agent classes (Predator, Prey, base agent)
├── world/           # Environment and configuration
├── ui/              # Pygame visualization classes
├── main.py          # Entry point
└── pyproject.toml   # Project configuration and dependencies
```

## Dependencies

- **mesa** - Agent-based modeling framework
- **pygame** - Game development library for visualization
- **torch** - PyTorch for neural networks (if using AI agents)
- **numpy** - Numerical computing
- **matplotlib** - Plotting (if needed)
