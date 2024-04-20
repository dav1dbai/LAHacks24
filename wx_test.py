import wx
import wx.adv
import math
import random
import time

class TextPanel(wx.Panel):
    def __init__(self, parent, text):
        super(TextPanel, self).__init__(parent)

        # Create a static text control to display the text
        self.static_text = wx.StaticText(self, label=text)

        # Set up sizer to arrange the controls
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.static_text, 0, wx.ALL | wx.EXPAND, 10)  # Constrain vertical expansion
        self.SetSizer(sizer)

class Sprite(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Shaped Window",
                style = wx.STAY_ON_TOP | wx.FRAME_SHAPED | wx.SIMPLE_BORDER )
        #self.hasShape = True
        
        #movement
        self.delta = wx.Point(0,0)
    
        self.text = "hello!"
        self.panel = TextPanel(self,self.text)

        #gif translation
        self.frame = 0
        self.max_frame = 7
        self.updateImage()
    
        #positions
        self.win = self.GetScreenPosition()
        self.screen_size = wx.DisplaySize()[0]

        #event bindings
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.Bind(wx.EVT_RIGHT_UP, self.OnExit)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)

        #self.anim = wx.adv.Animation('./assets/testtrans.gif')
        #self.anim_ctrl = wx.adv.AnimationCtrl(self, -1, self.anim)
        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(self.anim_ctrl)
        #self.SetSizerAndFit(sizer)
        #self.Show()
        #self.anim_ctrl.Play()

    def updateImage(self):
        self.imgpath = rf'./assets/{self.frame}.png'
        image = wx.Image(self.imgpath)          
        self.bmp = wx.Bitmap(image)
        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        self.dc = wx.ClientDC(self)
        self.dc.DrawBitmap(self.bmp, 0,0, True)
        self.SetWindowShape()

    def SetWindowShape(self, evt=None):
        r = wx.Region(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)

    def OnExit(self, evt):
        self.Close()

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def updateCoords(self):
        self.screen_size = wx.DisplaySize()
        self.win = self.GetScreenPosition()

    def traverse(self):
        self.updateCoords()
        dest_x = random.randint(int(self.screen_size[0]*0.1),int(self.screen_size[0]*0.9))
        dest_y = random.randint(int(self.screen_size[0]*0.1),int(self.screen_size[1]*0.9))
        dx = dest_x - self.win.x
        dy = dest_y - self.win.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance != 0:
            dx_unit = dx / distance
            dy_unit = dy / distance
        else:
            dx_unit, dy_unit = 0, 0

        steps = int(distance)
        for step in range(steps):
            # Calculate the new position based on the step along the trajectory
            x = self.win[0] + int(step * dx_unit)
            y = self.win[1] + int(step * dy_unit)
            # Move the root window to the new position
            if step % 9 == 0:
                self.updateImage()
                self.frame += 1
                self.frame = self.frame % self.max_frame
            p = wx.Point(x,y)
            self.Move(p)
            wx.GetApp().Yield()
            time.sleep(0.01)


if __name__ == '__main__':
    app = wx.App()
    s = Sprite()
    s.Show()
    while True:
        s.traverse()
    app.MainLoop()