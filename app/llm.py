from app.models import MCQ
import re


def extract_keywords(text, top_n=5):
    words = re.findall(r'\b[A-Za-z]{5,}\b', text)

    stop = {
        "section", "which", "their", "there", "about",
        "these", "those", "shall", "would", "could",
        "under", "after", "before", "while"
    }

    freq = {}

    for w in words:
        w = w.lower()

        if w in stop:
            continue

        freq[w] = freq.get(w, 0) + 1

    sorted_words = sorted(freq.items(),
                          key=lambda x: x[1],
                          reverse=True)

    return [w[0] for w in sorted_words[:top_n]]


def generate_mcqs(section_text, weak_topics=None, n=5):

    keywords = extract_keywords(section_text)

    if weak_topics:
        keywords = weak_topics + keywords

    keywords = list(dict.fromkeys(keywords))

    questions = []

    for i in range(min(n, len(keywords))):

        topic = keywords[i]

        q = MCQ(
            question=f"What is the role/significance of '{topic}' in this section?",
            options=[
                f"{topic} is critical",
                f"{topic} is irrelevant",
                f"{topic} is optional",
                f"{topic} is deprecated"
            ],
            answer=f"{topic} is critical",
            explanation=f"The section emphasizes {topic}.",
            topic=topic
        )

        questions.append(q.dict())

    return questions