def calculator_result(num1, num2, operation):
	num_1 = int(num1)
	num_2 = int(num2)
	operation = operation.lower()
	if operation == 'add':
		return num_1 + num_2
	elif operation == 'subtract':
		return num_1 - num_2
	elif operation == 'multiply':
		return num_1 * num_2
	elif operation == 'divide':
		return num_1 / num_2
