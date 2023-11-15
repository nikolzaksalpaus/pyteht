from tkinter import *
import sqlite3

kirjautuaminen = Tk()
kirjautuaminen.title("Tietokanta")
kirjautuaminen.geometry("450x400")

conn = sqlite3.connect("users.db")

    c = conn.cursor()

    # Poista tietokantataulu nimeltä tasks, jos sellainen on jo olemassa
    c.execute("DROP TABLE IF EXISTS tasks")

    # luo taulu
    sql = '''CREATE TABLE tasks (
        task VARCHAR (255)
    )'''

    c.execute(sql)

    # committa muutokset
    conn.commit()

    # sulje tietokantayhteys
    conn.close()

def paneeli():
    # Kirjautumisen jälkeen avautuvan ikkunan näkymä
    # Paneelin ikkuna, kun käyttäjä kirjautui
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

    global query_btn
    query_btn = Button(paneeli, text="Näytä tehtävät", command=query)
    query_btn.grid (row=3, column=0, columnspan=2, pady=10, padx=10)

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

    paneeli.mainloop()

    global query_label
    query_label = Label(paneeli)

def query():
    print("a1")

    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    c.execute("SELECT task, oid FROM tasks")
    records=c.fetchall()

    print_records = ''

    for record in records:
        print_records += str(record [0]) + "\t" + str(record [1]) + "\n"
    
    heading_label = Label(paneeli, text="Helvetica", font=("Helvetica", 16))

    heading_label['text'] = "Tehtävä \t ID"
    heading_label.grid (row=7, column=0, columnspan=2)

    query_label['text'] = print_records
    query_label.grid (row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

def submit():
    print("a2")

    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    # Insert into table

    c.execute("INSERT INTO tasks VALUES (:task)",
        {
        'task': task.get()
        })
    
    # commit changes
    conn.commit()

    # close connection
    conn.close()
    
    task.delete(0, END)

def delete():

    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()

def update():
    print("a4")
    conn = sqlite3.connect("tasklist.db")

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

def edit():
    print("a5")

    global editor
    editor = Tk()
    editor.title("Päivitä")
    editor.geometry("400x400")

    conn = sqlite3.connect("tasklist.db")

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

def register():     
    # luo tietokanta nimeltä tasklist
    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    # Poista tietokantataulu nimeltä tasks, jos sellainen on jo olemassa
    c.execute("DROP TABLE IF EXISTS tasks")

    # luo taulu
    sql = '''CREATE TABLE tasks (
        task VARCHAR (255)
    )'''

    c.execute(sql)

    # committa muutokset
    conn.commit()

    # sulje tietokantayhteys
    conn.close()

def login():
    print("asd")


loginLogin = Entry(kirjautuaminen, width=30)
loginLogin.grid(row=0, column=1, padx=20, pady=(10,0))

loginPassword = Entry(kirjautuaminen, width=30)
loginPassword.grid(row=1, column=1, padx=20, pady=(10,0))

loginButton = Button(kirjautuaminen, text="Kirjaudu", command=submit)
loginButton.grid (row=2, column=1, columnspan=1, pady=10, padx=10)

registerLogin = Entry(kirjautuaminen, width=30)
registerLogin.grid(row=0, column=2, padx=20, pady=(10,0))

registerPassword = Entry(kirjautuaminen, width=30)
registerPassword.grid(row=1, column=2, padx=20, pady=(10,0))

registerButton = Button(kirjautuaminen, text="Luo tili", command=register)
registerButton.grid (row=2, column=2, columnspan=2, pady=10, padx=10)

    
kirjautuaminen.mainloop()