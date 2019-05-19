import os


class IrDataPathUtil():

    def __init__(self):
        self.dataPath = 'E:/Code/ThinkingPython/IrMapTool/IrProvinceData'

    def getDataPath(self):
        return self.dataPath

    def setDataPath(self, data_path):
        self.dataPath = data_path
