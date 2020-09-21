import wx
import time
import random

class FlashPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.label = 'changing fkndjnksjnd'
        self.flashing_text = wx.StaticText(self, label=self.label)
        self.flashing_text.SetFont(self.font)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)

        self.timer.Start(100)

    def update(self, event):
        colors = [(3, 152, 252, 244)]
        self.flashing_text.SetLabel(self.label)
        self.flashing_text.SetForegroundColour(random.choice(colors))

class FlashFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='cooltown')
        self.panel = FlashPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = FlashFrame()
    app.MainLoop()