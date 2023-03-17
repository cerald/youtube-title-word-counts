# youtube-title-word-counts

# Program to count the most common words in the titles of a YouTube channel's uploaded videos
This program uses the YouTube Data API to retrieve a YouTube channel's uploaded videos and count the most common words in their titles.

### Prerequisites
* Python 3.x
* google-auth and google-api-python-client modules
* A Google Cloud Platform project with the YouTube Data API enabled
* A service account with credentials stored in a JSON file
### Installation
1. Clone this repository or download the script file.
2. Install the required modules using pip:
``` pip install google-auth google-api-python-client```
3. Create a Google Cloud Platform project and enable the YouTube Data API.
4. Create a service account and download the credentials as a JSON file.
5. Move the JSON file to the same directory as the script file.

### Usage
1. Open a terminal or command prompt and navigate to the directory containing the script file and the JSON file with the credentials.
2. Run the script using Python:
```python script.py```
3. The program will output the 10 most common words in the titles of the uploaded videos for the specified YouTube channel.

### Customization
You can also modify the `maxResults` parameter in the `playlist_items_response` request to retrieve more or fewer videos per API call. Note that there is a quota limit for the number of API requests that can be made per day.
