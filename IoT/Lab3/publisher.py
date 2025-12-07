import asyncio
import nats

async def main():
    # Connect to NATS server
    nc = await nats.connect("nats://localhost:4222")
    
    # Publish messages
    messages = [
        "Temperature: 25.5C",
        "Humidity: 60%",
        "Pressure: 1013 hPa"
    ]
    
    for msg in messages:
        await nc.publish("iot.sensor", msg.encode())
        print(f"Published: {msg}")
        await asyncio.sleep(0.5)
    
    await nc.drain()
    print("Done publishing")

if __name__ == "__main__":
    asyncio.run(main())
