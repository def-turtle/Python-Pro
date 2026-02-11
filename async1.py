import asyncio

async def say_hello(to:str):
    print(f"Привіт, {to}!")
    await asyncio.sleep(2)
    print("Пройшло 2 секунди")

async def main():
    await asyncio.gather(
        say_hello("Mario"),
        say_hello("Menna"),
    )
if __name__ == "__main__":
    asyncio.run(main())
