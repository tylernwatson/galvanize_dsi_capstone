# The Net Neutrality Debate on Twitter: Is There Anybody Out There?

Please clone or download this repo and run the EDA_notebook.ipynb file to follow along with the work I did.

[Interactive Network Graphs Available Here](http://18.221.173.186/)

## Motivation

The recent debate about net neutrality has resulted in large public participation, both on Twitter and through filings with the FCC during the open comment period. Of these filings, many were submitted as part of guided information campaigns - websites provided form paragraphs or links that allowed people to post without writing anything themselves. Many voices participated in the conversation on Twitter about net neutrality as well. Were these unique opinions held by individuals, or was this another example of information campaigns drowning out original thought? 

## Who Cares?

As Twitter becomes further entrenched as a medium for public discourse, knowing how to weigh opinions and identify their sources is vital. The most recent presidential election is a good example of how a high enough volume of content promoting certain views can drown out opposing views and influence real-world events. News outlets regularly go to Twitter now to identify and research breaking stories. Being able to identify what content is just being repeated versus stories that are developing organically is important for the continued existence of a free press that isn't easily steered by high-volume Twitter campaigns where participation takes no effort beyond clicking. 

I wanted to look at this phenomenon in the context of the net neutrality debate since it was recent and had high participation. Twitter voiced their support for maintaining net neutrality, which brought a lot of attention to the platform. Identifying which tweets are original and which are repetition, what type of language is used by both, and what networks were formed gives us a better understanding of the important background information users of Twitter need when weighing views. I collected tweets using the hashtag #NetNeutrality and used NLP and graph theory to:
* Determine differences in opinions shared in original tweets vs tweets that were parts of guided information campaigns
* Uncover communities formed by Twitter users during this conversation

My hypotheses are the following:

The majority of tweets using #NetNeutrality were part of guided information campaigns and therefore not unique views expressed by individuals.

Community detection will reveal that people were using this campaign as a mouthpiece to voice concern about the repeal of net neutrality to their elected officials more than to have a discussion about the issue.

## Approach & Findings

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/stack.png "Stack")
    
For my project, I used [this](https://github.com/taspinar/twitterscraper) Twitter scraper to collect tweets that used the hashtag #NetNeutrality from 11/28-12/14. Since the Twitter API restricts free developer access to tweets older than one week, I was not able to use their API for this part of the project. The tool above allowed me to get around this and collect historical tweets for this time period, but it did not include the metadata that the Twitter API provides.

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/original_data_sample.png "Sample of Original Data")

From here, I began extracting features and cleaning my raw text. I performed my data cleaning, feature engineering, and basic visualization using the standard Pandas and Matplotlib packages. By looking at the number of times the exact same text was showing up in multiple tweets, I was able to divide my data into original tweets and campaign tweets. There were a very small number of tweets I identified that were actually speaking against net neutrality - I excluded these from future analysis by using hashtags I found that were unique to them.

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/original_vs_campaign.png "Original vs Campaign Tweets")

I then wanted to take a look at the daily breakdown of tweets from each category. The graphic below shows a clear difference in volume for the two types grouped on 12/4-12/6 and 12/12-12/13. Since these were Tues-Thu and Tues-Wed, I suspect that this is reflective of the fact that people were taking breaks during the middle of the week at work. It is easy to imagine somebody checking Twitter for a few minutes, seeing that this issue is being discussed, realizing they have an opinion about it, and then noticing that they can easily follow a link and click a button on a website to participate in a campaign in a way that doesn't require much effort. The other significant burst in activity is on 12/2, a Saturday. I suspect that a campaign may have been launched that day - this is something I would like to look in to more.

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/tweets_by_day.png "Tweets by Day")
    
A look at the frequency distributions of replies and retweets to the different categories of tweets was also revealing. It's readily apparent from the visualization below that Twitter users were far more likely to engage with tweets that were original vs tweets that were parts of campaigns (even though they were not labeled as such when they were posted). The differences were stark:

Original Tweets With Replies: 13.8%
Campaign Tweets With Replies: 1.2%

Original Tweets With Retweets: 31.9%
Campaign Tweets With Retweets: 10.0%

This demonstrates that Twitter users have a clear idea whether they are looking at a tweet reflecting someone's original opinion or content from elsewhere that they are repeating. This is useful for organizations to keep in mind - if your goal is to raise awareness of an issue or product and get a lot of eyes on it, then a guided information campaign works. The volume of tweets has the potential to get much higher. On the other hand, in some situations an organization would prefer engagement and conversations over awareness. If this is the end goal, working with individuals that usually get lots of replies to spread your message would be preferable. 

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/replies_retweets.png "Replies and Retweets by Category")

After completing the above analysis and cleaning the raw text in my data so that it was possible to tokenize and parse it, I passed it through **SpaCy**'s part of speech tagger to identify adjectives. From this, I found that campaign tweets used the word "slow" far more than any other adjective. Original tweets, on the other hand, favored the word "free". Campaign tweets were focused on the downsides of eliminating net neutrality, namely that it would make certain sites slower. Original tweets emphasized the idea that the internet should be free, reflecting a difference in the messages that they wanted to spread.

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/word_usage.png "Most Common Adjectives by Category")

Following the part of speech tagging I began creating network graphs using the **NetworkX** package and **D3**. My graphs focus on users who were mentioned together in tweets. My motivation for this was a desire to see what communities were being created by Twitter users - what people were users associating, regardless of whether they have a stated connection between them? Knowing this helped me figure out how people were using Twitter during this period and who they were interacting with. As a next step towards this end, I used **Louvain modularity** to identify communities in the graph.

After creating my first graph, I saw that the FCC account and FCC Chairman Ajit Pai's account were showing up so frequently that they were pulling a large percentage of other nodes into their orbit and skewing the community detection. I then used **betweenness centrality** to confirm that those two nodes were the most central and iteratively remove them to reveal more informative communities. The link below will take you to a **Flask** web app running from an **AWS EC2** machine.

[Interactive Network Graphs](http://18.221.173.186/)

![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/images/network_graph_preview.png "Network Graph Preview")

Exploring those graphs results in a few findings - first of all, it looks like people were talking a lot about tech companies, news organizations, and elected officials. In particular, people spent a lot of time tweeting at Republicans (who were mostly supporting the repeal of net neutrality) and much less time tweeting at Democrats (who were supporting maintaining net neutrality). This is revealing of how people were using Twitter during this period - since the #netneutrality was blessed by Twitter as a way to support net neutrality, it's clear that people were using it much more as a way to express discontent and disapproval than as a way to express support for officals who were promoting the cause they supported. This was not the case with tech companies - many of the companies who showed up in the network graph had voiced support for keeping net neutrality. Why were they showing up linked to Verizon and Comcast, two companies who stand to benefit from the change in regulations? It seems that people were either confused about the actors on both sides of the issue and were tweeting incorrect information or were intentionally spreading misinformation in large enough volume to show up on the graphs.

## Conclusions

* People can tell when someone is not using their own language in their tweets and are much less likely to engage.
* In this case, the opinions expressed in information campaigns did not accurately mirror the sentiments of original tweets.
* When tweeting, people are more likely to voice discontent through mentions of other users than they are to voice support.

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
