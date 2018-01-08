# The Net Neutrality Debate on Twitter: Is Anyone Out There?

## Motivation

The recent debate about net neutrality has resulted in large public participation, both on Twitter and through filings with the FCC during
the open comment period. Many of the filings (at least 1.3 million out of 23 million total) were submitted by bots or from IP addresses in Russia, diluting the impact of real citizen filings (which were overwhelmingly in favor of keeping net neutrality). These filings used natural language generation to add “voices” speaking in favor of repealing net neutrality legislation. 

While there are undoubtedly misinformation campaigns on Twitter being promulgated by those with political motivations, recent analysis of political tweets has shown that many of these "non-human" accounts participating in the conversation on Twitter are not controlled by those motivated by politics, but likely something much more banal: [ad revenue](https://pushpullfork.com/fake-news-adtech-misinformation/). When there is a large conversation happening on Twitter, people controlling bot rings have learned that by coopting trending hashtags they can steer outbound traffic through URL shortener links that pay the show ads while redirecting and pay the creator per click.

The article linked above shows how this technique has been used to route users to what look like right-wing news sites by using hashtags usually associated with right-wing Twitter accounts. I hypothesize that a non-trivial part of the conversation on Twitter using #NetNeutrality was driven by this as well - clearly it works! Knowing how much of this discourse was real people sharing their opinions versus clever people using an emotional conversation to grab free money will be useful in the future for identifying fraudulent accounts and with the public's continued reckoning about Twitter's role in public discourse.

## General Plan

For my project, I plan to use the [twitterscraper scraping tool](https://github.com/taspinar/twitterscraper) I found on Github to collect tweets from 11/28 - 12/14 (the date of the Congressional net neutrality vote) using the hashtag #netneutrality. I will then extract the domain names of all URLs included in these tweets to look at the most commonly referenced sites and see what adtech links were used. I will then use natural language processing to see what the common phrases and words were for tweets providing no links, tweets providing non-adtech links, and tweets providing adtech links to see what patterns show up in the language of each group. I will plan to use Scikit-Learn's TfidfVectorizer to extract the most unique used words in each corpus by category. I will also be able to use SpaCy to do Named Entity Recognition on each category to see who/what they are speaking about.

This is a well-motivated question since social media platforms like Twitter are becoming the primary way many Americans consume news. With the growth of bots and increased coding literacy around the world, additional safeguards will need to be added to avoid or increase awareness about abuse by actors that are not sharing legitimate content. Without this, it will become impossible to tell to what degree public policy is being co-opted and influenced by profit-motivated actors tweeting misleading information or foreign agents with poltical motivations. 

In short, I want to know the following:

    1.  During the period under consideration, what percent of #netneutrality tweets were misdirecting users to adtech sites?
    2.  What were distinctive words or phrases used by each category of tweeter (those without links, those with legitimate links, those with adtech links)?
    3.  What percentage of tweets were actually original and what percentage were parts of campaigns?

## MOEs & MOPs

MOE

I will measure the effectiveness of my natural language processing system by its ability to pull distinctive words and phrases used by my different categories of accounts. If it is able to find differences in the phrases both classes are using, that will be an indicator of effectiveness. 

MOP

This model may require an AWS virtual machine instance. If it does, I will put all the scraped tweets into the virtual machine and then use it to run the necessary Scikit-Learn and SpaCy code. I will be dealing with a huge number of tweets and features, so I may not be able to do this on my personal computer.

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
