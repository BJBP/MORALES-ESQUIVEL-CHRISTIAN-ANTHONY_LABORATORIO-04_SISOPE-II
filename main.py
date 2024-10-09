import tkinter as tk
import subprocess

def request_client_names(n_clients):
    def start_simulation():
        client_names = entry_names.get().split(',') if entry_names.get() else []

        if len(client_names) != 0 and len(client_names) != n_clients:
            status_label.config(text=f"Error: Debe ingresar {n_clients} nombres separados por comas o dejar el campo vacío para nombres automáticos.", fg="red")
            return

        # Inicia el servidor
        subprocess.Popen(['python', 'chat_server.py'])
        
        # Inicia los clientes con nombres
        for i in range(n_clients):
            client_name = client_names[i] if client_names else f"Cliente {i + 1}"
            subprocess.Popen(['python', 'chat_client.py', client_name])
        
        status_label.config(text=f"Simulación iniciada con {n_clients} clientes.", fg="green")

    # Eliminar los widgets anteriores y solicitar los nombres
    for widget in root.winfo_children():
        widget.destroy()

    instruction_names = tk.Label(root, text=f"Ingrese los nombres de los {n_clients} clientes (opcional):", font=label_font, bg="#1e1e1e", fg="white")
    instruction_names.pack(pady=10)

    entry_names = tk.Entry(root, font=entry_font, width=30, justify="center")
    entry_names.pack(pady=10)

    start_button = tk.Button(root, text="Iniciar Simulación", font=button_font, bg="#4caf50", fg="white", activebackground="#45a049", width=20, command=start_simulation)
    start_button.pack(pady=20)

    global status_label
    status_label = tk.Label(root, text="", font=label_font, bg="#1e1e1e", fg="white")
    status_label.pack(pady=10)

def get_client_count():
    try:
        n_clients = int(entry_clients.get())
        if n_clients < 1:
            raise ValueError("El número de clientes debe ser al menos 1")
        request_client_names(n_clients)
    except ValueError as e:
        status_label.config(text=f"Error: {e}", fg="red")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador de Chat Grupal")
root.geometry("400x350")
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
entry_clients = tk.Entry(root, font=entry_font, width=10, justify="center")
entry_clients.pack(pady=10)

# Botón para continuar a la solicitud de nombres
start_button = tk.Button(root, text="Siguiente", font=button_font, bg="#4caf50", fg="white", activebackground="#45a049", width=20, command=get_client_count)
start_button.pack(pady=20)

# Etiqueta para mostrar mensajes de estado
status_label = tk.Label(root, text="", font=label_font, bg="#1e1e1e", fg="white")
status_label.pack(pady=10)

root.mainloop()
