from TikTokApi import TikTokApi
import asyncio
import os
import json

ms_token = os.environ.get("ms_token", None)  # set your own ms_token
sound_id = "7016547803243022337"


async def sound_info():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        sound_info_result = await api.sound(id='7016547803243022337').info()
       
        # Save the sound info to a JSON file
        with open('sound_info.json', 'w') as f:
            json.dump(sound_info_result, f, indent=4)

        print("Sound info saved to sound_info.json")


if __name__ == "__main__":
    asyncio.run(sound_info())
