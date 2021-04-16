# redditCMS
python code to print dictionary of all mentioned cryptos and the time when those cryptos got mentioned

I've used praw library which python based api wrapper 

pre requisites to run this program 
1. reddit account 
2. reddit application (https://www.reddit.com/prefs/apps)
3. Update properties after creating application (starting from lline 6)
   reddit = praw.Reddit(client_id='CLIENT-ID', 
                     client_secret='CLIENT-SECRET, 
                     user_agent='NAME_OF_APPLICATION', 
                     username='REDDIT_USERNAME', 
                     password='REDDIT_PASSWORD')
4. PRAW package installed on your environment (pip install praw)



ALGO: 
1. fetching all details of cryptoMoonShots by using praw 
2. Creating regex to find all words starting with $ and are alphabets
3. LOOP for all posts
    - fetching and merging all cryptos from title and body of post
    - removing duplicate mentioned of same post (one post can have multiple crptos mentioned)
    - converting all cryptos to upper case to follow consistency
    - adding to dictionary and if dictionary already contains crpyto adding date to list
    LOOP END
    
    

   