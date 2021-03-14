from mock_customers import MOCKCUSTOMERS


def main():
    for cust in MOCKCUSTOMERS:
        print(f"Name: {cust.name}; Address: {cust.address}")


if __name__ == "__main__":
    main()