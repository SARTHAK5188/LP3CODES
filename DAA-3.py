class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def main():
    items = []
    while True:
        print("\n=== Fractional Knapsack Menu ===")
        print("1. Enter items")
        print("2. Solve fractional knapsack")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            items.clear()
            n = int(input("Enter number of items: "))

            if n <= 0:
                print("Enter a positive number of items!")
                continue

            for i in range(n):
                value = int(input(f"Item {i + 1} value: "))
                weight = int(input(f"Item {i + 1} weight: "))

                if value < 0 or weight <= 0:
                    print("Value must be non-negative and weight must be positive!")
                    items.clear()
                    break

                items.append(Item(value, weight))

        elif choice == 2:
            if not items:
                print("Please enter items first!")
                continue

            capacity = int(input("Enter knapsack capacity: "))

            if capacity < 0:
                print("Capacity cannot be negative!")
                continue

            items.sort(key=lambda item: item.ratio, reverse=True)

            total_value = 0.0
            remaining = capacity

            print("\nItems taken (value/weight fraction):")

            for item in items:
                if remaining == 0:
                    break

                if item.weight <= remaining:
                    print(f"{item.value}/{item.weight} -> Full")
                    total_value += item.value
                    remaining -= item.weight
                else:
                    fraction = remaining / item.weight
                    print(f"{item.value}/{item.weight} -> {fraction * 100:.2f}%")
                    total_value += item.value * fraction
                    remaining = 0

            print(f"Maximum total value in knapsack: {total_value:.2f}")

        elif choice == 3:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()