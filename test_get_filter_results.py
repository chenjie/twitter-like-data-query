import unittest
import twitterverse_functions as tf


class TestGetFilterResults(unittest.TestCase):
    '''unittests'''
#-------------------------------name_includes-----------------------------------
    def test_name_includes_empty_list(self):
        """ Test get_filter_results with a query of name-includes and an 
        empty list of list_of_usernames """
        
        twitter_dict = {'a':{'name':'aapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'bapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'capple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = []
        filter_dict = {'name-includes': 'apple'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected)

    def test_name_includes_one(self):
        """ Test get_filter_results with a query of name-includes and a 
        twitter_dict and list_of_usernames of length 1 """
        
        twitter_dict = {'a':{'name':'aapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a']
        filter_dict = {'name-includes': 'apple'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_name_includes_lower(self):
        """ Test get_filter_results with a query of name-includes with all 
        lower case letters """
        
        twitter_dict = {'a':{'name':'aApplE', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'BaPple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'Cap.pLe', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'name-includes': 'apple'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b']
        self.assertEqual(actual, expected) 
        
    def test_name_includes_upper(self):
        """ Test get_filter_results with a query of name-includes with all 
        upper case letters """
        
        twitter_dict = {'a':{'name':'aApplE', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'BaP.ple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'CappLe', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'name-includes': 'APPLE'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'c']
        self.assertEqual(actual, expected) 

    def test_name_includes_mixed(self):
        """ Test get_filter_results with a query of name-includes with mixed 
        lower case and upper case letters """
        
        twitter_dict = {'a':{'name':'aApplE', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'BaPple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'CappLe', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'name-includes': 'ApPlE'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b', 'c']
        self.assertEqual(actual, expected)
    
    def test_name_includes_normal(self):
        """ Test get_filter_results with a normal query of name-includes """
        
        twitter_dict = {'a':{'name':'aapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'babpple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'capple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'name-includes': 'apple'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'c']
        self.assertEqual(actual, expected)    
    
    def test_name_includes_best_case(self):
        """ Test get_filter_results with the best query of name-includes, 
        which means that the result list is exactly the same as 
        list_of_usernames """
        
        twitter_dict = {'a':{'name':'aapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'bapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'capple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'name-includes': 'apple'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b', 'c']
        self.assertEqual(actual, expected)    
    
    def test_name_includes_worst_case(self):
        """ Test get_filter_results with the worst query of name-includes, 
        which means that the result list is an empty list """
        
        twitter_dict = {'a':{'name':'aapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'babpple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'capple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'name-includes': 'vpple'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected)     
    
    def test_name_includes_mutation(self):
        """ Confirm that get_filter_results with a query of name-includes 
        does not mutate the list it's given."""
        
        twitter_dict = {'a':{'name':'aapple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'b':{'name':'babpple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'capple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'name-includes': 'apple'}
        tf.get_filter_results(twitter_dict, list_of_usernames, filter_dict)
        
        twitter_dict_expected = {'a':{'name':'aapple', 'location':'', 'web':'',\
                             'bio':'', 'following':[]}, \
                        'b':{'name':'babpple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'capple', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames_expected = ['a', 'b', 'c']
        filter_dict_expected = {'name-includes': 'apple'}
        
        self.assertEqual(twitter_dict, twitter_dict_expected)
        self.assertEqual(list_of_usernames, list_of_usernames_expected)
        self.assertEqual(filter_dict, filter_dict_expected)

#---------------------------location_includes-----------------------------------
    def test_location_includes_empty_list(self):
        """ Test get_filter_results with a query of location-includes and an 
        empty list of list_of_usernames """
        
        twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = []
        filter_dict = {'location-includes': 'apple'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected)
        
    def test_location_includes_one(self):
        """ Test get_filter_results with a query of location_includes and a 
        twitter_dict and list_of_usernames of length 1 """
        
        twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a']
        filter_dict = {'location-includes': 'UsA'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a']
        self.assertEqual(actual, expected)        

    def test_location_includes_upper(self):
        """ Test get_filter_results with a query of location-includes with all 
        upper case letters """
        
        twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'location-includes': 'USA'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b', 'c']
        self.assertEqual(actual, expected)
        
    def test_location_includes_lower(self):
        """ Test get_filter_results with a query of location-includes with all 
        lower case letters """
        
        twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'location-includes': 'usa'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b', 'c']
        self.assertEqual(actual, expected)        
        
    def test_location_includes_mixed(self):
        """ Test get_filter_results with a query of location-includes with mixed 
        upper case and lower case letters """
        
        twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'location-includes': 'UsA'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b', 'c']
        self.assertEqual(actual, expected)        
        
    def test_location_includes_best_case(self):
        """ Test get_filter_results with the best query of location-includes, 
        which means that the result list is exactly the same as 
        list_of_usernames """
        
        twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'location-includes': 'USA'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b', 'c']
        self.assertEqual(actual, expected)        
        
    def test_location_includes_worst_case(self):
        """ Test get_filter_results with the worst query of location-includes, 
        which means that the result list is an empty list """
        
        twitter_dict = {'a':{'name':'', 'location':'Modesto, California, USA', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'location-includes': 'China'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected)        
        
    def test_location_includes_normal(self):
        """ Test get_filter_results with normal query of location-includes """
        
        twitter_dict = {'a':{'name':'', 'location':'China', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'location-includes': 'USA'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['b', 'c']
        self.assertEqual(actual, expected)        
    
    def test_location_includes_mutation(self):
        """ Confirm that get_filter_results with a query of location_includes 
        does not mutate the list it's given."""
        
        twitter_dict = {'a':{'name':'', 'location':'China', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'location-includes': 'USA'}
        tf.get_filter_results(twitter_dict, list_of_usernames, filter_dict)
        
        twitter_dict_expected = {'a':{'name':'', 'location':'China', \
                             'web':'', 'bio':'', 'following':[]}, \
                        'b':{'name':'', 'location':'kansas, uSa', 'web':'', \
                             'bio':'', 'following':[]}, \
                        'c':{'name':'', 'location':'Musala, Bulgaria', \
                             'web':'', 'bio':'', 'following':[]}}
        list_of_usernames_expected = ['a', 'b', 'c']
        filter_dict_expected = {'location-includes': 'USA'}
        
        self.assertEqual(twitter_dict, twitter_dict_expected)
        self.assertEqual(list_of_usernames, list_of_usernames_expected)
        self.assertEqual(filter_dict, filter_dict_expected)
        
#---------------------------------follower--------------------------------------
    def test_follower_empty_list(self):
        """ Test get_filter_results with a query of follower and an 
        empty list of list_of_usernames """
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'b']}}
        list_of_usernames = []
        filter_dict = {'follower': 'a'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected)

    def test_follower_best_case(self):
        """ Test get_filter_results with the best query of follower, 
        which means that the result list includes the maximum elements """
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'b']}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'follower': 'a'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['b', 'c']
        self.assertEqual(actual, expected)

    def test_follower_worst_case(self):
        """ Test get_filter_results with the worst query of follower, 
        which means that the result list is an empty list """      
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a']}}
        list_of_usernames = ['b', 'c']
        filter_dict = {'follower': 'b'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected)

    def test_follower_normal_case(self):
        """ Test get_filter_results with normal query of follower """
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a']}}
        list_of_usernames = ['a', 'b']
        filter_dict = {'follower': 'b'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a']
        self.assertEqual(actual, expected)      

    def test_follower_mutation(self):
        """ Confirm that get_filter_results with a query of follower 
        does not mutate the list it's given."""
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a']}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'follower': 'b'}
        tf.get_filter_results(twitter_dict, list_of_usernames, filter_dict)
        
        twitter_dict_expected = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b', 'c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a', 'c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['a']}}
        list_of_usernames_expected = ['a', 'b', 'c']
        filter_dict_expected = {'follower': 'b'}
        
        self.assertEqual(twitter_dict, twitter_dict_expected)
        self.assertEqual(list_of_usernames, list_of_usernames_expected)
        self.assertEqual(filter_dict, filter_dict_expected)

#------------------------------following----------------------------------------        
    def test_following_empty_list(self):
        """ Test get_filter_results with a query of following and an 
        empty list of list_of_usernames """
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = []
        filter_dict = {'following': 'c'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected) 
        
    def test_following_best_case(self):
        """ Test get_filter_results with the best query of following, 
        which means that the result list includes the maximum elements """
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'following': 'c'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['a', 'b']
        self.assertEqual(actual, expected)
    
    def test_following_worst_case(self):
        """ Test get_filter_results with the worst query of following, 
        which means that the result list is an empty list """
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'following': 'b'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = []
        self.assertEqual(actual, expected)
    
    def test_following_normal_case(self):
        """ Test get_filter_results with normal query of following """
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'following': 'c'}
        actual = tf.get_filter_results(twitter_dict, \
                                       list_of_usernames, filter_dict)
        expected = ['b']
        self.assertEqual(actual, expected)
        
    def test_following_mutation(self):
        """ Confirm that get_filter_results with a query of following 
        does not mutate the list it's given."""
        
        twitter_dict = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames = ['a', 'b', 'c']
        filter_dict = {'following': 'c'}
        tf.get_filter_results(twitter_dict, list_of_usernames, filter_dict)
        
        twitter_dict_expected = {'a':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['b']}, \
                        'b':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':['c']}, \
                        'c':{'name':'', 'location':'', 'web':'', \
                             'bio':'', 'following':[]}}
        list_of_usernames_expected = ['a', 'b', 'c']
        filter_dict_expected = {'following': 'c'}
        
        self.assertEqual(twitter_dict, twitter_dict_expected)
        self.assertEqual(list_of_usernames, list_of_usernames_expected)
        self.assertEqual(filter_dict, filter_dict_expected)        

#-------------------------------------------------------------------------------
    
if __name__ == '__main__':
    unittest.main(exit=False)
