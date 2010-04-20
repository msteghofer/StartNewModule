#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.6.3 on Tue Apr 13 14:28:24 2010
import wx
# begin wxGlade: extracode
# end wxGlade

import os
import sys
import CreateNewModule
import logging.config
from about import About

pathToResources = ""

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.mainFrame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "About", "", wx.ITEM_NORMAL)
        self.mainFrame_menubar.Append(wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.mainFrame_menubar)
        # Menu Bar end
        self.mainFrame_statusbar = self.CreateStatusBar(1, 0)
        self.lblProjectRoot = wx.StaticText(self, -1, "Module Root")
        self.txtProjectRoot = wx.TextCtrl(self, -1, "")
        self.btnSelectProjectRoot = wx.Button(self, -1, "...")
        self.textProjectRootHelp = wx.TextCtrl(self, -1, "\"Module Root\" should be the path to your module (ie. ToolkitSrc/src/cilabModules for a library or ToolkitSrc/src/Apps/Plugins for a plugin).", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.lblNewProjectName = wx.StaticText(self, -1, "Name")
        self.txtNewProjectName = wx.TextCtrl(self, -1, "")
        self.lblNewProjectType = wx.StaticText(self, -1, "Type")
        self.cmbNewProjectType = wx.ComboBox(self, -1, choices=["Library", "GIMIAS Plugin", "GIMIAS Plugin Widget"], style=wx.CB_DROPDOWN)
        self.textCreateProjectHelp = wx.TextCtrl(self, -1, "Users at CISTIB should consult the Scientific Development Team before creating a new module.", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.btnCreateProject = wx.Button(self, -1, "Start new Module")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnAbout, id=-1)
        self.Bind(wx.EVT_TEXT, self.OnTypingProjectRoot, self.txtProjectRoot)
        self.Bind(wx.EVT_BUTTON, self.OnSelectProjectRoot, self.btnSelectProjectRoot)
        self.Bind(wx.EVT_BUTTON, self.OnCreateNewProject, self.btnCreateProject)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("StartNewModule")
        self.SetSize((-1, 300))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.mainFrame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        mainFrame_statusbar_fields = ["mainFrame_statusbar"]
        for i in range(len(mainFrame_statusbar_fields)):
            self.mainFrame_statusbar.SetStatusText(mainFrame_statusbar_fields[i], i)
        self.txtProjectRoot.SetToolTipString("Optional field for the root of the source tree that contains the Project Folder. CSnake will search this source tree for other projects.")
        self.btnSelectProjectRoot.SetToolTipString("Browse disk...")
        self.cmbNewProjectType.SetSelection(0)
        self.btnCreateProject.SetToolTipString("Start a new project in the Project Folder based on a template.")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        boxCreateProjectBtn = wx.BoxSizer(wx.HORIZONTAL)
        boxCreateProjectHelp = wx.BoxSizer(wx.HORIZONTAL)
        boxCreateProject = wx.BoxSizer(wx.HORIZONTAL)
        sizeNewProjectType = wx.BoxSizer(wx.HORIZONTAL)
        sizeNewProjectName = wx.BoxSizer(wx.HORIZONTAL)
        boxProjectRootHelp = wx.BoxSizer(wx.HORIZONTAL)
        boxProjectRoot = wx.BoxSizer(wx.HORIZONTAL)
        sizeProjectRoot = wx.BoxSizer(wx.HORIZONTAL)
        sizeProjectRoot.Add(self.lblProjectRoot, 0, wx.ALL|wx.EXPAND, 5)
        sizeProjectRoot.Add(self.txtProjectRoot, 2, wx.ALL, 5)
        sizeProjectRoot.Add(self.btnSelectProjectRoot, 0, wx.ALL, 5)
        boxProjectRoot.Add(sizeProjectRoot, 2, wx.ALL, 5)
        sizer_main.Add(boxProjectRoot, 0, wx.EXPAND, 0)
        boxProjectRootHelp.Add(self.textProjectRootHelp, 2, 0, 0)
        sizer_main.Add(boxProjectRootHelp, 0, wx.EXPAND, 0)
        sizeNewProjectName.Add(self.lblNewProjectName, 0, wx.ALL|wx.EXPAND, 5)
        sizeNewProjectName.Add(self.txtNewProjectName, 2, wx.ALL, 5)
        boxCreateProject.Add(sizeNewProjectName, 2, wx.ALL|wx.EXPAND, 5)
        sizeNewProjectType.Add(self.lblNewProjectType, 0, wx.ALL|wx.EXPAND, 5)
        sizeNewProjectType.Add(self.cmbNewProjectType, 0, wx.ALL, 5)
        boxCreateProject.Add(sizeNewProjectType, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5)
        sizer_main.Add(boxCreateProject, 0, wx.EXPAND, 0)
        boxCreateProjectHelp.Add(self.textCreateProjectHelp, 2, 0, 0)
        sizer_main.Add(boxCreateProjectHelp, 0, wx.EXPAND, 0)
        boxCreateProjectBtn.Add((0, 0), 1, wx.ALL, 20)
        boxCreateProjectBtn.Add(self.btnCreateProject, 0, wx.ALL, 20)
        sizer_main.Add(boxCreateProjectBtn, 0, wx.ALL|wx.EXPAND, 0)
        self.SetSizer(sizer_main)
        self.Layout()
        # end wxGlade

    def OnAbout(self, event): # wxGlade: MainFrame.<event_handler>
        about = About()
        about.read(pathToResources + "/about.txt")
        info = about.getWxAboutDialogInfo()
        wx.AboutBox(info)

    def OnTypingProjectRoot(self, event): # wxGlade: MainFrame.<event_handler>
        event.Skip()

    def OnSelectProjectRoot(self, event): # wxGlade: MainFrame.<event_handler>
        dlg = wx.DirDialog(None, "Select Project Root Folder")
        if dlg.ShowModal() == wx.ID_OK:
            self.txtProjectRoot.SetValue(dlg.GetPath())

    def OnCreateNewProject(self, event): # wxGlade: MainFrame.<event_handler>
        if( self.cmbNewProjectType.GetValue() == "Library" ):
            try:
                CreateNewModule.CreateLibrary(self.txtProjectRoot.GetValue(), self.txtNewProjectName.GetValue(), pathToResources)
            except ValueError, error:
                self._handleError("Error creating library", error)
            except IOError, error:
                self._handleError("Error creating library", error)
        if( self.cmbNewProjectType.GetValue() == "GIMIAS Plugin" ):
            try:
                CreateNewModule.CreatePlugin(self.txtProjectRoot.GetValue(), self.txtNewProjectName.GetValue(), pathToResources)
            except ValueError, error:
                self._handleError("Error creating plugin", error)
            except IOError, error:
                self._handleError("Error creating plugin", error)
        if( self.cmbNewProjectType.GetValue() == "GIMIAS Plugin Widget" ):
            try:
                CreateNewModule.CreatePluginWidget(self.txtProjectRoot.GetValue(), self.txtNewProjectName.GetValue(), pathToResources)
            except ValueError, error:
                self._handleError("Error creating widget", error)
            except IOError, error:
                self._handleError("Error creating widget", error)
        event.Skip()
        
    def _handleError(self, message, error):
        """ Handle errors. """
        wx.MessageBox("%s: %s\nSee log file for details." % (message, str(error)), 'Error', wx.ICON_ERROR)
        logger.exception("%s." % message)
        

# end of class MainFrame

if __name__ == "__main__":
    # Possible resources folders
    root = os.path.dirname(sys.argv[0])
    # '/resources' for built application
    # '/../resources' for running from source
    resourceFolders = ["/resources", "/../resources"]
    for folder in resourceFolders:
        pathToResources = root + folder
        if os.path.exists( pathToResources ):
            break
    assert os.path.exists("%s/TemplatePlugin" % pathToResources), "Template plugin folder not found in: %s" % pathToResources
    assert os.path.exists("%s/TemplateLibrary" % pathToResources), "Template library folder not found in: %s" % pathToResources
    
    # logging init
    logging.config.fileConfig(pathToResources + "/logging.conf")
    logger = logging.getLogger("StartNewModule")
    logger.info("Starting program.")

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    mainFrame = MainFrame(None, -1, "")
    app.SetTopWindow(mainFrame)
    mainFrame.Show()
    app.MainLoop()

    logger.info("Ending program.")
