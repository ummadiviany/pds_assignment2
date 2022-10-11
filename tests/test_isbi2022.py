# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-10-11 20:53:37
#  * @modify date 2022-10-11 20:53:37
#  * @desc [description]
#  */

import unittest
from json import load
from tasks.isbi2022 import get_authors, get_titles, get_word_cloud


class TestISBI2022(unittest.TestCase):
    authors = load(open('tests/isbi2022_outputs/get_authors.json', 'r', encoding='utf-8'))
    titles = load(open('tests/isbi2022_outputs/get_titles.json', 'r', encoding='utf-8'))
    word_cloud = load(open('tests/isbi2022_outputs/get_word_cloud.json', 'r', encoding='utf-8'))
    
    def test_len_get_authors(self):
        assert len(get_authors()) == len(self.authors)
        
    def test_content_get_authors(self):
        assert get_authors() == self.authors
        
    def test_len_get_titles(self):
        assert len(get_titles()) == len(self.titles)
        
    def test_content_get_titles(self):
        assert get_titles() == self.titles
        
    def test_len_get_word_cloud(self):
        assert len(get_word_cloud()) == len(self.word_cloud)
        
    def test_content_get_word_cloud(self):
        assert get_word_cloud() == self.word_cloud
        
        
if __name__ == "__main__":
    unittest.main()