def my_reduce_generator_simple(func, iterable, initial=None):
    def reduce_generator():
        iterator = iter(iterable)
        
        if initial is None: 
            current = next(iterator)
        else:
            current = initial
        
        for item in iterator:
            current = func(current, item)
            yield current

    results = list(reduce_generator())
    return results[-1]

numbers_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers_input.split()))

result = my_reduce_generator_simple(lambda x, y: x + y, numbers)
print(f"Sum: {result}")