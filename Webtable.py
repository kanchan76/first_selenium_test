# 1. http://the-internet.herokuapp.com/tables -
#      Example 2 - Delete the row containing jdoe in Email Column.
# For doing this assignment create a utility class having the following methods
# - get_row_count()
# - get_column_count()
# - get_data_rows()
# - delete_a_row(colum_name, column_value) # delete_a_row("Email", "jdoe@hotmail.com")
# - edit_a_row(colum_name, column_value)
from selenium.common.exceptions import UnexpectedTagNameException
from selenium import webdriver
from first_selenium_test.Webtable import WebtableOptimized

class WebtableOptimized:

    def __init__(self,webtable):
        if webtable.tag_name.lower() != "table":
            raise UnexpectedTagNameException(
                " Unexpected tagname <%s>" %
                webtable.tag_name)
        self.table = webtable

    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr"))-1

    def get_column_count(self):
        row = self.get_data_rows()[0]
        columns = row.find_elements_by_tag_name("td")
        return len(columns)

    def get_data_rows(self):
        all_rows = self.table.find_elements_by_tag_name("tr")
        noofrows = len(self.table.find_elements_by_tag_name("tr"))
        return all_rows[1:noofrows]

    def get_data_rows(self):
        all_rows = self.table.find_elements_by_tag_name("tr")
        noofrows = len(self.table.find_elements_by_tag_name("tr"))
        return all_rows[1:noofrows]

    def searchrow(self,columnvalue):
        self.columnvalue=columnvalue
        rowdata = self.get_data_rows()
        for row in rowdata:
            for column in row.find_elements_by_tag_name("td"):
                if columnvalue in column.text:
                    return row

    def delete_a_row(self,colum_name, column_value):
        self.columnname =colum_name
        self.columnvalue = column_value
        deleterow = self.searchrow(self.columnvalue)
        deleterow.find_element_by_link_text("delete")

    def edit_a_row(self,colum_name, column_value):
        self.columnname =colum_name
        self.columnvalue = column_value
        editrow = self.searchrow(self.columnvalue)
        editrow.find_element_by_link_text("edit")










