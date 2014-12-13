import praw
r = praw.Reddit(user_agent='Image crawler by /u/leonlg')

number_of_images = 1000
subreddit = 'earthporn'

submissions = r.get_subreddit(subreddit).get_hot(limit=number_of_images)

stylesheet = open('style.css', 'w')
html = open('index.html', 'w')

content = "<html><head><title>test crawler</title><link rel='stylesheet' href='style.css'></head><body>"
style = "body, html { padding: 0; margin: 0; height: 100%; width: 100%; } .img { width: 100vw; height: 50vw; }"
j = 0
for x in submissions:
    if not x.is_self and x.url.endswith(".jpg") or x.url.endswith(".png"):
        style += ' #img%d { background: url(%s); }' % ( j, x.url )
        content += '<div id="img%d" class="img"></div>\n' % j
    j += 1

for k in range(number_of_images):
    style += '#img%d,' % k
style = style[:-1]
style += '{ background-size: cover; background-attachment: fixed; }'

content += "</body></html>"

html.write(content)
stylesheet.write(style)
html.close()
stylesheet.close()
