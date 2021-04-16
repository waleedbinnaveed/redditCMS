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
    
    

SAMPLE OUTPUT 


{
   "ELONGATE":[
      "2021-04-12 22:24:10"
   ],
   "GHOUL":[
      "2021-03-26 07:37:01"
   ],
   "SITH":[
      "2021-04-14 03:06:06",
      "2021-04-12 20:50:04",
      "2021-04-10 07:58:59",
      "2021-04-11 11:24:55"
   ],
   "BNB":[
      "2021-04-14 03:06:06"
   ],
   "VIBE":[
      "2021-03-22 12:51:25"
   ],
   "COVAL":[
      "2021-03-23 15:36:31",
      "2021-03-20 15:14:57"
   ],
   "BOG":[
      "2021-04-06 17:10:52",
      "2021-04-05 08:10:24",
      "2021-04-14 06:31:14",
      "2021-04-04 00:32:46",
      "2021-03-05 05:17:31",
      "2021-03-17 01:25:21",
      "2021-04-11 04:32:06",
      "2021-03-11 03:56:31",
      "2021-03-31 00:53:53"
   ],
   "HITCOIN":[
      "2021-03-18 10:51:32"
   ],
   "DMT":[
      "2021-03-24 07:16:26"
   ],
   "EYE":[
      "2021-03-11 06:18:51",
      "2021-04-15 12:07:30"
   ],
   "FUEL":[
      "2021-03-20 15:14:57"
   ],
   "SNFT":[
      "2021-03-17 13:44:44",
      "2021-04-07 04:22:40"
   ],
   "VIDYA":[
      "2021-03-14 09:06:42"
   ],
   "LIGHT":[
      "2021-04-07 06:37:59"
   ],
   "DEOR":[
      "2021-03-25 10:14:52"
   ],
   "LLT":[
      "2021-04-09 06:46:24"
   ],
   "NDS":[
      "2021-04-13 05:58:02"
   ],
   "SPOWL":[
      "2021-04-12 09:56:36",
      "2021-04-15 14:01:04"
   ],
   "FOAM":[
      "2021-03-26 15:13:01"
   ],
   "FSAFE":[
      "2021-04-10 22:18:55"
   ],
   "WENMOON":[
      "2021-04-12 14:19:56"
   ],
   "VAI":[
      "2021-04-01 06:04:50",
      "2021-04-02 04:33:17"
   ],
   "BLIMPSROCK":[
      "2021-04-14 04:11:15",
      "2021-04-14 04:11:15"
   ],
   "BLAST":[
      "2021-04-13 09:43:45",
      "2021-04-13 09:43:45"
   ],
   "RAMEN":[
      "2021-03-23 09:49:46"
   ],
   "VOX":[
      "2021-03-31 08:01:53"
   ],
   "OCTANS":[
      "2021-04-08 01:45:44"
   ],
   "OCTA":[
      "2021-04-08 01:45:44"
   ],
   "MOON":[
      "2021-04-06 23:45:37",
      "2021-04-06 23:45:37"
   ],
   "BNF":[
      "2021-04-15 08:05:38",
      "2021-04-14 08:29:10"
   ],
   "BINGUS":[
      "2021-04-10 04:17:56",
      "2021-04-13 01:08:07",
      "2021-04-11 02:00:04"
   ],
   "DMDHANDS":[
      "2021-03-25 13:10:53",
      "2021-03-25 13:10:53"
   ],
   "SAH":[
      "2021-04-09 16:45:21"
   ],
   "EBOX":[
      "2021-03-27 21:29:42",
      "2021-03-29 11:40:48"
   ],
   "FROGE":[
      "2021-04-03 09:18:15"
   ],
   "BFC":[
      "2021-04-06 05:28:31"
   ],
   "PHNX":[
      "2021-04-06 05:28:31"
   ],
   "OPEN":[
      "2021-04-06 05:28:31"
   ],
   "MARX":[
      "2021-04-03 11:58:09"
   ],
   "ALOHA":[
      "2021-04-10 08:02:26"
   ],
   "KET":[
      "2021-04-11 06:03:24"
   ],
   "SAFEMOON":[
      "2021-03-13 16:17:33",
      "2021-03-18 01:10:58",
      "2021-03-13 11:47:55",
      "2021-03-13 11:47:55"
   ],
   "SPCATS":[
      "2021-04-16 01:52:08"
   ],
   "POODL":[
      "2021-04-06 08:26:38",
      "2021-04-06 08:26:38",
      "2021-04-07 13:26:47"
   ],
   "FVT":[
      "2021-03-29 07:41:57"
   ],
   "IFUND":[
      "2021-03-14 17:08:22",
      "2021-03-14 17:08:22"
   ],
   "SCX":[
      "2021-04-15 12:07:30"
   ],
   "XSPACE":[
      "2021-04-02 10:19:26"
   ],
   "NGMI":[
      "2021-03-11 03:56:31"
   ],
   "DOGE":[
      "2021-04-07 13:26:47"
   ],
   "HOGE":[
      "2021-04-07 13:26:47",
      "2021-03-13 11:47:55"
   ],
   "PSWAP":[
      "2021-04-15 10:02:22"
   ],
   "CAKE":[
      "2021-03-31 00:53:53"
   ]
}

   