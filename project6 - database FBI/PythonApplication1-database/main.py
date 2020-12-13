import os
import sys
import logging

from PyQt4 import QtGui, QtCore
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from model import Base
from settings import DATABASE_URL, BASE_PATH

rus = {
    'category': 'категории',
    'item': 'товары',
    'manufacturer': 'производители',
    'order': 'заказы',
    'buyer': 'покупатели',
    'id': 'id',
    'id_item': 'id товара',
    'id_buyer': 'id покупателя',
    'id_category': 'id категории',
    'id_manufacturer': 'id производителя',
    'name': 'Название',
    'nick': 'Имя',
    'email': 'Электронная почта',
    'description': 'Описание',
    'price': 'Цена',
    'count': 'Количество',
}


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)

        self.db_metadata = Base.metadata

        self.main_widget = QtGui.QWidget()
        self.main_layout = QtGui.QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        self.menu_buttons = []
        self.tab_tables = TabTablesWidget()
        self.toolbar = self.addToolBar('Работа с БД')

        self.build_toolbar()
        self.build_widgets()

    def build_toolbar(self):
        """
        Создает меню с интрументами
        """
        add_action = QtGui.QAction(
            QtGui.QIcon('icons/add.png'), 'Добавить новую запись', self
        )
        add_action.triggered.connect(self.add_new_row)

        rm_action = QtGui.QAction(
            QtGui.QIcon('icons/delete.png'), 'Удалить строку', self
        )
        rm_action.triggered.connect(self.remove_row)

        update_action = QtGui.QAction(
            QtGui.QIcon('icons/update.png'), 'Обновить', self
        )
        update_action.triggered.connect(self.update_table_view)

        self.toolbar.addAction(add_action)
        self.toolbar.addAction(rm_action)
        self.toolbar.addAction(update_action)

    def build_widgets(self):
        """
        Создает основные виджеты окна
        """
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(self.create_menu())
        splitter.addWidget(self.create_tabs_area())

        self.main_layout.addWidget(splitter)

    def create_menu(self):
        """
        Создает меню, где отображаются все таблицы БД и из которого можно
        перейти к нужной таблице для редактирования
        """
        menu = QtGui.QFrame(self)
        menu.setLayout(QtGui.QVBoxLayout())
        menu.setFrameShape(QtGui.QFrame.StyledPanel)

        for table_name in self.db_metadata.sorted_tables:
            table_name = table_name.name
            button = QtGui.QPushButton(rus[table_name].capitalize())
            button.clicked.connect(
                lambda event, name=table_name: self.tab_tables.create_tab(name)
            )
            menu.layout().addWidget(button)
        menu.layout().addStretch(len(self.menu_buttons))
        menu.setFixedWidth(menu.sizeHint().width())

        return menu

    def create_tabs_area(self):
        """
        Создает виджет, отображающий открытые для редактирования таблицы
        """
        tabs_area = QtGui.QFrame(self)
        tabs_area.setLayout(QtGui.QVBoxLayout())
        tabs_area.layout().addWidget(self.tab_tables)
        tabs_area.setFrameShape(QtGui.QFrame.StyledPanel)

        return tabs_area

    def add_new_row(self):
        """
        Запускает диалог добавления новой записи в БД
        """
        current_widget = self.tab_tables.current_widget()
        if current_widget:
            self.dialog = DialogAddingNewRecord(current_widget.table)
            self.dialog.button_ok.clicked.connect(
                lambda: current_widget.add_new_row(self.dialog.get_values())
            )
            self.dialog.button_ok.clicked.connect(self.dialog.close)
            self.dialog.exec_()

    def remove_row(self):
        """
        Удаляет выделеную строку из таблицы
        """
        current_widget = self.tab_tables.current_widget()

        if not current_widget:
            return
        elif not current_widget.selected_cell:
            QtGui.QMessageBox.warning(
                self, 'Ошибка', 'Выберите строку, которую хотите удалить',
                QtGui.QMessageBox.Yes
            )
            return

        current_widget.remove_row()

    def update_table_view(self):
        """
        Обновляет данные в таблице (синхронизует таблицу с таблицей БД)
        """
        current_widget = self.tab_tables.current_widget()

        if current_widget:
            current_widget.load_data()


class DatabaseTableView(QtGui.QTableWidget):
    """
    Виджет отображает данные из базы данных и работает непосредственно с БД
    """
    def __init__(self, table_name):
        super(DatabaseTableView, self).__init__()

        self.table_name = table_name
        self.db_metadata = Base.metadata
        self.table = sys.modules['model'].__dict__[table_name.capitalize()]

        self.selected_cell = ()
        self.clicked.connect(self.view_clicked)

        self.setColumnCount(len(self.db_metadata.tables[table_name].columns))
        self.setHorizontalHeaderLabels(
            [rus[i.name] for i in self.db_metadata.tables[table_name].columns]
        )
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.setSortingEnabled(True)

        self.load_data()

    def load_data(self):
        """
        Загружает в таблицу данные из базы данных
        """
        result = session.query(self.table)
        self.setRowCount(result.count())

        for column, data in enumerate(result.all()):
            for row, attr in enumerate(data.__table__.columns.keys()):
                self.setItem(column, row,
                             QtGui.QTableWidgetItem(str(getattr(data, attr)))
                             )

        # self.setRowHeight(0, 10)

    def view_clicked(self, index_clicked):
        self.selected_cell = (index_clicked.row(), index_clicked.column())

    def add_new_row(self, values):
        """
        Добавляет в базу новую запись
        """
        if not values['id']:
            values.pop('id')

        new_record = self.table(**values)
        session.add(new_record)

        try:
            session.commit()
        except Exception:
            session.rollback()
            QtGui.QMessageBox.warning(
                self, 'Ошибка', 'Ошибка добавления данных в БД',
                QtGui.QMessageBox.Yes
            )
        else:
            self.load_data()

    def remove_row(self):
        """
        Удаляет из базы данных выделенную в таблице строку и удаляет
        ее из таблицы
        """
        try:
            id_row = self.item(self.selected_cell[0], 0).text()
        except AttributeError:
            message = 'Выберите строку, котору хотите удалить.'
            QtGui.QMessageBox.warning(
                self, 'Ошибка', message, QtGui.QMessageBox.Yes
            )
            return

        session.query(self.table).filter(self.table.id == id_row).delete()
        try:
            session.commit()
        except Exception:
            session.rollback()
            QtGui.QMessageBox.warning(
                self, 'Ошибка', 'Ошибка удаления данных из БД',
                QtGui.QMessageBox.Yes
            )
        else:
            self.removeRow(self.selected_cell[0])


class TabTablesWidget(QtGui.QTabWidget):
    """
    Виджет для отображения таблиц из базы данных в виде вкладок
    """
    def __init__(self):
        super(TabTablesWidget, self).__init__()
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

        self.all_tabs = {}

    def create_tab(self, table_name):
        """
        Добавляет в окно вкладку
        """
        if table_name in self.all_tabs:
            widget = self.all_tabs[table_name]
        else:
            widget = DatabaseTableView(table_name)
            self.all_tabs[table_name] = widget

        # Добавляем новую вкладку, если она ещё не добавлена
        for widget_index in range(self.count()):
            if self.widget(widget_index).table_name == table_name:
                self.setCurrentIndex(widget_index)
                break
        else:
            self.addTab(widget, rus[table_name].capitalize())
            self.setCurrentIndex(self.count() - 1)

    def close_tab(self, current_index):
        """
        Запускается для удаления вкладки из виджета
        """
        current_widget = self.widget(current_index)
        current_widget.hide()
        self.removeTab(current_index)

    def current_widget(self) -> DatabaseTableView:
        """
        Возвращает текущую таблицу
        """
        current_widget = self.currentWidget()

        if current_widget:
            return current_widget
        else:
            message = 'Не выбрана таблица. Откройте таблицу с которой ' \
                      'хотите работать.'
            QtGui.QMessageBox.warning(
                self, 'Ошибка', message, QtGui.QMessageBox.Yes
            )
            return


class DialogAddingNewRecord(QtGui.QDialog):
    """
    Диалог открывающийся для добавления новой записи в БД
    """
    def __init__(self, table):
        super(DialogAddingNewRecord, self).__init__()

        self.setWindowTitle('Добавление новой записи')
        self.main_layout = QtGui.QGridLayout(self)
        self.button_ok = QtGui.QPushButton('Ok')
        self.button_cancel = QtGui.QPushButton('Отмена')
        self.button_cancel.clicked.connect(self.close)
        self.fields = {}

        self.table = table

        self.build_widgets()

    def build_widgets(self):
        """
        Создает все виджеты отображаемые в диаологе
        """
        columns = self.table.__table__.columns.keys()

        for row, column_name in enumerate(columns):
            label = QtGui.QLabel(rus[column_name] + ':')
            line_edit = QtGui.QLineEdit()
            self.main_layout.addWidget(label, row, 0)
            self.main_layout.addWidget(line_edit, row, 1)

            self.fields[column_name] = [label, line_edit]

        self.main_layout.addWidget(self.button_ok, len(columns), 0)
        self.main_layout.addWidget(self.button_cancel, len(columns), 1)

    def get_values(self):
        """
        Возвращает данные введеные пользователем в поля
        """
        return {i[0]: i[1][1].text() for i in self.fields.items()}


def create_db_session() -> Session:
    """
    Создает сессию работы с БД
    """
    engine = create_engine(DATABASE_URL)
    new_session = sessionmaker(bind=engine)
    return new_session()


def create_sql_logger():
    """
    Создает логгер записывающий все выполняющиеся sql запросы
    """
    logging.basicConfig()
    sql = logging.getLogger('sqlalchemy.engine')
    sql.setLevel(logging.INFO)

    handler = logging.FileHandler(os.path.join(BASE_PATH, 'sql-query-log.log'))
    handler.setLevel(logging.INFO)
    sql.addHandler(handler)


session = create_db_session()
create_sql_logger()

app = QtGui.QApplication(sys.argv)
main_window = MainWindow()
main_window.setWindowTitle('Редактор базы данных')
main_window.setGeometry(0, 0, 700, 400)
main_window.show()
app.exec_()
