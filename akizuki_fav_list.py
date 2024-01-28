#!/usr/bin/env python3
# akizuki_fav_list.py
#   秋月電子さんの「お気に入り」内容をtsvファイル化する（2024/01/26リニューアル対応）
#   「ウェブページ、htmlのみ」で保存した00.html〜99.htmlから抽出
#   by @pado3@mstdn.jp
#   r1.0 2024/01/28 initial release
#   r1.1 2024/01/28 単ファイル読み込み後closeし忘れていたのを修正
#
import os
import re
from bs4 import BeautifulSoup


# 保存してあるファイル名を取得
def get_files(path: str):
    # matchさせる部分ファイル名のパターン。00.html~99.html
    ptn = re.compile(r"[0-9][0-9].html")
    files = [file for file in os.listdir(path) if ptn.match(file)]
    return sorted(files)


# soupからアイテム名のリストを取得する
def get_names(s_soup: BeautifulSoup):
    tmp_soup = s_soup.find_all(class_="js-enhanced-ecommerce-goods-name")
    tmp = [t.text.replace('\n', '').replace('\t', '') for t in tmp_soup]
    return tmp


# soupから販売単位のリストを取得する
def get_qtys(s_soup: BeautifulSoup):
    tmp_soup = s_soup.find_all(class_="block-favorite--sales_qty")
    tmp = [t.text.replace('\n', '').replace('\t', '') for t in tmp_soup]
    return tmp


# soupから販売単価のリストを取得する
def get_prices(s_soup: BeautifulSoup):
    tmp_soup = s_soup.find_all(class_="price")
    tmp = [t.text.replace('\n', '').replace('\t', '').
           replace('￥', '').replace(',', '') for t in tmp_soup]
    return tmp


# soupから税抜単価のリストを取得する
def get_nets(s_soup: BeautifulSoup):
    tmp_soup = s_soup.find_all(class_="net-price")
    tmp = [t.text.replace('\n', '').replace('\t', '').
           replace('税抜 ￥', '').replace(',', '') for t in tmp_soup]
    return tmp


# soupからメモのリストを取得する
def get_memos(s_soup: BeautifulSoup):
    tmp_soup = s_soup.find_all(class_="block-favorite--comment-message")
    tmp = [t.text.replace('\n', '').replace('\t', '') for t in tmp_soup]
    return tmp


# soupから商品リンクのリストを取得する
def get_hrefs(s_soup: BeautifulSoup):
    tmp_soup = s_soup.find_all(class_="js-enhanced-ecommerce-goods-name")
    srv = 'https://akizukidenshi.com/'
    tmp = [srv + t.get('href') for t in tmp_soup]
    return tmp


''' テンプレ
# soupから〜のリストを取得する
def get_s(s_soup: BeautifulSoup):
    tmp_soup = s_soup.find_all(class_="〜")
    tmp = [t.text for t in tmp_soup]
    return tmp
'''


# 単ファイルを読み込み、【品名、販売単位、販売価格、税抜価格、メモ、リンク】のリストを出力
def single_soup(file: str):
    s = open(file, 'r')
    s_soup = BeautifulSoup(s, "html.parser")
    s.close()
    # soupから各項目のリストを取得
    n = get_names(s_soup)
    q = get_qtys(s_soup)
    p = get_prices(s_soup)
    z = get_nets(s_soup)    # 税抜
    m = get_memos(s_soup)
    h = get_hrefs(s_soup)
    ''' テンプレ
     = get_s(s_soup)
    '''
    # 各項目のリストをアイテムごとにまとめる
    s_list = [[n[i], q[i], p[i], z[i], m[i], h[i]] for i in range(len(n))]
    return s_list


# 結果の出力
def save_result(lists: list, outfile: str):
    if os.path.exists(outfile):
        os.remove(outfile)
    with open(outfile, mode='w', encoding="utf-8") as f:
        for items in lists:
            for cell in items:
                f.write("{}\t".format(cell))
            f.write('\n')
    '''
    # コンソールへの出力
    for items in lists:
        for cell in items:
            print("{}\t".format(cell), end="")
        print()
    '''


# メイン
def akizuki_fav_list():
    path = './'     # htmlファイルのパス、このスクリプトと同じフォルダに置く
    outfile = 'fav.tsv'
    # 結果リストをタイトル行で初期化（2重リストなのはアイテム毎にリスト化するため）
    lists = [['品名', '販売単位', '販売価格', '税抜価格', 'メモ', 'リンク']]
    # 00〜99.htmlのファイル名リスト
    files = get_files(path)
    # ファイル毎にアイテムリストを得て結果リストにまとめる
    for file in files:
        s_list = single_soup(file)
        lists += s_list
    # 結果をoutfileに書き込む
    save_result(lists, outfile)
    print("終了しました")


# お約束
if __name__ == "__main__":
    akizuki_fav_list()
