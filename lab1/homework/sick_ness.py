from gmail import GMail, Message
from random import randint
from datetime import datetime

sickness = ["Viêm họng", "Đau bụng", "Gãy chân"]
n = randint(0, len(sickness) - 1)

html_template = '''
<p>Anh Huy ơi,</p>
<p>H&ocirc;m nay em bị {{sickness}}, anh cho em nghỉ nh&aacute; :&lt;</p>
<p><span style="color: #ff0000;">Y&ecirc;u anh&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></span></p>
'''

html_content = html_template.replace("{{sickness}}", sickness[n])

gmail = GMail("kedgarnguyen2981", "kedgarlovejun")
msg = Message("Xin nghỉ ốm", to = "C4e.techkidsvn@gmail.com", html = html_content )

current_hour = datetime.now().hour

while True:
    if current_hour > 7:
        gmail.send(msg)
        break
    else:
        pass
