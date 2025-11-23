
import sys

def main():
    if len(sys.argv) < 3:
        print("Error: Please provide two numbers.")
        print("Example: python add_sub.py 10 20")
        return

    # Convert command-line arguments to numbers
    a = float(sys.argv[1])
    b = float(sys.argv[2])

    addition = a + b
    subtraction = a - b

    print("Addition:", addition)
    print("Subtraction:", subtraction)

if __name__ == "__main__":
    main()