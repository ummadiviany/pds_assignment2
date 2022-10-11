# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-10-11 20:53:37
#  * @modify date 2022-10-11 20:53:37
#  * @desc [description]
#  */


import unittest
from tasks.recursive_text_search import get_emails_recursive
    

class TestRecursiveTextSearch(unittest.TestCase):
    
    emails = get_emails_recursive()
    def test_len(self):
        self.assertEqual(len(self.emails), 14)
    def test_type(self):
        self.assertIsInstance(self.emails, list)
    def test_content(self):
        self.assertEqual(self.emails, ['AMARMAJHI@KGPIAN.IITKGP.AC.IN', 'BHANUMEENA27@KGPIAN.IITKGP.AC.IN', 'DR.RAMKUMARKRISHNADHAS@KGPIAN.IITKGP.AC.IN', 'DRPRABHUKALYAN@KGPIAN.IITKGP.AC.IN', 'DRREFLEXPATEL94@KGPIAN.IITKGP.AC.IN', 'KAMLESHTONY10@KGPIAN.IITKGP.AC.IN', 'KAVINPURI@KGPIAN.IITKGP.AC.IN', 'MAMTA.RANI@KGPIAN.IITKGP.AC.IN', 'NAJAFARA.FATHIMA@KGPIAN.IITKGP.AC.IN', 'POOJA.JAIN@KGPIAN.IITKGP.AC.IN', 'SATHISHBT@KGPIAN.IITKGP.AC.IN', 'SAURABHCHAUDHARI97@KGPIAN.IITKGP.AC.IN', 'SOUMITAGURIAPHD22@KGPIAN.IITKGP.AC.IN', 'samriddha.das2000@kgpian.iitkgp.ac.in'])
    
    
        
if __name__ == "__main__":
    unittest.main()