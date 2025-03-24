import aiohttp


class RickAndMortyClient:
	BASE_URL = 'https://rickandmortyapi.com/api'
	
	def __init__(self):
		self.session = None
		
	async def __aenter__(self):
		self.session = aiohttp.ClientSession()
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self.session.close()
		
	async def _fetch_all_pages(self, endpoint):
		"""Fetch all pages of data from a given endpoint"""
		results = []
		url = f'{self.BASE_URL}/{endpoint}'
		
		async with self.session.get(url) as response:
			data = await response.json()
			results.extend(data['results'])
			next_url = data['info']['next']
		
		while next_url:
			async with self.session.get(next_url) as response:
				data = await response.json()
				results.extend(data['results'])
				next_url = data['info']['next']

		return results

	async def get_characters(self):
		"""Fetch all characters"""
		return await self._fetch_all_pages('character')

	async def get_locations(self):
		"""Fetch all locations"""
		return await self._fetch_all_pages('location')

	async def get_episodes(self):
		"""Fetch all episodes"""
		return await self._fetch_all_pages('episode')
