table = driver.find_element(by="xpath", value="//table[@id='webtable']")
# row_count = len(table.find_elements(By.TAG_NAME, value="tr"))
row_count = len(table.find_elements(By.TAG_NAME, "tr"))
assert row_count == 5, "Row count did not match"
print("Row count", row_count)
col_count = len(driver.find_elements(By.XPATH, "//table[@id='webtable']//th"))
assert col_count == 3, "Column count did not match"
print("Col count", col_count)
head_values = driver.find_elements(By.XPATH, "//table[@id='webtable']//th")
for cell in head_values:
    print("%25s" %cell.text, end=" ")
for row in table.find_elements(By.TAG_NAME, "tr"):
    for cell in row.find_elements(By.TAG_NAME, "td"):
        print("%25s" %cell.text, end=" ")
    print()
