# YouTube Playlist Automator

A simple Python CLI tool to automate playback of YouTube videos and generate personalized daily video playlists directly in your web browser.

## Features

* Open a custom list of YouTube URLs or IDs in sequence using your default browser
* Generate and play a daily video playlist based on predefined schedules
* Easily extendable: add new days, videos, or integrate with YouTube Data API for more advanced features

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/youtube-playlist-automator.git
   cd youtube-playlist-automator
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on macOS/Linux
   venv\Scripts\activate    # on Windows
   ```

3. Install requirements (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

* **Play a custom playlist**:

  ```bash
  python main.py
  ```

  Choose option `2` and enter comma-separated YouTube URLs or IDs.

* **Play your personal daily playlist**:
  Choose option `1` to open today’s scheduled playlist in your browser.

* **Inform videos URLs**:
  Choose option `2` to review or update your scheduled URLs file.

## Project Structure

```
.
├── main.py                 # Entry point for the CLI
├── get_videos_list.py      # Menu logic and command handling
├── youtube_utils.py        # Core functions: URL parsing, playlist URL building, browser opening
└── .gitignore              # Files and folders to ignore in git
```

## Contributing

Feel free to open issues or submit pull requests for bug fixes and new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
