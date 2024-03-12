class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = [self.items[i:i + self.pageSize] for i in range(0, len(self.items), self.pageSize)]
        self.currentPage = self.totalPages[0]

    def getVisibleItems(self):
        return print(self.currentPage)

    def prevPage(self):
        current_index = self.totalPages.index(self.currentPage)
        if self.currentPage != self.totalPages[0]:
            self.currentPage = self.totalPages[current_index - 1]
        else:
            print("It is the first page")
        return self

    def nextPage(self):
        current_index = self.totalPages.index(self.currentPage)
        if self.currentPage != self.totalPages[-1]:
            self.currentPage = self.totalPages[current_index + 1]
        else:
            print("It is the last page")
        return self

    def lastPage(self):
        if self.currentPage != self.totalPages[-1]:
            self.currentPage = self.totalPages[-1]
        else:
            print("It is the last page")
        return self

    def firstPage(self):
        if self.currentPage != self.totalPages[0]:
            self.currentPage = self.totalPages[0]
        else:
            print("It is the first page")
        return self

    def go_to_page(self, page):
        if 0 < page < len(self.totalPages):
            self.currentPage = self.totalPages[page - 1]
        elif page > len(self.totalPages):
            self.currentPage = self.totalPages[-1]
        elif page < 0:
            self.currentPage = self.totalPages[0]
        elif page == 0:
            self.currentPage = self.totalPages[0]
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.getVisibleItems()
p.nextPage().nextPage().getVisibleItems()
p.lastPage().getVisibleItems()
p.lastPage()
p.prevPage().getVisibleItems()
p.firstPage().getVisibleItems()
p.go_to_page(3).getVisibleItems()
print("------")

alphabetList2 = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList2)
p.getVisibleItems()
p.nextPage().nextPage().getVisibleItems()
p.lastPage().getVisibleItems()
p.lastPage()
p.prevPage().getVisibleItems()
p.firstPage().getVisibleItems()
p.go_to_page(3).getVisibleItems()