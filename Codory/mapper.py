from tkinter import *



class Coordinate(Canvas):
    def __init__(self, master):
        super().__init__(master)
        # 区域内显示的Beat数
        self.beatPerScreen = 1

        self.originWidth = 800
        self.originHeight = 600
        self.width = 800
        self.height = 600

    def Refresh(self, startBeat, track, acc=100):
        """
        刷新并显示v-beat图像
        :param startBeat: 图像的左端点
        :param track: Track对象
        :param acc: 精确度。1beat被分为acc份
        :return:
        """
        # 先计算在原始尺寸下的图像的位置，再在最后用倍率放大图像
        # 绘制网格线
        gridXList = []
        pxPerBeat = self.originWidth / self.beatPerScreen







class Window(Tk):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.coordinateCanvas = Coordinate(self)
        self.coordinateCanvas.place(x=0, y=0)


if __name__ == '__main__':
    window = Window()
    window.setup()
    mainloop()