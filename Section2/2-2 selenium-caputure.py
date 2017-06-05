from selenium import webdriver

url = "http://j-lyric.net/artist/a0006b5/l00e6aa.html"

# PhantomJSのドライバを得る
browser = webdriver.PhantomJS()
# 暗黙的な待機を最大3秒。ドライバの初期化待ち
browser.implicitly_wait(3)
# URLの読み込み
browser.get(url)
# 画面キャプチャしてファイルに保存
browser.save_screenshot("Website.png")
# ブラウザ終了
browser.quit()