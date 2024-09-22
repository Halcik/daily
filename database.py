import sqlite3
import pandas as pd
import os
import sys
from pathlib import Path

path = sys.argv[0][:-12]
db_name = "daily.db"

db = Path(path, db_name)
if db.exists():
  sys.exit()

conn = sqlite3.connect(db)
# cursor = conn.cursor()
# query =
# conn.commit()

conn.close()

