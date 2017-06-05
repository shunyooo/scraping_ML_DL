# coding: utf-8
from selenium import webdriver

ID = "****"
PASS = "****"

# PhantomJSのドライバーを得る
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# トップページにアクセス
url_top = "https://oh-o2.meiji.ac.jp/portal/index"
browser.get(url_top)
print("トップページにアクセスしました")

# ログインページにアクセス
e = browser.find_element_by_css_selector(".login a")
print("ログインページ > ",e.get_attribute('href'))
e.click()
print("遷移後ログインページ > ",browser.current_url)

# id,passの入力
# テキストボックスに文字を入力
e = browser.find_element_by_name("ACCOUNTUID")
e.clear()
e.send_keys(ID)
e = browser.find_element_by_name("PASSWORD")
e.clear()
e.send_keys(PASS)

# フォームを送信
frm = browser.find_element_by_css_selector(".form_container form")
frm.submit()
print("情報を入力してログインボタンを押しました")

#browser.save_screenshot("Meiji.png")

# 時間割ページ
classweb_url = "https://oh-o2.meiji.ac.jp/portal/oh-o_meiji/classweb"
browser.get(classweb_url)
print("classwebにアクセスしました")

browser.save_screenshot("classweb.png")

nendo = browser.find_element_by_css_selector("#targetNendo > option").text
beginTerm = browser.find_element_by_css_selector("#beginTerm > option").text

table = browser.find_element_by_css_selector("#classwebStudentForm .calenderLayout > table")

# ヘッダー(時限と曜日)
ths = table.find_elements_by_css_selector("tr .heading > th")
headerList = [th.text for th in ths]

# 科目名
classTitleList = []
trs = table.find_elements_by_css_selector("tr .classTitle")
for tr in trs:# 科目名のみ。
	ths = tr.find_elements_by_css_selector("th")
	tds = tr.find_elements_by_css_selector("td")

	# 時限と科目名
	classTitleHeader = tr.find_element_by_css_selector("th").text
	classTitles = [td.text for td in tds]
	classTitleList.append([classTitleHeader,classTitles])

browser.quit()

print(headerList)
print(classTitleList)


output_str = """時間割:{0} {1}\n""".format(nendo,beginTerm)
for c in classTitleList:
	class_time = c[0]
	class_titles = c[1]
	for i,title in enumerate(class_titles):
		if title != ' ':
			output_str += "{}曜 {} {}\n".format(headerList[i+1],class_time,title)

with open('classweb.txt', 'w') as f:
	f.write(output_str)



