# Simple text-based "visualization" (works anywhere)

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

print("X:", x)
print("Y:", y)

print("\nSimple Bar Visualization:\n")

for i in range(len(x)):
    print(f"{x[i]} | {'█' * (y[i] // 2)} ({y[i]})")