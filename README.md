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

## Data Pipelining



## Related Projects/Articles

[More than a Million Pro-Repeal Net Neutrality Comments were Likely Faked](https://hackernoon.com/more-than-a-million-pro-repeal-net-neutrality-comments-were-likely-faked-e9f0e3ed36a6)
[Building a realtime Twitter sentiment dashboard with Firebase and NLP](https://codeburst.io/building-a-realtime-twitter-sentiment-dashboard-with-firebase-and-nlp-7064bb30f5ab_
[Comparing tweets about Trump & Hillary with natural language processing](https://medium.com/google-cloud/comparing-tweets-about-trump-hillary-with-natural-language-processing-a0064e949666)

## Further Work

## Anticipated Hurdles

Some challenges I expect:

    1.  Botometer is a good classifier, but not infallible. Some of these tweets may be miscategorized.
    2.  Of the tweets classed as bots, some may be organizational pages (which often get classed this way). I will need to decide if I want to include these or find a way to partition them out.
    3.  Certain words and phrases are likely to be repeated by both classes and it may be necessary to exclude these from analysis.
    
## Scope

## Data

## Relevant Links
[FCC Must Investigate Fraud Before Voting on Net Neutrality](https://www.wired.com/story/fcc-must-investigate-fraud-before-voting-on-net-neutrality/)
[How Bots Broke the FCC's Public Comment System](https://www.wired.com/story/bots-broke-fcc-public-comment-system/)
[Public Comments to the Federal Communications Commission About Net Neutrality Contain Many Inaccuracies and Duplicates](http://www.pewinternet.org/2017/11/29/public-comments-to-the-federal-communications-commission-about-net-neutrality-contain-many-inaccuracies-and-duplicates/)
[Reply All Episode 112 - The Prophet](https://gimletmedia.com/episode/112-the-prophet/)
[Twitter API](https://developer.twitter.com/)
[Botometer API](https://botometer.iuni.iu.edu/#!/api)
