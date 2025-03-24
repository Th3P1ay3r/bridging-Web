motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print("after append element")
print(motorcycles)

motorcycles.insert(0,'hyundai')
print ("after insert element at index 0")
print(motorcycles)

del motorcycles[0]
print ("after deleting element at index 0")
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(f"remaining motorcycle after pop call {motorcycles}")
print(f"popped motorcycle{popped_motorcycles}")
print(motorcycles)
print(f"popped element {motorcycles.pop(0)}")
print(f" remaining element {motorcycles}")