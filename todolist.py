from cgitb import text
from itertools import tee
from PyQt5 import QtCore, QtGui, QtWidgets
import database as db


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add_item = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.add_item())
        self.Add_item.setGeometry(QtCore.QRect(10, 80, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Add_item.setFont(font)
        self.Add_item.setObjectName("Add_item")
        self.Delete_item = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.delete_item())
        self.Delete_item.setGeometry(QtCore.QRect(110, 80, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Delete_item.setFont(font)
        self.Delete_item.setObjectName("Delete_item")
        self.AddToListInput = QtWidgets.QLineEdit(self.centralwidget)
        self.AddToListInput.setGeometry(QtCore.QRect(10, 10, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddToListInput.setFont(font)
        self.AddToListInput.setObjectName("AddToListInput")
        self.Clear_item = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.clear_item())
        self.Clear_item.setGeometry(QtCore.QRect(210, 80, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Clear_item.setFont(font)
        self.Clear_item.setObjectName("Clear_item")
        self.Save_item = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.save_data())
        self.Save_item.setGeometry(QtCore.QRect(310, 80, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Save_item.setFont(font)
        self.Save_item.setObjectName("Save_item")
        self.itemTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.itemTabs.setGeometry(QtCore.QRect(16, 149, 421, 401))
        self.itemTabs.setMovable(True)
        self.itemTabs.setObjectName("itemTabs")
        self.AddItemsTab = QtWidgets.QWidget()
        self.AddItemsTab.setObjectName("AddItemsTab")
        self.LocalListItem = QtWidgets.QListWidget(self.AddItemsTab)
        self.LocalListItem.setGeometry(QtCore.QRect(0, 0, 411, 371))
        self.LocalListItem.setObjectName("LocalListItem")
        self.itemTabs.addTab(self.AddItemsTab, "")
        self.ViewItemTabs = QtWidgets.QWidget()
        self.ViewItemTabs.setObjectName("ViewItemTabs")
        self.RealItemList = QtWidgets.QListWidget(self.ViewItemTabs)
        self.RealItemList.setGeometry(QtCore.QRect(0, 0, 411, 361))
        self.RealItemList.setObjectName("RealItemList")
        self.itemTabs.addTab(self.ViewItemTabs, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 26))
        self.menubar.setObjectName("menubar")
        self.menurefersh_list = QtWidgets.QMenu(self.menubar)
        self.menurefersh_list.setObjectName("menurefersh_list")
        # self.menurefersh_list.addAction(open)
        self.menurefersh_list.triggered.connect(lambda: self.fetch_all())
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menurefersh_list.menuAction())

        self.retranslateUi(MainWindow)
        self.fetch_all()
        self.itemTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # add item to local list
    def add_item(self):
        # LIST ITEM FROM INPUT FIELDS
        item = self.AddToListInput.text()
        # ADDING ITEM TO LOCALLIST VIEW
        self.LocalListItem.addItem(item)
        # LIST ITEM INPUT EMPTY
        self.AddToListInput.setText("")

    # delete item from local list
    def delete_item(self):
        # FETCH CURRENT ROW OF LOCAL LIST
        currentItem = self.LocalListItem.currentRow()
        # DELETE ITEM FROM LOCAL LIST ACCORDING TO  CURRENT LIST
        self.LocalListItem.takeItem(currentItem)

        # FETCH CURRENT ROW OF LOCAL LIST
        currentItem2 = self.RealItemList.currentRow()
        # DELETE ITEM FROM LOCAL LIST ACCORDING TO  CURRENT LIST
        self.RealItemList.takeItem(currentItem2)

    # CLEAR ALL ITEM FROM LOCAL LIST
    def clear_item(self):
        self.LocalListItem.clear()

    def fetch_all(self):
        db.sq.execute("SELECT * FROM items")
        myresult = db.sq.fetchall()
        self.RealItemList.clear()
        print("ads")
        for item in myresult:
            self.RealItemList.addItem(str(item[1]))

    
    def save_data(self):
        items = []
        for index in range(self.LocalListItem.count()):
            items.append(self.LocalListItem.item(index))

        if (len(items) > 0):
            for item in items:
                print(item.text())
                sql = "INSERT INTO items (item) VALUES (%s)"
                val = (f'{item.text()}')
                db.sq.execute(sql, val)
            db.myobj.commit()
            print(db.sq.rowcount, "record inserted.")
        self.fetch_all()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo List"))
        MainWindow.setWindowIcon(QtGui.QIcon('image/todolist.ico'))
        self.Add_item.setText(_translate("MainWindow", "Add item"))
        self.Delete_item.setText(_translate("MainWindow", "Delete"))
        self.AddToListInput.setPlaceholderText(
            _translate("MainWindow", "List item name"))
        self.Clear_item.setText(_translate("MainWindow", "Clear"))
        self.Save_item.setText(_translate("MainWindow", "Save"))
        self.itemTabs.setTabText(self.itemTabs.indexOf(
            self.AddItemsTab), _translate("MainWindow", "Add items"))
        self.itemTabs.setTabText(self.itemTabs.indexOf(
            self.ViewItemTabs), _translate("MainWindow", "View List"))
        self.menurefersh_list.setTitle(_translate("MainWindow", "Refersh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
