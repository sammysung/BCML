# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\macad\Documents\Git\BCML-2\.vscode\install.ui',
# licensing of 'c:\Users\macad\Documents\Git\BCML-2\.vscode\install.ui' applies.
#
# Created: Fri Sep 13 20:33:44 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_InstallDialog(object):
    def setupUi(self, InstallDialog):
        InstallDialog.setObjectName("InstallDialog")
        InstallDialog.resize(226, 358)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InstallDialog.sizePolicy().hasHeightForWidth())
        InstallDialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(InstallDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(InstallDialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lstQueue = QtWidgets.QListWidget(InstallDialog)
        self.lstQueue.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstQueue.setAlternatingRowColors(True)
        self.lstQueue.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lstQueue.setObjectName("lstQueue")
        self.verticalLayout_3.addWidget(self.lstQueue)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnAddFile = QtWidgets.QPushButton(InstallDialog)
        self.btnAddFile.setStyleSheet("padding: 4px 8px;")
        self.btnAddFile.setObjectName("btnAddFile")
        self.gridLayout.addWidget(self.btnAddFile, 0, 0, 1, 1)
        self.btnAddFolder = QtWidgets.QPushButton(InstallDialog)
        self.btnAddFolder.setStyleSheet("padding: 4px 8px;")
        self.btnAddFolder.setObjectName("btnAddFolder")
        self.gridLayout.addWidget(self.btnAddFolder, 0, 1, 1, 1)
        self.btnRemove = QtWidgets.QPushButton(InstallDialog)
        self.btnRemove.setStyleSheet("padding: 4px 12px;")
        self.btnRemove.setObjectName("btnRemove")
        self.gridLayout.addWidget(self.btnRemove, 1, 1, 1, 1)
        self.btnClear = QtWidgets.QPushButton(InstallDialog)
        self.btnClear.setStyleSheet("padding: 4px 12px;")
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdvanced = QtWidgets.QPushButton(InstallDialog)
        self.btnAdvanced.setObjectName("btnAdvanced")
        self.horizontalLayout.addWidget(self.btnAdvanced)
        self.label_2 = QtWidgets.QLabel(InstallDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spnPriority = QtWidgets.QSpinBox(InstallDialog)
        self.spnPriority.setMinimum(1)
        self.spnPriority.setMaximum(9998)
        self.spnPriority.setObjectName("spnPriority")
        self.horizontalLayout.addWidget(self.spnPriority)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(InstallDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(InstallDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), InstallDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), InstallDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InstallDialog)

    def retranslateUi(self, InstallDialog):
        InstallDialog.setWindowTitle(QtWidgets.QApplication.translate("InstallDialog", "Mod Install", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("InstallDialog", "Mod(s) to install ", None, -1))
        self.btnAddFile.setToolTip(QtWidgets.QApplication.translate("InstallDialog", "Browse to add a mod in ZIP, RAR, 7z, or BNP format", None, -1))
        self.btnAddFile.setText(QtWidgets.QApplication.translate("InstallDialog", "Add File...", None, -1))
        self.btnAddFolder.setToolTip(QtWidgets.QApplication.translate("InstallDialog", "Browse to add an unpacked mod from a folder containing a \"content\" folder and a rules.txt", None, -1))
        self.btnAddFolder.setText(QtWidgets.QApplication.translate("InstallDialog", "Add Folder...", None, -1))
        self.btnRemove.setText(QtWidgets.QApplication.translate("InstallDialog", "Remove", None, -1))
        self.btnClear.setText(QtWidgets.QApplication.translate("InstallDialog", "Clear All", None, -1))
        self.btnAdvanced.setText(QtWidgets.QApplication.translate("InstallDialog", "Advanced...", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("InstallDialog", "Start Priority:", None, -1))

