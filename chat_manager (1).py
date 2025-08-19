
from collections import deque
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Message:
    content: str
    timestamp: str

class ChatManager:
    def __init__(self):
        self.incoming_queue = deque()
        self.sent_stack = []
        self.redo_stack = []

    def receive_message(self, message_text):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        message = Message(message_text, timestamp)
        self.incoming_queue.append(message)
        print(f"[RECEIVED] {message.content} @ {message.timestamp}")

    def send_message(self):
        if not self.incoming_queue:
            print("No incoming messages to send.")
            return
        message = self.incoming_queue.popleft()
        self.sent_stack.append(message)
        print(f"[SENT] {message.content} @ {message.timestamp}")

    def undo_message(self):
        if not self.sent_stack:
            print("No message to undo.")
            return
        message = self.sent_stack.pop()
        self.redo_stack.append(message)
        print(f"[UNDO] {message.content} undone.")

    def redo_message(self):
        if not self.redo_stack:
            print("No message to redo.")
            return
        message = self.redo_stack.pop()
        self.sent_stack.append(message)
        print(f"[REDO] {message.content} re-sent.")

    def show_history(self):
        print("\n--- Sent Message History ---")
        if not self.sent_stack:
            print("No sent messages.")
        for msg in self.sent_stack:
            print(f"{msg.content} @ {msg.timestamp}")
        print("-----------------------------\n")


def demo():
    cm = ChatManager()

    # Simulate some incoming messages
    cm.receive_message("Hello!")
    cm.receive_message("How are you?")
    cm.receive_message("Let's meet at 5.")

    # Process (send) messages
    cm.send_message()
    cm.send_message()

    # Undo last message
    cm.undo_message()

    # Redo it again
    cm.redo_message()

    # Send the remaining message
    cm.send_message()

    # Display history
    cm.show_history()

if __name__ == "__main__":
    demo()
