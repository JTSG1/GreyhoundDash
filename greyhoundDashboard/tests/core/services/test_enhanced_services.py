import unittest
from unittest.mock import patch, MagicMock
from core.services import EnhancedVikunja, EnhancedPortainer, EnhancedNavidrome

class MockRegisteredService:
    def __init__(self, url, username, password):
        self.url = url
        self.auth_fields = {"username": username, "password": password}

class TestEnhancedPortainer(unittest.TestCase):

    @patch("requests.get")
    @patch("requests.post")
    def test_get_success(self, mock_post, mock_get):
        mock_post.return_value.json.return_value = {"jwt": "mock_jwt"}

        mock_get.side_effect = [
            MagicMock(status_code=200),  # up_check
            MagicMock(status_code=200, json=lambda: [{"Id": 1}]),  # get_environment
            MagicMock(status_code=200, json=lambda: [
                {"State": "running"},
                {"State": "exited"},
            ])  # get_containers
        ]

        service = EnhancedPortainer(MockRegisteredService("http://localhost", "user", "pass"))
        result = service.get()

        self.assertTrue(result.state["up"])
        self.assertEqual(result.state["running"], 1)
        self.assertEqual(result.state["exited"], 1)

class TestEnhancedNavidrome(unittest.TestCase):

    @patch("requests.get")
    def test_get_success(self, mock_get):
        def get_side_effect(url, *args, **kwargs):
            if "getNowPlaying" in url:
                return MagicMock(json=lambda: {
                    "subsonic-response": {
                        "nowPlaying": {
                            "entry": [{
                                "artist": "Artist",
                                "album": "Album",
                                "title": "Title",
                                "coverArt": "123"
                            }]
                        }
                    }
                })
            elif "getCoverArt" in url:
                mock_response = MagicMock()
                mock_response.content = b"fakeimage"
                return mock_response

        mock_get.side_effect = get_side_effect

        service = EnhancedNavidrome(MockRegisteredService("http://localhost", "user", "pass"))
        with patch.object(service, 'up_check', return_value=True):
            result = service.get()
            self.assertEqual(result.state["artist"], "Artist")
            self.assertEqual(result.state["album"], "Album")
            self.assertEqual(result.state["title"], "Title")
            self.assertTrue(result.state["art"].startswith("data:image/png;base64,"))

class TestEnhancedVikunja(unittest.TestCase):

    @patch("requests.get")
    @patch("requests.post")
    def test_get_success(self, mock_post, mock_get):
        mock_post.return_value.json.return_value = {"token": "mock_token"}

        mock_get.side_effect = [
            MagicMock(status_code=200),  # up_check
            MagicMock(status_code=200, json=lambda: [
                {"done": False},
                {"done": True}
            ])
        ]

        service = EnhancedVikunja(MockRegisteredService("http://localhost", "user", "pass"))
        result = service.get()

        self.assertTrue(result.state["up"])
        self.assertEqual(result.state["active"], 1)
        self.assertEqual(result.state["done"], 1)

if __name__ == "__main__":
    unittest.main()
