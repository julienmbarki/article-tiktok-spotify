from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("ms_token", None)  # set your own ms_token
sound_id = "7016547803243022337"


async def sound_info():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        sound_info = await api.sound(id='7016547803243022337').info()
        print(sound_info)


if __name__ == "__main__":
    asyncio.run(sound_info())

# Convert sound info dict to json
import json
print(json.dumps(sound_info, indent=4))
