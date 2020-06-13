import os
import sys
import tkinter as tk
from tkinter import font, END, Scrollbar


class Sora:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Sora GB2312检测工具')
        self.window.resizable(width=False, height=False)

        self.exec_path = os.path.dirname(sys.path[0])
        self.window.iconbitmap(self.exec_path + r'\Sora.ico')

        self.fontStyle = font.Font(size=12)
        self.input_str_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.input_text = tk.Text(self.window, width=70, height=7, highlightcolor='green', highlightthickness=1)
        self.output_text = tk.Text(self.window, width=70, height=7, highlightcolor='red', highlightthickness=1)
        self.input_scroll = Scrollbar()
        self.output_scroll = Scrollbar()
        self.app()

    def app(self):
        tk.Label(self.window, text="请输入待检测内容:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=8)
        self.input_text.grid(row=1, column=0)
        self.input_scroll.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E)
        self.input_scroll.config(command=self.input_text.yview)
        self.input_text.config(yscrollcommand=self.input_scroll.set)

        tk.Button(self.window, text="执行检测", width=20, height=1,
                  command=self.check_gb2312).grid(row=2, column=0, padx=5, pady=5)

        tk.Label(self.window, text="检测结果:",).grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.output_text.grid(row=4, column=0, padx=10, pady=10)
        self.output_scroll.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E)
        self.output_scroll.config(command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.output_scroll.set)

    def check_gb2312(self):
        error = []
        self.result_var.set("")
        self.output_text.delete('1.0', END)
        content = self.input_text.get('1.0', END).strip('\n')
        if len(content):
            for index, value in enumerate(content):
                try:
                    value.encode("gb2312")
                except UnicodeEncodeError:
                    error.append(value)
            if not error:
                self.result_var.set('检测通过，均在GB2312编码范围内')
            else:
                self.result_var.set('非GB2312内字符: {}'.format(' '.join(error)))
        else:
            self.result_var.set('请输入待检测内容')
        self.output_text.insert(1.0, self.result_var.get())


if __name__ == '__main__':
    root = Sora()
    root.window.mainloop()
