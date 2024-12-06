# # api/utils.py

# import requests

# ANI_LIST_API_URL = "https://graphql.anilist.co/"

# def search_anime(query):
#     query = """
#     query ($search: String) {
#       Media(search: $search, type: ANIME) {
#         id
#         title {
#           romaji
#         }
#         genres
#         description
#       }
#     }
#     """
#     variables = {"search": query}
#     response = requests.post(ANI_LIST_API_URL, json={"query": query, "variables": variables})
#     return response.json()



