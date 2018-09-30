#include "mainwindow.h"
#include <QApplication>
#include <QListWidget>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow *w = new MainWindow();
    w->setGeometry(100,100,200,200);
    QListWidget *list = new QListWidget(w);
    list->setGeometry(50,50,100,100);
    QListWidgetItem *item=new QListWidgetItem(list);
    item->setText("方法一");
    list->addItem(item);

    w->show();

    return a.exec();
}
