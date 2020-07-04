from selenium import webdriver
from selenium.common.exceptions import UnexpectedTagNameException


class WebTable_Optimized:
    def __init__(self, webtable):
        if webtable.tag_name.lower() != "table":
            raise UnexpectedTagNameException(
                "Select only works on <select> elements, not on <%s>" %
                webtable.tag_name)
        self.table = webtable

    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr"))

    def get_rows(self):  # 3 elements
        return self.table.find_elements_by_tag_name("tr")

    def get_data_rows(self):  # 2 elements
        all_rows = self.table.find_elements_by_tag_name("tr")
        noOfRows = len(all_rows)
        return all_rows[1:noOfRows]

    def get_column_count(self):
        all_rows = self.table.find_elements_by_tag_name('tr')
        all_columns = all_rows[1].find_elements_by_tag_name("td")
        return len(all_columns)

    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}

    # w.row_data(2)
    def row_data(self, row_number):  # 2
        if row_number == 0:
            raise Exception("Row number starts from 1")

        selected_row = self.get_data_rows()[row_number - 1]
        all_columns = selected_row.find_elements_by_tag_name("td")
        rData = []
        for webElement in all_columns:
            rData.append(webElement.text)

        return rData

    def column_data(self, column_number):
        all_data_rows = self.get_data_rows()
        #        all_columns = all_data_rows.find_elements_by_xpath("//td["+str(column_number)+"]")
        rData = []
        for webElement in all_data_rows:
            selected_column = webElement.find_element_by_xpath(".//td[" + str(column_number) + "]")
            rData.append(selected_column.text)
        return rData

    def get_all_data(self):
        # get number of rows
        noOfRows = len(self.table.find_elements_by_xpath("//tr")) - 1
        # get number of columns
        noOfColumns = len(self.table.find_elements_by_xpath("//tr[2]/td"))
        allData = []
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(2, noOfRows):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, noOfColumns):
                # get text from the i th row and j th column
                ro.append(self.table.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text)

            # add the row data to allData of the self.table
            allData.append(ro)

        return allData

    def presence_of_data(self, data):

        # verify the data by getting the size of the element matches based on the text/data passed
        dataSize = len(self.table.find_elements_by_xpath("//td[normalize-space(text())='" + data + "']"))
        presence = False
        if dataSize > 0:
            presence = True
        return presence

    def get_cell_data(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")

        row_number = row_number + 1
        cellData = self.table.find_element_by_xpath("//tr[" + str(row_number) + "]/td[" + str(column_number) + "]").text
        return cellData

    def select_cell_element(self, row_number, column_number):
        if row_number == 0:
            raise Exception("Row number starts from 1")

        row_number = row_number + 1
        cellData = self.table.find_element_by_xpath("//tr[" + str(row_number) + "]/td[" + str(column_number) + "]")
        return cellData



