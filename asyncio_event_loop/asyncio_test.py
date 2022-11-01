# Performs fetch and writes output of words definitions asynchrously.

import asyncio
import aiofiles
from aiohttp import ClientSession


WORDS_TO_SEARCH = [
    "test",
    "loop",
    "event",
    "asynchronous"
]

DICTIONARY_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

# Async data fetching from free dictionaryapi
async def fetch_meaning(session: ClientSession, word: str) -> str:
    url = DICTIONARY_URL + word
    resp = await session.request("GET", url)
    resp.raise_for_status()
    definition = await resp.text()
    return definition


# Persists the information in files asynchronously
async def write_results(json_resp: str, word: str) -> None:
    async with aiofiles.open(f"{word}.txt", "a") as file:
        await file.write(json_resp)


# Performs the async fetching and writing
async def perform_query(session: ClientSession, word: str) -> None:
    defintion = await fetch_meaning(session, word)
    await write_results(defintion, word)


# Creates multiple tasks of "perform" for each word and gathers them
async def append_tasks(words_list: list[str]):
    tasks = list()
    async with ClientSession() as session:
        for word in words_list:
            tasks.append(perform_query(session, word))
        # gets all the coroutines from the words to check the definitions
        await asyncio.gather(*tasks)


# main function to perform gathered tasks
async def main():
    await append_tasks(WORDS_TO_SEARCH)

# Async loop
asyncio.run(main())