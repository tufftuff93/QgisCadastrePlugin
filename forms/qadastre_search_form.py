# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qadastre_search_form.ui'
#
# Created: Mon Sep 16 17:01:01 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_qadastre_search_form(object):
    def setupUi(self, qadastre_search_form):
        qadastre_search_form.setObjectName(_fromUtf8("qadastre_search_form"))
        qadastre_search_form.resize(355, 625)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea_3 = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 335, 580))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.liAdresse = QtGui.QComboBox(self.groupBox)
        self.liAdresse.setEditable(True)
        self.liAdresse.setObjectName(_fromUtf8("liAdresse"))
        self.gridLayout_3.addWidget(self.liAdresse, 0, 1, 1, 1)
        self.btSearchAdresse = QtGui.QPushButton(self.groupBox)
        self.btSearchAdresse.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btSearchAdresse.setObjectName(_fromUtf8("btSearchAdresse"))
        self.gridLayout_3.addWidget(self.btSearchAdresse, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.liParcelleAdresse = QtGui.QComboBox(self.groupBox)
        self.liParcelleAdresse.setEditable(True)
        self.liParcelleAdresse.setObjectName(_fromUtf8("liParcelleAdresse"))
        self.gridLayout_3.addWidget(self.liParcelleAdresse, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btCentrerAdresse = QtGui.QPushButton(self.groupBox)
        self.btCentrerAdresse.setObjectName(_fromUtf8("btCentrerAdresse"))
        self.horizontalLayout.addWidget(self.btCentrerAdresse)
        self.btZoomerAdresse = QtGui.QPushButton(self.groupBox)
        self.btZoomerAdresse.setObjectName(_fromUtf8("btZoomerAdresse"))
        self.horizontalLayout.addWidget(self.btZoomerAdresse)
        self.btSelectionnerAdresse = QtGui.QPushButton(self.groupBox)
        self.btSelectionnerAdresse.setObjectName(_fromUtf8("btSelectionnerAdresse"))
        self.horizontalLayout.addWidget(self.btSelectionnerAdresse)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_13.addWidget(self.groupBox)
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_5)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.liCommune = QtGui.QComboBox(self.groupBox_5)
        self.liCommune.setObjectName(_fromUtf8("liCommune"))
        self.gridLayout.addWidget(self.liCommune, 0, 1, 1, 1)
        self.liSection = QtGui.QComboBox(self.groupBox_5)
        self.liSection.setObjectName(_fromUtf8("liSection"))
        self.gridLayout.addWidget(self.liSection, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.liParcelle = QtGui.QComboBox(self.groupBox_5)
        self.liParcelle.setEditable(True)
        self.liParcelle.setObjectName(_fromUtf8("liParcelle"))
        self.horizontalLayout_4.addWidget(self.liParcelle)
        self.btSearchParcelle = QtGui.QPushButton(self.groupBox_5)
        self.btSearchParcelle.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btSearchParcelle.setObjectName(_fromUtf8("btSearchParcelle"))
        self.horizontalLayout_4.addWidget(self.btSearchParcelle)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btCentrerLieu = QtGui.QPushButton(self.groupBox_5)
        self.btCentrerLieu.setObjectName(_fromUtf8("btCentrerLieu"))
        self.horizontalLayout_2.addWidget(self.btCentrerLieu)
        self.btZoomerLieu = QtGui.QPushButton(self.groupBox_5)
        self.btZoomerLieu.setObjectName(_fromUtf8("btZoomerLieu"))
        self.horizontalLayout_2.addWidget(self.btZoomerLieu)
        self.btSelectionnerLieu = QtGui.QPushButton(self.groupBox_5)
        self.btSelectionnerLieu.setObjectName(_fromUtf8("btSelectionnerLieu"))
        self.horizontalLayout_2.addWidget(self.btSelectionnerLieu)
        self.verticalLayout_14.addLayout(self.horizontalLayout_2)
        self.verticalLayout_13.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btSearchProprietaire = QtGui.QPushButton(self.groupBox_6)
        self.btSearchProprietaire.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btSearchProprietaire.setObjectName(_fromUtf8("btSearchProprietaire"))
        self.gridLayout_2.addWidget(self.btSearchProprietaire, 0, 2, 1, 1)
        self.liProprietaire = QtGui.QComboBox(self.groupBox_6)
        self.liProprietaire.setEditable(True)
        self.liProprietaire.setObjectName(_fromUtf8("liProprietaire"))
        self.gridLayout_2.addWidget(self.liProprietaire, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_6)
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.liParcelleProprietaire = QtGui.QComboBox(self.groupBox_6)
        self.liParcelleProprietaire.setEditable(True)
        self.liParcelleProprietaire.setObjectName(_fromUtf8("liParcelleProprietaire"))
        self.gridLayout_2.addWidget(self.liParcelleProprietaire, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_6)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btCentrerProprietaire = QtGui.QPushButton(self.groupBox_6)
        self.btCentrerProprietaire.setObjectName(_fromUtf8("btCentrerProprietaire"))
        self.horizontalLayout_3.addWidget(self.btCentrerProprietaire)
        self.btZoomerProprietaire = QtGui.QPushButton(self.groupBox_6)
        self.btZoomerProprietaire.setObjectName(_fromUtf8("btZoomerProprietaire"))
        self.horizontalLayout_3.addWidget(self.btZoomerProprietaire)
        self.btSelectionnerProprietaire = QtGui.QPushButton(self.groupBox_6)
        self.btSelectionnerProprietaire.setObjectName(_fromUtf8("btSelectionnerProprietaire"))
        self.horizontalLayout_3.addWidget(self.btSelectionnerProprietaire)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_13.addWidget(self.groupBox_6)
        self.txtLog = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.txtLog.setObjectName(_fromUtf8("txtLog"))
        self.verticalLayout_13.addWidget(self.txtLog)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea_3)
        qadastre_search_form.setWidget(self.dockWidgetContents)

        self.retranslateUi(qadastre_search_form)
        QtCore.QMetaObject.connectSlotsByName(qadastre_search_form)
        qadastre_search_form.setTabOrder(self.scrollArea_3, self.liAdresse)
        qadastre_search_form.setTabOrder(self.liAdresse, self.btSearchAdresse)
        qadastre_search_form.setTabOrder(self.btSearchAdresse, self.liParcelleAdresse)
        qadastre_search_form.setTabOrder(self.liParcelleAdresse, self.btCentrerAdresse)
        qadastre_search_form.setTabOrder(self.btCentrerAdresse, self.btZoomerAdresse)
        qadastre_search_form.setTabOrder(self.btZoomerAdresse, self.btSelectionnerAdresse)
        qadastre_search_form.setTabOrder(self.btSelectionnerAdresse, self.liCommune)
        qadastre_search_form.setTabOrder(self.liCommune, self.liSection)
        qadastre_search_form.setTabOrder(self.liSection, self.liParcelle)
        qadastre_search_form.setTabOrder(self.liParcelle, self.btSearchParcelle)
        qadastre_search_form.setTabOrder(self.btSearchParcelle, self.btCentrerLieu)
        qadastre_search_form.setTabOrder(self.btCentrerLieu, self.btZoomerLieu)
        qadastre_search_form.setTabOrder(self.btZoomerLieu, self.btSelectionnerLieu)
        qadastre_search_form.setTabOrder(self.btSelectionnerLieu, self.liProprietaire)
        qadastre_search_form.setTabOrder(self.liProprietaire, self.btSearchProprietaire)
        qadastre_search_form.setTabOrder(self.btSearchProprietaire, self.liParcelleProprietaire)
        qadastre_search_form.setTabOrder(self.liParcelleProprietaire, self.btCentrerProprietaire)
        qadastre_search_form.setTabOrder(self.btCentrerProprietaire, self.btZoomerProprietaire)
        qadastre_search_form.setTabOrder(self.btZoomerProprietaire, self.btSelectionnerProprietaire)
        qadastre_search_form.setTabOrder(self.btSelectionnerProprietaire, self.txtLog)

    def retranslateUi(self, qadastre_search_form):
        qadastre_search_form.setWindowTitle(_translate("qadastre_search_form", "Qadastre - Outils de recherche", None))
        self.groupBox.setTitle(_translate("qadastre_search_form", "Recherche d\'adresse", None))
        self.btSearchAdresse.setText(_translate("qadastre_search_form", "...", None))
        self.label_5.setText(_translate("qadastre_search_form", "Adresse", None))
        self.label_6.setText(_translate("qadastre_search_form", "Parcelle", None))
        self.btCentrerAdresse.setText(_translate("qadastre_search_form", "Centrer", None))
        self.btZoomerAdresse.setText(_translate("qadastre_search_form", "Zoomer", None))
        self.btSelectionnerAdresse.setText(_translate("qadastre_search_form", "Sélectionner", None))
        self.groupBox_5.setTitle(_translate("qadastre_search_form", "Recherche de lieux", None))
        self.label_12.setText(_translate("qadastre_search_form", "Commune", None))
        self.label_2.setText(_translate("qadastre_search_form", "Parcelle", None))
        self.label.setText(_translate("qadastre_search_form", "Section", None))
        self.btSearchParcelle.setText(_translate("qadastre_search_form", "...", None))
        self.btCentrerLieu.setText(_translate("qadastre_search_form", "Centrer", None))
        self.btZoomerLieu.setText(_translate("qadastre_search_form", "Zoomer", None))
        self.btSelectionnerLieu.setText(_translate("qadastre_search_form", "Sélectionner", None))
        self.groupBox_6.setTitle(_translate("qadastre_search_form", "Recherche de propriétaire", None))
        self.btSearchProprietaire.setText(_translate("qadastre_search_form", "...", None))
        self.label_3.setText(_translate("qadastre_search_form", "Parcelle", None))
        self.label_4.setText(_translate("qadastre_search_form", "Nom", None))
        self.btCentrerProprietaire.setText(_translate("qadastre_search_form", "Centrer", None))
        self.btZoomerProprietaire.setText(_translate("qadastre_search_form", "Zoomer", None))
        self.btSelectionnerProprietaire.setText(_translate("qadastre_search_form", "Sélectionner", None))
        self.txtLog.setHtml(_translate("qadastre_search_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
