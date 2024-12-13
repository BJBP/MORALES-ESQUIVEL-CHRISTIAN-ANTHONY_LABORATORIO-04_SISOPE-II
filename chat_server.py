import socket
import threading
import tkinter as tk
import time
import sqlite3
import sys

client_count = 0

HOST = '127.0.0.1'
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 65432 # Get port from argument

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

# Database setup
conn = sqlite3.connect('chat_history.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        message TEXT,
        timestamp TEXT
    )
''')
conn.commit()

def handle_client(client_socket, client_address, client_name):
    global client_count
    client_id = client_count
    client_count += 1
    print(f"Accepted connection from {client_address} (ID: {client_id}, Name: {client_name})")
    
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            decrypted_data = decrypt(data)
            timestamp = time.strftime("%H:%M:%S", time.localtime())
            broadcast_message = f" {decrypted_data}  {timestamp.rjust(50)}"
            print(f"Received from {client_name}: {decrypted_data}")
            
            # Store message in database
            cursor.execute("INSERT INTO messages (sender, message, timestamp) VALUES (?, ?, ?)", (client_name, decrypted_data, timestamp))
            conn.commit()

            # Broadcast to other clients
            for c in clients:
                if c != client_socket:
                    c.send(encrypt(broadcast_message).encode())
        except Exception as e:
            print(f"Error handling client {client_address} (ID: {client_id}): {e}")
            break
    client_socket.close()
    clients.remove(client_socket)
    print(f"Client {client_address} (ID: {client_id}, Name: {client_name}) disconnected")

def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        client_name = client_socket.recv(1024).decode()  # Receive the client name during connection
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_name))
        client_thread.start()

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
clients = []

# GUI setup
root = tk.Tk()
root.title("Servidor de Chat")
root.geometry("400x500")
root.configure(bg="#1e1e1e")

# Estilos
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Ventana de mensajes
message_list = tk.Listbox(root, width=50, height=20, bg="#333333", fg="white", font=entry_font)
message_list.pack(pady=10)

# Hilo para aceptar conexiones
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

root.mainloop()
