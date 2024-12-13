import tkinter as tk
import subprocess
import os
import signal
import random

# Lista para almacenar los procesos de la simulación
processes = []
server_ports = []

def start_simulation(n_clients, group_name):
    if not group_name:
        status_label.config(text="Error: Debe ingresar un nombre para el grupo.", fg="red")
        return

    client_names = entry_names.get().split(',') if entry_names.get() else []

    if len(client_names) != 0 and len(client_names) != n_clients:
        status_label.config(text=f"Error: Debe ingresar {n_clients} nombres separados por comas o dejar el campo vacío para nombres automáticos.", fg="red")
        return

    # Inicia múltiples servidores
    n_servers = 3  # Número de servidores a simular
    for i in range(n_servers):
        port = 65432 + i
        server_ports.append(port)
        server_process = subprocess.Popen(['python', 'chat_server.py', str(port)])
        processes.append(server_process)  # Almacena el proceso del servidor

    # Inicia los clientes con nombres
    for i in range(n_clients):
        client_name = client_names[i] if client_names else f"Cliente {i + 1}"
        client_process = subprocess.Popen(['python', 'chat_client.py', client_name, group_name, ','.join(map(str, server_ports))])
        processes.append(client_process)  # Almacena los procesos de los clientes

    status_label.config(text=f"Simulación del grupo '{group_name}' iniciada con {n_clients} clientes y {n_servers} servidores.", fg="green")

def stop_simulation():
    # Termina todos los procesos almacenados
    for process in processes:
        process.terminate()
    status_label.config(text="Simulación finalizada. Todas las ventanas han sido cerradas.", fg="red")

def request_client_names():
    try:
        n_clients = int(entry_clients.get())
        if n_clients < 1:
            raise ValueError("El número de clientes debe ser al menos 1")

        # Limpiar y mostrar el campo para nombres y el botón de simulación
        for widget in root.winfo_children():
            widget.destroy()

        instruction_group = tk.Label(root, text="Ingrese el nombre del grupo:", font=label_font, bg="#1e1e1e", fg="white")
        instruction_group.pack(pady=10)

        global entry_group_name
        entry_group_name = tk.Entry(root, font=entry_font, width=30, justify="center")
        entry_group_name.pack(pady=10)

        instruction_names = tk.Label(root, text=f"Ingrese los nombres de los {n_clients} clientes (opcional):", font=label_font, bg="#1e1e1e", fg="white")
        instruction_names.pack(pady=10)

        global entry_names
        entry_names = tk.Entry(root, font=entry_font, width=30, justify="center")
        entry_names.pack(pady=10)

        start_button = tk.Button(root, text="Iniciar Simulación", font=button_font, bg="#4caf50", fg="white", activebackground="#45a049", width=20,
                                 command=lambda: start_simulation(n_clients, entry_group_name.get()))
        start_button.pack(pady=20)

        stop_button = tk.Button(root, text="Finalizar Simulación", font=button_font, bg="#f44336", fg="white", activebackground="#e53935", width=20, command=stop_simulation)
        stop_button.pack(pady=20)

        global status_label
        status_label = tk.Label(root, text="", font=label_font, bg="#1e1e1e", fg="white", wraplength=350)
        status_label.pack(pady=10)

    except ValueError as e:
        status_label.config(text=f"Error: {e}", fg="red")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador de Chat Grupal")
root.geometry("400x400")
root.configure(bg="#1e1e1e")  # Fondo oscuro

# Estilos
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Título de la aplicación
title_label = tk.Label(root, text="Simulación de Chat Grupal", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=20)

# Instrucciones para el número de clientes
instruction_label = tk.Label(root, text="Ingrese el número de clientes a simular:", font=label_font, bg="#1e1e1e", fg="white")
instruction_label.pack(pady=10)

# Campo de entrada para el número de clientes
entry_clients = tk.Entry(root, font=entry_font, width=10, justify="center")
entry_clients.pack(pady=10)

# Botón para continuar a la solicitud de nombres
next_button = tk.Button(root, text="Siguiente", font=button_font, bg="#4caf50", fg="white", activebackground="#45a049", width=20, command=request_client_names)
next_button.pack(pady=20)

# Etiqueta para mostrar mensajes de estado
status_label = tk.Label(root, text="", font=label_font, bg="#1e1e1e", fg="white", wraplength=350)
status_label.pack(pady=10)

root.mainloop()
