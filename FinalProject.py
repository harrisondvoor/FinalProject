access_token = 'EAACEdEose0cBAPVteQrYbIXztKIEajeBtffCKZCZAPJJq2ZBIuZCvjZAkXq5v7id4iJftweHd35IoO4bfe13I6z938frAq7c4AfZBlz0R7B0YYFm6KwCpMLMEGpPfp4Dl7d2M8GkZBAjDZClqBg6w2nrBldz1yBsNkr4F3BuKmMvvo8EfmWETo3V5WkJQObDK2QZD'
graph = facebook.GraphAPI(access_token=access_token_in, version="2.1")
    tagged_pics = graph.request('/me/posts?limit=100')
    tagged