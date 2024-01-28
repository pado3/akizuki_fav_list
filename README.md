# akizuki_fav_list
秋月電子の「お気に入り」をリスト化するPythonスクリプト

2024年1月26日に、いつもお世話になっている<a href="https://akizukidenshi.com/" target="_blank" rel="noopener">秋月電子通商さんの通販サイト</a>がリニューアルされました。リニューアル内容は<a href="https://forest.watch.impress.co.jp/docs/serial/yajiuma/1564071.html" target="_blank" rel="noopener">窓の杜の記事に詳しい</a>のですが、ざっと回った限り見やすくなっていて歓迎です。<br />
ただ、上記の記事にもあるように若干不便になったと感じるところもあり、私の場合その最たる物が「マイページ ＞ お気に入り」です。従来は全件が1ページにまとまっていて、ブラウザのページ内検索で簡単に内容へアクセスできていたのですが、デフォルトでは20件ごとに分割されていて探しにくくなりました。そこで、スクレイピングしてリストを作ることを考えました。<br />
<hr>
使い方は次の通り：<br />
0. <a href="https://www.python.org/" target="_blank" rel="noopener">Python3</a>と<a href="https://pypi.org/project/beautifulsoup4/" target="_blank" rel="noopener">beautifulsoup4</a>が必要です。それぞれ公式のインストール手順に従って下さい。web上にチュートリアルはたくさんあります。<br />
1. <a href="https://akizukidenshi.com/catalog/customer/bookmark.aspx?ps=50" target="_blank" rel="noopener">自分のお気に入りページ</a>を開きます。ここでURLの末尾に「?ps=50」と入れると表示が50件になります。（左記リンクで開けば入ります。）<br />
2. ローカルにhtml形式で保存します。Chromeだと「ファイル ＞ ページを別名で保存…」で、形式を「ウェブページ、HTMLのみ」として、ファイル名を「01.html」として下さい。スクリプトでは「【2ケタの数字】.html」しか受け付けません。<br />
3. 「→」を押して2ページ目を表示し、ファイル名を「02.html」として保存。これを最後のページまで繰り返します。<br />
4. Pythonスクリプト「akizuki_fav_list.py」と同じフォルダにダウンロードしたhtmlファイルをおいて下さい。<br />
5. Pythonスクリプトを実行すると、同じフォルダに「fav.tsv」というタブ区切りテキストファイルが出力されます。スクリプトに引数はありません。
<p></p>
なお、tsvにしたのは品名やメモにカンマが入る場合があると思ったからです。抽出している内容は「品名, 販売単位, 販売価格, 税抜価格, メモ, リンク」で、増減したければスクリプトを変更して下さい。<br />
内容はブログにもまとめていますので、ご参考まで：<br />
https://pado.tea-nifty.com/top/2024/01/post-a10813.html
