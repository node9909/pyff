# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Aug 31 13:24:37 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942,693)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,30,942,640))
        self.centralwidget.setObjectName("centralwidget")
        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.hboxlayout.addWidget(self.lineEdit)
        self.toolButton_clearFilter = QtGui.QToolButton(self.centralwidget)
        self.toolButton_clearFilter.setObjectName("toolButton_clearFilter")
        self.hboxlayout.addWidget(self.toolButton_clearFilter)
        self.toolButton_addFeedbackController = QtGui.QToolButton(self.centralwidget)
        self.toolButton_addFeedbackController.setObjectName("toolButton_addFeedbackController")
        self.hboxlayout.addWidget(self.toolButton_addFeedbackController)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)
        self.comboBox_player = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_player.sizePolicy().hasHeightForWidth())
        self.comboBox_player.setSizePolicy(sizePolicy)
        self.comboBox_player.setObjectName("comboBox_player")
        self.hboxlayout.addWidget(self.comboBox_player)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.hboxlayout.addWidget(self.label_5)
        self.comboBox_feedback = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_feedback.sizePolicy().hasHeightForWidth())
        self.comboBox_feedback.setSizePolicy(sizePolicy)
        self.comboBox_feedback.setObjectName("comboBox_feedback")
        self.hboxlayout.addWidget(self.comboBox_feedback)
        self.toolButton_sendinit = QtGui.QToolButton(self.centralwidget)
        self.toolButton_sendinit.setObjectName("toolButton_sendinit")
        self.hboxlayout.addWidget(self.toolButton_sendinit)
        self.toolButton_send = QtGui.QToolButton(self.centralwidget)
        self.toolButton_send.setObjectName("toolButton_send")
        self.hboxlayout.addWidget(self.toolButton_send)
        self.toolButton_get = QtGui.QToolButton(self.centralwidget)
        self.toolButton_get.setObjectName("toolButton_get")
        self.hboxlayout.addWidget(self.toolButton_get)
        self.toolButton_play = QtGui.QToolButton(self.centralwidget)
        self.toolButton_play.setObjectName("toolButton_play")
        self.hboxlayout.addWidget(self.toolButton_play)
        self.toolButton_pause = QtGui.QToolButton(self.centralwidget)
        self.toolButton_pause.setObjectName("toolButton_pause")
        self.hboxlayout.addWidget(self.toolButton_pause)
        self.toolButton_quit = QtGui.QToolButton(self.centralwidget)
        self.toolButton_quit.setObjectName("toolButton_quit")
        self.hboxlayout.addWidget(self.toolButton_quit)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.vboxlayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,942,30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,670,942,23))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/fileopen.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/filesave.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/filesaveas.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionQuit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/exit.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPlay = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/player_play.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/player_pause.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionPause.setIcon(icon)
        self.actionPause.setObjectName("actionPause")
        self.actionGet = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/mail_get.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionGet.setIcon(icon)
        self.actionGet.setObjectName("actionGet")
        self.actionSendInit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/mail_forward.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionSendInit.setIcon(icon)
        self.actionSendInit.setObjectName("actionSendInit")
        self.actionSend = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/mail_generic.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionSend.setIcon(icon)
        self.actionSend.setObjectName("actionSend")
        self.actionQuit1 = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/remove.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionQuit1.setIcon(icon)
        self.actionQuit1.setObjectName("actionQuit1")
        self.actionAddFeedbackController = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/add.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionAddFeedbackController.setIcon(icon)
        self.actionAddFeedbackController.setObjectName("actionAddFeedbackController")
        self.actionClearFilter = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../usr/share/icons/default.kde/16x16/actions/clear_left.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionClearFilter.setIcon(icon)
        self.actionClearFilter.setObjectName("actionClearFilter")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Send to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Feedback:", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open an Existing File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGet.setText(QtGui.QApplication.translate("MainWindow", "Get", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSendInit.setText(QtGui.QApplication.translate("MainWindow", "SendInit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSend.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit1.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFeedbackController.setText(QtGui.QApplication.translate("MainWindow", "addFeedbackController", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearFilter.setText(QtGui.QApplication.translate("MainWindow", "clearFilter", None, QtGui.QApplication.UnicodeUTF8))

