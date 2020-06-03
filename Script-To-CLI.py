import fire

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
        
if __name__ == "__main__":
    fire.Fire(Calculator)
    
python clac.py add 5 4
9