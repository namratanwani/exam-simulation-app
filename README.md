# AI-103 Exam Simulator

A local practice-question app for the Microsoft **AI-103: Developing AI Apps
and Agents on Azure** exam (Azure AI Apps and Agents Developer Associate).

1,389+ questions across all 4 official learning paths, pulled from Microsoft
Learn content in `modules/`.

## Setup

```
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run it

**Web UI** — open http://127.0.0.1:5050 in your browser:
```
python app.py
```

**CLI** — no dependencies needed, runs straight in the terminal:
```
python scripts/quiz.py
```

Either way, you pick:
- **Section-wise**, **module-wise**, or **full-exam** quiz
- How many questions (randomly sampled)

Answer them one at a time, then get a score and a review of anything missed.

## Structure

```
modules/
  01-develop-generative-ai-apps-in-azure/
  02-develop-ai-agents-on-azure/
  03-develop-natural-language-solutions-in-azure/
  04-extract-insights-from-visual-data-on-azure/
```

Numbered and named to match the official Microsoft Learn course order, so
the number tells you what to study next. Each module folder has:
- `content.md` — study notes for that module
- `questions.md` — practice questions with answers and explanations

See [MODULES.md](MODULES.md) for the full module list with source links.
