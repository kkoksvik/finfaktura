# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finfaktura\ui\sendepost.ui'
#
# Created: Wed Aug 27 01:08:49 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_sendEpost(object):
    def setupUi(self, sendEpost):
        sendEpost.setObjectName("sendEpost")
        sendEpost.resize(667, 378)
        sendEpost.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(sendEpost)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tittel = QtGui.QLabel(sendEpost)
        self.tittel.setTextFormat(QtCore.Qt.RichText)
        self.tittel.setWordWrap(False)
        self.tittel.setObjectName("tittel")
        self.gridLayout.addWidget(self.tittel, 0, 0, 1, 2)
        self.tekst = QtGui.QPlainTextEdit(sendEpost)
        self.tekst.setTabChangesFocus(True)
        self.tekst.setObjectName("tekst")
        self.gridLayout.addWidget(self.tekst, 1, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(sendEpost)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(sendEpost)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), sendEpost.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), sendEpost.reject)
        QtCore.QMetaObject.connectSlotsByName(sendEpost)

    def retranslateUi(self, sendEpost):
        sendEpost.setWindowTitle(QtGui.QApplication.translate("sendEpost", "Send faktura per epost", None, QtGui.QApplication.UnicodeUTF8))
        self.tittel.setText(QtGui.QApplication.translate("sendEpost", "Sender epost til", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sendEpost = QtGui.QDialog()
    ui = Ui_sendEpost()
    ui.setupUi(sendEpost)
    sendEpost.show()
    sys.exit(app.exec_())

