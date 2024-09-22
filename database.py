import sqlite3
import pandas as pd
import sys
from pathlib import Path

path = sys.argv[0][:-12]
db_name = "daily.db"

db = Path(path, db_name)
if db.exists():
  sys.exit()

conn = sqlite3.connect(db)
cursor = conn.cursor()

queries = ['''CREATE TABLE "weather" (
	"id"	INTEGER NOT NULL,
	"state"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''',

'''CREATE TABLE "status" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''',

'''CREATE TABLE "sickness" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''',

'''CREATE TABLE "priority" (
	"id"	INTEGER NOT NULL,
	"priority"	INTEGER NOT NULL UNIQUE,
	"color"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''',

'''CREATE TABLE "emotions" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''',

'''CREATE TABLE "category" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL UNIQUE,
	"icon"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''',

'''CREATE TABLE "tasks" (
	"id"	INTEGER NOT NULL,
	"date_t"	DATE,
	"name"	TEXT,
	"category_id"	INTEGER,
	"status_id"	INTEGER,
	"end_date"	DATE,
	"repeat"	TIME,
	"priority_id"	INTEGER,
	"start_time"	TIME,
	"end_time"	TIME,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "category"("id"),
	FOREIGN KEY("priority_id") REFERENCES "priority"("id"),
	FOREIGN KEY("status_id") REFERENCES "status"("id")
);''',

'''CREATE TABLE "monitoring" (
	"date_m"	DATE NOT NULL,
	"day_assessment"	INTEGER,
	"weather_id"	INTEGER,
	"temperature"	INTEGER,
	"sleep_time"	REAL,
	"sickness_id"	INTEGER,
	PRIMARY KEY("date_m"),
	FOREIGN KEY("sickness_id") REFERENCES "sickness"("id"),
	FOREIGN KEY("weather_id") REFERENCES "weather"("id")
);''',

'''CREATE TABLE "day_emotions" (
	"date_m"	DATE NOT NULL,
	"emotion_id"	INTEGER NOT NULL,
	"intensity"	INTEGER,
	FOREIGN KEY("date_m") REFERENCES "monitoring"("date_m"),
	FOREIGN KEY("emotion_id") REFERENCES "emotions"("id")
);''']
for query in queries:
  cursor.execute(query)

conn.commit()
conn.close()

