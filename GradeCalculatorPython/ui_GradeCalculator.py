# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GradeCalculatorGUItvoQPj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1445, 514)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 343, 416))
        self.hwVertLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.hwVertLayout.setObjectName(u"hwVertLayout")
        self.hwVertLayout.setContentsMargins(0, 0, 0, 0)
        self.hwLabel = QLabel(self.verticalLayoutWidget)
        self.hwLabel.setObjectName(u"hwLabel")
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.hwLabel.setFont(font)
        self.hwLabel.setLayoutDirection(Qt.LeftToRight)

        self.hwVertLayout.addWidget(self.hwLabel)

        self.hw1HorizLayout = QHBoxLayout()
        self.hw1HorizLayout.setObjectName(u"hw1HorizLayout")
        self.hw1Label = QLabel(self.verticalLayoutWidget)
        self.hw1Label.setObjectName(u"hw1Label")

        self.hw1HorizLayout.addWidget(self.hw1Label)

        self.hw1DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw1DoubleSpinBox.setObjectName(u"hw1DoubleSpinBox")

        self.hw1HorizLayout.addWidget(self.hw1DoubleSpinBox)

        self.hw1CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw1CheckBox.setObjectName(u"hw1CheckBox")

        self.hw1HorizLayout.addWidget(self.hw1CheckBox)


        self.hwVertLayout.addLayout(self.hw1HorizLayout)

        self.hw2HorizLayout = QHBoxLayout()
        self.hw2HorizLayout.setObjectName(u"hw2HorizLayout")
        self.hw2Label = QLabel(self.verticalLayoutWidget)
        self.hw2Label.setObjectName(u"hw2Label")

        self.hw2HorizLayout.addWidget(self.hw2Label)

        self.hw2DoubleSpinBox_2 = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw2DoubleSpinBox_2.setObjectName(u"hw2DoubleSpinBox_2")

        self.hw2HorizLayout.addWidget(self.hw2DoubleSpinBox_2)

        self.hw2CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw2CheckBox.setObjectName(u"hw2CheckBox")

        self.hw2HorizLayout.addWidget(self.hw2CheckBox)


        self.hwVertLayout.addLayout(self.hw2HorizLayout)

        self.hw3HorizLayout = QHBoxLayout()
        self.hw3HorizLayout.setObjectName(u"hw3HorizLayout")
        self.hw3Label = QLabel(self.verticalLayoutWidget)
        self.hw3Label.setObjectName(u"hw3Label")

        self.hw3HorizLayout.addWidget(self.hw3Label)

        self.hw2DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw2DoubleSpinBox.setObjectName(u"hw2DoubleSpinBox")

        self.hw3HorizLayout.addWidget(self.hw2DoubleSpinBox)

        self.hw3CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw3CheckBox.setObjectName(u"hw3CheckBox")

        self.hw3HorizLayout.addWidget(self.hw3CheckBox)


        self.hwVertLayout.addLayout(self.hw3HorizLayout)

        self.hw4HorizLayout = QHBoxLayout()
        self.hw4HorizLayout.setObjectName(u"hw4HorizLayout")
        self.hw4Label = QLabel(self.verticalLayoutWidget)
        self.hw4Label.setObjectName(u"hw4Label")

        self.hw4HorizLayout.addWidget(self.hw4Label)

        self.hw4DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw4DoubleSpinBox.setObjectName(u"hw4DoubleSpinBox")

        self.hw4HorizLayout.addWidget(self.hw4DoubleSpinBox)

        self.hw4CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw4CheckBox.setObjectName(u"hw4CheckBox")

        self.hw4HorizLayout.addWidget(self.hw4CheckBox)


        self.hwVertLayout.addLayout(self.hw4HorizLayout)

        self.hw5HorizLayout = QHBoxLayout()
        self.hw5HorizLayout.setObjectName(u"hw5HorizLayout")
        self.hw5Label = QLabel(self.verticalLayoutWidget)
        self.hw5Label.setObjectName(u"hw5Label")

        self.hw5HorizLayout.addWidget(self.hw5Label)

        self.hw5DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw5DoubleSpinBox.setObjectName(u"hw5DoubleSpinBox")

        self.hw5HorizLayout.addWidget(self.hw5DoubleSpinBox)

        self.hw5CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw5CheckBox.setObjectName(u"hw5CheckBox")

        self.hw5HorizLayout.addWidget(self.hw5CheckBox)


        self.hwVertLayout.addLayout(self.hw5HorizLayout)

        self.hw6HorizLayout = QHBoxLayout()
        self.hw6HorizLayout.setObjectName(u"hw6HorizLayout")
        self.hw6Label = QLabel(self.verticalLayoutWidget)
        self.hw6Label.setObjectName(u"hw6Label")

        self.hw6HorizLayout.addWidget(self.hw6Label)

        self.hw6DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw6DoubleSpinBox.setObjectName(u"hw6DoubleSpinBox")

        self.hw6HorizLayout.addWidget(self.hw6DoubleSpinBox)

        self.hw6CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw6CheckBox.setObjectName(u"hw6CheckBox")

        self.hw6HorizLayout.addWidget(self.hw6CheckBox)


        self.hwVertLayout.addLayout(self.hw6HorizLayout)

        self.hw7HorizLayout = QHBoxLayout()
        self.hw7HorizLayout.setObjectName(u"hw7HorizLayout")
        self.hw7Label = QLabel(self.verticalLayoutWidget)
        self.hw7Label.setObjectName(u"hw7Label")

        self.hw7HorizLayout.addWidget(self.hw7Label)

        self.hw7DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw7DoubleSpinBox.setObjectName(u"hw7DoubleSpinBox")

        self.hw7HorizLayout.addWidget(self.hw7DoubleSpinBox)

        self.hw7CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw7CheckBox.setObjectName(u"hw7CheckBox")

        self.hw7HorizLayout.addWidget(self.hw7CheckBox)


        self.hwVertLayout.addLayout(self.hw7HorizLayout)

        self.hw8HorizLayout = QHBoxLayout()
        self.hw8HorizLayout.setObjectName(u"hw8HorizLayout")
        self.hw8Label = QLabel(self.verticalLayoutWidget)
        self.hw8Label.setObjectName(u"hw8Label")

        self.hw8HorizLayout.addWidget(self.hw8Label)

        self.hw8DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw8DoubleSpinBox.setObjectName(u"hw8DoubleSpinBox")

        self.hw8HorizLayout.addWidget(self.hw8DoubleSpinBox)

        self.hw8CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw8CheckBox.setObjectName(u"hw8CheckBox")

        self.hw8HorizLayout.addWidget(self.hw8CheckBox)


        self.hwVertLayout.addLayout(self.hw8HorizLayout)

        self.hw9HorizLayout = QHBoxLayout()
        self.hw9HorizLayout.setObjectName(u"hw9HorizLayout")
        self.hw9Label = QLabel(self.verticalLayoutWidget)
        self.hw9Label.setObjectName(u"hw9Label")

        self.hw9HorizLayout.addWidget(self.hw9Label)

        self.hw9DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw9DoubleSpinBox.setObjectName(u"hw9DoubleSpinBox")

        self.hw9HorizLayout.addWidget(self.hw9DoubleSpinBox)

        self.hw9CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw9CheckBox.setObjectName(u"hw9CheckBox")

        self.hw9HorizLayout.addWidget(self.hw9CheckBox)


        self.hwVertLayout.addLayout(self.hw9HorizLayout)

        self.hw10HorizLayout = QHBoxLayout()
        self.hw10HorizLayout.setObjectName(u"hw10HorizLayout")
        self.hw10Label = QLabel(self.verticalLayoutWidget)
        self.hw10Label.setObjectName(u"hw10Label")

        self.hw10HorizLayout.addWidget(self.hw10Label)

        self.hw10DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.hw10DoubleSpinBox.setObjectName(u"hw10DoubleSpinBox")

        self.hw10HorizLayout.addWidget(self.hw10DoubleSpinBox)

        self.hw10CheckBox = QCheckBox(self.verticalLayoutWidget)
        self.hw10CheckBox.setObjectName(u"hw10CheckBox")

        self.hw10HorizLayout.addWidget(self.hw10CheckBox)


        self.hwVertLayout.addLayout(self.hw10HorizLayout)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(370, 30, 343, 416))
        self.vertLayout2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vertLayout2.setObjectName(u"vertLayout2")
        self.vertLayout2.setContentsMargins(0, 0, 0, 0)
        self.projectsLabel = QLabel(self.verticalLayoutWidget_2)
        self.projectsLabel.setObjectName(u"projectsLabel")
        self.projectsLabel.setFont(font)
        self.projectsLabel.setLayoutDirection(Qt.LeftToRight)

        self.vertLayout2.addWidget(self.projectsLabel)

        self.projHorizLayout = QHBoxLayout()
        self.projHorizLayout.setObjectName(u"projHorizLayout")
        self.projLabel = QLabel(self.verticalLayoutWidget_2)
        self.projLabel.setObjectName(u"projLabel")

        self.projHorizLayout.addWidget(self.projLabel)

        self.projDoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.projDoubleSpinBox.setObjectName(u"projDoubleSpinBox")

        self.projHorizLayout.addWidget(self.projDoubleSpinBox)

        self.projCheckBox = QCheckBox(self.verticalLayoutWidget_2)
        self.projCheckBox.setObjectName(u"projCheckBox")

        self.projHorizLayout.addWidget(self.projCheckBox)


        self.vertLayout2.addLayout(self.projHorizLayout)

        self.assign1HorizLayout = QHBoxLayout()
        self.assign1HorizLayout.setObjectName(u"assign1HorizLayout")
        self.assign1Label = QLabel(self.verticalLayoutWidget_2)
        self.assign1Label.setObjectName(u"assign1Label")

        self.assign1HorizLayout.addWidget(self.assign1Label)

        self.assign1DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.assign1DoubleSpinBox.setObjectName(u"assign1DoubleSpinBox")

        self.assign1HorizLayout.addWidget(self.assign1DoubleSpinBox)

        self.assign1CheckBox = QCheckBox(self.verticalLayoutWidget_2)
        self.assign1CheckBox.setObjectName(u"assign1CheckBox")

        self.assign1HorizLayout.addWidget(self.assign1CheckBox)


        self.vertLayout2.addLayout(self.assign1HorizLayout)

        self.assign2HorizLayout = QHBoxLayout()
        self.assign2HorizLayout.setObjectName(u"assign2HorizLayout")
        self.assign2Label_ = QLabel(self.verticalLayoutWidget_2)
        self.assign2Label_.setObjectName(u"assign2Label_")

        self.assign2HorizLayout.addWidget(self.assign2Label_)

        self.assign2DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.assign2DoubleSpinBox.setObjectName(u"assign2DoubleSpinBox")

        self.assign2HorizLayout.addWidget(self.assign2DoubleSpinBox)

        self.assign2CheckBox = QCheckBox(self.verticalLayoutWidget_2)
        self.assign2CheckBox.setObjectName(u"assign2CheckBox")

        self.assign2HorizLayout.addWidget(self.assign2CheckBox)


        self.vertLayout2.addLayout(self.assign2HorizLayout)

        self.assign3HorizLayout = QHBoxLayout()
        self.assign3HorizLayout.setObjectName(u"assign3HorizLayout")
        self.assign3Label = QLabel(self.verticalLayoutWidget_2)
        self.assign3Label.setObjectName(u"assign3Label")

        self.assign3HorizLayout.addWidget(self.assign3Label)

        self.assign3DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.assign3DoubleSpinBox.setObjectName(u"assign3DoubleSpinBox")

        self.assign3HorizLayout.addWidget(self.assign3DoubleSpinBox)

        self.assign3CheckBox = QCheckBox(self.verticalLayoutWidget_2)
        self.assign3CheckBox.setObjectName(u"assign3CheckBox")

        self.assign3HorizLayout.addWidget(self.assign3CheckBox)


        self.vertLayout2.addLayout(self.assign3HorizLayout)

        self.midProjHorizLayout = QHBoxLayout()
        self.midProjHorizLayout.setObjectName(u"midProjHorizLayout")
        self.midProjLabel = QLabel(self.verticalLayoutWidget_2)
        self.midProjLabel.setObjectName(u"midProjLabel")

        self.midProjHorizLayout.addWidget(self.midProjLabel)

        self.midProjDoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.midProjDoubleSpinBox.setObjectName(u"midProjDoubleSpinBox")

        self.midProjHorizLayout.addWidget(self.midProjDoubleSpinBox)

        self.midProjCheckBox = QCheckBox(self.verticalLayoutWidget_2)
        self.midProjCheckBox.setObjectName(u"midProjCheckBox")

        self.midProjHorizLayout.addWidget(self.midProjCheckBox)


        self.vertLayout2.addLayout(self.midProjHorizLayout)

        self.finalProjHorizLayout = QHBoxLayout()
        self.finalProjHorizLayout.setObjectName(u"finalProjHorizLayout")
        self.finalProjLabel = QLabel(self.verticalLayoutWidget_2)
        self.finalProjLabel.setObjectName(u"finalProjLabel")

        self.finalProjHorizLayout.addWidget(self.finalProjLabel)

        self.finalProjDoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.finalProjDoubleSpinBox.setObjectName(u"finalProjDoubleSpinBox")

        self.finalProjHorizLayout.addWidget(self.finalProjDoubleSpinBox)

        self.finalProjCheckBox = QCheckBox(self.verticalLayoutWidget_2)
        self.finalProjCheckBox.setObjectName(u"finalProjCheckBox")

        self.finalProjHorizLayout.addWidget(self.finalProjCheckBox)


        self.vertLayout2.addLayout(self.finalProjHorizLayout)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(720, 30, 343, 231))
        self.examsVertLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.examsVertLayout.setObjectName(u"examsVertLayout")
        self.examsVertLayout.setContentsMargins(0, 0, 0, 0)
        self.examsLabel = QLabel(self.verticalLayoutWidget_3)
        self.examsLabel.setObjectName(u"examsLabel")
        self.examsLabel.setFont(font)
        self.examsLabel.setLayoutDirection(Qt.LeftToRight)

        self.examsVertLayout.addWidget(self.examsLabel)

        self.exam1HorizLayout = QHBoxLayout()
        self.exam1HorizLayout.setObjectName(u"exam1HorizLayout")
        self.exam1Label = QLabel(self.verticalLayoutWidget_3)
        self.exam1Label.setObjectName(u"exam1Label")

        self.exam1HorizLayout.addWidget(self.exam1Label)

        self.exam1DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.exam1DoubleSpinBox.setObjectName(u"exam1DoubleSpinBox")

        self.exam1HorizLayout.addWidget(self.exam1DoubleSpinBox)

        self.exam1CheckBox = QCheckBox(self.verticalLayoutWidget_3)
        self.exam1CheckBox.setObjectName(u"exam1CheckBox")

        self.exam1HorizLayout.addWidget(self.exam1CheckBox)


        self.examsVertLayout.addLayout(self.exam1HorizLayout)

        self.exam2HorizLayout = QHBoxLayout()
        self.exam2HorizLayout.setObjectName(u"exam2HorizLayout")
        self.exam2Label = QLabel(self.verticalLayoutWidget_3)
        self.exam2Label.setObjectName(u"exam2Label")

        self.exam2HorizLayout.addWidget(self.exam2Label)

        self.exam2DoubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.exam2DoubleSpinBox.setObjectName(u"exam2DoubleSpinBox")

        self.exam2HorizLayout.addWidget(self.exam2DoubleSpinBox)

        self.exam2CheckBox = QCheckBox(self.verticalLayoutWidget_3)
        self.exam2CheckBox.setObjectName(u"exam2CheckBox")

        self.exam2HorizLayout.addWidget(self.exam2CheckBox)


        self.examsVertLayout.addLayout(self.exam2HorizLayout)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(720, 270, 341, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gradeDisplayLabel = QLabel(self.horizontalLayoutWidget)
        self.gradeDisplayLabel.setObjectName(u"gradeDisplayLabel")
        self.gradeDisplayLabel.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setWeight(75)
        self.gradeDisplayLabel.setFont(font1)
        self.gradeDisplayLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.gradeDisplayLabel)

        self.gradePrecentLabel = QLabel(self.horizontalLayoutWidget)
        self.gradePrecentLabel.setObjectName(u"gradePrecentLabel")
        self.gradePrecentLabel.setFont(font)
        self.gradePrecentLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.gradePrecentLabel)

        self.calcGradePushButton = QPushButton(self.centralwidget)
        self.calcGradePushButton.setObjectName(u"calcGradePushButton")
        self.calcGradePushButton.setGeometry(QRect(940, 340, 121, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1445, 29))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hwLabel.setText(QCoreApplication.translate("MainWindow", u"Homework", None))
        self.hw1Label.setText(QCoreApplication.translate("MainWindow", u"Homework 1", None))
        self.hw1CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw2Label.setText(QCoreApplication.translate("MainWindow", u"Homework 2", None))
        self.hw2CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw3Label.setText(QCoreApplication.translate("MainWindow", u"Homework 3", None))
        self.hw3CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw4Label.setText(QCoreApplication.translate("MainWindow", u"Homework 4", None))
        self.hw4CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw5Label.setText(QCoreApplication.translate("MainWindow", u"Homework 5", None))
        self.hw5CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw6Label.setText(QCoreApplication.translate("MainWindow", u"Homework 6", None))
        self.hw6CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw7Label.setText(QCoreApplication.translate("MainWindow", u"Homework 7", None))
        self.hw7CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw8Label.setText(QCoreApplication.translate("MainWindow", u"Homework 8", None))
        self.hw8CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw9Label.setText(QCoreApplication.translate("MainWindow", u"Homework 9", None))
        self.hw9CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.hw10Label.setText(QCoreApplication.translate("MainWindow", u"Homework 10", None))
        self.hw10CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.projectsLabel.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.projLabel.setText(QCoreApplication.translate("MainWindow", u"Project Proposal", None))
        self.projCheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.assign1Label.setText(QCoreApplication.translate("MainWindow", u"Assignment 1", None))
        self.assign1CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.assign2Label_.setText(QCoreApplication.translate("MainWindow", u"Assignment 2", None))
        self.assign2CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.assign3Label.setText(QCoreApplication.translate("MainWindow", u"Assignment 3", None))
        self.assign3CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.midProjLabel.setText(QCoreApplication.translate("MainWindow", u"Midterm Project", None))
        self.midProjCheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.finalProjLabel.setText(QCoreApplication.translate("MainWindow", u"Final Project", None))
        self.finalProjCheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.examsLabel.setText(QCoreApplication.translate("MainWindow", u"Exams", None))
        self.exam1Label.setText(QCoreApplication.translate("MainWindow", u"Exam 1", None))
        self.exam1CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.exam2Label.setText(QCoreApplication.translate("MainWindow", u"Exam 2", None))
        self.exam2CheckBox.setText(QCoreApplication.translate("MainWindow", u"Graded", None))
        self.gradeDisplayLabel.setText(QCoreApplication.translate("MainWindow", u"Num", None))
        self.gradePrecentLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.calcGradePushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate Grade", None))
    # retranslateUi

