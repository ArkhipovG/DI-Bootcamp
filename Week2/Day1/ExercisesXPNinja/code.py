class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        who_called_who = f"{self.phone_number} called to {other_phone.phone_number}"
        self.call_history.append(who_called_who)
        other_phone.call_history.append(who_called_who)

    def show_call_history(self):
        print(f"Call history of  {self.phone_number}")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, text):
        new_message = {'to': other_phone.phone_number, 'from': self.phone_number, 'content': text}
        self.messages.append(new_message)
        other_phone.messages.append(new_message)

    def show_outgoing_messages(self):
        print(f"My outgoing messages:")
        for message in self.messages:
            if message['from'] == self.phone_number:
                print(f"Message to {message['to']}: {message['content']}")

    def show_incoming_messages(self):
        print(f"My incoming messages:")
        for message in self.messages:
            if message['from'] != self.phone_number:
                print(f"Message from {message['from']}: {message['content']}")

    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number}:")
        for message in self.messages:
            if message['from'] == other_phone.phone_number:
                print(message['content'])


f_phone = Phone("058-777-77-77")
s_phone = Phone("058-666-66-66")
t_phone = Phone("058-555-55-55")
f_phone.call(s_phone)
t_phone.call(s_phone)
s_phone.call(t_phone)
f_phone.show_call_history()
print("------")
s_phone.show_call_history()
print("------")
t_phone.show_call_history()
print("------")
f_phone.send_message(s_phone, "First test message")
t_phone.send_message(s_phone, "Second test message")
s_phone.send_message(t_phone, "Third test message")
t_phone.send_message(s_phone, "Fourth test message")
s_phone.show_outgoing_messages()
print("------")
s_phone.show_incoming_messages()
print("------")
s_phone.show_messages_from(t_phone)
