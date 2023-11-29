import unittest
import sys
sys.path.append("..")

from src.loader import SlackDataLoader


data_loader =  SlackDataLoader

slack_data = data_loader.slack_parser('../data/all-week1/')


class SlackDataTest(unittest.TestCase):
    expected_columns = ['msg_type', 'msg_content', 'sender_name', 'msg_sent_time',
               'msg_dist_type', 'time_thread_start', 'reply_count',
               'reply_users_count', 'reply_users', 'tm_thread_end', 'channel']
    
    def test_columns_equal(self):
        self.assertEqual(list(slack_data.columns), self.expected_columns)

if __name__ == '__main__':
    unittest.main()
