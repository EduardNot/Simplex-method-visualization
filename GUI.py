import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry('400x800')
root.title('Simplex method visualizer')

def calculate():
    print('TEST')


def max_min_toggle():
    if max_min_button.cget('text') == 'Maximize':
        max_min_button.configure(text='Minimize')
        main_func.configure(placeholder_text='Minimize')
    else:
        max_min_button.configure(text='Maximize')
        main_func.configure(placeholder_text='Maximize')


def add_constraint():
    size = len(all_constraints)
    ent = customtkinter.CTkEntry(master=frame, placeholder_text='Constraint')
    ent.grid(pady=12, padx=10, column=0, row=3+size)
    # ent.pack(pady=12, padx=10)

    # add_field_button.grid(pady=12, padx=10, column=0, row=3+size)
    # calc_button.grid(pady=12, padx=10, column=1, row=3+size)

    all_constraints.append(ent)


frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=10, fill='both', expand=True)

max_min_button = customtkinter.CTkButton(master=frame, text='Maximize', command=max_min_toggle)
max_min_button.grid(pady=12, padx=10, column=0, row=0)
# max_min_button.pack(pady=12, padx=10)

main_func = customtkinter.CTkEntry(master=frame, placeholder_text='Maximize')
main_func.grid(pady=12, padx=10, column=1, row=0)
# main_func.pack(pady=12, padx=10)

subject_to_label = customtkinter.CTkLabel(master=frame, text='Subject to', font=('Roboto', 14))
subject_to_label.grid(pady=12, padx=10, column=0, row=1)
# subject_to_label.pack(pady=12, padx=10)

all_constraints = []

add_field_button = customtkinter.CTkButton(master=frame, text='Add Constraint', command=add_constraint)
add_field_button.grid(pady=12, padx=10, column=0, row=2)
# add_field_button.pack(pady=12, padx=10)

calc_button = customtkinter.CTkButton(master=frame, text='Calculate', command=calculate)
calc_button.grid(pady=12, padx=10, column=1, row=2)
# calc_button.pack(pady=12, padx=10)

root.mainloop()
