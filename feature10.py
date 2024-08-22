import asyncio


# Define an asynchronous coroutine
async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)  # Simulate an I/O-bound task with a delay
    print("Data fetched!")
    return {"data": 42}


# Define another asynchronous coroutine that depends on fetch_data
async def process_data():
    print("Processing data...")
    data = await fetch_data()  # Wait for fetch_data coroutine to complete
    print(f"Processed data: {data['data']}")


# Run the async functions
async def main():
    print("Main coroutine started")
    await process_data()  # Run the process_data coroutine
    print("Main coroutine finished")


# Entry point to run the async code
if __name__ == "__main__":
    asyncio.run(main())
