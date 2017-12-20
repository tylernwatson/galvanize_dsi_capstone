# The Net Neutrality Debate on Twitter: Bot vs Bot

## Motivation

The recent debate about net neutrality has resulted in large public participation, both on Twitter and through filings with the FCC during the open comment period. Many of the filings (at least 1.3 million out of 23 million total) were submitted by bots or from IP addresses in Russia, diluting the impact of real citizen filings (which were overwhelmingly in favor of keeping net neutrality). These filings used natural language generation to add “voices” speaking in favor of repealing net neutrality legislation. 

I hypothesize that a large part of the conversation on Twitter was driven by bots as well. Knowing how much of this discourse was real people versus bots repeating opinions or intentionally creating noise to distract will lead to a greater understanding of the role Twitter plays in public life and what steps can be taken to hinder bot networks and fraudulent accounts.

## General Plan

For my project, I plan to use the Twitter API and scraping tools I have found on Github to collect tweets from 11/14 - 12/14 (the date of the Congressional net neutrality vote) using the hashtag #netneutrality. I will then use the Botometer API to categorize these twitter accounts into human and bot. The counts of these categories will be informative on their own. I will then use natural language processing to see what the common phrases and words were for each of these four categories and determine what percentage of tweets in both categories were duplicates or likely machine-generated. Knowing how much of this converstion which could potentially help in future efforts to combat bots. 

This is a well-motivated question since public comment on FCC and other administrative organization actions has always been required. With the growth of bots and increased coding literacy around the world, additional safeguards will need to be added or the current public comment system will need to change. Without this, it will become impossible to tell to what degree public policy is being co-opted and influenced by domestic bad actors or foreign agents. 

In short, I want to know the following:

    1.  During the month under consideration, what percent of #netneutrality tweets were made by humans vs bots?
    2.  How many bot tweets were duplicates? Human tweets?
    3.  What were distinctive words or phrases used by bots?

## MOEs & MOPs

MOE

I will measure the effectiveness of my natural language processing system by its ability to pull distinctive words and phrases used by human and bot twitter accounts. If it is able to find differences in the phrases both classes are using, that will be an indicator of effectiveness. 

MOP

This model will require an AWS virtual machine instance. I will put all the scraped tweets into the virtual machine and then use it to run the Botometer and get my TF-IDF vectors. The remaining NLP will happen this way as well. I will be dealing with a huge number of tweets and features, so I won't be able to do this on my personal computer.

## Data Pipelining

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/Images/flowchart.png "Pipeline")

## Related Projects/Articles

[The ISIS Twitter Census: Defining and describing the population of ISIS supporters on Twitter](https://www.brookings.edu/wp-content/uploads/2016/06/isis_twitter_census_berger_morgan.pdf)
[More than a Million Pro-Repeal Net Neutrality Comments were Likely Faked](https://hackernoon.com/more-than-a-million-pro-repeal-net-neutrality-comments-were-likely-faked-e9f0e3ed36a6)
[Building a realtime Twitter sentiment dashboard with Firebase and NLP](https://codeburst.io/building-a-realtime-twitter-sentiment-dashboard-with-firebase-and-nlp-7064bb30f5ab_)
[Comparing tweets about Trump & Hillary with natural language processing](https://medium.com/google-cloud/comparing-tweets-about-trump-hillary-with-natural-language-processing-a0064e949666)

## Further Work

It would be informative to further classify tweets into pro-net neutrality and pro-repeal, and see if bots came from mostly one side. Research into comments filed during the FCC public comment period show that the vast majority of human comments were pro-net neutrality and the majority of pro-repeal comments were made by bots. I imagine this would be the same breakdown for tweets. This is beyond the scope of this project.

Obviously, futher research into the people behind the bots would be revealing. This is a job for an investigative journalist.

It would also be interesting to use geolocations and place tweets for and against net neutrality on a map. Finding this information given the sparse metadata in the tweets scraped would be non-trivial.

## Anticipated Hurdles

Some challenges I expect:

    1.  Botometer is a good classifier, but not infallible. Some of these tweets may be miscategorized.
    2.  Of the tweets classed as bots, some may be organizational pages (which often get classed this way). I will need to decide if I want to include these or find a way to partition them out.
    3.  Certain words and phrases are likely to be repeated by both classes and it may be necessary to exclude these from analysis.
    
## Data
The below is a sample of scraped tweets.

   ![alt text](https://github.com/tylernwatson/galvanize_dsi_capstone/blob/master/Images/data_preview.png "More to come")

## Relevant Links
[FCC Must Investigate Fraud Before Voting on Net Neutrality](https://www.wired.com/story/fcc-must-investigate-fraud-before-voting-on-net-neutrality/)
[How Bots Broke the FCC's Public Comment System](https://www.wired.com/story/bots-broke-fcc-public-comment-system/)
[Public Comments to the Federal Communications Commission About Net Neutrality Contain Many Inaccuracies and Duplicates](http://www.pewinternet.org/2017/11/29/public-comments-to-the-federal-communications-commission-about-net-neutrality-contain-many-inaccuracies-and-duplicates/)
[Reply All Episode 112 - The Prophet](https://gimletmedia.com/episode/112-the-prophet/)
[Twitter API](https://developer.twitter.com/)
[Botometer API](https://botometer.iuni.iu.edu/#!/api)
