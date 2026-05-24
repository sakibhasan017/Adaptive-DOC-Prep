# Adaptive Document Preparation System

## Overview

This project is an adaptive study assistant that turns a long PDF document into a section-based preparation system.

A user can select one or more sections from the PDF, and the system will:
- extract the selected content,
- generate multiple-choice questions from those sections,
- accept and score user answers,
- explain wrong answers,
- store every prep session in a local SQLite database,
- and use past mistakes to generate better questions in later sessions.

The goal of the system is to make revision more efficient by focusing on the topics the user struggles with most, while avoiding unnecessary repetition of already-mastered content.

## Tech Stack
- Python
- FastAPI
- SQLite
- PyMuPDF
- Pydantic

## Project Structure
```text
app/
 ├── ingest.py   # PDF parsing and section extraction
 ├── llm.py      # question generation logic
 ├── kb.py       # SQLite knowledge base
 ├── prep.py     # end-to-end prep workflow
 ├── cli.py      # command-line interface
 └── main.py     # FastAPI REST API
```

## Install
```bash
pip install -r requirements.txt
```

## Run parser
```bash
python app/ingest.py
```

## Run single prep
```bash
python -m app.cli --sections 3 7
```

## Run Scenario B
```bash
python -m app.cli --scenario_b
```

Outputs created:
- outputs/scenario_b_iter1/
- outputs/scenario_b_iter2/
- outputs/scenario_b_iter3/

## Run API
```bash
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000/docs

## Notes
- Current implementation uses lightweight keyword extraction from the selected PDF sections to generate section aware MCQs without relying on paid APIs.
- The architecture is designed so that `app/llm.py` can be easily replaced with a real LLM backend such as Ollama, Groq, or Gemini.
- User answers are currently simulated during CLI runs to demonstrate scoring, history persistence, and adaptive behavior across sessions.