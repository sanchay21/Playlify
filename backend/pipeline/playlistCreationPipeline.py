class PlaylistPipeline:
    def __init__(
        self,
        rate_limiter,
        intent_classifier,
        rag_retriever,
        user_music_prefernces,
        llm_client,
        spotify_playlist_creation,
        chat_func
        ):
            self.rate_limiter = rate_limiter
            self.intent_classifier = intent_classifier
            self.rag_retriever = rag_retriever
            self.user_music_prefernces = user_music_prefernces
            self.llm_client = llm_client
            self.spotify_playlist_creation = spotify_playlist_creation
            self.chat_func = chat_func
            
            


    def run(self, ctx):
        # To be Implemented
        # ctx.intent = self.intent_classifier.classify(ctx.user_query)
        # ctx.rag_context = self.rag_retriever.retrieve(ctx.user_query)
        # ctx.playlist_url = self.spotify_service.create_playlist(
        #     user_id=ctx.user_id,
        #     songs=ctx.songs,
        # )

        ctx.user_preferences = self.user_music_prefernces(ctx.user_id)
        ctx.songs = self.chat_func(ctx.user_query, ctx.user_preferences)
        print(ctx.songs)
        # {'songs':
        #     [
        #         'Perfect', 'Stitches', 'One Call Away', 'Kho Jaane De', 'Thinking Out Loud', 'A Thousand Years', 'Stay with Me', 'Love Someone', 'Eastside', "I'm Yours"
        #     ]
        # }

        # songs = response["songs"]

        return ctx