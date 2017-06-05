from selenium import webdriver

# PhantomJSのドライバーを得る 
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# 適当なWebサイトを開く
browser.get("https://google.com")

# JavaScriptを実行
r = browser.execute_script("return 100 + 50")
print(r)