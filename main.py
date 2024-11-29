import functions_framework
import authentication

@functions_framework.http
def tweet(request=None):
    if not request:
        return "No request", 200
    try:
        data = request.get_json()
        if data and "tweet_text" in data:
            tweet_text = data["tweet_text"]
            print(tweet_text)

            client = authentication.client

            client.create_tweet(
                text=tweet_text
            )
            print("Tweeted!")
            return {"message": "Tweeted!"}, 200
        else:
            return {"error": "No tweet_text in request"}, 400
    except Exception as e:
        print("An error occurred")
        print(e)
        return {"error": str(e)}, 500