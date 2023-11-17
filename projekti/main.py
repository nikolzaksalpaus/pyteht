from tkinter import *
import sqlite3

global kirjautuminen # Kirjautumisen ikunan muuttuja

kirjautuminen = Tk()
kirjautuminen.title("Tietokanta")
kirjautuminen.geometry("450x400") # Ikkunan koko

conn = sqlite3.connect("tasks.db") # Tietokantaan yhdistäminen

c = conn.cursor()

# Luo tehtävien taulu jos ei jo ole olemassa
sql = '''CREATE TABLE IF NOT EXISTS tasks (
    task VARCHAR (255),
    userOid INT
)'''

c.execute(sql)

# Luo käyttäjien taulu jos ei jo ole olemassa
sql = '''CREATE TABLE IF NOT EXISTS users (
    login VARCHAR (255),
    password VARCHAR (255)
)'''

c.execute(sql)

# Committa muutokset
conn.commit()

# Sulje tietokantayhteys
conn.close()

def avaaPaneeli():
    # Kirjautumisen jälkeen avautuvan ikkunan näkymä
    # Paneelin ikkuna, kun käyttäjä kirjautui
    global paneeli # Paneelin ikkuna
    paneeli = Tk()
    paneeli.title("Tietokanta")
    paneeli.geometry("400x400")

    global task_label
    task_label = Label(paneeli, text="Tehtävä")
    task_label.grid (row=0, column=0, pady=(10,0))

    global task
    task = Entry(paneeli, width=30)
    task.grid(row=0, column=1, padx=20, pady=(10,0))

    global submit_btn
    submit_btn = Button(paneeli, text="Lisää tehtävä tietokantaan", command=submit)
    submit_btn.grid (row=2, column=0, columnspan=2, pady=10, padx=10)

    global select_label
    select_label = Label(paneeli, text="Valitse ID")
    select_label.grid (row=4, column=0, pady=5)

    global delete_box
    delete_box = Entry(paneeli, width=30)
    delete_box.grid (row=4, column=1, pady=5)

    global delete_btn
    delete_btn = Button(paneeli, text="Poista tehtävä", command=delete)
    delete_btn.grid (row=5, column=0, columnspan=2, pady=10, padx=10)

    edit_btn = Button (paneeli, text="Muokkaa tehtävää", command=edit)
    edit_btn.grid (row=6, column=0, columnspan=2, pady=10, padx=10)

    query() # Päivittää tasklista ikkunassa

    kirjautuminen.destroy() # Sulkea tasklista ikkunassa

    paneeli.mainloop()

def query():
    conn = sqlite3.connect("tasks.db")

    c = conn.cursor()

    c.execute("SELECT task, oid FROM tasks WHERE userOid = " + str(kayttaja))
    records=c.fetchall()

    print_records = ''

    for record in records:
        print_records += str(record [0]) + "\t" + str(record [1]) + "\n"
    
    heading_label = Label(paneeli, text="Helvetica", font=("Helvetica", 16))

    heading_label['text'] = "Tehtävä \t ID"
    heading_label.grid (row=7, column=0, columnspan=2)

    query_label = Label(paneeli)

    query_label['text'] = print_records
    query_label.grid (row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

def submit():
    conn = sqlite3.connect("tasks.db")

    c = conn.cursor()

    # Insert into table

    c.execute("INSERT INTO tasks VALUES (:task, :userOid)",
        {
        'task': task.get(),
        'userOid': kayttaja
        })
    
    # commit changes
    conn.commit()

    # close connection
    conn.close()
    
    task.delete(0, END)

    query() # Päivittää tasklista ikkunassa

def delete():
    conn = sqlite3.connect("tasks.db")

    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    query() # Päivittää tasklista ikkunassa

def update():
    conn = sqlite3.connect("tasks.db")

    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("""UPDATE tasks SET
        task = :task
        WHERE oid = :oid""",
        {
            'task': task_editor.get(),
            'oid': record_id
        })
    
    conn.commit()
    conn.close()
    editor.destroy()

    query() # Päivittää tasklista ikkunassa

def edit():
    global editor
    editor = Tk()
    editor.title("Päivitä")
    editor.geometry("400x400")

    conn = sqlite3.connect("tasks.db")

    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM tasks WHERE oid = ?", (record_id,))
    records=c.fetchall()

    global task_editor

    task_label = Label(editor, text="Tehtävä")
    task_label.grid (row=0, column=0, pady=(10,0))

    task_editor = Entry(editor, width=30)
    task_editor.grid (row=0, column=1, padx=20, pady=(10,0))

    for record in records:
        task_editor.insert(0, record [0])

    save_btn = Button(editor, text="Tallenna", command=update)
    save_btn.grid (row=2, column=0, columnspan=2, pady=10, padx=10)

    query() # Päivittää tasklista ikkunassa

def register():     
    # Luo tietokanta nimeltä tasks
    conn = sqlite3.connect("tasks.db")

    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (:login, :password) WHERE NOT EXISTS (SELECT 1 FROM users WHERE login = ':login')",
        {
        'login': loginInput.get(),
        'password': passwordInput.get()
        }) # Luo uuden käyttäjän jos sama käyttäjän nimi ei ole olemassa

    # Committa muutokset
    conn.commit()

    # Sulje tietokantayhteys
    conn.close()

def login():
    # Luo tietokanta nimeltä tasks
    conn = sqlite3.connect("tasks.db")

    c = conn.cursor()

    c.execute("SELECT login, password, oid FROM users WHERE login = '" + loginInput.get() + "'") # Etisä käyttäjää
    records=c.fetchall()

    if len(records) == 0:
        return False

    if records[0][1] != passwordInput.get():
        return False
    
    global kayttaja

    kayttaja = records[0][2]


    # Committa muutokset
    conn.commit()

    # Sulje tietokantayhteys
    conn.close()

    avaaPaneeli() # Avaa paneelin

task_label = Label(kirjautuminen, text="Login")
task_label.grid (row=0, column=0, pady=(10,0))

loginInput = Entry(kirjautuminen, width=30)
loginInput.grid(row=0, column=1, padx=20, pady=(10,0))

task_label = Label(kirjautuminen, text="Password")
task_label.grid (row=1, column=0, pady=(10,0))

passwordInput = Entry(kirjautuminen, width=30)
passwordInput.grid(row=1, column=1, padx=20, pady=(10,0))

loginButton = Button(kirjautuminen, text="Kirjaudu", command=login)
loginButton.grid (row=2, column=1, columnspan=1, pady=10, padx=10)

registerButton = Button(kirjautuminen, text="Luo tili", command=register)
registerButton.grid (row=2, column=2, columnspan=2, pady=10, padx=10)


kirjautuminen.mainloop()