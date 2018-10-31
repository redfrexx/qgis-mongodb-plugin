# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadMongoDB_dialog_base.ui'
#
# Created: Sun Jul 26 14:04:46 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!


try:
    from PyQt5.QtCore import QSize, QRect, Qt, QObject, QMetaObject
    from PyQt5.QtWidgets import QApplication, QSizePolicy, QTabWidget, QWidget, QProgressBar, QPushButton, QLabel, QGridLayout, QCheckBox, QTreeWidget, QComboBox, QGroupBox, QListWidget
except:
    from PyQt4.QtCore import QString, QSize, QRect, Qt, SIGNAL, QObject, QMetaObject
    from PyQt4.QtGui import QApplication, QSizePolicy, QTabWidget, QWidget, QProgressBar, QPushButton, QLabel, QGridLayout, QCheckBox, QTreeWidget, QComboBox, QGroupBox, QListWidget

try:
    _fromUtf8 = QString.fromUtf8
except:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_loadMongoDBDialogBase(object):
    def setupUi(self, loadMongoDBDialogBase):
        loadMongoDBDialogBase.setObjectName(_fromUtf8("loadMongoDBDialogBase"))
        loadMongoDBDialogBase.resize(689, 487)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loadMongoDBDialogBase.sizePolicy().hasHeightForWidth())
        loadMongoDBDialogBase.setSizePolicy(sizePolicy)
        loadMongoDBDialogBase.setMinimumSize(QSize(689, 487))
        loadMongoDBDialogBase.setMaximumSize(QSize(689, 487))
        self.tabWidget = QTabWidget(loadMongoDBDialogBase)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(10, 10, 671, 471))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setGeometry(QRect(20, 410, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.Close_button = QPushButton(self.tab)
        self.Close_button.setGeometry(QRect(550, 410, 114, 32))
        self.Close_button.setObjectName(_fromUtf8("Close_button"))
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setGeometry(QRect(30, 10, 611, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.dbName = QComboBox(self.layoutWidget)
        self.dbName.setEditable(True)
        self.dbName.setObjectName(_fromUtf8("dbName"))
        self.gridLayout.addWidget(self.dbName, 1, 1, 1, 4)
        self.serverName = QComboBox(self.layoutWidget)
        self.serverName.setEditable(True)
        self.serverName.setObjectName(_fromUtf8("serverName"))
        self.gridLayout.addWidget(self.serverName, 0, 1, 1, 4)
        self.geom_field = QComboBox(self.layoutWidget)
        self.geom_field.setEditable(True)
        self.geom_field.setObjectName(_fromUtf8("geom_field"))
        self.gridLayout.addWidget(self.geom_field, 2, 1, 1, 4)

        self.query_field = QComboBox(self.layoutWidget)
        self.query_field.setEditable(True)
        self.query_field.setObjectName(_fromUtf8("query_field"))
        self.gridLayout.addWidget(self.query_field, 3, 1, 1, 4)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setGeometry(QRect(10, 180, 641, 221))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.createFile = QPushButton(self.groupBox)
        self.createFile.setGeometry(QRect(10, 20, 114, 32))
        self.createFile.setObjectName(_fromUtf8("createFile"))
        self.load_collection = QPushButton(self.groupBox)
        self.load_collection.setGeometry(QRect(120, 20, 114, 32))
        self.load_collection.setObjectName(_fromUtf8("load_collection"))
        self.listCol = QTreeWidget(self.groupBox)
        self.listCol.setGeometry(QRect(10, 50, 621, 161))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listCol.sizePolicy().hasHeightForWidth())
        self.listCol.setSizePolicy(sizePolicy)
        self.listCol.setObjectName(_fromUtf8("listCol"))
        self.listCol.headerItem().setText(1, _fromUtf8("Geometry"))
        self.listCol.header().setDefaultSectionSize(210)
        self.listCol.header().setMinimumSectionSize(200)
        self.listCol.header().setStretchLastSection(False)
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QRect(450, 20, 21, 20))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setCheckable(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.load_field = QComboBox(self.groupBox)
        self.load_field.setGeometry(QRect(480, 20, 151, 26))
        self.load_field.setEditable(False)
        self.load_field.setObjectName(_fromUtf8("load_field"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.view_all = QListWidget(self.tab_2)
        self.view_all.setEnabled(False)
        self.view_all.setGeometry(QRect(10, 10, 221, 371))
        self.view_all.setObjectName(_fromUtf8("view_all"))
        self.distinct_button = QPushButton(self.tab_2)
        self.distinct_button.setEnabled(False)
        self.distinct_button.setGeometry(QRect(120, 380, 111, 41))
        self.distinct_button.setObjectName(_fromUtf8("distinct_button"))
        self.view_distinct = QListWidget(self.tab_2)
        self.view_distinct.setEnabled(False)
        self.view_distinct.setGeometry(QRect(240, 10, 171, 181))
        self.view_distinct.setObjectName(_fromUtf8("view_distinct"))
        self.set_button = QPushButton(self.tab_2)
        self.set_button.setEnabled(False)
        self.set_button.setGeometry(QRect(300, 190, 114, 41))
        self.set_button.setObjectName(_fromUtf8("set_button"))
        self.view_button = QPushButton(self.tab_2)
        self.view_button.setEnabled(False)
        self.view_button.setGeometry(QRect(10, 380, 111, 41))
        self.view_button.setObjectName(_fromUtf8("view_button"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label = QLabel(loadMongoDBDialogBase)
        self.label.setGeometry(QRect(560, 0, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(loadMongoDBDialogBase)
        self.tabWidget.setCurrentIndex(0)

        try:
            self.Close_button.clicked.connect(loadMongoDBDialogBase.close)
        except:
            QObject.connect(self.Close_button, SIGNAL(_fromUtf8("clicked()")), loadMongoDBDialogBase.close)
        
        QMetaObject.connectSlotsByName(loadMongoDBDialogBase)
        loadMongoDBDialogBase.setTabOrder(self.serverName, self.dbName)
        loadMongoDBDialogBase.setTabOrder(self.dbName, self.geom_field)
        loadMongoDBDialogBase.setTabOrder(self.geom_field, self.createFile)
        loadMongoDBDialogBase.setTabOrder(self.createFile, self.load_collection)
        loadMongoDBDialogBase.setTabOrder(self.load_collection, self.listCol)
        loadMongoDBDialogBase.setTabOrder(self.listCol, self.Close_button)

    def retranslateUi(self, loadMongoDBDialogBase):
        loadMongoDBDialogBase.setWindowTitle(_translate("loadMongoDBDialogBase", "Load MongoDB Points", None))
        self.Close_button.setText(_translate("loadMongoDBDialogBase", "Close", None))
        self.label_3.setText(_translate("loadMongoDBDialogBase", "Database:", None))
        self.label_5.setText(_translate("loadMongoDBDialogBase", "Server URI:", None))
        self.label_6.setText(_translate("loadMongoDBDialogBase", "Geometry field:", None))
        self.label_7.setText(_translate("loadMongoDBDialogBase", "Query:", None))
        self.createFile.setText(_translate("loadMongoDBDialogBase", "Connect", None))
        self.load_collection.setText(_translate("loadMongoDBDialogBase", "Load", None))
        self.listCol.headerItem().setText(0, _translate("loadMongoDBDialogBase", "Items", None))
        self.listCol.headerItem().setText(2, _translate("loadMongoDBDialogBase", "Count", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("loadMongoDBDialogBase", "Connection", None))
        self.distinct_button.setText(_translate("loadMongoDBDialogBase", "Distinct", None))
        self.set_button.setText(_translate("loadMongoDBDialogBase", "Set", None))
        self.view_button.setText(_translate("loadMongoDBDialogBase", "View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("loadMongoDBDialogBase", "Settings", None))
        self.label.setText(_translate("loadMongoDBDialogBase", "MongoDB Loader", None))

