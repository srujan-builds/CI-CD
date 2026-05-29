def transform_data(data):
    if not data:
        raise ValueError("No data provided")
    # Simple transformation: convert everything to uppercase
    return [d.upper() for d in data]

if __name__ == "__main__":
    raw_data = ["apple", "banana", "cherry"]
    print(f"Processed Data: {transform_data(raw_data)}")