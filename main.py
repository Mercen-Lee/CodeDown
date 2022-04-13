from selenium import webdriver
problem = input()
driver = webdriver.Chrome(r'./chromedriver')
driver.get('https://codeup.kr/problem.php?id='+problem)
driver.get('https://www.google.com/search?q=코드업 '+driver.find_element_by_xpath('/html/body/main/div/h2').text)
for i in range(1,10):
    try:
        driver.find_element_by_xpath('//*[@id="rso"]/div['+str(i)+']/div/div[1]/div/a/h3').click()
        if 'return 0;' in driver.find_element_by_xpath("/html/body").text: break
        else: driver.back()
    except: pass
print('#include <stdio.h>\n    int main'+driver.find_element_by_xpath("/html/body").text.split('int main')[-1].split('return 0;')[0]+'return 0;\n}')
driver.quit()
