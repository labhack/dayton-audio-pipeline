#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnAdd_clicked()
{
    if(ui->txtCommand->text().isEmpty())
        return;
    ui->lstCommands->addItem(ui->txtCommand->text());
}

void MainWindow::on_btnRemove_clicked()
{
    if(ui->lstCommands->selectedItems().count() == 0)
        return;
    qDeleteAll(ui->lstCommands->selectedItems());
}

void MainWindow::on_btnRun_clicked()
{
    if(ui->lstCommands->count() == 0)
        return;
    for(int i = 0; i < ui->lstCommands->count(); i++)
    {
        QListWidgetItem* item = ui->lstCommands->item(i);
        system(item->text().toStdString().c_str());
    }

}
