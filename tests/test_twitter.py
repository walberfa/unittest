import unittest
from unittest.mock import Mock
from short_tweeter import Tweet


class TweetTest(unittest.TestCase):
    def test_example(self):
        mock_twitter = Mock()
        Tweet.tweet(mock_twitter, "a song of ice and fire")
        mock_twitter.PostUpdate.assert_called_with("a song of ice and fire")

    def test_example2(self):
        mock_twitter = Mock()
        Tweet.tweet(mock_twitter, "a song of ice and fire is a serie of books write by george martin!!!")
        mock_twitter.PostUpdate.assert_called_with("a song of ice & fire is a serie of books write by george martin")


if __name__ == '__main__':
    unittest.main()
