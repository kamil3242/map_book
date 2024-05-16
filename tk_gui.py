from tkinter import *

import tkintermapview

users:list=[]

class User:
    def __init__(self,name,surname,posts,location):
        self.name=name
        self.surname=surname
        self.posts=posts
        self.location=location


def add_new_user():
    user=User(name=entry_name.get(), surname=entry_surname.get(), posts=entry_posts.get(), location=entry_location.get())
    users.append(user)
    display_users()
    entry_name.delete(0,END)
    entry_surname.delete(0,END)
    entry_posts.delete(0, END)
    entry_location.delete(0,END)
    entry_name.focus()

def display_users():
    listbox_lista_użytkowników.delete(0,END)
    for idx, user in enumerate(users):
       listbox_lista_użytkowników.insert(idx, f'{idx+1}. {user.name} {user.surname}')

def delete_user():
    print(listbox_lista_użytkowników.index(ACTIVE))
    users.pop(listbox_lista_użytkowników.index(ACTIVE))
    display_users()

def show_user_details():
    i=listbox_lista_użytkowników.index(ACTIVE)
    label_opis_name_użytkownika_wartość.config(text=users[i].name)
    label_opis_surname_użytkownika_wartość.config(text=users[i].surname)
    label_opis_posts_użytkownika_wartość.config(text=users[i].posts)
    label_opis_location_użytkownika_wartość.config(text=users[i].location)

def edit_user():
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_posts.delete(0, END)
    entry_location.delete(0, END)
    i=listbox_lista_użytkowników.index(ACTIVE)
    entry_name.insert(END, users[i].name)
    entry_surname.insert(END, users[i].surname)
    entry_posts.insert(END, users[i].posts)
    entry_location.insert(END, users[i].location)
    entry_name.focus()

    button_dodaj_użytkownika.config(text='zapisz zmiany', command=lambda: update_user(i))

def update_user(i):
    users[i].name = entry_name.get()
    users[i].surname = entry_surname.get()
    users[i].posts = entry_posts.get()
    users[i].location = entry_location.get()
    display_users()
    button_dodaj_użytkownika.config(text='dodaj użytkownika', command=add_new_user)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_posts.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()



root=Tk()
root.geometry('800x700')
root.title("MapBook")

# ramki do porządkowania struktóry
ramka_lista_użytkowników=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegóły_użytkownika=Frame(root)


ramka_lista_użytkowników.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegóły_użytkownika.grid(row=1, column=0, columnspan=2, padx=50, pady=20)

# ramka lista użytkowników
label_lista_użytkowników=Label(ramka_lista_użytkowników, text='lista użytkowników: ')
listbox_lista_użytkowników=Listbox(ramka_lista_użytkowników, width=30)
buttton_pokaż_szczegóły=Button(ramka_lista_użytkowników, text='pokaż szczegóły', command=show_user_details)
button_usuń_użytkownika=Button(ramka_lista_użytkowników, text='usuń', command=delete_user)
button_edytuj_użytkownika=Button(ramka_lista_użytkowników, text='edytuj', command=edit_user)

label_lista_użytkowników.grid(row=0, column=0)
listbox_lista_użytkowników.grid(row=1, column=0, columnspan=3)
buttton_pokaż_szczegóły.grid(row=2, column=0)
button_usuń_użytkownika.grid(row=2, column=1)
button_edytuj_użytkownika.grid(row=2, column=2)

# ramka fotmularz
label_napis_formularz=Label(ramka_formularz, text='formularz edycji i dodawania')
label_name=Label(ramka_formularz, text='imię')
labal_surname=Label(ramka_formularz, text='surname')
label_posts=Label(ramka_formularz, text='liczba postów')
label_location=Label(ramka_formularz, text='miejscowość')

entry_name=Entry(ramka_formularz)
entry_surname=Entry(ramka_formularz, width=30)
entry_posts=Entry(ramka_formularz)
entry_location=Entry(ramka_formularz)

button_dodaj_użytkownika=Button(ramka_formularz, text='dodaj użytkownika', command=add_new_user)

label_napis_formularz.grid(row=0, column=0, columnspan=2)
label_name.grid(row=1, column=0, sticky=W)
labal_surname.grid(row=2, column=0, sticky=W)
label_posts.grid(row=3, column=0, sticky=W)
label_location.grid(row=4, column=0, sticky=W)

entry_name.grid(row=1, column=1, sticky=W)
entry_surname.grid(row=2, column=1, sticky=W)
entry_posts.grid(row=3, column=1, sticky=W)
entry_location.grid(row=4, column=1, sticky=W)

button_dodaj_użytkownika.grid(row=5, column=0, columnspan=2)


# ramka pokaż szczegóły
label_opis_użytkownika=Label(ramka_szczegóły_użytkownika, text='szczegóły użytkownika')
label_opis_name_użytkownika=Label(ramka_szczegóły_użytkownika, text='imię')
label_opis_name_użytkownika_wartość=Label(ramka_szczegóły_użytkownika, text='...', width=10)
label_opis_surname_użytkownika=Label(ramka_szczegóły_użytkownika, text='nazwisko')
label_opis_surname_użytkownika_wartość=Label(ramka_szczegóły_użytkownika, text='...', width=10)
label_opis_posts_użytkownika=Label(ramka_szczegóły_użytkownika, text='liczba postów')
label_opis_posts_użytkownika_wartość=Label(ramka_szczegóły_użytkownika, text='...', width=10)
label_opis_location_użytkownika=Label(ramka_szczegóły_użytkownika, text='miejscowość')
label_opis_location_użytkownika_wartość=Label(ramka_szczegóły_użytkownika, text='...', width=10)

label_opis_użytkownika.grid(row=0, column=0)
label_opis_name_użytkownika.grid(row=1, column=1)
label_opis_name_użytkownika_wartość.grid(row=1, column=2)
label_opis_surname_użytkownika.grid(row=1, column=3)
label_opis_surname_użytkownika_wartość.grid(row=1, column=4)
label_opis_posts_użytkownika.grid(row=1, column=5)
label_opis_posts_użytkownika_wartość.grid(row=1, column=6)
label_opis_location_użytkownika.grid(row=1, column=7)
label_opis_location_użytkownika_wartość.grid(row=1, column=8)


map_widget=tkintermapview.TkinterMapView(ramka_szczegóły_użytkownika, width=700, height=300)
map_widget.grid(row=2, column=0, columnspan=8)
map_widget.set_position(52.21, 21.00)
map_widget.set_zoom(10)

root.mainloop()