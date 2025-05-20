# lambda

# def doubled(x):
#     return x * 2
# Instade of this use lambda function like below

doubled = lambda num : num * 2
squared = lambda num : pow(num,2)
# result = doubled(12)
result = squared(12)
# print(result)


numbers = [2, 4, 5, 8, 6, 12]
# doubled_nums = map(doubled, numbers) or 
doubled_nums = map(lambda num : num * 2, numbers)
print(numbers)
print(list(doubled_nums))

actors = [
    {'name': 'saban', 'age': 65},
    {'name': 'sabnoor', 'age': 55},
    {'name': 'sabila', 'age': 30},
    {'name': 'sanom', 'age': 45},
    {'name': 'apu biswas', 'age': 38},
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
print(list(juniors))