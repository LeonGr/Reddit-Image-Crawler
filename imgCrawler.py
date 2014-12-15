import praw
import urllib
r = praw.Reddit(user_agent='Image crawler by /u/leonlg v1.0.2')

""" Choose number of posts and what subreddit here """
number_of_images = raw_input("How many images do you want? ")
subreddit = raw_input("What subreddit do you want to crawl? ")
download = raw_input("Do you want to download these images? (y/n) ")

submissions = r.get_subreddit(subreddit).get_hot(limit=int(number_of_images))

""" Open files where to put images """
stylesheet = open('style.css', 'w')
html = open('index.html', 'w')

content = "<html><head><title>test crawler</title><link rel='stylesheet' href='style.css'></head><body>"
style = "body, html { padding: 0; margin: 0; height: 100%; width: 100%; } .img { width: 100vw; height: 50vw; }"

for i, sub in enumerate(submissions):
    if not sub.is_self and sub.url.endswith(".jpg") or sub.url.endswith(".png"):
        style += ' #img%d { background: url(%s); }' % ( i, sub.url )
        content += '<div id="img%d" class="img"></div>\n' % i
        if download == "y":
            f = urllib.urlopen(sub.url)
            with open("images/img%d" % i, "wb") as imgFile:
                imgFile.write(f.read())
            f.close()

for k in range(int(number_of_images)):
    style += '#img%d,' % k
style = style[:-1]
style += '{ background-size: cover; background-attachment: fixed; }'

content += "</body></html>"

html.write(content)
stylesheet.write(style)
html.close()
stylesheet.close()

print("Process finished, open index.html")
