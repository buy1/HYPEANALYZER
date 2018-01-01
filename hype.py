#Import the necessary methods from tweepy library
import tweepy as tp

#Variables that contains the user credentials to access Twitter API 
access_token = "4255093813-tNAjc5Pa6N7GDZxXqR1sR0669SjRz6ZeLYZPKWo"
access_token_secret = "H54qdIoxg1yAoTBynYIhCsmHZ2YdF72EY8itJZyYvvQNC"
consumer_key = "RBHUFOxvArccvsOkgnmKlCsOv"
consumer_secret = "tjHiBSpxyDxGvsixjCvOwrT4ky33MyUxz41KdOkBbdKLLLBPxE"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(tp.streaming.StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = tp.OAuthHandler(consumer_key, consumer_secret) #auth is a key handling object that you pass to tweepy to get requests
    auth.set_access_token(access_token, access_token_secret)
    stream = tp.Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])