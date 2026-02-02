#Quiz game
questions = {
    "What is the national bird of India ? ": "Peacock" ,
    "Which Languange is used in AI ?" : "Python" ,
    "Who is the Father of the Nation ? " : "Mahatma Gandhi" ,
    "What is 8 + 2 ?" : "10"
}

score = 0

for q, ans in questions.items():
    user_ans = input(q + " ")
    if user_ans.lower() == ans.lower():
        score += 1
        print("Correct Amswer")
    else:
        print("Wrong Answer")  

print(f"Your Score : {score}/{len(questions)}")  

#Simple E-commerece cart system
class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self,name,price):
        self.items[name] = price 
        print(f"{name} added to cart")
    
    def view_cart(self):
        total = 0
        for item, price in self.items.items():
            print(item, ":" ,price)
            total += price
            print("Total Price :" ,total)

cart = Cart()
cart.add_item("Book", 400)
cart.add_item("Pen", 20)
cart.view_cart()            




