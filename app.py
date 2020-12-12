from flask import Flask, render_template, request, redirect
from collections import OrderedDict
import string

app = Flask(__name__)

#base url
BASE_URL = 'http://localhost:5000/'

# chars for hashing
charset = [str(i) for i in range(10)]
charset.extend(i for i in string.ascii_uppercase)
charset.extend(i for i in string.ascii_lowercase)

# storing shortened urls
urls = OrderedDict()
# def loadurls():
#     global urls
#     try:
#         with open("urls.txt") as f:
#             for line in f:
#                 (key, val) = line.split()
#                 urls[key] = val
#     except:
#         return "<h1>Error</h1>"

# get next string for storing url recursively
def increment(url, index):
    if index<0:
        return url
    char = charset.index(url[index])+1
    if char == len(charset):
        url[index] = charset[0]
        return increment(url, index-1)
    else:
        url[index] = charset[char]
        return url

# hash function for urls
def furyoku(url):
    last = next(reversed(urls))
    shamanlist = [i for i in last]
    return ''.join(increment(shamanlist, len(shamanlist)-1))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = request.form['url']
        short = furyoku(url)
        if not url in urls.values():
            print('NEW')
            urls[short] = url
            # with open("urls.txt",'a') as f:
            #     f.write(short+' '+url+'\n')
        for k,v in urls.items():
            if v == url:
                return render_template('index.html', url = BASE_URL + k)

@app.route('/<string:url_id>')
def goto(url_id):
    if urls.get(url_id):
        return redirect(urls.get(url_id))
    else:
        return render_template('index.html', error = "Bruh it's 404, add it first")

if __name__ == '__main__':
    # loadurls()
    app.run(port=8000)
