# Import module
import requests

# Create Soundcharts API client
class SoundchartsClient(object):
    base_url = "https://customer.api.soundcharts.com/api/"

    # Constructor
    def __init__(self, x_app_id, x_api_key):
        self.headers = {
            'x-app-id': x_app_id,
            'x-api-key': x_api_key
        }

    # Get resource generic function
    def get_resource(self, endpoint, params=None, data=None):
        url = f"{self.base_url}{endpoint}"

        response = requests.get(url, headers=self.headers, params=params)

        print(f"Status code: {response.status_code}")
        
        if response.status_code not in range(200,299):
            return{}
        return response.json()
    
    # Get TikTok's top charts 
    def get_tiktok_charts(self, offset=0, limit=100, date=''):
        endpoint = f"v2/chart/tiktok/music/weekly/ranking/{date}"

        params = {
            'offset': offset,
            'limit': limit,
        }

        return self.get_resource(endpoint, params=params)
    
    # Get track's TikTok streams by date
    def get_tiktok_streams_by_date(self, endDate='', period=90, track_id=''):
        endpoint = f"v2/tiktok/music/{track_id}/video/volume"

        params = {
            'endDate': endDate,
            'period': period
        }

        return self.get_resource(endpoint, params=params)

    # Get track's Spotify streams by date
    def get_track_streams_by_date(self, startDate='', endDate='', track_id=''):
        endpoint = f"v2/song/{track_id}/audience/spotify"

        params = {
            'startDate': startDate,
            'endDate': endDate
        }

        return self.get_resource(endpoint, params=params)
    
    # Get track's metadata
    def get_track_metadata(self, track_id='track_id'):
        endpoint = f"v2.25/song/{track_id}"

        return self.get_resource(endpoint)

    # Get artist's Spotify streams by date
    def get_artist_streams_by_date(self, startDate='', endDate='', artist_id=''):
        endpoint = f"v2/artist/{artist_id}/streaming/spotify/listening"

        params = {
            'startDate': startDate,
            'endDate': endDate
        }

        return self.get_resource(endpoint, params=params)
    
    # Get artist's popularity by date
    def get_artist_tiktok_followers_by_date(self, startDate='', endDate='', artist_id=''):
        endpoint = f"v2/artist/{artist_id}/audience/tiktok"

        params = {
            'startDate': startDate,
            'endDate': endDate
        }

        return self.get_resource(endpoint, params=params)
