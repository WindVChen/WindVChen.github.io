if __name__ == '__main__':
    base_dir = '../_pages/includes/'
    _intro = open(f'{base_dir}/intro.md').read().strip()
    _homepage = open(f'{base_dir}/homepage.md').read().strip()
    _news_full = open(f'{base_dir}/news.md').read().strip()
    # Extract only the news content before the collapsible section
    _news = _news_full.split('<div class="container">')[0].strip()
    _news += '\n- ... (*For more news, please see personal page.*)'
    with open('README.md', 'w') as f:
        f.write(_intro)
        f.write('\n\n##')
        f.write(_homepage)
        f.write('\n\n##')
        f.write(_news)