import sqlite3
import json

DB = "prep.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        section_ids TEXT,
        score INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        question TEXT,
        topic TEXT,
        correct INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_session(section_ids, score, results):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO sessions(section_ids, score) VALUES (?,?)",
        (json.dumps(section_ids), score)
    )

    session_id = c.lastrowid

    for r in results:
        c.execute("""
        INSERT INTO questions(session_id, question, topic, correct)
        VALUES (?,?,?,?)
        """, (
            session_id,
            r["question"],
            r["topic"],
            r["correct"]
        ))

    conn.commit()
    conn.close()

    return session_id


def weak_topics(section_ids):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    SELECT topic, COUNT(*)
    FROM questions
    WHERE correct = 0
    GROUP BY topic
    ORDER BY COUNT(*) DESC
    """)

    rows = c.fetchall()
    conn.close()

    return [r[0] for r in rows[:5]]


def snapshot():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    SELECT * FROM sessions
    ORDER BY id DESC
    LIMIT 5
    """)

    rows = c.fetchall()
    conn.close()

    return rows