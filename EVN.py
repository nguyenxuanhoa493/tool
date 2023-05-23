import requests

url = "https://elearning-api.evn.com.vn/user/login"


payload = {'lname': 'evn',
'pass': 'vieted@2022@123',
'submit': '1',
'_sand_ajax': '1',
'_sand_platform': '3',
'_sand_readmin': '1',
'_sand_is_wan': 'false',
'_sand_ga_sessionToken': '',
'_sand_ga_browserToken': '',
'_sand_domain': 've',
'_sand_masked': ''}

{'lname': 'evn', 
 'pass': 'vieted@2022@123', 
 'submit': '1', 
 '_sand_ajax': '1', 
 '_sand_platform': '3', 
 '_sand_readmin': '1', 
 '_sand_is_wan': 'false', 
 '_sand_ga_sessionToken': '', 
 '_sand_ga_browserToken': '', 
 '_sand_domain': 've', 
 '_sand_masked': ''}

headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
  'Connection': 'keep-alive',
  'Origin': 'https://elearning.evn.com.vn',
  'Referer': 'https://elearning.evn.com.vn/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

HEADER2 = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.request("POST", url, headers=HEADER2, data=payload, verify=False)

print(response.text)
