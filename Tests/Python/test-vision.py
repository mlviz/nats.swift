import asyncio
import nats
import json
import random 
import datetime


async def main():
    # Connect to NATS
    nc = await nats.connect("nats://local:szEvgXonDd9UjjGgVryJhQlDYlI1NVjW@localhost:56894")
    
    # Send a test message
    await nc.publish("viz.test", b"Hello from Python!")
    print("✅ Sent message to visionOS!")
    
    # Send some data
    import json
    print(datetime.datetime.now())
    for i in range(100_000):
        data = {"x": i, "y": random.randint(1, 2000) * 0.1, "z": random.randint(1, 2000) * 0.1}
        await nc.publish("viz.data", json.dumps(data).encode())
        await asyncio.sleep(0.00001)
        #print(f"✅ Sent data: {data}")
    print(datetime.datetime.now())
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
