# pycalc

A tiny Python calculator library, built as a practice project for learning
CI/CD with GitHub Actions.

## What's here

- `calculator.py` — the app (add, subtract, multiply, divide, is_prime, factorial)
- `test_calculator.py` — pytest unit tests
- `requirements.txt` — dependencies (pytest, flake8)
- `.github/workflows/ci.yml` — GitHub Actions workflow: runs lint + tests
  on every push/PR to `main`

## Run it locally

```bash
pip install -r requirements.txt
python calculator.py       # run the demo
pytest -v                  # run tests
flake8 . --max-line-length=100   # lint
```

## Set up the pipeline

1. Create a new GitHub repo (e.g. `pycalc`).
2. Push this folder to it:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: calculator app + tests"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
3. Go to the **Actions** tab on GitHub — the `CI` workflow should run
   automatically on the push.
4. Try breaking a test on purpose, push it, and watch the workflow fail —
   then fix it and watch it go green. That's the core CI feedback loop.

## Ideas to extend once this works

- Add a badge to this README showing the build status.
- Add a second job that only runs on `main` and builds a Docker image.
- Add a step that uploads a coverage report (`pytest --cov`).
- Add a deploy job (e.g. push to PyPI test index, or deploy to AWS) gated
  on the test job passing — this is where CI turns into CD.
