from mock_customers import MOCKCUSTOMERS
from mock_vendors import MOCKVENDORS

data = MOCKCUSTOMERS + MOCKVENDORS

def main():
    for cust in data:
        print(f"Name: {cust.name}; Address: {cust.address}")


if __name__ == "__main__":
    main()