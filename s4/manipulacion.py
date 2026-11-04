nums = [10, 20, 30, 40, 20, 50]
print(nums)
nums.append(60)
print("Appending 60...")
print(nums)
# eliminar el ultimo
print("Removiendo:", nums.pop())
print("Popping el ultimo...")
print(nums)
# eliminar en base a un valor
nums.remove(20)
print(nums)
nums.insert(4,45)
print(nums)

# eliminar en base a indice
print("Removiendo indice 3:", nums.pop(3))
print(nums)