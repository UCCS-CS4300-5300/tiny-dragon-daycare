# Tiny Dragon Daycare

A deliberately tiny Django teaching application for CS 4300/5300 Advanced Software Engineering.

This repository will evolve throughout the semester as we introduce testing, GitHub workflows, CI/CD, architecture, security, AI-assisted engineering, and legacy-code practices.

## Recommended: Run in GitHub Codespaces

1. On the repository page, click **Code**.
2. Open the **Codespaces** tab.
3. Click **Create codespace on main**.
4. Wait for the environment to finish setting up. Dependencies and database migrations are installed automatically.
5. In the Codespaces terminal, run:

```bash
python manage.py runserver 0.0.0.0:8000
```

Codespaces should automatically offer/open a preview of Tiny Dragon Daycare.

Run the tests with:

```bash
pytest
```

## Alternative: Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# Windows PowerShell: .venv\Scripts\Activate.ps1

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Run the tests

```bash
pytest
```

The starter app intentionally has only two very readable tests. We will grow the application and its engineering practices throughout the semester.
