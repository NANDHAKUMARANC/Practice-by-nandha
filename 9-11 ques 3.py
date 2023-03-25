a={'Honda': ['Honda Civic', 'Honda Accord'], 'Toyota': ['Toyota Corolla', 'Toyota Camry'], 'Ford': ['Ford Fusion', 'Ford Escape'], 'Nissan': ['Nissan Sentra'], 'Hyundai': ['Hyundai Elantra']}
b=list(map(lambda values: a[values],a.keys()))
print(b)

