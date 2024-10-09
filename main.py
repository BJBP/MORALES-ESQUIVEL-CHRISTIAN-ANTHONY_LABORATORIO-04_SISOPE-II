import tkinter as tk
import subprocess

def start_simulation():
    try:
        n_clients = int(entry.get())
        if n_clients < 1:
            raise ValueError("El número de clientes debe ser al menos 1")
        
        # Inicia el servidor
        subprocess.Popen(['python', 'chat_server.py'])
        
        # Inicia los clientes
        for i in range(n_clients):
            subprocess.Popen(['python', 'chat_client.py'])
        
        status_label.config(text=f"Simulación iniciada con {n_clients} clientes.", fg="green")
    except ValueError as e:
        status_label.config(text=f"Error: {e}", fg="red")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador de Chat Grupal")
root.geometry("400x300")
root.configure(bg="#1e1e1e")  # Fondo oscuro

# Estilos
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Título de la aplicación
title_label = tk.Label(root, text="Simulación de Chat Grupal", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=20)

# Instrucciones para el usuario
instruction_label = tk.Label(root, text="Ingrese el número de clientes a simular:", font=label_font, bg="#1e1e1e", fg="white")
instruction_label.pack(pady=10)

# Campo de entrada para el número de clientes
entry = tk.Entry(root, font=entry_font, width=10, justify="center")
entry.pack(pady=10)

# Botón para iniciar la simulación
start_button = tk.Button(root, text="Iniciar Simulación", font=button_font, bg="#4caf50", fg="white", activebackground="#45a049", width=20, command=start_simulation)
start_button.pack(pady=20)

# Etiqueta para mostrar mensajes de estado
status_label = tk.Label(root, text="", font=label_font, bg="#1e1e1e", fg="white")
status_label.pack(pady=10)

root.mainloop()
