def minimize_expression(expression):
    parts = expression.split('-')
    
    initial_sum = sum(map(int, parts[0].split('+')))
    
    subsequent_sum = sum(sum(map(int, part.split('+'))) for part in parts[1:])
    
    result = initial_sum - subsequent_sum
    
    return result

expression = input().strip()

print(minimize_expression(expression))