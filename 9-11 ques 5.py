from functools import reduce
car_models=['Honda Civic','Honda Accord','Toyota Corolla','Toyota Camry','Ford Fusion','Ford Fusion','Ford Escape','Nissan Sentra','Hyundai Elantra']
str=' '

a = [reduce(lambda w, t:t, o.split()) for o in car_models]
print(','.join(a))
