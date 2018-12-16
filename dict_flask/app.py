from flask import Flask, request, render_template
import dict_craw
# import requests
# import re
# from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['DEBUG'] = True


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        data = request.form['data']
        url_addr, flag = dict_craw.build_url(data)
        if flag == 1:
            p_data = dict_craw.EN_CH(url_addr)
            # print(p_data)
        else:
            p_data = dict_craw.CH_EN(url_addr)
            print(p_data)
        return render_template('process.html', p_list=p_data)


if __name__ == '__main__':
    app.run()
