import unittest
import sort
import os.path
import re
import requests

USER_AGENT = "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"

class TestCase(unittest.TestCase):

    def test_readme_exist(self):
        self.assertTrue(os.path.isfile('README.md'))

    def test_link_status_ok(self):
        with open('README.md', 'r', encoding='UTF-8') as read_me_file:
            for line in read_me_file:
                s_line = line.lstrip()
                if any([s_line.startswith(s) for s in ['|']]):
                    match = re.findall(r'(https?://[^)]+)', s_line)
                    if match:
                        try:
                            headers = {'user-agent': USER_AGENT}
                            r = requests.head(match[0], allow_redirects=False, headers=headers)
                            if r.status_code == 200:
                                print(match[0], '--> ok')
                        except requests.exceptions.Timeout as e:
                            print(match[0], ' --> ', e)
                        except requests.exceptions.TooManyRedirects as e:
                            print(match[0], ' --> ', e)
                        except requests.exceptions.RequestException as e:
                            print(match[0], ' --> ', e)
                                                    
                        self.assertTrue(requests.codes.ok)

if __name__ == '__main__':
    unittest.main()
