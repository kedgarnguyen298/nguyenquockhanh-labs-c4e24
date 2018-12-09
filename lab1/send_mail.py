# Send a mail
from gmail import GMail, Message
from random import randint

sickness_list = ["thương hàn", "kiết lị", "tiêu chảy"]
#1 Randomly a sickness
n = randint(0, len(sickness_list) - 1)
sickness = sickness_list[n]

html_template = '''
<p>Anh Huy ơi,</p>
<p>H&ocirc;m nay em bị {{sickness}}, anh cho em nghỉ nh&aacute; :&lt;</p>
<p><span style="color: #ff0000;">Y&ecirc;u anh&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></span></p>
'''
#2 sickness + html_template => html_content
# hint: String replace
html_content = html_template.replace("{{sickness}}", sickness)

gmail = GMail("kedgarnguyen2981", "kedgarlovejun")
msg = Message("Test", to = "C4e.techkidsvn@gmail.com", html = html_content)
gmail.send(msg)
