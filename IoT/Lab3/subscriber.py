import asyncio
import nats

async def main():
    # Connect to NATS server
    nc = await nats.connect("nats://localhost:4222")
    
    # Message handler
    async def message_handler(msg):
        print(f"Received: {msg.data.decode()} on {msg.subject}")
    
    # Subscribe to topic
    sub = await nc.subscribe("iot.sensor", cb=message_handler)
    
    print("Subscriber listening on 'iot.sensor'...")
    print("Press Ctrl+C to stop")
    
    try:
        # Keep running
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        await sub.unsubscribe()
        await nc.drain()

if __name__ == "__main__":
    asyncio.run(main())
