from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust this to your frontend's URL
    allow_origin_regex="http://localhost:5173",  # Allow any subdomain of localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/creators")
async def get_creators():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, page_url FROM creators")
    creators = [{"id": row[0], "name": row[1], "page_url": row[2]} for row in cursor.fetchall()]
    conn.close()
    return creators

@app.get("/lessons")
async def get_lessons():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT l.id, l.title, l.content, l.file_path, c.name
        FROM lessons l
        JOIN creators c ON l.creator_id = c.id
    """)
    lessons = [{"id": row[0], "title": row[1], "content": row[2], "file_path": row[3], "creator_name": row[4]}
              for row in cursor.fetchall()]
    conn.close()
    return lessons