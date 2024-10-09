import socket
import threading
import tkinter as tk

HOST = '127.0.0.1'
PORT = 65432

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
            decrypted_data = decrypt(data)
            message_list.insert(tk.END, decrypted_data)
            message_list.see(tk.END)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_message():
    message = entry.get()
    if message:
        encrypted_message = encrypt(message)
        client_socket.send(encrypted_message.encode())
        message_list.insert(tk.END, f"Tú: {message}")
        message_list.see(tk.END)
        entry.delete(0, tk.END)

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# GUI setup
root = tk.Tk()
root.title("Cliente de Chat")
root.geometry("400x500")
root.configure(bg="#1e1e1e")

# Estilos
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Ventana de mensajes
message_list = tk.Listbox(root, width=50, height=20, bg="#333333", fg="white", font=entry_font)
message_list.pack(pady=10)

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
