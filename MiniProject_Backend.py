import sqlite3

def MovieData():
    try:
        con = sqlite3.connect("movie1.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Movie_ID TEXT, Movie_Name TEXT, Release_Date TEXT, Director TEXT, Cast TEXT, Budget TEXT, Duration TEXT, Rating TEXT)")
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print("Error while creating table:", e)

def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    try:
        con = sqlite3.connect("movie1.db")
        cur = con.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
        con.commit()
        con.close()
        print("Record added successfully!")
    except sqlite3.Error as e:
        print("Error while adding record:", e)

def ViewMovieData():
    try:
        con = sqlite3.connect("movie1.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        con.close()
        return rows
    except sqlite3.Error as e:
        print("Error while fetching records:", e)

def DeleteMovieRec(id):
    try:
        con = sqlite3.connect("movie1.db")
        cur = con.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        con.commit()
        con.close()
        print("Record deleted successfully!")
    except sqlite3.Error as e:
        print("Error while deleting record:", e)

def SearchMovieData(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    try:
        con = sqlite3.connect("movie1.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?", (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
        rows = cur.fetchall()
        con.close()
        return rows
    except sqlite3.Error as e:
        print("Error while fetching records:", e)

def UpdateMovieData(id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    try:
        con = sqlite3.connect("movie1.db")
        cur = con.cursor()
        cur.execute("UPDATE book SET Movie_ID=?, Movie_Name=?, Release_Date=?, Director=?, Cast=?, Budget=?, Duration=?, Rating=? WHERE id=?", (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating, id))
        con.commit()
        con.close()
        print("Record updated successfully!")
    except sqlite3.Error as e:
        print("Error while updating record:", e)
