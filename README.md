# Rick and Morty API Integration

This project provides a simple integration with the [Rick and Morty API](https://rickandmortyapi.com/) to fetch and save data about characters, locations, and episodes. It consists of a client module for API interactions and a sample application demonstrating its usage.

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/unreider/rickandmorty_integration.git
   cd rickandmorty_integration
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Launch the script:
```bash
python main.py
```

This will fetch all characters, locations, and episodes from the API and save them to `data/characters.json`, `data/locations.json`, and `data/episodes.json` in the project root.

## Project Structure
- `rickandmorty_client.py`: Client module with async data-fetching functionality.
- `main.py`: Application that uses the client to fetch and save data.
- `data/`: Output directory for saved JSON files (created automatically).
- `requirements.txt`: List of Python dependencies.

## Implementation Details
- **API Choice**: This solution uses the REST interface of the Rick and Morty API (`https://rickandmortyapi.com/api/`).  
  - **Why REST over GraphQL?**: While I’m experienced with GraphQL and appreciate its ability to fetch all data in a single query, I chose REST for this task to keep the implementation straightforward and aligned with the requirement to "avoid over-engineering". REST’s paginated endpoints are simple to handle asynchronously, and the provided solution efficiently fetches all data using a clean, iterative approach. GraphQL could reduce requests but would introduce query syntax complexity unnecessary for this scope.
- **Async Operations**: The client module leverages `aiohttp` for non-blocking HTTP requests, with pagination handled in a single method (`_fetch_all_pages`). The sample app uses `asyncio.gather` to fetch and save data concurrently, optimizing performance.
- **File Handling**: The `data/` directory is created automatically using `os.makedirs`, ensuring the script runs out of the box. Data is saved as pretty-printed JSON with `aiofiles` for async I/O.

## Notes
- No error handling (e.g., HTTP 404) is included, as per the task’s instructions.
- The solution prioritizes simplicity, clarity, and adherence to requirements.

## Submission
This project is submitted as a Git repository for review. Feel free to reach out with any questions!
