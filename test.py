# import requests

# url = "https://rr3---sn-u0g3uxax3-pnus.googlevideo.com/videoplayback?expire=1652375763&ei=c-x8YrnSGoH01wLjl6SYCQ&ip=78.183.45.158&id=o-AGVCJ_SBkQBTpyPm4JMcJLC-Lo9C2sLD6JuRMdgCHmER&itag=247&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C271%2C278%2C313&source=youtube&requiressl=yes&mh=VU&mm=31%2C29&mn=sn-u0g3uxax3-pnus%2Csn-h0jeenle&ms=au%2Crdu&mv=m&mvi=3&pl=21&initcwndbps=647500&spc=4ocVCwcjaUDACZvxkXP6RnwJ54qVGcAu70RkepGtyw&vprv=1&mime=video%2Fwebm&ns=HLjMCFL9y3KZOMU9jEGYBvYG&gir=yes&clen=84518762&dur=1182.199&lmt=1607454503396016&mt=1652353734&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=6316222&n=4GvAEXiV-tq3dA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIga7azqdXhGLdX17dDIcIoxUKRgxeAvVAvlv292H2ayHYCIFo5W9mOG03lLEmlJrjMxwSOCURNBjE3NlotBvqFx-pt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgIfqH2ELijj4fRcPmgpcXaffmVF6-gjYS-JvyBYCy2vUCIQC7JIM3J9dHxB6fJ5odJUDwRsoCiI2xKROtivipU-d4yA%3D%3D&alr=yes&cpn=k03NDFlZptUpW24V&cver=2.20220511.01.00&range=0-314139&rn=1&rbuf=0"

# r = requests.get(url, stream=True)

# with open("vio2.webm", "wb") as video:
#     for chunk in r.iter_content(chunk_size=1024):
#         if chunk:
#             video.write(chunk)

import m3u8
import requests
from bs4 import BeautifulSoup
# from tqdm import tqdm_notebook as tqdm
import subprocess
url = "https://www.youtube.com/watch?v=xJQBnrJXyv4&ab_channel=TrevorSullivan"
sess = requests.Session()
r = sess.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
video_id = soup.find('video', attrs={'id': 'playlistPlayer'})['data-video-id']
account_id = soup.find('video', attrs={'id': 'playlistPlayer'})['data-account']
url = "https://secure.brightcove.com/services/mobile/streaming/index/master.m3u8"

params = {
    'videoId': video_id,
    'pubId': account_id,
    'secure': True
}

r = sess.get(url, params=params)
m3u8_master = m3u8.loads(r.text)
m3u8_playlist_uris = [playlist['uri'] for playlist in m3u8_master.data['playlists']]
m3u8_master.data
# {'media_sequence': None,
#  'is_variant': True,
#  'is_endlist': False,
#  'is_i_frames_only': False,
#  'is_independent_segments': False,
#  'playlist_type': None,
#  'playlists': [{'uri': 'http://c.brightcove.com/services/mobile/streaming/index/rendition.m3u8?assetId=5790251759001&pubId=3588749423001&videoId=5790241186001',
#    'stream_info': {'program_id': 1,
#     'bandwidth': 514000,
#     'resolution': '480x270'}},
#   {'uri': 'http://c.brightcove.com/services/mobile/streaming/index/rendition.m3u8?assetId=5790251660001&pubId=3588749423001&videoId=5790241186001',
#    'stream_info': {'program_id': 1,
#     'bandwidth': 795000,
#     'resolution': '640x360'}},
#   {'uri': 'http://c.brightcove.com/services/mobile/streaming/index/rendition.m3u8?assetId=5790250742001&pubId=3588749423001&videoId=5790241186001',
#    'stream_info': {'program_id': 1,
#     'bandwidth': 997000,
#     'resolution': '640x360'}},
#   {'uri': 'http://c.brightcove.com/services/mobile/streaming/index/rendition.m3u8?assetId=5790247422001&pubId=3588749423001&videoId=5790241186001',
#    'stream_info': {'program_id': 1,
#     'bandwidth': 1297000,
#     'resolution': '960x540'}},
#   {'uri': 'http://c.brightcove.com/services/mobile/streaming/index/rendition.m3u8?assetId=5790247421001&pubId=3588749423001&videoId=5790241186001',
#    'stream_info': {'program_id': 1,
#     'bandwidth': 1828000,
#     'resolution': '960x540'}},
#   {'uri': 'http://c.brightcove.com/services/mobile/streaming/index/rendition.m3u8?assetId=5790251575001&pubId=3588749423001&videoId=5790241186001',
#    'stream_info': {'program_id': 1,
#     'bandwidth': 2134000,
#     'resolution': '1280x720'}}],
#  'segments': [],
#  'iframe_playlists': [],
#  'media': [],
#  'keys': []}
playlist_uri = m3u8_playlist_uris[0]
r = sess.get(playlist_uri)
playlist = m3u8.loads(r.text)
m3u8_segment_uris = [segment['uri'] for segment in playlist.data['segments']]
with open("video.ts", 'wb') as f:
    for segment_uri in m3u8_segment_uris:
        r = sess.get(segment_uri)
        f.write(r.content)
