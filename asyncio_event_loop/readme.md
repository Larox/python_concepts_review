# Event Loop and asyncio.run()

The event loop can be thought as a `while True` loop that monitors
coroutines, loogin for things that can be executed in the meantime.

This event loop is handled by the function call:

```py
asyncio.run(main())
```

This function will be runing tasks until they are markedas complete and
then will close the event loop.

Another option to manage the loop is with `get_event_loop()`:

```py
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main)
finally:
    loop.close()
```

This is a less common approach, since `async.run(main())` is enough in
most of the use cases.

The `loop` usage is recommended when interacting with the loop is needed
since it provides functions like `is_running()` and `is_closed()` and
it can also be passed as an argument.

## Coroutines

Coroutines follow the `async def` interface and in their body can use
await.

```py
import asyncio

async def main():
    print("foo")
    await asyncio.sleep(1)
    print("foo")

x = main()
# <coroutine object main at 0x1027a7892>
```
