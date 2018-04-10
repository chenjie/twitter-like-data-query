"""
Type descriptions of Twitterverse and Query dictionaries
(for use in docstrings)

Twitterverse dictionary:  dict of {str: dict of {str: object}}
    - each key is a username (a str)
    - each value is a dict of {str: object} with items as follows:
        - key "name", value represents a user's name (a str)
        - key "location", value represents a user's location (a str)
        - key "web", value represents a user's website (a str)
        - key "bio", value represents a user's bio (a str)
        - key "following", value represents all the usernames of users this 
          user is following (a list of str)
       
Query dictionary: dict of {str: dict of {str: object}}
   - key "search", value represents a search specification dictionary
   - key "filter", value represents a filter specification dictionary
   - key "present", value represents a presentation specification dictionary

Search specification dictionary: dict of {str: object}
   - key "username", value represents the username to begin search at (a str)
   - key "operations", value represents the operations to perform (a list of str)

Filter specification dictionary: dict of {str: str}
   - key "following" might exist, value represents a username (a str)
   - key "follower" might exist, value represents a username (a str)
   - key "name-includes" might exist, value represents a str to match (a case-insensitive match)
   - key "location-includes" might exist, value represents a str to match (a case-insensitive match)

Presentation specification dictionary: dict of {str: str}
   - key "sort-by", value represents how to sort results (a str)
   - key "format", value represents how to format results (a str)
       
"""

# Write your Twitterverse functions here

def process_data(file):
    """ (file open for reading) -> Twitterverse dictionary
    
    Return the data of file in the Twitterverse dictionary format. 
    
    """
    
    # Initialize the twitter_dict.
    twitter_dict = {}
    
    next_part = file.readline().strip()
    while next_part != '':
        # Generate the key: 'name', 'location', 'web' and their values 
        # in the username dictionary.
        username = next_part
        twitter_dict[username] = {}
        twitter_dict[username]['name'] = file.readline().strip()
        twitter_dict[username]['location'] = file.readline().strip()
        twitter_dict[username]['web'] = file.readline().strip()
        
        # Generate the key: 'bio' and its value in the username dictionary.
        line = file.readline()
        bio = ''
        while line != 'ENDBIO\n':
            bio += line
            line = file.readline()
        twitter_dict[username]['bio'] = bio.strip()
        
        # Generate the key: 'following' and its value in the username dictionary.
        twitter_dict[username]['following'] = []
        following = file.readline().strip()
        while following != 'END':
            twitter_dict[username]['following'].append(following)
            following = file.readline().strip()
        
        next_part = file.readline().strip()
    
    return twitter_dict


def process_query(file):
    """ (file open for reading) -> query dictionary
    
    Return the query of file in the query dictionary format. 
    
    """
    
    # Initialize the query_dict.
    query_dict = {}
    line = file.readline().strip()
    
    # Generate the key: 'search' and its value in the query_dict.
    query_dict['search'] = {}
    query_dict['search']['username'] = file.readline().strip()
    query_dict['search']['operations'] = []
    operations = file.readline().strip()
    while operations != 'FILTER':
        query_dict['search']['operations'].append(operations)
        operations = file.readline().strip()
    
    # Generate the key: 'filter' and its value in the query_dict.
    query_dict['filter'] = {}
    line = file.readline().strip()
    while line != 'PRESENT':
        a = line.split()
        query_dict['filter'][a[0]] = a[1]
        line = file.readline().strip()
    
    # Generate the key: 'present' and its value in the query_dict.
    query_dict['present'] = {}
    line = file.readline().strip()
    while line != '':
        b = line.split()
        query_dict['present'][b[0]] = b[1]
        line = file.readline().strip()
    
    return query_dict


def all_followers(twitter_dict, username):
    """ (Twitterverse dictionary, str) -> list of str
    
    Return all the usernames that are following the username as a list based 
    on the twitter_dict.
    
    >>> twitter_dict1 = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b']}}
    >>> all_followers(twitter_dict1, 'a')
    ['b']
    
    >>> twitter_dict2 = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a']}}
    >>> all_followers(twitter_dict2, 'b')
    []
    """
    
    result = []
    for i in twitter_dict:
        if username in twitter_dict[i]['following']:
            result.append(i)
    return result



def get_search_results(twitter_dict, search_dict):
    """ (Twitterverse dictionary, search specification dictionary) -> list of str
    
    Return a list of strings representing usernames that match the search 
    criteria in the search_dict based on twitter_dict.
    
    >>> twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b']}}
    >>> search_dict1 = {'operations': ['following'], 'username': 'a'}
    >>> get_search_results(twitter_dict, search_dict1)
    ['b', 'c']
    >>> search_dict2 = {'operations': ['followers'], 'username': 'a'}
    >>> get_search_results(twitter_dict, search_dict2)
    []
    """
    
    # Check if the operations list is empty.
    if search_dict['operations'] == []:
        return [search_dict['username']]
    
    else:
        # Generate the first result.
        if search_dict['operations'][0] == 'following':
            result = twitter_dict[search_dict['username']]['following']
        elif search_dict['operations'][0] == 'followers':
            result = all_followers(twitter_dict, search_dict['username'])
            
        # Use for loop to generate the final result autometically based 
        # on the first result.
        if len(search_dict['operations']) > 1:
            for operation in search_dict['operations'][1:]:
                sub_result = []
                for item in result:
                    if operation == 'following':
                        part = twitter_dict[item]['following']
                    elif operation == 'followers':
                        part = all_followers(twitter_dict, item)
                    sub_result += part
                
                # Delet the repeated items.
                result = []
                for i in sub_result:
                    if not(i in result):
                        result.append(i)
        return result
    
    

def get_filter_results(twitter_dict, list_of_usernames, filter_dict):
    """ (Twitterverse dictionary, list of str, filter specification dictionary) -> list of str
    
    Apply the filter_dict to the given username list based on twitter_dict to 
    determine which usernames in the list_of_usernames to keep, and return the 
    resulting list of usernames.
    
    >>> twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
    >>> list_of_usernames1 = []
    >>> filter_dict1 = {'location-includes': 'apple'}
    >>> get_filter_results(twitter_dict, list_of_usernames1, filter_dict1)
    []
    >>> list_of_usernames2 = ['a', 'b', 'c']
    >>> filter_dict2 = {'location-includes': 'UsA'}
    >>> get_filter_results(twitter_dict, list_of_usernames2, filter_dict2)
    ['a', 'b', 'c']
    """
    
    # The list_of_usernames can't be modified, so I created copies. 
    result = list_of_usernames.copy()
    mod_usernames = result.copy()
    for operation in filter_dict:
        
        # To remove every username that doesn't satisfy the condition.
        for username in result:
            if operation == 'name-includes':
                if not(filter_dict[operation].lower() in \
                       twitter_dict[username]['name'].lower()):
                    mod_usernames.remove(username)
        
            elif operation == 'location-includes':
                if not(filter_dict[operation].lower() in \
                       twitter_dict[username]['location'].lower()):
                    mod_usernames.remove(username)
            
            elif operation == 'follower':
                if not(username in twitter_dict[filter_dict[operation]]['following']):
                    mod_usernames.remove(username)
            
            elif operation == 'following':
                if not(filter_dict[operation] in twitter_dict[username]['following']):
                    mod_usernames.remove(username)
            
        result = mod_usernames.copy()
    
    return result
    
    
    
def get_present_string(twitter_dict, list_of_usernames, pre_dict):
    """ (Twitterverse dictionary, list of str, presentation specification dictionary) -> str
    
    Format the results of list_of_usernames for presentation based on 
    pre_dict according to twitter_dict and return the formatted string. 
    
    >>> twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b']}}
    >>> list_of_usernames1 = ['a', 'b', 'c']
    >>> pre_dict1 = {'sort-by': 'username', 'format': 'short'}
    >>> get_present_string(twitter_dict, list_of_usernames1, pre_dict1)
    "['a', 'b', 'c']"
    >>> list_of_usernames2 = []
    >>> pre_dict2 = {'sort-by': 'popularity', 'format': 'long'}
    >>> get_present_string(twitter_dict, list_of_usernames2, pre_dict2)
    '----------\\n----------\\n'
    """
    
    # The list_of_usernames can't be modified, so I created copies. 
    mod_list_of_usernames = list_of_usernames.copy()
    
    # Creat a function dictionary, so we can call it easily.
    word_to_funcs = {'popularity': more_popular, 'username': \
                     username_first, 'name': name_first}
    
    # Before we present it, let's sort it by using the Sorting Helper Functions.
    tweet_sort(twitter_dict, mod_list_of_usernames, \
               word_to_funcs[pre_dict['sort-by']])
    
    # Present the format.
    if pre_dict['format'] == 'long':
        flag = 0
        result = '----------\n'  
        # If the for loop is not executed, then print another line of dashes.
        for i in mod_list_of_usernames:
            flag += 1
            result += str(i) + '\n'
            result += 'name: ' + str(twitter_dict[i]['name']) + '\n'
            result += 'location: ' + str(twitter_dict[i]['location']) + '\n'
            result += 'website: ' + str(twitter_dict[i]['web']) + '\n'
            result += 'bio:\n'
            result += str(twitter_dict[i]['bio']) + '\n'
            result += 'following: ' + str(twitter_dict[i]['following']) + '\n'
            result += '----------\n'
        if flag == 0:
            result += '----------\n'
        return result
            
    elif pre_dict['format'] == 'short':
        return str(mod_list_of_usernames)
   
# --- Sorting Helper Functions ---
def tweet_sort(twitter_data, results, cmp):
    """ (Twitterverse dictionary, list of str, function) -> NoneType
    
    Sort the results list using the comparison function cmp and the data in 
    twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['c', 'a', 'b']
    >>> tweet_sort(twitter_data, result_list, username_first)
    >>> result_list
    ['a', 'b', 'c']
    >>> tweet_sort(twitter_data, result_list, name_first)
    >>> result_list
    ['b', 'a', 'c']
    """
    
    # Insertion sort
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and cmp(twitter_data, results[position - 1], current) > 0:
            results[position] = results[position - 1]
            position = position - 1 
        results[position] = current  
            
def more_popular(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return -1 if user a has more followers than user b, 1 if fewer followers, 
    and the result of sorting by username if they have the same, based on the 
    data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> more_popular(twitter_data, 'a', 'b')
    1
    >>> more_popular(twitter_data, 'a', 'c')
    -1
    """
    
    a_popularity = len(all_followers(twitter_data, a)) 
    b_popularity = len(all_followers(twitter_data, b))
    if a_popularity > b_popularity:
        return -1
    if a_popularity < b_popularity:
        return 1
    return username_first(twitter_data, a, b)
    
def username_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return 1 if user a has a username that comes after user b's username 
    alphabetically, -1 if user a's username comes before user b's username, 
    and 0 if a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> username_first(twitter_data, 'c', 'b')
    1
    >>> username_first(twitter_data, 'a', 'b')
    -1
    """
    
    if a < b:
        return -1
    if a > b:
        return 1
    return 0

def name_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
        
    Return 1 if user a's name comes after user b's name alphabetically, 
    -1 if user a's name comes before user b's name, and the ordering of their
    usernames if there is a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> name_first(twitter_data, 'c', 'b')
    1
    >>> name_first(twitter_data, 'b', 'a')
    -1
    """
    
    a_name = twitter_data[a]["name"]
    b_name = twitter_data[b]["name"]
    if a_name < b_name:
        return -1
    if a_name > b_name:
        return 1
    return username_first(twitter_data, a, b)       


if __name__ == '__main__':
    import doctest
    doctest.testmod()