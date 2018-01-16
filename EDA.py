import itertools
import numpy as np
import pandas as pd
import re
import spacy
import string
from collections import Counter

def import_files():
    '''
    Pull in all of the json files, concat them into one nice dataframe.

    :return: Concatenated dataframe of all tweets.
    '''
    nov_28_df = pd.read_json('11-28.json')
    nov_29_df = pd.read_json('11-29.json')
    nov_30_df = pd.read_json('11-30 redo.json')
    nov_30_df_2 = pd.read_json('11-30_2.json')

    nov_30_concat = pd.concat([nov_30_df, nov_30_df_2], ignore_index=True)
    nov_30_concat = nov_30_concat.drop_duplicates()
    nov_30_concat_df = nov_30_concat.sort_values(by=['timestamp'])

    dec_1_df = pd.read_json('12-1.json')
    dec_2_df = pd.read_json('12-2.json')
    dec_3_df = pd.read_json('12-3.json')

    dec_4_df = pd.read_json('12-4 redo.json')
    dec_4_df_2 = pd.read_json('12-4_2.json')

    dec_4_concat = pd.concat([dec_4_df, dec_4_df_2], ignore_index=True)
    dec_4_concat = dec_4_concat.drop_duplicates()
    dec_4_concat_df = dec_4_concat.sort_values(by=['timestamp'])

    dec_5_df = pd.read_json('12-5.json')
    dec_6_df = pd.read_json('12-6.json')
    dec_7_df = pd.read_json('12-7.json')

    dec_8_df = pd.read_json('12-8.json')
    dec_8_df_2 = pd.read_json('12-8_2.json')

    dec_8_concat = pd.concat([dec_8_df, dec_8_df_2], ignore_index=True)
    dec_8_concat = dec_8_concat.drop_duplicates()
    dec_8_concat_df = dec_8_concat.sort_values(by=['timestamp'])

    dec_9_df = pd.read_json('12-9.json')
    dec_9_df_2 = pd.read_json('12-9_2.json')

    dec_9_concat = pd.concat([dec_9_df, dec_9_df_2], ignore_index=True)
    dec_9_concat = dec_9_concat.drop_duplicates()
    dec_9_concat_df = dec_9_concat.sort_values(by=['timestamp'])

    dec_10_df = pd.read_json('12-10.json')
    dec_11_df = pd.read_json('12-11.json')
    dec_12_df = pd.read_json('12-12.json')
    dec_13_df = pd.read_json('12-13.json')
    dec_14_df = pd.read_json('12-14.json')

    mega_df = pd.concat([nov_28_df, nov_29_df, nov_30_concat_df, dec_1_df, dec_2_df, dec_3_df, \
                         dec_4_concat_df, dec_5_df, dec_6_df, dec_7_df, dec_8_concat_df, dec_9_concat_df, \
                         dec_10_df, dec_11_df, dec_12_df, dec_13_df, dec_14_df], ignore_index=True)

    return mega_df

def get_hashtags(text):
    '''
    Function to be used in apply - returns properly formatted hashtags other than #netneutrality

    :param text: When used in apply functions, this is the column from the dataframe being passed in. In my case,
    it's the 'text' field.
    :return: Returns a list of list of hashtags meant to be passed in to the apply function to create the new column
    called 'other hashtags'.
    '''
    hashtags = []
    for t in text.lower().split():
        if (t.startswith("#")) & (t != '#netneutrality'):
            result = re.findall('#[\w_]+', t)
            for x in result:
                hashtags.append(x)
    return hashtags

def get_links(text):
    '''
    Function to be used in apply - returns links.

    :param text: When used in apply functions, this is the column from the dataframe being passed in. In my case,
    it's the 'text' field.
    :return: Returns a list of list of links meant to be passed in to the apply function to create the new column
    called 'links'.
    '''
    links = []
    for t in text.lower().split():
        if t.startswith("http"):
            links.append(t)
    return links

def get_mentions(text):
    '''
    Function to be used in apply - returns mentions of other users.

    :param text: When used in apply functions, this is the column from the dataframe being passed in. In my case,
    it's the 'text' field.
    :return: Returns a list of list of mentions meant to be passed in to the apply function to create the new column
    called '@s'.
    '''
    mentions = []
    for t in text.lower().split():
        if t.startswith("@"):
            if re.match("^[A-Za-z0-9_]+$", t[1:]):
                # t = re.sub(r'?', '', t)
                t = re.sub('http[\S]*', '', t)
                t = re.sub('pic.twitter[\S]*', '', t)
                t = re.sub(':', '', t)
                t = re.sub(',', '', t)
                t = re.sub('\.', '', t)
                t = re.sub("\'s", '', t)
                t = re.sub("!", '', t)
                mentions.append(t)
    return mentions

def clean_text(text):
    '''
    Function to be used in apply - returns properly formatted text.

    :param text: When used in apply functions, this is the column from the dataframe being passed in. In my case,
    it's the 'text' field.
    :return: Returns a string of cleaned text meant to be passed in to the apply function to create the new column
    called 'cleaned_text'.
    '''
    cleaned = re.sub('(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|(\w+:\/\/\S+)|(\\n)|(\\xa0)|([0-9])', '', text).lower()
    cleaned = re.sub((' +'), ' ', cleaned)
    cleaned = cleaned.replace('...', '')
    cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
    cleaned = cleaned.strip()
    return cleaned

def tweet_text_dict_fn(df):
    '''
    Create Counter that will tally up the number of times exact text appears in tweets in my data set. This helps
    identify guided information campaigns (tweets that were not original tweets by the author, but part of an
    organized activist effort).

    :param df: The dataframe to receive this treatment.
    :return: Counter dictionary with counts of all tweets in data set.
    '''
    tweet_text_dict = Counter()
    for item in df['cleaned_text']:
        tweet_text_dict[item] += 1
    return tweet_text_dict

def create_campaign_tweet_set(tweet_text_dict):
    '''
    Create set of those repeated tweets that showed up 100 or more times in the data. These are the ones I am
    classifying as large information campaigns.

    :param tweet_text_dict: The returned counter from the tweet_text_dict_fn function.
    :return: A set of text from tweets that were part of large campaigns.
    '''
    campaign_tweet_set = set()
    for k, v in tweet_text_dict.items():
        if v > 99:
            campaign_tweet_set.add(k)
    return campaign_tweet_set

def create_original_tweet_set(tweet_text_dict):
    '''
    Create set of tweets that only showed up 1 time in the data. These are the ones I am classifying as original
    tweets (not part of campaigns).

    :param tweet_text_dict: The returned counter from the tweet_text_dict_fn function.
    :return: A set of text from tweets that were original.
    '''
    orig_tweet_set = set()
    for k, v in tweet_text_dict.items():
        if v == 1:
            orig_tweet_set.add(k)
    return orig_tweet_set

# def info_campaign(text):
#     '''
#     To be used in an apply function that will create a binary classification for 'part of information campaign.'
#
#     :param text: When used in apply functions, this is the column from the dataframe being passed in. In my case,
#     it's the 'text' field.
#     :param campaign_tweet_set: The return from the create_campaign_tweet_set function.
#     :return: 1 or 0 to classify tweets as part of information campaigns or not.
#     '''
#     if text in campaign_tweet_set:
#         return 1
#     else:
#         return 0
#
# def original_tweet(text):
#     '''
#     To be used in an apply function that will create a binary classification for 'original tweet.'
#
#     :param text: When used in apply functions, this is the column from the dataframe being passed in. In my case,
#     it's the 'text' field.
#     :param orig_tweet_set: The return from the create_original_tweet_set function.
#     :return: 1 or 0 to classify tweets as original tweet or not.
#     '''
#     if text in orig_tweet_set:
#         return 1
#     else:
#         return 0

def negative_tweet_grab(other_hashtags):
    '''
    Function to be used in apply - labels tweets that appear to be pro-repeal of net neutrality using a list of
    hashtags that I identified as pro-repeal in the data.

    :param other_hashtags: When used in apply functions, this is the column from the dataframe being passed in. In my case,
    it's the 'other_hashtags' field.
    :return: 1 or 0 to classify tweets as having pro-repeal hashtags or not.
    '''
    hashtag_list = ['#notonetneutrality', '#nonetneutrality', '#maga', '#trumptrain', '#libtard', '#presidenttrump',\
                    '#presidentdonaldtrump', '#makeamericagreatagain', '#draintheswamp', '#deplorables', '#soros',\
                    '#tcot', '#tgdn', '#gabfam', '#sjw', '#RestoreInternetFreedom', '#RestoringInternetFreedomOrder',\
                    '#IdiotDems', '#obama']
    if len(other_hashtags) > 0:
        for hashtag in other_hashtags:
            if hashtag in hashtag_list:
                return 1
        else:
            return 0
    else:
        return 0

def remove_outliers(df, field):
    '''
    Removes outliers from the X values passed in that are > 3 standard deviations away from the mean.
    :param df: Dataframe to be manipulated.
    :param field: The column whose outliers you want removed.
    :return: Series of field values with outliers removed.
    '''
    series_outliers_removed = df[field][np.abs(df[field] - df[field].mean()) <= (3 * df[field].std())]
    return series_outliers_removed

def get_adj_lemmas(dataframe, spacy_model='en_core_web_sm', threads=3):
    '''
    WARNING: THIS WILL TAKE *FOREVER* AND POSSIBLY CRASH YOUR MACHINE IF IT'S A LARGE DATAFRAME
    (GREATER THAN 50,000 TWEETS)! CONSIDER SPLITTING YOUR DATAFRAME AND CONCATENATING LATER.

    Takes in a dataframe, a SpaCy model, and a number of threads and adds a column to the dataframe where every entry
    has all lemmatized adjectives from the tweet as a list.

    :param dataframe: Dataframe to get lemmatized adjective column.
    :param spacy_model: Which SpaCy model? Defaults to the small English one.
    :param threads: Number of threads to use when running this function.
    :return: Dataframe with the new 'adj_lemmas' column added.
    '''
    nlp = spacy.load(spacy_model)
    lemma = []
    for doc in nlp.pipe(dataframe['cleaned_text'].astype('unicode').values, batch_size=50,
                            n_threads=threads):
        if doc.is_parsed:
            lemma.append([n.lemma_ for n in doc if (n.pos_ == 'ADJ') & (n.lemma_ != '-PRON-')])
        else:
            # We want to make sure that the lists of parsed results have the
            # same number of entries of the original Dataframe, so add some blanks in case the parse fails
            lemma.append(None)

    dataframe['adj_lemmas'] = lemma
    return dataframe

def create_set_of_ats(df):
    '''
    A function to create a set of all users who are mentioned in tweets in the dataframe.

    :param df: Dataframe to create set from.
    :return: Set of all users mentioned in tweets in the param df.
    '''
    set_of_ats= set()

    for ats in df['@s']:
        if len(ats) > 0:
            for at in ats:
                set_of_ats.add(at)
    return set_of_ats

def combos_of_ats(df):
    '''
    Creates a list of all combinations of @s that appear in tweets in the data set.

    :param df: Dataframe containing column '@s' used to create combinations.
    :return: List of all pairs of @s found in data set.
    '''
    combo_list = []
    for ats in df['@s']:
        if (len(ats) > 1) & ('@' not in ats):
            combos = list(itertools.combinations(ats, 2))
            combo_list.append(combos)
    flat_list = [item for sublist in combo_list for item in sublist]
    return flat_list

def alpha_tuples(flat_list):
    '''
    Takes list of combos of @s, returns array where each pair is in alphabetical order.

    :param flat_list: Output of combo_of_ats function - every @ pair combination that appears in the data set.
    :return: Input list with each entry rearranged to be in alphabetical order.
    '''
    updated_flat_list = []
    for item_1, item_2 in flat_list:
        if item_1[1:] > item_2[1:]:
            # Put item_2 first
            updated_flat_list.append((item_2, item_1))
        else:
            # No change
            updated_flat_list.append((item_1, item_2))
    alpha_array = np.array(updated_flat_list)
    return alpha_array

def create_links_list(grouped_source_target_df, unique_ats):
    '''
    Reformat the list of all edges found in the data so that it refers to all nodes by index numbers.

    :param temp_links_list: The original version of this with strings instead of indexes.
    :param unique_ats: All of the unique mentions from the original data. Created by earlier function.
    :return: List of all edges.
    '''
    temp_links_list = list(grouped_source_target_df.apply(lambda row: {"source": row['source'], "target": row['target'],\
                                                                       "value": row['count']}, axis=1))
    links_list = []
    for link in temp_links_list:
        record = {"value":link['value'], "source":unique_ats.get_loc(link['source']),
         "target": unique_ats.get_loc(link['target'])}
        links_list.append(record)
    return links_list

def create_grouped_source_target(array_of_ats):
    '''
    Function to take an array of pairs of mentions and arrange them into a Dataframe with counts of every time a pair
    shows up.

    :param array_of_ats: Numpy array of pairs of mentions
    :return: Dataframe with every pair arranged into 'source' and 'target' columns. 'count' column shows number of times
    each pair appears in the data.
    '''
    d = {'source': array_of_ats[:, 0], 'target': array_of_ats[:, 1]}
    source_target_df = pd.DataFrame(data=d)
    grouped_source_target_df = source_target_df.groupby(['source', 'target']).size().reset_index()
    grouped_source_target_df.rename(columns={0: 'count'}, inplace=True)
    return grouped_source_target_df

def create_nodes_list(unique_ats):
    '''
    Create a list of nodes (all in the same group).

    :param unique_ats: All of the unique mentions from the original data. Created by earlier function.
    :return: List of all nodes.
    '''
    nodes_list = []
    for at in unique_ats:
        nodes_list.append({"name": at, "group": 1})
    return nodes_list