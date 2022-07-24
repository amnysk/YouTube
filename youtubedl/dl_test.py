
import youtube_dl
import yt_dlp

import subprocess

download_path = './movie/'
opt ={  'format': 'best',
        'writethumbnail': True,                         #サムネイルを取得
        'outtmpl': download_path+'%(title)s.%(ext)s',   #downloadするフォルダを指定
        'writeinfojson': True,                          #infoをjsonファイルに書き込む
        
        'writeautosub':True,                            #
        'subtitle': '--write-sub --sub-lang ja',
        'writecomments' : True ,
        'writesub' : True

}

sub_opt ={
    'sublang':'ja',
    'writeautosub':True,
    'skipdownload':True
}


#ydl = youtube_dl.YoutubeDL(opt)
ydl = yt_dlp.YoutubeDL(opt)
info = ydl.extract_info("https://www.youtube.com/watch?v=hm2IpFMyB44")

print(info['id'])
print(info['title'])

id = info['id']
title =info['title']

args = ['youtube-comment-downloader','-y',id,'-o',download_path + 'comment_' +title + '.json']


res = subprocess.check_call(args)
#yt = yt_dlp.YoutubeDL(sub_opt)
#info2 = yt.extract_info("https://www.youtube.com/watch?v=hm2IpFMyB44")