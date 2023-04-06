import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5 import QtGui, QtWidgets, QtCore
from taba import Ui_Dialog

# clase para colocar la pestaña de manera horizontal
class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
            painter.restore()



#clase de la app principal de donde se llama la interfaze creada en derigner
class app_window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #se implementa la class TabBar
        self.ui.tabWidget.setTabBar(TabBar(self.ui.tabWidget))
        self.ui.tabWidget.setTabPosition(self.ui.tabWidget.West)

        self.ui.tabWidget.resize(500, 350)
        #se añaden los tab y se renombran
        self.ui.tabWidget.insertTab(0, self.ui.tab, "My tab")
        self.ui.tabWidget.insertTab(0, self.ui.tab_2, "My tabrst")
        self.ui.tabWidget.insertTab(0, self.ui.tab_3, "Maaaa")

        #llamar boton y crear una señal
        #self.ui.pushButton_reach.clicked.connect(self.display)

      

        self.show()

    def display(self):
        print("reached")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = app_window()
    w.show()
    sys.exit(app.exec_())