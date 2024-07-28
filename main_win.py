from PySide6.QtWidgets import QMainWindow,QListWidgetItem
from PySide6.QtCore import Qt,QDateTime
from UI.MainWindow import Ui_MainWindow
from DAL import DBH

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gotostack(1)
        self.init()
        self.windowFun()
    #信号和槽
    def init(self):
        self.closeBtn.clicked.connect(self.close)
        self.hiding.clicked.connect(self.showMinimized)
        self.enlarge.clicked.connect(self.showMaximized)

        self.event.clicked.connect(lambda: self.gotostack(1))
        self.add.clicked.connect(lambda: self.gotostack(2))
        self.four.clicked.connect(lambda: self.gotostack(0))

        self.save_btn.clicked.connect(self.add_data)

        self.list1.itemClicked.connect(self.Edit_event)
        self.list2.itemClicked.connect(self.Edit_event)
        self.list3.itemClicked.connect(self.Edit_event)
        self.list4.itemClicked.connect(self.Edit_event)
    def gotostack(self,index):
        if index==1:

            self.list1.clear()
            self.list2.clear()
            self.list3.clear()
            self.list4.clear()
            self.FQD()
        if index==2:
            self.dateEdit(1)
        self.stackedWidget.setCurrentIndex(index)


    #四象限
    def FQD(self):
        DBH.update_due()
        records = DBH.select_event()
        for record in records:
            id=record[0]
            event=record[1]
            sort=record[2]
            pt=record[3]
            item = QListWidgetItem(event)
            item.setData(Qt.UserRole,id)
            if sort<=2:
                if pt <=2:
                    self.list1.addItem(item)
                else:
                    self.list2.addItem(item)
            else:
                if pt <= 2:
                    self.list4.addItem(item)
                else:
                    self.list3.addItem(item)




    #编辑任务
    def Edit_event(self, item):
        self.gotostack(0)
        id = item.data(Qt.UserRole)
        record = DBH.select_edit(id)
        r = record[0]
        print(r)

        self.event_txt.setText(str(r[1]))
        self.textEdit.setText(str(r[2]))
        self.date_edit(r[3])

        print("r4=",r[4])
        if 1==int(r[4]):
            self.label_16.setText("已完成")
            self.checkBox.setChecked(True)
        self.save_btn_2.clicked.connect(lambda: self.update_data(id))
        self.delete_btn.clicked.connect(lambda: DBH.delete_record(id))
        self.delete_btn.clicked.connect(self.clear_edit)
        self.radiobtn_data(r[5])
    def update_data(self,id):
        event = self.event_txt.text()
        description = self.textEdit.toPlainText()
        due_date = self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd HH:mm')
        status = self.checkBox.isChecked()
        sort = self.check_Rbtn(0)
        Pt = self.calculate_remaining_time(0)
        DBH.update_record(id,event,description,due_date,status,sort,Pt)
        print("编辑成功")

    def radiobtn_data(self, n):
        if n == 1:
            self.radioButton.setChecked(True)
        if n == 2:
            self.radioButton.setChecked(True)
        if n == 3:
            self.radioButton.setChecked(True)
        if n == 4:
            self.radioButton.setChecked(True)
    def date_edit(self,date_str):
        date=QDateTime.fromString(date_str,'yyyy-MM-dd HH:mm')
        self.dateTimeEdit_2.setDateTime(date)
    def clear_edit(self):
        self.event_txt.clear()
        self.textEdit.clear()
        self.dateEdit(0)


    #添加任务
    def add_data(self):

        event=self.Event_txt.text()
        description=self.des_txt.toPlainText()
        due_date=self.dateTimeEdit.dateTime().toString('yyyy-MM-dd HH:mm')
        status=self.status_check.isChecked()
        IM=self.check_Rbtn(1)
        Pt=self.calculate_remaining_time(1)
        DBH.save_data(event,description,due_date,status,IM,Pt)
        print("添加成功")
        self.Event_txt.clear()
        self.des_txt.clear()
        self.dateEdit(1)
        self.status_check.setChecked(False)
    def calculate_remaining_time(self,flog):
        if flog==1:
            selected_date_time = self.dateTimeEdit.dateTime()
        else:
            selected_date_time = self.dateTimeEdit_2.dateTime()
        remaining_time = selected_date_time.toSecsSinceEpoch() - QDateTime.currentDateTime().toSecsSinceEpoch()
        remaining_days = remaining_time // (24 * 3600)
        return remaining_days
    def check_Rbtn(self,flog):
        if flog==1:
            if self.RBtn1.isChecked()==True:
                return 1
            if self.RBtn2.isChecked()==True:
                return 2
            if self.RBtn3.isChecked()==True:
                return 3
            if self.RBtn4.isChecked()==True:
                return 4
        else:
            if self.radioButton.isChecked() == True:
                return 1
            if self.radioButton_2.isChecked() == True:
                return 2
            if self.radioButton_3.isChecked() == True:
                return 3
            if self.radioButton_4.isChecked() == True:
                return 4
    def windowFun(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    def dateEdit(self,flog):
        current_datetime=QDateTime.currentDateTime()
        if flog==1:
            self.dateTimeEdit.setMinimumDateTime(current_datetime)
        else:
            self.dateTimeEdit_2.setMinimumDateTime(current_datetime)

