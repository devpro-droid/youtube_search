from youtube_search import YoutubeSearch
import youtube_search


class TestSearch:

    def test_init_defaults(self):
        search = YoutubeSearch('test')
        assert search.max_results is None
        assert 1 <= len(search.videos)

    def test_init_max_results(self):
        search = YoutubeSearch('test', max_results=10)
        assert 10 == search.max_results
        assert 10 == len(search.videos)

    def test_dict(self):
        search = YoutubeSearch('test', max_results=10)
        assert isinstance(search.to_dict(), list)

    def test_json(self):
        search = YoutubeSearch('test', max_results=10)
        assert isinstance(search.to_json(), str)

import sys

if len(sys.argv) > 1:
    results = YoutubeSearch(sys.argv[1], max_results=int(sys.argv[2])).to_json()
    print(results)
else:
    youtube_search.print_hi()



