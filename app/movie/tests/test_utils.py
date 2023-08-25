from django.test import TestCase

from app.movie import utils


class MovieUtilsTestCase(TestCase):
    def test_get_movie_list_returns_list(self):
        movie_list = utils.search_utelly_movies_by_keyword("Avengers")
        self.assertIsInstance(movie_list, list)
        self.assertGreater(len(movie_list), 0)


{
    "variant": "rapidapi_basic",
    "results": [
        {
            "locations": [
                {
                    "display_name": "Google Play",
                    "id": "5d8260b128fbcd0052aed197",
                    "url": "https://play.google.com/store/tv/show/Marvel_s_Avengers_Assemble?id=Q4Gptplumso&hl=en&gl=US&cdid=tvseason-su6OFPwq3csNJAg8j6pLxQ",
                    "name": "GooglePlayIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/GooglePlayIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "iTunes",
                    "id": "5d80a9a5d51bef861d3740d3",
                    "url": "https://itunes.apple.com/us/tv-season/tchalla-royale/id1436519582?i=1440262405&uo=4",
                    "name": "iTunesIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/iTunesIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "Disney+",
                    "id": "5e220e9036f2f6c40e974ed6",
                    "url": "https://www.disneyplus.com/en-us/video/0a545cfe-65fb-4183-ab49-efec75647966",
                    "name": "DisneyPlusIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/DisneyPlusIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "Amazon Instant Video",
                    "id": "5d82609332ac2f0051962fe6",
                    "url": "https://www.amazon.com/gp/video/detail/B01MQKPLTO&tag=utellycom00-21",
                    "name": "AmazonInstantVideoIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonInstantVideoIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
            ],
            "weight": 7523,
            "id": "5d91419a302b840050ad37ae",
            "external_ids": {
                "imdb": {
                    "url": "https://www.imdb.com/title/tt2455546",
                    "id": "tt2455546",
                },
                "tmdb": {"url": "https://www.themoviedb.org/tv/59427", "id": "59427"},
                "iva": {"id": "445272"},
                "facebook": None,
                "rotten_tomatoes": None,
                "wiki_data": {
                    "url": "https://www.wikidata.org/wiki/Q3896442",
                    "id": "Q3896442",
                },
                "iva_rating": None,
                "gracenote": None,
            },
            "picture": "https://utellyassets9-4.imgix.net/api/Images/7d742402fae78206a47ff2f8cca5f4e2/Redirect?fit=crop&auto=compress&crop=faces,top",
            "provider": "iva",
            "name": "Avengers Assemble",
        },
        {
            "locations": [
                {
                    "display_name": "Amazon Prime Video",
                    "id": "5d8257243ed3f000513540ec",
                    "url": "https://www.amazon.com/gp/video/detail/B00KG22RGM&tag=utellycom00-21",
                    "name": "AmazonPrimeVideoIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "Amazon Instant Video",
                    "id": "5d82609332ac2f0051962fe6",
                    "url": "https://www.amazon.com/gp/video/detail/B00KG22RGM&tag=utellycom00-21",
                    "name": "AmazonInstantVideoIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonInstantVideoIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "iTunes",
                    "id": "5d80a9a5d51bef861d3740d3",
                    "url": "https://tv.apple.com/us/episode/the-50000-breakfast/umc.cmc.5t9z28rmn26n07w5tcxow48f3?playableId=tvs.sbd.9001%3a851337387&showId=umc.cmc.11q3yqne3abpwkdxrrstnorx1",
                    "name": "iTunesIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/iTunesIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
            ],
            "weight": 6160,
            "id": "5d97dab29a76a40056de6860",
            "external_ids": {
                "imdb": {
                    "url": "https://www.imdb.com/title/tt0054518",
                    "id": "tt0054518",
                },
                "tmdb": {"url": "https://www.themoviedb.org/tv/2473", "id": "2473"},
                "iva": {"id": "685421"},
                "facebook": None,
                "rotten_tomatoes": None,
                "wiki_data": {
                    "url": "https://www.wikidata.org/wiki/Q113700",
                    "id": "Q113700",
                },
                "iva_rating": None,
                "gracenote": None,
            },
            "picture": "https://utellyassets9-4.imgix.net/api/Images/7e452240276d858a81c809b0419f76a4/Redirect?fit=crop&auto=compress&crop=faces,top",
            "provider": "iva",
            "name": "The Avengers",
        },
        {
            "locations": [
                {
                    "display_name": "Amazon Instant Video",
                    "id": "5d82609332ac2f0051962fe6",
                    "url": "https://www.amazon.com/gp/video/detail/B08T7WRGNG/ref=atv_sr_def_c_unkc_7_1_7?sr=1-7&pageTypeIdSource=ASIN&pageTypeId=B08T7WRGNG&qid=1656051466&tag=utellycom00-21",
                    "name": "AmazonInstantVideoIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonInstantVideoIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                }
            ],
            "weight": 0,
            "id": "5e28ebe4e847f9277fa0333e",
            "external_ids": {
                "imdb": {
                    "url": "https://www.imdb.com/title/tt0200421",
                    "id": "tt0200421",
                },
                "tmdb": {
                    "url": "https://www.themoviedb.org/movie/30936",
                    "id": "30936",
                },
                "iva": {"id": "154518"},
                "facebook": None,
                "rotten_tomatoes": None,
                "wiki_data": {
                    "url": "https://www.wikidata.org/wiki/Q1497100",
                    "id": "Q1497100",
                },
                "iva_rating": None,
                "gracenote": None,
            },
            "picture": "https://utellyassets9-2.imgix.net/api/Images/0cbe3e4d402a1be58a4d8db09233c74e/Redirect?fit=crop&auto=compress&crop=faces,top",
            "provider": "iva",
            "name": "Teenage Alien Avengers",
        },
        {
            "locations": [
                {
                    "display_name": "Amazon Instant Video",
                    "id": "5d82609332ac2f0051962fe6",
                    "url": "https://www.amazon.com/gp/video/detail/B001UA4GKY/ref=atv_sr_def_c_unkc_20_1_20?sr=1-20&pageTypeIdSource=ASIN&pageTypeId=B0091W4ZQI&qid=1656050705&tag=utellycom00-21",
                    "name": "AmazonInstantVideoIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonInstantVideoIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "Google Play",
                    "id": "5d8260b128fbcd0052aed197",
                    "url": "https://play.google.com/store/movies/details/The_Avengers?id=Ssv0lfyhfXM&hl=en&gl=US",
                    "name": "GooglePlayIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/GooglePlayIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "iTunes",
                    "id": "5d80a9a5d51bef861d3740d3",
                    "url": "https://itunes.apple.com/us/movie/the-avengers-1998/id353421214?uo=4",
                    "name": "iTunesIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/iTunesIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
            ],
            "weight": 0,
            "id": "5d97daae9a76a40056de6372",
            "external_ids": {
                "imdb": {
                    "url": "https://www.imdb.com/title/tt0118661",
                    "id": "tt0118661",
                },
                "tmdb": {"url": "https://www.themoviedb.org/movie/9320", "id": "9320"},
                "iva": {"id": "7627"},
                "facebook": None,
                "rotten_tomatoes": None,
                "wiki_data": {
                    "url": "https://www.wikidata.org/wiki/Q494985",
                    "id": "Q494985",
                },
                "iva_rating": None,
                "gracenote": None,
            },
            "picture": "https://utellyassets9-2.imgix.net/api/Images/ddfa52e8c3622702bc5f549ba6fb4533/Redirect?fit=crop&auto=compress&crop=faces,top",
            "provider": "iva",
            "name": "The Avengers",
        },
        {
            "locations": [
                {
                    "display_name": "Amazon Instant Video",
                    "id": "5d82609332ac2f0051962fe6",
                    "url": "https://www.amazon.com/gp/video/detail/B00V34GW5E/ref=atv_sr_def_c_unkc_11_1_11?sr=1-11&pageTypeIdSource=ASIN&pageTypeId=B00V35UMKE&qid=1656039610&tag=utellycom00-21",
                    "name": "AmazonInstantVideoIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonInstantVideoIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "Amazon Prime Video",
                    "id": "5d8257243ed3f000513540ec",
                    "url": "https://www.amazon.com/gp/video/detail/B00UZG5C8O/ref=atv_br_def_r_br_c_vQHLwismr_1_490&tag=utellycom00-21",
                    "name": "AmazonPrimeVideoIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "Google Play",
                    "id": "5d8260b128fbcd0052aed197",
                    "url": "https://play.google.com/store/movies/details/Crippled_Avengers?id=RijKopmQmA0&hl=en&gl=US",
                    "name": "GooglePlayIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/GooglePlayIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
                {
                    "display_name": "iTunes",
                    "id": "5d80a9a5d51bef861d3740d3",
                    "url": "https://itunes.apple.com/us/movie/crippled-avengers/id775935761?uo=4",
                    "name": "iTunesIVAUS",
                    "icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/iTunesIVAUS.png?w=92&auto=compress&app_version=20e4278a-332e-458b-9e01-70497630bad3_1e1210o12023-08-25",
                },
            ],
            "weight": 0,
            "id": "5e28ec21e847f9277fa05727",
            "external_ids": {
                "imdb": {
                    "url": "https://www.imdb.com/title/tt0077292",
                    "id": "tt0077292",
                },
                "tmdb": {
                    "url": "https://www.themoviedb.org/movie/40081",
                    "id": "40081",
                },
                "iva": None,
                "facebook": None,
                "rotten_tomatoes": None,
                "wiki_data": {
                    "url": "https://www.wikidata.org/wiki/Q5185841",
                    "id": "Q5185841",
                },
                "iva_rating": None,
                "gracenote": None,
            },
            "picture": "https://utellyassets9-1.imgix.net/api/Images/b517b15274ce5d6e727874eb4b849cb3/Redirect?fit=crop&auto=compress&crop=faces,top",
            "provider": "iva",
            "name": "Crippled Avengers",
        },
    ],
    "updated": "2023-08-25T05:06:19+0100",
    "term": "Avengers",
    "status_code": 200,
}
