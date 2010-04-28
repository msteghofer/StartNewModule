import wx

class HelpDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: HelpDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        
        text = ""
        text += "1. Put the name you want for your module in field Name\n"
        text += "2. Set the root path to your module:\n"
        text += "    * for type \"library\" gimiasSRC/src/cilabModules\n"
        text += "    * for type \"Gimias Plugin\" gimiasSRC/src/Apps/Plugins\n"
        text += "    * for type \"Gimias Plugin widget\" gimiasSRC/src/Apps/Plugins/YourPlugin\n"
        text += "3. Select Type \"library\" or \"Gimias Plugin\" or \"Gimias Plugin widget\"\n"
        text += "4. (for type \"library\" and \"Gimias Plugin\" only) Set Toolkit csn file to your gimiasSRC/src/csnCISTIBToolkit.py\n"
        text += "5. (for type \"Gimias Plugin\" only) Set your Gimias csn file to your gimiasSRC/src/Apps/csnGIMIASOS.py\n"
        text += "6. Press on StartNewModule\n"

        self.textBasicHelp = wx.TextCtrl(self, -1, text, style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: HelpDialog.__set_properties
        self.SetTitle("Basic Help")
        self.SetSize((400, 200))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: HelpDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.textBasicHelp, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade