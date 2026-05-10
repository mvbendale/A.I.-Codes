# Knowledge Base: Separating logic from data
rules = {
    ("hello", "hi", "hey"): "Bot: Hello! How can I assist you today?",
    ("order", "track", "status"): "Bot: Please provide your order ID to check the status.",
    ("return", "exchange"): "Bot: Our return policy allows returns within 7 days of delivery.",
    ("refund", "money back"): "Bot: Refunds are processed within 5-7 working days.",
    ("payment", "card", "upi", "pay"): "Bot: We accept credit cards, debit cards, UPI, and net banking.",
    ("delivery", "shipping", "arrive"): "Bot: Delivery usually takes 3-5 business days.",
    ("cancel",): "Bot: You can cancel your order before it is shipped."
}

def get_response(user_input):
    # Iterate through our Knowledge Base instead of using if-else chains
    for keywords, response in rules.items():
        for word in keywords:
            if word in user_input:
                return response
    
    # Fallback response
    return "Bot: Sorry, I didn't understand that. Can you please rephrase?"

def chatbot():
    print("🤖 Welcome to Customer Support Chatbot!")
    print("Type 'exit' to end the chat.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit" or user_input == "quit":
            print("Bot: Thank you for visiting! Have a nice day 😊")
            break
            
        # Get response dynamically from the rules engine
        response = get_response(user_input)
        print(response)

if __name__ == "__main__":
    chatbot()
