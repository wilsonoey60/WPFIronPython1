import wpf

from System.Windows import Application, Window

class Window1(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Window1.xaml')
        
    def cetakhasil_Click(self, sender, e):
        self.Hasil.Content = "Hello world!"
        pass
       
if __name__ == '__main__':
    Application().Run(MyWindow())