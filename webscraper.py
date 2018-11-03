import unittest
from selenium import webdriver
import requests
import lxml.html as LH
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import pymssql
import time

conn = pymssql.connect("localhost", "SA", "sql@23456789", "TestDB")
cursor = conn.cursor()
dict_univ = {}
f = open("web.txt", "a")
class PythonOrgSearch(unittest.TestCase):
	def setUp(self):
		options = Options()
		options.add_argument("--headless")
		self.driver = webdriver.Firefox(options=options)

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://web3.ncaa.org/directory/memberList?type=12&division=I")
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div[2]/div/div[1]/div[1]/div/label/select").send_keys(100)
		time.sleep(2)
		#/html/body/div[1]/div/div[2]/section/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/a
		while True:
			try:
				for i in range(1,101):
					elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div[2]/div/div[2]/div/table/tbody/tr["+str(i)+"]/td[1]/a")
					root = LH.fromstring(requests.get(elem.get_attribute('href')).text)
					name = elem.text
					address = " ".join(root.xpath('//address')[0].text_content().replace('\n', "").split())
					new_address = address.split(" ")
					zipcode = new_address[-1]
					state = new_address[-2]
					website = ""
					for i in root.xpath('//a'):
						s = i.text_content().split(".")[-1].rstrip()
						if s  == "edu" or s == "edu/":
							website = i.text_content().rstrip()
							break
					dict_univ[name] = name+" "+address+" "+state+" "+zipcode+" "+website
					print(dict_univ[name])
					cursor.execute("INSERT INTO UNIVDATA VALUES (%s, %s, %s, %s, %s)",(name,address,state,zipcode,website))
					conn.commit()
				driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div[2]/div/div[3]/div[2]/div/ul/li[6]/a").click()

			except NoSuchElementException as e:
				#print(e)
				break

		for key,val in dict_univ.items():
			#print(val)
			f.write(val+"\n")
		f.close()
		conn.close()
		assert "No results found." not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()