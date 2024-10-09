import socket
import threading
import tkinter as tk
import sys
import time

HOST = '127.0.0.1'
PORT = 65432
client_name = sys.argv[1] if len(sys.argv) > 1 else "Cliente Desconocido"
group_name = sys.argv[2] if len(sys.argv) > 2 else "Grupo Desconocido"

# Simple encryption (for demonstration purposes only - NOT SECURE for real-world use)
def encrypt(message):
    encrypted = ""
    for char in message:
        encrypted += chr(ord(char) + 1)
    return encrypted

def decrypt(message):
    decrypted = ""
    for char in message:
        decrypted += chr(ord(char) - 1)
    return decrypted

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            display_message(decrypt(data))
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def display_message(message, sender=False):
    message_text, timestamp = message.rsplit(' ', 1)  # Separa el mensaje del timestamp
    message_parts = message_text.split(':', 1)  # Separar nombre del mensaje
    sender_name = message_parts[0]
    actual_message = message_parts[1].strip()

    # Cuadro para el mensaje
    message_frame = tk.Frame(message_list_frame, bg="#333333")
    message_frame.pack(fill='x', pady=5, padx=10, anchor='w' if not sender else 'e')

    # Mostrar nombre alineado a la izquierda (o "Yo" si es el mensaje del propio cliente)
    name_label = tk.Label(message_frame, text=sender_name if not sender else "Yo", bg="#333333", fg="#4caf50", font=("Helvetica", 10, "bold"), anchor="w")
    name_label.pack(fill="x", side="top", padx=5)

    # Mostrar mensaje alineado a la izquierda
    message_label = tk.Label(message_frame, text=actual_message, wraplength=300, bg="#333333", fg="white", font=entry_font, justify="left", anchor="w")
    message_label.pack(fill="x", side="top", padx=5)

    # Mostrar la hora siempre alineada a la derecha
    time_label = tk.Label(message_frame, text=timestamp, bg="#333333", fg="white", font=("Helvetica", 10))
    time_label.pack(side='right', padx=5)

def send_message():
    message = entry.get()
    if message:
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        formatted_message_for_self = f"{client_name}: {message} {timestamp}"  # Formato para el propio cliente
        encrypted_message_for_server = encrypt(f"{client_name}: {message}")  # Solo envía el mensaje
        client_socket.send(encrypted_message_for_server.encode())
        display_message(formatted_message_for_self, sender=True)  # Marca que es el mensaje del propio cliente
        entry.delete(0, tk.END)

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(client_name.encode())  # Send the client name to the server

# GUI setup
root = tk.Tk()
root.title(f"Chat - {client_name} en {group_name}")
root.geometry("400x500")
root.configure(bg="#1e1e1e")

# Estilos
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Frame para mostrar los mensajes
message_list_frame = tk.Frame(root, bg="#1e1e1e")
message_list_frame.pack(fill='both', expand=True, pady=10)

# Campo de entrada para mensajes
entry = tk.Entry(root, font=entry_font, width=30, bg="#2e2e2e", fg="white")
entry.pack(pady=10)

# Botón de enviar
send_button = tk.Button(root, text="Enviar", font=button_font, bg="#4caf50", fg="white", activebackground="#45a049", width=15, command=send_message)
send_button.pack(pady=10)

# Hilo para recibir mensajes
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()
