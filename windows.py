# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 908)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_main = QtWidgets.QWidget(self.centralwidget)
        self.widget_main.setStyleSheet("QWidget#widget_main{background:#1F1F1F;border-radius:2px;}")
        self.widget_main.setObjectName("widget_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_main)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_top = QtWidgets.QWidget(self.widget_main)
        self.widget_top.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_top.setStyleSheet("")
        self.widget_top.setObjectName("widget_top")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_top)
        self.horizontalLayout_5.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_top_l1 = QtWidgets.QWidget(self.widget_top)
        self.widget_top_l1.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_top_l1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_top_l1.setObjectName("widget_top_l1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_top_l1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_face = QtWidgets.QLabel(self.widget_top_l1)
        self.label_face.setMinimumSize(QtCore.QSize(50, 50))
        self.label_face.setMaximumSize(QtCore.QSize(50, 50))
        self.label_face.setStyleSheet("QLabel{border-radius:22px;background:Transparent}")
        self.label_face.setText("")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
        self.horizontalLayout.addWidget(self.label_face)
        self.pushButton_nickname = QtWidgets.QPushButton(self.widget_top_l1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_nickname.setFont(font)
        self.pushButton_nickname.setStyleSheet("QPushButton{background:Transparent;text-align: left;color:white;}QPushButton:hover{color:rgba(255,255,255, 0.8);}")
        self.pushButton_nickname.setText("")
        self.pushButton_nickname.setObjectName("pushButton_nickname")
        self.horizontalLayout.addWidget(self.pushButton_nickname)
        self.horizontalLayout_5.addWidget(self.widget_top_l1)
        self.widget_top_l2 = QtWidgets.QWidget(self.widget_top)
        self.widget_top_l2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_top_l2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_top_l2.setObjectName("widget_top_l2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_top_l2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_notify = QtWidgets.QPushButton(self.widget_top_l2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_notify.setFont(font)
        self.pushButton_notify.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_notify.setStyleSheet("QPushButton{background:Transparent;text-align: left;color:white;}QPushButton:hover{color:rgba(255,255,255, 0.8);}")
        self.pushButton_notify.setObjectName("pushButton_notify")
        self.horizontalLayout_3.addWidget(self.pushButton_notify)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5.addWidget(self.widget_top_l2)
        self.widget_top_l3 = QtWidgets.QWidget(self.widget_top)
        self.widget_top_l3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_top_l3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_top_l3.setObjectName("widget_top_l3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_top_l3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_feedback = QtWidgets.QPushButton(self.widget_top_l3)
        self.pushButton_feedback.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_feedback.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_feedback.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(255,112,158,0.8);}")
        self.pushButton_feedback.setText("")
        self.pushButton_feedback.setObjectName("pushButton_feedback")
        self.horizontalLayout_4.addWidget(self.pushButton_feedback)
        self.pushButton_setting = QtWidgets.QPushButton(self.widget_top_l3)
        self.pushButton_setting.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_setting.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_setting.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(255,112,158,0.8);}")
        self.pushButton_setting.setText("")
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.horizontalLayout_4.addWidget(self.pushButton_setting)
        self.pushButton_min = QtWidgets.QPushButton(self.widget_top_l3)
        self.pushButton_min.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_min.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_min.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(255,112,158,0.8);}")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout_4.addWidget(self.pushButton_min)
        self.pushButton_max = QtWidgets.QPushButton(self.widget_top_l3)
        self.pushButton_max.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_max.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_max.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(255,112,158,0.8);}")
        self.pushButton_max.setText("")
        self.pushButton_max.setObjectName("pushButton_max")
        self.horizontalLayout_4.addWidget(self.pushButton_max)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_top_l3)
        self.pushButton_close.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_close.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_close.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(255,112,158,0.8);}")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_4.addWidget(self.pushButton_close)
        self.horizontalLayout_5.addWidget(self.widget_top_l3)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 8)
        self.horizontalLayout_5.setStretch(2, 1)
        self.gridLayout_2.addWidget(self.widget_top, 0, 0, 1, 1)
        self.widget_down = QtWidgets.QWidget(self.widget_main)
        self.widget_down.setStyleSheet("QWidget#widget_down{background:#F0F5FF;border-bottom-left-radius:2px;border-bottom-right-radius:2px;}")
        self.widget_down.setObjectName("widget_down")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_down)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_left = QtWidgets.QWidget(self.widget_down)
        self.widget_left.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_left.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_left.setStyleSheet("QWidget#widget_left{background:#F0F5FF;border-bottom-left-radius:2px;border-right-width:1px;border-style:solid;border-color:rgba(69,104,220,0.3);}")
        self.widget_left.setObjectName("widget_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_left)
        self.verticalLayout_2.setContentsMargins(0, 11, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_left_t1 = QtWidgets.QWidget(self.widget_left)
        self.widget_left_t1.setStyleSheet("QWidget#widget_left_t1{background:rgba(255,255,255,0.5);border-bottom-right-radius:2px;}")
        self.widget_left_t1.setObjectName("widget_left_t1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_left_t1)
        self.verticalLayout_3.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_left_t1)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_level = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_level.setFont(font)
        self.label_level.setObjectName("label_level")
        self.horizontalLayout_7.addWidget(self.label_level)
        self.label_exp = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_exp.setFont(font)
        self.label_exp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_exp.setObjectName("label_exp")
        self.horizontalLayout_7.addWidget(self.label_exp)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.progressBar = QtWidgets.QProgressBar(self.widget_left_t1)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar.setStyleSheet("QProgressBar::chunk{background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #36d1dc,stop:1 #5b86e5);}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.widget_5 = QtWidgets.QWidget(self.widget_left_t1)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_coin = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_coin.setFont(font)
        self.pushButton_coin.setStyleSheet("QPushButton{background:Transparent;text-align: left;}")
        self.pushButton_coin.setObjectName("pushButton_coin")
        self.horizontalLayout_8.addWidget(self.pushButton_coin)
        self.pushButton_balance = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_balance.setFont(font)
        self.pushButton_balance.setStyleSheet("QPushButton{background:Transparent;text-align: left;}")
        self.pushButton_balance.setObjectName("pushButton_balance")
        self.horizontalLayout_8.addWidget(self.pushButton_balance)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.verticalLayout_2.addWidget(self.widget_left_t1)
        self.widget_left_t8 = QtWidgets.QWidget(self.widget_left)
        self.widget_left_t8.setStyleSheet("QWidget#widget_left_t8{background:rgba(255,255,255,0.5);border-bottom-right-radius:2px;}")
        self.widget_left_t8.setObjectName("widget_left_t8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_left_t8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_left_t8)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.widget_9 = QtWidgets.QWidget(self.widget_left_t8)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_creative = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_creative.setFont(font)
        self.label_creative.setAlignment(QtCore.Qt.AlignCenter)
        self.label_creative.setObjectName("label_creative")
        self.horizontalLayout_16.addWidget(self.label_creative)
        self.label_influence = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_influence.setFont(font)
        self.label_influence.setAlignment(QtCore.Qt.AlignCenter)
        self.label_influence.setObjectName("label_influence")
        self.horizontalLayout_16.addWidget(self.label_influence)
        self.label_credit = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_credit.setFont(font)
        self.label_credit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_credit.setObjectName("label_credit")
        self.horizontalLayout_16.addWidget(self.label_credit)
        self.verticalLayout_5.addWidget(self.widget_9)
        self.verticalLayout_2.addWidget(self.widget_left_t8)
        self.widget_left_t5 = QtWidgets.QWidget(self.widget_left)
        self.widget_left_t5.setStyleSheet("QWidget#widget_left_t5{background:rgba(255,255,255,0.5);border-bottom-right-radius:2px;}")
        self.widget_left_t5.setObjectName("widget_left_t5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_left_t5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_left_t5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget_left_t2 = QtWidgets.QWidget(self.widget_left_t5)
        self.widget_left_t2.setStyleSheet("QWidget#widget_left_t2{background:Transparent;border-bottom-right-radius:2px;}")
        self.widget_left_t2.setObjectName("widget_left_t2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_left_t2)
        self.horizontalLayout_6.setContentsMargins(0, 11, 0, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_follower = QtWidgets.QLabel(self.widget_left_t2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_follower.setFont(font)
        self.label_follower.setAlignment(QtCore.Qt.AlignCenter)
        self.label_follower.setObjectName("label_follower")
        self.horizontalLayout_6.addWidget(self.label_follower)
        self.label_view = QtWidgets.QLabel(self.widget_left_t2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_view.setFont(font)
        self.label_view.setAlignment(QtCore.Qt.AlignCenter)
        self.label_view.setObjectName("label_view")
        self.horizontalLayout_6.addWidget(self.label_view)
        self.label_like = QtWidgets.QLabel(self.widget_left_t2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_like.setFont(font)
        self.label_like.setAlignment(QtCore.Qt.AlignCenter)
        self.label_like.setObjectName("label_like")
        self.horizontalLayout_6.addWidget(self.label_like)
        self.label_coin = QtWidgets.QLabel(self.widget_left_t2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_coin.setFont(font)
        self.label_coin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_coin.setObjectName("label_coin")
        self.horizontalLayout_6.addWidget(self.label_coin)
        self.verticalLayout.addWidget(self.widget_left_t2)
        self.widget_left_t3 = QtWidgets.QWidget(self.widget_left_t5)
        self.widget_left_t3.setStyleSheet("QWidget#widget_left_t3{background:Transparent;border-bottom-right-radius:2px;}")
        self.widget_left_t3.setObjectName("widget_left_t3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_left_t3)
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_reply = QtWidgets.QLabel(self.widget_left_t3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_reply.setFont(font)
        self.label_reply.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reply.setObjectName("label_reply")
        self.horizontalLayout_9.addWidget(self.label_reply)
        self.label_danmaku = QtWidgets.QLabel(self.widget_left_t3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_danmaku.setFont(font)
        self.label_danmaku.setAlignment(QtCore.Qt.AlignCenter)
        self.label_danmaku.setObjectName("label_danmaku")
        self.horizontalLayout_9.addWidget(self.label_danmaku)
        self.label_share = QtWidgets.QLabel(self.widget_left_t3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_share.setFont(font)
        self.label_share.setAlignment(QtCore.Qt.AlignCenter)
        self.label_share.setObjectName("label_share")
        self.horizontalLayout_9.addWidget(self.label_share)
        self.label_favorite = QtWidgets.QLabel(self.widget_left_t3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_favorite.setFont(font)
        self.label_favorite.setAlignment(QtCore.Qt.AlignCenter)
        self.label_favorite.setObjectName("label_favorite")
        self.horizontalLayout_9.addWidget(self.label_favorite)
        self.verticalLayout.addWidget(self.widget_left_t3)
        self.verticalLayout_2.addWidget(self.widget_left_t5)
        self.widget_left_t4 = QtWidgets.QWidget(self.widget_left)
        self.widget_left_t4.setStyleSheet("QWidget#widget_left_t4{background:rgba(255,255,255,0.5);border-bottom-right-radius:2px;}")
        self.widget_left_t4.setObjectName("widget_left_t4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_left_t4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_left_t4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.widget_left_t6 = QtWidgets.QWidget(self.widget_left_t4)
        self.widget_left_t6.setStyleSheet("QWidget#widget_left_t6{background:Transparent;border-bottom-right-radius:2px;}")
        self.widget_left_t6.setObjectName("widget_left_t6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_left_t6)
        self.horizontalLayout_13.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_artview = QtWidgets.QLabel(self.widget_left_t6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_artview.setFont(font)
        self.label_artview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_artview.setObjectName("label_artview")
        self.horizontalLayout_13.addWidget(self.label_artview)
        self.label_artlike = QtWidgets.QLabel(self.widget_left_t6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_artlike.setFont(font)
        self.label_artlike.setAlignment(QtCore.Qt.AlignCenter)
        self.label_artlike.setObjectName("label_artlike")
        self.horizontalLayout_13.addWidget(self.label_artlike)
        self.label_artcoin = QtWidgets.QLabel(self.widget_left_t6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_artcoin.setFont(font)
        self.label_artcoin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_artcoin.setObjectName("label_artcoin")
        self.horizontalLayout_13.addWidget(self.label_artcoin)
        self.verticalLayout_4.addWidget(self.widget_left_t6)
        self.widget_left_t7 = QtWidgets.QWidget(self.widget_left_t4)
        self.widget_left_t7.setStyleSheet("QWidget#widget_left_t7{background:Transparent;border-bottom-right-radius:2px;}")
        self.widget_left_t7.setObjectName("widget_left_t7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_left_t7)
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_artreply = QtWidgets.QLabel(self.widget_left_t7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_artreply.setFont(font)
        self.label_artreply.setAlignment(QtCore.Qt.AlignCenter)
        self.label_artreply.setObjectName("label_artreply")
        self.horizontalLayout_14.addWidget(self.label_artreply)
        self.label_artshare = QtWidgets.QLabel(self.widget_left_t7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_artshare.setFont(font)
        self.label_artshare.setAlignment(QtCore.Qt.AlignCenter)
        self.label_artshare.setObjectName("label_artshare")
        self.horizontalLayout_14.addWidget(self.label_artshare)
        self.label_artfav = QtWidgets.QLabel(self.widget_left_t7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_artfav.setFont(font)
        self.label_artfav.setAlignment(QtCore.Qt.AlignCenter)
        self.label_artfav.setObjectName("label_artfav")
        self.horizontalLayout_14.addWidget(self.label_artfav)
        self.verticalLayout_4.addWidget(self.widget_left_t7)
        self.verticalLayout_2.addWidget(self.widget_left_t4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 144, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.widget_3 = QtWidgets.QWidget(self.widget_left)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_left_b1 = QtWidgets.QLabel(self.widget_3)
        self.label_left_b1.setMinimumSize(QtCore.QSize(200, 200))
        self.label_left_b1.setMaximumSize(QtCore.QSize(200, 200))
        self.label_left_b1.setText("")
        self.label_left_b1.setTextFormat(QtCore.Qt.AutoText)
        self.label_left_b1.setPixmap(QtGui.QPixmap(":/images/demo1.png"))
        self.label_left_b1.setScaledContents(True)
        self.label_left_b1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_left_b1.setOpenExternalLinks(False)
        self.label_left_b1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_left_b1.setObjectName("label_left_b1")
        self.horizontalLayout_10.addWidget(self.label_left_b1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout_2.addWidget(self.widget_left)
        self.widget_right = QtWidgets.QWidget(self.widget_down)
        self.widget_right.setStyleSheet("QWidget#widget_right{background:#FFFFFF;border-bottom-right-radius:2px;}")
        self.widget_right.setObjectName("widget_right")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_right)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_right)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane{border-top-width:1px;border-style:solid;border-color:rgba(69,104,220,0.3);background:transparent;}\n"
"QTabWidget::tab-bar{background:transparent;subcontrol-position:left;}\n"
"QTabBar::tab{min-width:70px;min-height:50px;background:transparent;}\n"
"QTabBar::tab:selected{color: rgb(69,104,220);background-color:rgba(240,245,255,0.8);}\n"
"QTabBar::tab:!selected{color: blank;background:transparent;}\n"
"QTabBar::tab:hover{color: rgb(69,104,220);background-color:rgba(240,245,255,0.8);}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setStyleSheet("QListWidget{background:transparent;border:0px solid grey;margin:10px;}")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_5.addWidget(self.listWidget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_vtot = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_vtot.setFont(font)
        self.label_vtot.setText("")
        self.label_vtot.setObjectName("label_vtot")
        self.horizontalLayout_11.addWidget(self.label_vtot)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.pushButton_vrenew = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_vrenew.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_vrenew.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_vrenew.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(240,245,255,0.8);}")
        self.pushButton_vrenew.setText("")
        self.pushButton_vrenew.setObjectName("pushButton_vrenew")
        self.horizontalLayout_11.addWidget(self.pushButton_vrenew)
        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget_6 = QtWidgets.QWidget(self.tab_3)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listWidget_article = QtWidgets.QListWidget(self.widget_6)
        self.listWidget_article.setStyleSheet("QListWidget{background:transparent;border:0px solid grey;margin:10px;}")
        self.listWidget_article.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_article.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_article.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_article.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_article.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_article.setObjectName("listWidget_article")
        self.gridLayout_6.addWidget(self.listWidget_article, 1, 0, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_atot = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_atot.setFont(font)
        self.label_atot.setText("")
        self.label_atot.setObjectName("label_atot")
        self.horizontalLayout_12.addWidget(self.label_atot)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.pushButton_arenew = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_arenew.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_arenew.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_arenew.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(240,245,255,0.8);}")
        self.pushButton_arenew.setText("")
        self.pushButton_arenew.setObjectName("pushButton_arenew")
        self.horizontalLayout_12.addWidget(self.pushButton_arenew)
        self.gridLayout_6.addWidget(self.widget_7, 0, 0, 1, 1)
        self.horizontalLayout_15.addWidget(self.widget_6)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.widget_8 = QtWidgets.QWidget(self.tab_4)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.listWidget_reply = QtWidgets.QListWidget(self.widget_8)
        self.listWidget_reply.setStyleSheet("QListWidget{background:transparent;border:0px solid grey;margin:10px;}")
        self.listWidget_reply.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_reply.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_reply.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_reply.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_reply.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_reply.setObjectName("listWidget_reply")
        self.gridLayout_7.addWidget(self.listWidget_reply, 1, 0, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.widget_8)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_rtot = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_rtot.setFont(font)
        self.label_rtot.setText("")
        self.label_rtot.setObjectName("label_rtot")
        self.horizontalLayout_17.addWidget(self.label_rtot)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem4)
        self.pushButton_rrenew = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_rrenew.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_rrenew.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_rrenew.setStyleSheet("QPushButton{background:Transparent;border:0px solid grey;}QPushButton:hover{background-color:rgba(240,245,255,0.8);}")
        self.pushButton_rrenew.setText("")
        self.pushButton_rrenew.setObjectName("pushButton_rrenew")
        self.horizontalLayout_17.addWidget(self.pushButton_rrenew)
        self.gridLayout_7.addWidget(self.widget_10, 0, 0, 1, 1)
        self.horizontalLayout_18.addWidget(self.widget_8)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_right)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.gridLayout_2.addWidget(self.widget_down, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "哔哩哔哩UP主助手"))
        self.label_face.setToolTip(_translate("MainWindow", "<html><head/><body><p>头像</p></body></html>"))
        self.pushButton_nickname.setToolTip(_translate("MainWindow", "<html><head/><body><p>点击打开个人主页</p></body></html>"))
        self.pushButton_notify.setText(_translate("MainWindow", "暂无通知消息"))
        self.pushButton_feedback.setToolTip(_translate("MainWindow", "<html><head/><body><p>反馈与建议</p></body></html>"))
        self.pushButton_min.setToolTip(_translate("MainWindow", "<html><head/><body><p>最小化</p></body></html>"))
        self.pushButton_max.setToolTip(_translate("MainWindow", "<html><head/><body><p>窗口最大化</p></body></html>"))
        self.pushButton_close.setToolTip(_translate("MainWindow", "<html><head/><body><p>关闭</p></body></html>"))
        self.label_level.setText(_translate("MainWindow", "等级"))
        self.label_exp.setText(_translate("MainWindow", "0/∞"))
        self.pushButton_coin.setText(_translate("MainWindow", "硬币："))
        self.pushButton_balance.setText(_translate("MainWindow", "电池："))
        self.label_3.setText(_translate("MainWindow", "电磁力"))
        self.label_creative.setText(_translate("MainWindow", "创作力\n"
"0"))
        self.label_influence.setText(_translate("MainWindow", "影响力\n"
"0"))
        self.label_credit.setText(_translate("MainWindow", "信用分\n"
"0"))
        self.label.setText(_translate("MainWindow", "视频稿件"))
        self.label_follower.setText(_translate("MainWindow", "粉丝\n"
"0"))
        self.label_view.setText(_translate("MainWindow", "播放\n"
"0"))
        self.label_like.setText(_translate("MainWindow", "点赞\n"
"0"))
        self.label_coin.setText(_translate("MainWindow", "投币\n"
"0"))
        self.label_reply.setText(_translate("MainWindow", "评论\n"
"0"))
        self.label_danmaku.setText(_translate("MainWindow", "弹幕\n"
"0"))
        self.label_share.setText(_translate("MainWindow", "分享\n"
"0"))
        self.label_favorite.setText(_translate("MainWindow", "收藏\n"
"0"))
        self.label_2.setText(_translate("MainWindow", "专栏文章"))
        self.label_artview.setText(_translate("MainWindow", "阅读量\n"
"0"))
        self.label_artlike.setText(_translate("MainWindow", "点赞\n"
"0"))
        self.label_artcoin.setText(_translate("MainWindow", "投币\n"
"0"))
        self.label_artreply.setText(_translate("MainWindow", "评论\n"
"0"))
        self.label_artshare.setText(_translate("MainWindow", "分享\n"
"0"))
        self.label_artfav.setText(_translate("MainWindow", "收藏\n"
"0"))
        self.pushButton_vrenew.setToolTip(_translate("MainWindow", "<html><head/><body><p>刷新</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "视频稿件"))
        self.pushButton_arenew.setToolTip(_translate("MainWindow", "<html><head/><body><p>刷新</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "专栏文章"))
        self.pushButton_rrenew.setToolTip(_translate("MainWindow", "<html><head/><body><p>刷新</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "评论管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "弹幕管理"))
import resources_rc