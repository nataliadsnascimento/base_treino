import os
import sqlite3

DB_NAME= "AtividadeTreino.db"
DB_PATH= os.path.join(os.path.dirname(__file__), DB_NAME)

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn
    