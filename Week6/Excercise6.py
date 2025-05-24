# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]
print([person for person in data if person['age']>25])