# New project setup: Git + uv + terminal (class workflow)

This handout is meant to be followed step-by-step during class.

By the end you will have:
- a local project with an isolated environment
- a Git repository with clean commits
- a GitHub remote you can push to
- a repeatable workflow for partners and group projects

---

## Prereqs (do once)

- Install VS Code
- Install Git (and sign in to GitHub)
- Install uv

Sanity checks:
```bash
git --version
uv --version
```

---

## Part 1: Create a new project (local)

### 1) Make a folder and initialize a uv project

Option A (one command creates the folder):
```bash
uv init myproject
cd myproject
```

Option B (initialize in an existing folder):
```bash
mkdir myproject
cd myproject
uv init
```

You should now have files like:
- `pyproject.toml`
- `.python-version`
- `README.md`
- `main.py`
- `.gitignore`

### 2) Initialize Git

```bash
git init
git status
```

If you do not see a `.gitignore` yet, create one and ignore the venv:
```bash
echo ".venv/" >> .gitignore
```

### 3) First commit

```bash
git add -A
git commit -m "Initial project scaffold"
```

---

## Part 2: Add dependencies and run code

### 4) Add a dependency
```bash
uv add httpx
```

### 5) Create a tiny script

Open `main.py` and replace its contents with:

```python
import httpx

def main() -> None:
    r = httpx.get(
        "https://icanhazdadjoke.com/",
        headers={"Accept": "application/json"},
        timeout=10,
    )
    r.raise_for_status()
    print(r.json()["joke"])

if __name__ == "__main__":
    main()
```

Run it:
```bash
uv run python main.py
```

### 6) Commit dependency changes

`uv add` updates `pyproject.toml` and `uv.lock`. Commit both.

```bash
git add pyproject.toml uv.lock main.py
git commit -m "Add httpx and fetch a JSON joke"
```

---

## Part 3: Connect to GitHub and push

### 7) Create a GitHub repo (web)
Create a new empty repo on GitHub. Do not add a README or .gitignore since you already have them locally.

### 8) Add a remote and push

Replace the URL with your repo URL.

```bash
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

---

## Part 4: VS Code integration (do this once per project)

### 9) Open the folder in VS Code
From the project folder:
```bash
code .
```

In VS Code:
- Install the **Python** extension
- Select the interpreter in `.venv` if prompted
- Open Source Control to view staged and unstaged changes

Tip: you can keep using the terminal with `uv run ...` and still use the Source Control UI for staging and commits.

---

## Short in-class exercise 1 (pairs, 10 minutes): "Reproduce my partner's project"

Goal: practice the reproducibility story.

1) Partner A pushes their repo.
2) Partner B runs:
   ```bash
   git clone <REPO_URL>
   cd <REPO_DIR>
   uv sync
   uv run python main.py
   ```
3) If it fails, diagnose together:
   - are you in the correct folder?
   - did you run `uv sync`?
   - is VS Code using `.venv` as the interpreter?

Swap roles if time.

---

## Short in-class exercise 2 (pairs or triads, 12 to 15 minutes): "Make and resolve a merge conflict in VS Code"

Goal: experience the conflict and learn the VS Code merge UI.

### Setup (shared)
One person is the "repo owner" and the other is the "collaborator".

1) Owner creates a new branch and changes the same line:
   ```bash
   git switch -c feature-owner
   ```
   Edit `README.md` and change a line like:
   - "Project description: ..." to "Project description: OWNER EDIT"
   Then:
   ```bash
   git add README.md
   git commit -m "Owner edits README"
   git push -u origin feature-owner
   ```

2) Collaborator creates a different branch and edits the same line differently:
   ```bash
   git switch -c feature-collab
   ```
   Edit the same line to "Project description: COLLAB EDIT"
   Then:
   ```bash
   git add README.md
   git commit -m "Collaborator edits README"
   git push -u origin feature-collab
   ```

### Trigger the conflict
Pick one of these approaches:

- **GitHub PR approach** (most realistic):
  - Open PR for `feature-owner` into `main`, merge it.
  - Open PR for `feature-collab` into `main`, observe conflict.

- **Local merge approach** (fastest in class):
  - On one machine:
    ```bash
    git switch main
    git pull
    git merge feature-collab
    ```
    You should now have a conflicted file.

### Resolve in VS Code
1) In VS Code, open the Source Control view.
2) Click the conflicted file. You should see conflict markers and resolution actions.
3) Use the inline buttons to choose:
   - Accept Current
   - Accept Incoming
   - Accept Both
   - Compare Changes
4) Edit the final text manually so it makes sense.
5) Save the file.
6) Stage, commit, and push:
   ```bash
   git add README.md
   git commit -m "Resolve merge conflict"
   git push
   ```

Success check: both partners `git pull` and confirm the README matches.
