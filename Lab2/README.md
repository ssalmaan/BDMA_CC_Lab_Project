# README #
**Q2.1.1:**

Top 10 common words and respective counts :
[('the', 1343), (',', 1251), ('.', 810), (')', 638), ('(', 637), ('of', 586), ('to', 491), ('a', 468), (':', 454), ('in', 417)]

Total number of words of the book:
25155

**Q2.1.2:**

Top 10 common words and respective counts without punctuations:
[('the', 1444), ('of', 586), ('to', 531), ('in', 506), ('a', 481), ('and', 346), ('is', 289), ('we', 279), ('that', 275), ('this', 268)]
3117

**Q2.1.3: Why "Tensorflow" is not the most frequent word? Which are the Stop Words?**
```
Because the top 10 most frequent words identified are stop words. 
The stop words are:
the
of
to
in
a
and 
is
we 
that 
this

Top 10 common words and respective counts without punctuations and after removing stop words:
[('tensorflow', 193), ('data', 102), ('tensor', 99), ('code', 90), ('learning', 81), ('function', 74), ('one', 73), ('use', 65), ('example', 64), ('available', 63)]

Total number of words from the book without punctuations and after removing stop words:
2998
```
**Q2.2.1: Is the data printed correctly? Is it yours?** 
```
shabana@LAPTOP-OHVDIRKU:~$ python Twitter_1.py
Name: Shabana Salmaan
Location: Barcelona, Spain
Friends: 2
Created: 2019-02-28 19:47:13
Description: Master student
```
**COMMENT:** Yes, the above output is from my twitter account and the given details are printed correctly.

**Q2.2: Keep track of your executions** 
```
shabana@LAPTOP-OHVDIRKU:~$ python Twitter_2.py
Name: Shabana Salmaan
Location: Barcelona, Spain
Friends: 2
Created: 2019-02-28 19:47:13
Description: Master student

Well, that’s one way to make your broccoli disappear… https://t.co/XOAEgTRKN2


{
  "contributors": null,
  "truncated": false,
  "text": "Well, that\u2019s one way to make your broccoli disappear\u2026 https://t.co/XOAEgTRKN2",
  "is_quote_status": false,
  "in_reply_to_status_id": null,
  "id": 1103380223897169920,
  "favorite_count": 570,
  "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
  "retweeted": false,
  "coordinates": null,
  "entities": {
    "symbols": [],
    "user_mentions": [],
    "hashtags": [],
    "urls": [
      {
        "url": "https://t.co/XOAEgTRKN2",
        "indices": [
          54,
          77
        ],
        "expanded_url": "http://bit.ly/2NOZRhC",
        "display_url": "bit.ly/2NOZRhC"
      }
    ]
  },
  "in_reply_to_screen_name": null,
  "in_reply_to_user_id": null,
  "retweet_count": 49,
  "id_str": "1103380223897169920",
  "favorited": false,
  "user": {
    "follow_request_sent": false,
    "has_extended_profile": false,
    "profile_use_background_image": true,
    "default_profile_image": false,
    "id": 15846407,
    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
    "verified": true,
    "translator_type": "regular",
    "profile_text_color": "000000",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1053330932906639362/9OfK5qOh_normal.jpg",
    "profile_sidebar_fill_color": "C4C6CC",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https://t.co/CIcbQ353CL",
            "indices": [
              0,
              23
            ],
            "expanded_url": "https://www.ellentube.com/madebyyou.html#channel=best-of-the-week",
            "display_url": "ellentube.com/madebyyou.html\u2026"
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "followers_count": 77152713,
    "profile_sidebar_border_color": "FFFFFF",
    "id_str": "15846407",
    "profile_background_color": "3ABEE3",
    "listed_count": 108190,
    "is_translation_enabled": true,
    "utc_offset": null,
    "statuses_count": 18849,
    "description": "Comedian, talk show host and ice road trucker. My tweets are real, and they\u2019re spectacular. @ellentube @theellenfund",
    "friends_count": 33049,
    "location": "California",
    "profile_link_color": "3ABEE3",
    "profile_image_url": "http://pbs.twimg.com/profile_images/1053330932906639362/9OfK5qOh_normal.jpg",
    "following": true,
    "geo_enabled": true,
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/15846407/1550616213",
    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
    "screen_name": "TheEllenShow",
    "lang": "en",
    "profile_background_tile": false,
    "favourites_count": 1514,
    "name": "Ellen DeGeneres",
    "notifications": false,
    "url": "https://t.co/CIcbQ353CL",
    "created_at": "Thu Aug 14 03:50:42 +0000 2008",
    "contributors_enabled": false,
    "time_zone": null,
    "protected": false,
    "default_profile": false,
    "is_translator": false
  },
  "geo": null,
  "in_reply_to_user_id_str": null,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en",
  "created_at": "Wed Mar 06 19:41:59 +0000 2019",
  "in_reply_to_status_id_str": null,
  "place": null
}
{
  "follow_request_sent": false,
  "has_extended_profile": false,
  "profile_use_background_image": true,
  "live_following": false,
  "default_profile_image": false,
  "id": 216447259,
  "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
  "translator_type": "none",
  "verified": true,
  "blocked_by": false,
  "profile_text_color": "666666",
  "muting": false,
  "profile_image_url_https": "https://pbs.twimg.com/profile_images/1099472798379008001/Yww1YOfi_normal.jpg",
  "profile_sidebar_fill_color": "252429",
  "entities": {
    "url": {
      "urls": [
        {
          "url": "https://t.co/xoOZ2MPUf7",
          "indices": [
            0,
            23
          ],
          "expanded_url": "http://www.facebook.com/AnirudhOfficial",
          "display_url": "facebook.com/AnirudhOfficial"
        }
      ]
    },
    "description": {
      "urls": []
    }
  },
  "followers_count": 6806530,
  "profile_sidebar_border_color": "FFFFFF",
  "id_str": "216447259",
  "profile_background_color": "1A1B1F",
  "listed_count": 953,
  "status": {
    "contributors": null,
    "truncated": false,
    "text": "RT @KaalaBhairava7: Can\u2019t wait for this to come out! \nA maddd high spirited track from the Rockstar \u2b50\ufe0f@anirudhofficial https://t.co/6FCCP1V\u2026",
    "is_quote_status": true,
    "in_reply_to_status_id": null,
    "id": 1103324702502576129,
    "favorite_count": 0,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "quoted_status_id": 1103244751808000000,
    "retweeted": false,
    "coordinates": null,
    "entities": {
      "symbols": [],
      "user_mentions": [
        {
          "id": 842738200233885696,
          "indices": [
            3,
            18
          ],
          "id_str": "842738200233885696",
          "screen_name": "KaalaBhairava7",
          "name": "Kaala Bhairava"
        },
        {
          "id": 216447259,
          "indices": [
            102,
            118
          ],
          "id_str": "216447259",
          "screen_name": "anirudhofficial",
          "name": "Anirudh Ravichander"
        }
      ],
      "hashtags": [],
      "urls": []
    },
    "in_reply_to_screen_name": null,
    "in_reply_to_user_id": null,
    "retweet_count": 218,
    "id_str": "1103324702502576129",
    "favorited": false,
    "retweeted_status": {
      "contributors": null,
      "truncated": false,
      "text": "Can\u2019t wait for this to come out! \nA maddd high spirited track from the Rockstar \u2b50\ufe0f@anirudhofficial https://t.co/6FCCP1VLqj",
      "is_quote_status": true,
      "in_reply_to_status_id": null,
      "id": 1103250824392658946,
      "favorite_count": 2518,
      "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
      "quoted_status_id": 1103244751808000000,
      "retweeted": false,
      "coordinates": null,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 216447259,
            "indices": [
              82,
              98
            ],
            "id_str": "216447259",
            "screen_name": "anirudhofficial",
            "name": "Anirudh Ravichander"
          }
        ],
        "hashtags": [],
        "urls": [
          {
            "url": "https://t.co/6FCCP1VLqj",
            "indices": [
              99,
              122
            ],
            "expanded_url": "https://twitter.com/anirudhofficial/status/1103244751808000000",
            "display_url": "twitter.com/anirudhofficia\u2026"
          }
        ]
      },
      "in_reply_to_screen_name": null,
      "in_reply_to_user_id": null,
      "retweet_count": 218,
      "id_str": "1103250824392658946",
      "favorited": false,
      "geo": null,
      "in_reply_to_user_id_str": null,
      "possibly_sensitive": false,
      "lang": "en",
      "created_at": "Wed Mar 06 11:07:48 +0000 2019",
      "quoted_status_id_str": "1103244751808000000",
      "in_reply_to_status_id_str": null,
      "place": null
    },
    "geo": null,
    "in_reply_to_user_id_str": null,
    "lang": "en",
    "created_at": "Wed Mar 06 16:01:22 +0000 2019",
    "quoted_status_id_str": "1103244751808000000",
    "in_reply_to_status_id_str": null,
    "place": null
  },
  "is_translation_enabled": false,
  "utc_offset": null,
  "statuses_count": 11712,
  "description": "Music Composer/Singer in the Indian Film Industry | Snapchat : anirudhofficial",
  "friends_count": 192,
  "location": "Chennai",
  "profile_link_color": "2FC2EF",
  "profile_image_url": "http://pbs.twimg.com/profile_images/1099472798379008001/Yww1YOfi_normal.jpg",
  "following": true,
  "geo_enabled": true,
  "profile_banner_url": "https://pbs.twimg.com/profile_banners/216447259/1544298104",
  "blocking": false,
  "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
  "screen_name": "anirudhofficial",
  "lang": "en",
  "profile_background_tile": true,
  "favourites_count": 5533,
  "name": "Anirudh Ravichander",
  "notifications": false,
  "url": "https://t.co/xoOZ2MPUf7",
  "created_at": "Tue Nov 16 19:13:06 +0000 2010",
  "contributors_enabled": false,
  "time_zone": null,
  "protected": false,
  "default_profile": false,
  "is_translator": false
}
```
**COMMENT:** I followed 10 famous personalities and their relevant twitter details are printed in JSON format.

**Q2.3: Add the code to Twitter_2.py**
```
Name: Shabana Salmaan
Location: Barcelona, Spain
Friends: 2
Created: 2019-02-28 19:47:13
Description: Master student

The women told all last night, and Caelynn tells even more on my #Bachelor Recap show. #TheBachelor @ellentube https://t.co/8C19cB0riD
```
**COMMENT:** The output displayed is from Ellen where I re-tweeted in my account.

**Q2.4: How long have you been working on this session? What have been the main difficulties you have faced and how have you solved them?**

Along with lab hours, we worked on it for 3 hours. The difficulties we faced was mostly the intendation errors which is with the code formatting. We solved by following the standard Indent with 4 spaces format using notepad++ editor.

