import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sv_ttk

class WindowLoader (tk.Frame):
    def __init__(self, master, MenuFont, EntryFont):
        super().__init__ (master)
        self.master = master
        self.MenuFont = MenuFont
        self.EntryFont = EntryFont
        self.pack()
        self.MainWindow()
    # 主函数
    def MainWindow(self):

        def SaveFiles():
            SaveFilesName = filedialog.asksaveasfilename(
                title="保存文件",
                initialdir=r"doc",
                filetypes=[("文本文档", ".txt"), ("HTML超文本", ".html .htm"), ("LightNoteBook专用", ".lnb"), ("测试页文件", ".test .中文测试")],
                defaultextension=".lnb"
            )
            MainTextVar = self.MainText.get("1.0", tk.END)
            SaveFilesDo = open(SaveFilesName, "w")
            SaveFilesDo.write(MainTextVar)
            SaveFilesDo.close()
            # 保存文件
        def OpenFile():
            OpenFileName = filedialog.askopenfilename(
                title="打开文件",
                initialdir=r"doc",
                filetypes=[("文本文档", ".txt"), ("HTML超文本", ".html .htm"), ("LightNoteBook专用", ".lnb"), ("测试页文件", ".test .中文测试")]
            )
            OpenFileDo = open(OpenFileName, "r")
            OpenFileVar = OpenFileDo.read()
            self.MainText.insert(tk.INSERT, OpenFileVar)
            # 打开文件


        self.MenuBar = tk.Menu(self)
        Window.config(menu=self.MenuBar)
        # 菜单条
        self.MenuFiles = tk.Menu(self.MenuBar, tearoff=False)
        self.MenuEdit = tk.Menu(self.MenuBar, tearoff=False)
        self.MenuOptions = tk.Menu(self.MenuBar, tearoff=False)
        self.MenuMore = tk.Menu(self.MenuBar, tearoff=False)
        # 创建菜单选项
        self.MenuFiles.add_command(label="新建[alt+n]", font=self.MenuFont)
        self.MenuFiles.add_command(label="打开[alt+o]", font=self.MenuFont, command=OpenFile)
        self.MenuFiles.add_command(label="保存[alt+s]", font=self.MenuFont, command=SaveFiles)
        self.MenuFiles.add_command(label="保存为...[alt+a]", font=self.MenuFont)
        self.MenuFiles.add_command(label="新窗口[alt+w]", font=self.MenuFont)
        self.MenuFiles.add_command(label="关闭[alt+x]", font=self.MenuFont)
        # MenuFiles的选项
        self.MenuEdit.add_command(label="撤回一步[ctrl+z]", font=self.MenuFont)
        self.MenuEdit.add_command(label="前进一步[ctrl+y]", font=self.MenuFont)
        self.MenuEdit.add_command(label="全选[alt+l]", font=self.MenuFont)
        self.MenuEdit.add_command(label="剪切[ctrl+x]", font=self.MenuFont)
        self.MenuEdit.add_command(label="复制[ctrl+c]", font=self.MenuFont)
        self.MenuEdit.add_command(label="粘贴[ctrl+v]", font=self.MenuFont)
        self.MenuEdit.add_command(label="删除[alt+d]", font=self.MenuFont)
        self.MenuEdit.add_command(label="插入富文本[alt+r]", font=self.MenuFont)
        # MenuEdit的选项
        self.MenuOptions.add_command(label="设置[alt+e]", font=self.MenuFont)
        self.MenuOptions.add_command(label="设为默认.txt程序", font=self.MenuFont)
        self.MenuOptions.add_command(label="打印[alt+p]", font=self.MenuFont)
        # MenuOptions的选项
        self.MenuMore.add_command(label="关于", font=self.MenuFont)
        self.MenuMore.add_command(label="官网", font=self.MenuFont)
        self.MenuMore.add_command(label="帮助", font=self.MenuFont)
        self.MenuMore.add_command(label="测试页", font=self.MenuFont)
        # MenuMore的选项
        self.MenuBar.add_cascade(label="文件", menu=self.MenuFiles)
        self.MenuBar.add_cascade(label="编辑", menu=self.MenuEdit)
        self.MenuBar.add_cascade(label="选项", menu=self.MenuOptions)
        self.MenuBar.add_cascade(label="更多", menu=self.MenuMore)
        # 菜单选项
        self.ToolsView = ttk.Labelframe(self, text="编辑栏", height=100, width=700, relief="groove")
        self.ToolsView.pack(side="top", anchor="n", padx=10, pady=10)
        self.ToolsView.pack_propagate(False)
        # 顶部工具栏
        self.FontKinds = ttk.Combobox(self.ToolsView, height=10, width=12)
        self.FontKinds.pack(side="top", anchor="w", padx=10, pady=10)
        # 字体选择器
        self.MainTextBar = ttk.Scrollbar(self)
        self.MainTextBar.pack(side="right", fill="y")
        # 主文本编辑框侧边条
        self.MainText = tk.Text(self, height=400, width=700, font=self.EntryFont, bg="#ffffff", tabs="1c", spacing1=5, spacing2=5, spacing3=5)
        self.MainText.pack(padx=10, pady=10)
        self.MainText.config(yscrollcommand=self.MainTextBar.set)
        # 主文本编辑框
        self.MainTextBar.config(command=self.MainText.yview)
        # 绑定侧边条


    # 主窗口函数

if __name__ == "__main__":
    Window = tk.Tk()
    App = WindowLoader(master=Window, MenuFont=("黑体",9), EntryFont=("等线", 13))
    Window.geometry("700x500")
    Window.title("LightNoteBook - 轻量记事本")
    Window.iconbitmap("icon\\WindowIcon.ico")
    # 实例化tkinter窗口主函数
    sv_ttk.set_theme("light")
    # 调用sv-ttk包,并调用light.tcl
    Window.mainloop()
    # tkinter窗口主函数终止