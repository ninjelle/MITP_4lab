import time
from functools import wraps

def timer(func):
    @wraps(func) 
    def wrapper(*args):
        start_time = time.time() 
        result = func(*args) 
        end_time = time.time()  
        
        elapsed_time = end_time - start_time 
        print(f"The function {func.__name__} was completed in {elapsed_time:.4f} seconds")
        
        return result  
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

result = slow_function()
print(f"Result: {result}")
