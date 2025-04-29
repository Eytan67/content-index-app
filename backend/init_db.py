import sqlite3

# צור קובץ database.db
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# צור טבלת creators
cursor.execute("""
    CREATE TABLE IF NOT EXISTS creators (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        page_url TEXT NOT NULL
    )
""")

# צור טבלת lessons
cursor.execute("""
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creator_id INTEGER,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        file_path TEXT NOT NULL,
        FOREIGN KEY (creator_id) REFERENCES creators(id)
    )
""")

# הוסף נתוני דמה ל-creators
cursor.execute("INSERT INTO creators (name, page_url) VALUES (?, ?)", ("Creator 1", "/creators/creator1"))
cursor.execute("INSERT INTO creators (name, page_url) VALUES (?, ?)", ("Creator 2", "/creators/creator2"))

# הוסף נתוני דמה ל-lessons (עם נתיבי קבצים דמה)
cursor.execute("INSERT INTO lessons (creator_id, title, content, file_path) VALUES (?, ?, ?, ?)",
              (1, "Python Basics", "Lesson about Python", "uploads/lesson1.mp4"))
cursor.execute("INSERT INTO lessons (creator_id, title, content, file_path) VALUES (?, ?, ?, ?)",
              (2, "React Tutorial", "Lesson about React", "uploads/lesson2.mp3"))

# שמור ושחרר
conn.commit()
conn.close()