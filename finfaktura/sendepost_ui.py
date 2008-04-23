# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sendepost.ui'
#
# Created: on. april 23 12:04:54 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.4
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *


class sendEpost(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("sendEpost")

        self.setModal(1)

        sendEpostLayout = QGridLayout(self,1,1,11,6,"sendEpostLayout")

        layout12 = QGridLayout(None,1,1,0,6,"layout12")

        self.sendEpostSend = QPushButton(self,"sendEpostSend")
        self.sendEpostSend.setDefault(1)

        layout12.addWidget(self.sendEpostSend,2,1)

        self.fakturaSendepostTittel = QLabel(self,"fakturaSendepostTittel")
        self.fakturaSendepostTittel.setTextFormat(QLabel.RichText)

        layout12.addMultiCellWidget(self.fakturaSendepostTittel,0,0,0,1)

        self.sendEpostTekst = QTextEdit(self,"sendEpostTekst")
        self.sendEpostTekst.setTextFormat(QTextEdit.PlainText)

        layout12.addMultiCellWidget(self.sendEpostTekst,1,1,0,1)

        self.sendEpostAvbryt = QPushButton(self,"sendEpostAvbryt")

        layout12.addWidget(self.sendEpostAvbryt,2,0)

        sendEpostLayout.addLayout(layout12,0,0)

        self.languageChange()

        self.resize(QSize(574,477).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Send faktura per epost"))
        self.sendEpostSend.setText(self.__tr("Send"))
        QToolTip.add(self.sendEpostSend,self.__tr("Sender efakturaen som PDF-fil til adressen over"))
        self.fakturaSendepostTittel.setText(self.__tr("Sender epost til"))
        QToolTip.add(self.sendEpostTekst,self.__tr("Valgfri tekst som vil bli vist i kundens epostprogram (fakturaen sendes som vedlegg)"))
        self.sendEpostAvbryt.setText(self.__tr("Avbryt"))
        QToolTip.add(self.sendEpostAvbryt,self.__tr("Avbryter sendingen av efaktura"))


    def __tr(self,s,c = None):
        return qApp.translate("sendEpost",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = sendEpost()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
