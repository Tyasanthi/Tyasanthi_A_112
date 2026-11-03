def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(f"Mengirim: {message}")
        sent_messages.append(message)

messages = ["Halo!", "Selamat pagi", "Apa kabar?", "Sampai jumpa"]
sent_messages = []

# Kirim salinan list agar list asli tetap utuh
send_messages(messages[:], sent_messages)

print(f"\nPesan asli (masih utuh): {messages}")
print(f"Pesan terkirim: {sent_messages}")