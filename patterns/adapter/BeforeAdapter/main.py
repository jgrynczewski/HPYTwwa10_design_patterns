from mock_customers import MOCKCUSTOMERS
from mock_vendors import MOCKVENDORS
TYPE = 'vendors'


def main():
    if TYPE == "customers":
        for cust in MOCKCUSTOMERS:
            print(f"Name: {cust.name}; Address: {cust.address}")
    elif TYPE == "vendors":
        for vendor in MOCKVENDORS:
            print(f"Name: {vendor.name}; Address: {vendor.street} {vendor.number}")
    else:
        raise ValueError(f"Incorrect type: {TYPE}")


if __name__ == "__main__":
    main()