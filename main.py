import asyncio
import json
import aiofiles
from rickandmorty_client import RickAndMortyClient


async def save_to_file(data, filename):
	"""Save data to a JSON file asynchronously"""
	async with aiofiles.open(filename, 'w') as file:
		await file.write(json.dumps(data, indent=2))


async def main():
	async with RickAndMortyClient() as client:
		characters, locations, episodes = await asyncio.gather(
			client.get_characters(),
			client.get_locations(),
			client.get_episodes()
		)
		
		await asyncio.gather(
			save_to_file(characters, 'data/characters.json'),
			save_to_file(locations, 'data/locations.json'),
			save_to_file(episodes, 'data/episodes.json')
		)
		print('Data fetched and saved successfully!')


if __name__ == '__main__':
	asyncio.run(main())
