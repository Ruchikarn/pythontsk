function_call_counter = 0


def sample_function():
    global function_call_counter
    function_call_counter = function_call_counter + 1
    print('Sample function is called')


sample_function()
sample_function()
sample_function()
sample_function()

print('No of sample function calls is ', function_call_counter)
