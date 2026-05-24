import random

from app.ingest import extract_sections
from app.llm import generate_mcqs
from app.kb import save_session, weak_topics


def run_prep(section_ids):

    sections = extract_sections("data/SLATEFALL_DOSSIER.pdf")

    combined = ""

    for sid in section_ids:
        combined += sections[sid] + "\n"

    weak = weak_topics(section_ids)

    questions = generate_mcqs(
        combined,
        weak_topics=weak,
        n=5
    )

    results = []
    score = 0

    for q in questions:

        if random.random() < 0.7:
            user_answer = q["answer"]
        else:
            wrongs = [
                x for x in q["options"]
                if x != q["answer"]
            ]
            user_answer = random.choice(wrongs)

        correct = user_answer == q["answer"]

        if correct:
            score += 1

        results.append({
            "question": q["question"],
            "topic": q["topic"],
            "correct": int(correct)
        })

    session_id = save_session(
        section_ids,
        score,
        results
    )

    return {
        "session_id": session_id,
        "score": score,
        "questions": questions,
        "weak_topics_used": weak
    }