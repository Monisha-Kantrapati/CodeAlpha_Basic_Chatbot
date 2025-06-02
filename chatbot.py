import tkinter as tk
from tkinter import scrolledtext
import spacy
import random

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define responses for various intents
responses = {
    "greeting": [
        "👋 Hello! How can I assist you today?",
        "😊 Hi there! What would you like to learn about?",
        "🌟 Hey! Ready to explore programming or blockchain?"
    ],
    "farewell": [
        "👋 Goodbye! Have a great day! 😊",
        "🚀 See you later! Keep coding!",
        "🌈 Take care! Come back soon!"
    ],
    "thanks": [
        "🙏 You're welcome!",
        "😊 Happy to help!",
        "✨ Anytime!"
    ],
    "programming": [
        "💻 Programming is fun! Ask me about Python, Java, C++, or any language.",
        "🤖 Want some coding tips or syntax help?",
        "📝 Need an example of a Python function or loop?"
    ],
    "python_syntax": [
        "🐍 Here's some Python syntax:\n"
        "Variables:\n    x = 10\n    name = \"Alice\"\n\n"
        "Conditional:\n    if x > 5:\n        print(\"x is greater\")\n\n"
        "Loops:\n    for i in range(5):\n        print(i)\n\n"
        "Functions:\n    def greet(person):\n        return \"Hello, \" + person",
    ],
    "blockchain": [
        "⛓️ Blockchain is a decentralized ledger that records transactions securely and transparently. It's the tech behind cryptocurrencies like Bitcoin.",
        "💡 Future of blockchain includes DeFi, NFTs, smart contracts, and more!"
    ],
    "blockchain_code": [
        "🧑‍💻 Here's a simple Python example of a blockchain:\n"
        "import hashlib, time\n\n"
        "class Block:\n"
        "    def __init__(self, index, previous_hash, data):\n"
        "        self.index = index\n"
        "        self.previous_hash = previous_hash\n"
        "        self.timestamp = time.time()\n"
        "        self.data = data\n"
        "        self.nonce = 0\n"
        "        self.hash = self.calculate_hash()\n\n"
        "    def calculate_hash(self):\n"
        "        block_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)\n"
        "        return hashlib.sha256(block_string.encode()).hexdigest()\n\n"
        "    def mine_block(self, difficulty):\n"
        "        while self.hash[:difficulty] != '0' * difficulty:\n"
        "            self.nonce += 1\n"
        "            self.hash = self.calculate_hash()\n"
        "\n"
        "class Blockchain:\n"
        "    def __init__(self):\n"
        "        self.chain = [self.create_genesis_block()]\n"
        "        self.difficulty = 4\n"
        "    def create_genesis_block(self):\n"
        "        return Block(0, '0', 'Genesis Block')\n"
        "    def add_block(self, new_block):\n"
        "        new_block.previous_hash = self.chain[-1].hash\n"
        "        new_block.mine_block(self.difficulty)\n"
        "        self.chain.append(new_block)\n"
        "\n"
        "my_chain = Blockchain()\n"
        "my_chain.add_block(Block(1, '', 'First transaction'))\n"
        "for block in my_chain.chain:\n"
        "    print(f\"Block {block.index} Hash: {block.hash}\")"
    ],
    "future_scope": [
        "🚀 The future of programming includes AI, Machine Learning, and Quantum Computing.",
        "🌍 Blockchain technology will expand into healthcare, supply chain, and more!"
    ],
    "general": [
        "🤔 I'm here to help! Ask me about programming, blockchain, or general questions.",
        "💬 Feel free to ask anything related to tech, coding, or future trends!"
    ],
    "unknown": [
        "😕 Sorry, I didn't understand that. Could you please rephrase?",
        "🤖 I'm still learning. Ask me about programming or blockchain!",
        "🧐 Could you specify if you want info on programming, blockchain, or just general chat?"
    ],
    "general_inquiry": [
        "🤖 Feel free to ask me anything about programming, blockchain, or tech!",
        "📝 I'm here to help! What would you like to know?",
        "💡 Ask me a question, and I'll do my best to assist!"
    ]
}

# Function to detect user intent
def detect_intent(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return "farewell"
    elif any(word in tokens for word in ["thank", "thanks"]):
        return "thanks"
    elif any(word in tokens for word in ["program", "code", "coding", "developer", "programming"]):
        return "programming"
    elif "python" in tokens or "syntax" in tokens:
        return "python_syntax"
    elif "blockchain" in tokens or "block chain" in tokens:
        return "blockchain"
    elif "code" in tokens or "example" in tokens:
        return "blockchain_code"
    elif "future" in tokens or "scope" in tokens:
        return "future_scope"
    elif "ask" in tokens or "anything" in tokens or "what" in tokens:
        # For general questions or "ask anything"
        return "general_inquiry"
    else:
        return "unknown"

# Function to select a response based on intent
def get_response(user_input):
    intent = detect_intent(user_input)
    res_list = responses.get(intent, responses["unknown"])
    return random.choice(res_list)

# GUI Application
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖✨ Basic Chatbot")
        self.root.geometry("850x600")
        self.root.configure(bg="#2c3e50")

        # Title label
        title = tk.Label(root, text="🤖✨ Basic Chatbot", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
        title.pack(pady=10)

        # Chat display
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 14), bg="#ecf0f1", fg="#2c3e50", state="disabled", width=90, height=20)
        self.chat_area.pack(padx=15, pady=10)

        # Entry box & Send button
        frame = tk.Frame(root, bg="#2c3e50")
        frame.pack(pady=10)

        self.entry = tk.Entry(frame, width=60, font=("Arial", 14), bg="#bdc3c7", fg="#2c3e50", relief=tk.FLAT)
        self.entry.pack(side=tk.LEFT, padx=(0,10))
        self.entry.bind("<Return>", self.send_message)

        send_btn = tk.Button(frame, text="🚀 Send", command=self.send_message, font=("Arial", 14, "bold"), bg="#2980b9", fg="white", relief=tk.FLAT)
        send_btn.pack(side=tk.LEFT)

        self.configure_tags()

    def configure_tags(self):
        self.chat_area.tag_configure("user", foreground="#e67e22", font=("Arial", 14, "bold"))
        self.chat_area.tag_configure("bot", foreground="#16a085", font=("Arial", 14))

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if user_input:
            # Display user message
            self.chat_area.config(state="normal")
            self.chat_area.insert(tk.END, "🧑‍💻 You: " + user_input + "\n", "user")
            self.chat_area.config(state="disabled")
            self.chat_area.see(tk.END)
            self.entry.delete(0, tk.END)

            # Get response
            response = get_response(user_input)
            self.chat_area.config(state="normal")
            self.chat_area.insert(tk.END, "🤖 Bot: " + response + "\n", "bot")
            self.chat_area.config(state="disabled")
            self.chat_area.see(tk.END)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()