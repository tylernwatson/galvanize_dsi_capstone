# The Net Neutrality Debate on Twitter: Is There Anybody Out There?

## Motivation

The recent debate about net neutrality has resulted in large public participation, both on Twitter and through filings with the FCC during the open comment period. Many of the filings (at least 1.3 million out of 23 million total) were submitted by bots or from IP addresses in Russia, diluting the impact of real citizen filings (which were overwhelmingly in favor of keeping net neutrality). These filings used natural language generation to add “voices” speaking in favor of repealing net neutrality legislation. 

We all already know that online fora are becoming extremely important in public discourse. We also know that a significant amount of conversation online, especially during political events, comes from bots or individuals controlling multiple accounts. The most recent significant example of this was when the FCC website was open for public comment on net neutrality. Of the 23 million comments filed, only six percent were unique. Many of the others came from bots, with 475,000 comments submitted at the exact same second in one particularly flagrant instance. Outside of bots, many of the comments filed came from guided information campaigns such as form posts provided by websites. Since many of these require no more effort than simply clicking a button to repeat a view, they obey the letter of the law requiring public comment periods but not the spirit. 

I wanted to look at this phenomenon on Twitter. I collected tweets using the hashtag #NetNeutrality and used NLP and graph theory to:
* Determine differences in opinions shared in original tweets vs tweets that were parts of guided information campaigns
* Uncover communities formed by Twitter users during this conversation

My hypotheses are the following:

The majority of tweets using #NetNeutrality were part of guided information campaigns and therefore not unique views expressed by individuals. 

Community detection will reveal that people were using this campaign as a way to voice concern about the repeal of net neutrality to their elected officials more than to have a discussion about the issue.

This is a well-motivated question since Twitter is becoming a larger part of public political discourse every day. News outlets regularly go to Twitter now to identify and research breaking stories. Being able to identify what content is just being repeated versus stories that are actually significant is important for the continued existence of a free press that isn't easily steered by high-volume Twitter campaigns where participation takes no effort beyond clicking. My work in this project that looked at how users engaged with tweets from guided information campaigns versus original tweets should be important to any company that is considering running a twitter campaign - do you really want to spend the money on a campaign if people are just repeating the same thing and not acting? Is there a better way to spend those resources?

## Approach

    ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/stack.png "Stack")
    
For my project, I used [this](https://github.com/taspinar/twitterscraper) Twitter scraper to collect tweets that used the hashtag #NetNeutrality from 11/28-12/14. Since the Twitter API restricts free developer access to tweets older than one week, I was not able to use their API for this part of the project. The tool above allowed me to get around this and collect historical tweets for this time period.

I performed my data cleaning, feature engineering, and basic visualization using the standard Pandas and Matplotlib packages.

After cleaning the raw text in my data so that it was possible to tokenize and parse it, I passed it through SpaCy's part of speech tagger to identify adjectives.

For my network graphs, I used the NetworkX package and visualized using D3. I then created a web app using Flask and hosted it on an Amazon Web Services EC2 machine.



## MOEs & MOPs

MOE

I will measure the effectiveness of my natural language processing system by its ability to pull distinctive words and phrases used by human and bot twitter accounts. If it is able to find differences in the phrases both classes are using, that will be an indicator of effectiveness. 

MOP

This model will require an AWS virtual machine instance. I will put all the scraped tweets into the virtual machine and then use it to run the Botometer and get my TF-IDF vectors. The remaining NLP will happen this way as well. I will be dealing with a huge number of tweets and features, so I won't be able to do this on my personal computer.

## Data Pipelining

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/Images/flowchart.png "Pipeline")


## Further Work

In the future, I would like to use other statistical analysis and machine learning techniques to identify accounts that are likely bots that are participating in these campaigns. This is also a huge issue that Twitter and the public need to decide how to address.

An opportunity for future work that is possible with the data I have would be to slice my data into shorter time period and identify people who are being mentioned more frequently than their average frequency of appearance over the entire time period would suggest. I could then make community maps of just these users. This would allow me to see what communities are being formed in the data at more specific times. My end goal with this would be to use it on live data from the Twitter Streaming API to detect news stories before they break based on who is showing up all of a sudden. Using other features such as location, followers, etc. would make this more robust.

## Related Projects/Articles

[The ISIS Twitter Census: Defining and describing the population of ISIS supporters on Twitter](https://www.brookings.edu/wp-content/uploads/2016/06/isis_twitter_census_berger_morgan.pdf)
[More than a Million Pro-Repeal Net Neutrality Comments were Likely Faked](https://hackernoon.com/more-than-a-million-pro-repeal-net-neutrality-comments-were-likely-faked-e9f0e3ed36a6)
[Building a realtime Twitter sentiment dashboard with Firebase and NLP](https://codeburst.io/building-a-realtime-twitter-sentiment-dashboard-with-firebase-and-nlp-7064bb30f5ab_)
[Comparing tweets about Trump & Hillary with natural language processing](https://medium.com/google-cloud/comparing-tweets-about-trump-hillary-with-natural-language-processing-a0064e949666)

## Relevant Links
[FCC Must Investigate Fraud Before Voting on Net Neutrality](https://www.wired.com/story/fcc-must-investigate-fraud-before-voting-on-net-neutrality/)
[How Bots Broke the FCC's Public Comment System](https://www.wired.com/story/bots-broke-fcc-public-comment-system/)
[Public Comments to the Federal Communications Commission About Net Neutrality Contain Many Inaccuracies and Duplicates](http://www.pewinternet.org/2017/11/29/public-comments-to-the-federal-communications-commission-about-net-neutrality-contain-many-inaccuracies-and-duplicates/)
[Reply All Episode 112 - The Prophet](https://gimletmedia.com/episode/112-the-prophet/)
