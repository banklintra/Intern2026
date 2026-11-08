# Innkeypslisti API
# Koyr við:  python -m uvicorn main:app --reload
import sqlite3
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Loyvir eini síðu (HTML ella React) á aðrari adressu at kalla á API'ið.
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Listin verður goymdur í hesi fíluni. Fílan er ein SQLite database.
DB = Path(__file__).parent.parent / "sql" / "innkeypslisti.db"


def query(sql, params=()):
    conn = sqlite3.connect(DB)
    rows = conn.execute(sql, params).fetchall()
    conn.commit()
    conn.close()
    return rows


@app.get("/api/items")
def get_items():
    rows = query("SELECT name FROM item ORDER BY id")
    return [row[0] for row in rows]


@app.post("/api/items")
def add_item(item: str):
    query("INSERT INTO item (name, amount, price) VALUES (?, 1, 0)", (item,))
    return get_items()
