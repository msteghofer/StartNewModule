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
import webbrowser
import utils

pathToResources = ""

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.mainFrame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.content = wx.MenuItem(wxglade_tmp_menu, 0, "Content", "Basic help information.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.content)
        self.about = wx.MenuItem(wxglade_tmp_menu, 1, "About", "About information.", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.about)
        self.mainFrame_menubar.Append(wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.mainFrame_menubar)
        # Menu Bar end
        self.mainFrame_statusbar = self.CreateStatusBar(1, 0)
        self.lblName = wx.StaticText(self, -1, "Name")
        self.txtName = wx.TextCtrl(self, -1, "")
        self.lblRootPath = wx.StaticText(self, -1, "Root path")
        self.txtRootPath = wx.TextCtrl(self, -1, "")
        self.btnSelectRootPath = wx.Button(self, -1, "...")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.lblType = wx.StaticText(self, -1, "Type")
        self.cmbType = wx.ComboBox(self, -1, choices=["Project", "Library", "GIMIAS Plugin", "GIMIAS Plugin Widget", "ThirdParty", "CommandLine Plugin"], style=wx.CB_DROPDOWN)
        self.lblToolkitFile = wx.StaticText(self, -1, "Toolkit csn file")
        self.txtToolkitFile = wx.TextCtrl(self, -1, "")
        self.btnSelectToolkitFile = wx.Button(self, -1, "...")
        self.lblGimiasFile = wx.StaticText(self, -1, "Gimias csn file")
        self.txtGimiasFile = wx.TextCtrl(self, -1, "")
        self.btnSelectGimiasFile = wx.Button(self, -1, "...")
        self.lblGimiasVersion = wx.StaticText(self, -1, "Gimias version")
        self.cmbGimiasVersion = wx.ComboBox(self, -1, choices=["1.5", "1.4", "1.3"], style=wx.CB_DROPDOWN)
        self.static_line_2 = wx.StaticLine(self, -1)
        self.btnCreate = wx.Button(self, -1, "Start New Module")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnMenuContent, self.content)
        self.Bind(wx.EVT_MENU, self.OnMenuAbout, self.about)
        self.Bind(wx.EVT_BUTTON, self.OnSelectRootPath, self.btnSelectRootPath)
        self.Bind(wx.EVT_TEXT, self.OnModuleTypeChoice, self.cmbType)
        self.Bind(wx.EVT_BUTTON, self.OnSelectToolkitFile, self.btnSelectToolkitFile)
        self.Bind(wx.EVT_BUTTON, self.OnSelectGimiasFile, self.btnSelectGimiasFile)
        self.Bind(wx.EVT_BUTTON, self.OnCreateNewProject, self.btnCreate)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("StartNewModule")
        self.__setIcon()
        self.SetSize((-1, 483))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.mainFrame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        mainFrame_statusbar_fields = [""]
        for i in range(len(mainFrame_statusbar_fields)):
            self.mainFrame_statusbar.SetStatusText(mainFrame_statusbar_fields[i], i)
        self.lblName.SetToolTipString("The name of the module.")
        self.lblRootPath.SetToolTipString("The path to the module (ie. ToolkitSrc/src/cilabModules for a library or ToolkitSrc/src/Apps/Plugins for a plugin).")
        self.txtRootPath.SetToolTipString("Optional field for the root of the source tree that contains the Project Folder. CSnake will search this source tree for other projects.")
        self.btnSelectRootPath.SetToolTipString("Browse disk...")
        self.lblType.SetToolTipString("The type of the module.")
        self.cmbType.SetSelection(0)
        self.lblToolkitFile.SetToolTipString("The location of the Toolkit csn file (csnMyToolkit.py).")
        self.txtToolkitFile.Enable(False)
        self.btnSelectToolkitFile.SetToolTipString("Browse disk...")
        self.btnSelectToolkitFile.Enable(False)
        self.lblGimiasFile.SetToolTipString("The location of the Gimias csn file (csnGIMIAS.py).")
        self.txtGimiasFile.Enable(False)
        self.btnSelectGimiasFile.SetToolTipString("Browse disk...")
        self.btnSelectGimiasFile.Enable(False)
        self.lblGimiasVersion.SetToolTipString("The Gimias version to be compatible with.")
        self.cmbGimiasVersion.Enable(False)
        self.cmbGimiasVersion.SetSelection(0)
        self.btnCreate.SetToolTipString("Start a new project in the Project Folder based on a template.")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        box_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizerCreateBtn = wx.BoxSizer(wx.HORIZONTAL)
        box_3 = wx.BoxSizer(wx.HORIZONTAL)
        gridFiles = wx.GridSizer(2, 1, 0, 0)
        sizerGimiasVersion = wx.BoxSizer(wx.HORIZONTAL)
        sizerGimiasFile = wx.BoxSizer(wx.HORIZONTAL)
        sizerToolkitFile = wx.BoxSizer(wx.HORIZONTAL)
        box_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerType = wx.BoxSizer(wx.HORIZONTAL)
        box_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerRootPath = wx.BoxSizer(wx.HORIZONTAL)
        box_0 = wx.BoxSizer(wx.HORIZONTAL)
        sizerName = wx.BoxSizer(wx.HORIZONTAL)
        sizerName.Add(self.lblName, 1, wx.ALL|wx.EXPAND, 5)
        sizerName.Add(self.txtName, 3, wx.ALL, 5)
        box_0.Add(sizerName, 4, wx.ALL|wx.EXPAND, 5)
        sizer_main.Add(box_0, 0, wx.EXPAND, 0)
        sizerRootPath.Add(self.lblRootPath, 1, wx.ALL|wx.EXPAND, 5)
        sizerRootPath.Add(self.txtRootPath, 2, wx.ALL, 5)
        sizerRootPath.Add(self.btnSelectRootPath, 1, wx.ALL, 5)
        box_1.Add(sizerRootPath, 4, wx.ALL|wx.EXPAND, 5)
        sizer_main.Add(box_1, 0, wx.EXPAND, 0)
        sizer_main.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizerType.Add(self.lblType, 1, wx.ALL|wx.EXPAND, 5)
        sizerType.Add(self.cmbType, 3, wx.ALL, 5)
        box_2.Add(sizerType, 4, wx.ALL|wx.EXPAND, 5)
        sizer_main.Add(box_2, 0, wx.EXPAND, 0)
        sizerToolkitFile.Add(self.lblToolkitFile, 1, wx.ALL|wx.EXPAND, 5)
        sizerToolkitFile.Add(self.txtToolkitFile, 2, wx.ALL, 5)
        sizerToolkitFile.Add(self.btnSelectToolkitFile, 1, wx.ALL, 5)
        gridFiles.Add(sizerToolkitFile, 4, wx.ALL|wx.EXPAND, 5)
        sizerGimiasFile.Add(self.lblGimiasFile, 1, wx.ALL|wx.EXPAND, 5)
        sizerGimiasFile.Add(self.txtGimiasFile, 2, wx.ALL, 5)
        sizerGimiasFile.Add(self.btnSelectGimiasFile, 1, wx.ALL, 5)
        gridFiles.Add(sizerGimiasFile, 4, wx.ALL|wx.EXPAND, 5)
        sizerGimiasVersion.Add(self.lblGimiasVersion, 1, wx.ALL|wx.EXPAND, 5)
        sizerGimiasVersion.Add(self.cmbGimiasVersion, 3, wx.ALL, 5)
        gridFiles.Add(sizerGimiasVersion, 4, wx.ALL|wx.EXPAND, 5)
        box_3.Add(gridFiles, 1, wx.EXPAND, 0)
        sizer_main.Add(box_3, 0, wx.EXPAND, 0)
        sizer_main.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizerCreateBtn.Add((0, 0), 2, wx.ALL|wx.EXPAND, 5)
        sizerCreateBtn.Add(self.btnCreate, 2, wx.ALL|wx.ALIGN_RIGHT, 5)
        box_4.Add(sizerCreateBtn, 4, wx.ALL|wx.EXPAND, 5)
        sizer_main.Add(box_4, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_main)
        self.Layout()
        # end wxGlade

    def __setIcon(self):
        _iconFile = pathToResources + "/startnewmodule.ico"
        _icon = wx.Icon(_iconFile, wx.BITMAP_TYPE_ICO)
        self.SetIcon(_icon)
    
    def OnMenuAbout(self, event): # wxGlade: MainFrame.<event_handler>
        about = About()
        about.read(pathToResources + "/about.txt")
        info = wx.AboutDialogInfo()
        info.SetName(about.getName())
        info.SetVersion(about.getVersion())
        info.SetDescription(about.getDescription())
        info.SetCopyright(about.getAuthor())
        wx.AboutBox(info)

    def OnMenuContent(self, event): # wxGlade: MainFrame.<event_handler>
        ''' Text displayed for help.'''
        root = utils.getRootFolder()
        indexFilename = root + "/doc/html/index.html"
        if os.path.exists(indexFilename):
            webbrowser.open(indexFilename)
        else:
            dialog = wx.MessageDialog(self, "Missing documentation.", 'Error', style = wx.OK | wx.ICON_ERROR)
            dialog.ShowModal()

    def OnSelectRootPath(self, event): # wxGlade: MainFrame.<event_handler>
        dlg = wx.DirDialog(None, "Select Project Root Folder")
        if not self.txtRootPath.GetValue() is None:
            dlg.SetPath(self.txtRootPath.GetValue()) 
        if dlg.ShowModal() == wx.ID_OK:
            self.txtRootPath.SetValue(dlg.GetPath())
        dlg.Destroy()

    def OnSelectToolkitFile(self, event): # wxGlade: MainFrame.<event_handler>
        dlg = wx.FileDialog(None, "Select the Toolkit csn file.")
        if self.txtRootPath.GetValue() is not None:
            dlg.SetPath(self.txtRootPath.GetValue()) 
        if dlg.ShowModal() == wx.ID_OK:
            self.txtToolkitFile.SetValue(dlg.GetPath())
        dlg.Destroy()

    def OnSelectGimiasFile(self, event): # wxGlade: MainFrame.<event_handler>
        dlg = wx.FileDialog(None, "Select the Gimias csn file.")
        if self.txtRootPath.GetValue() is not None:
            dlg.SetPath(self.txtRootPath.GetValue()) 
        if dlg.ShowModal() == wx.ID_OK:
            self.txtGimiasFile.SetValue(dlg.GetPath())
        dlg.Destroy()

    def OnModuleTypeChoice(self, event): # wxGlade: MainFrame.<event_handler>
        if( self.cmbType.GetValue() == "Library" ):
            self.txtToolkitFile.Enable()
            self.btnSelectToolkitFile.Enable()
            self.txtGimiasFile.Disable()
            self.btnSelectGimiasFile.Disable()
            self.cmbGimiasVersion.Disable()
        elif( self.cmbType.GetValue() == "GIMIAS Plugin" ):
            self.txtToolkitFile.Enable()
            self.btnSelectToolkitFile.Enable()
            self.txtGimiasFile.Enable()
            self.btnSelectGimiasFile.Enable()
            self.cmbGimiasVersion.Enable()
        elif( self.cmbType.GetValue() == "GIMIAS Plugin Widget" ):
            self.txtToolkitFile.Disable()
            self.btnSelectToolkitFile.Disable()
            self.txtGimiasFile.Disable()
            self.btnSelectGimiasFile.Disable()
            self.cmbGimiasVersion.Enable()
        elif( self.cmbType.GetValue() == "ThirdParty" ):
            self.txtToolkitFile.Enable()
            self.btnSelectToolkitFile.Enable()
            self.txtGimiasFile.Disable()
            self.btnSelectGimiasFile.Disable()
            self.cmbGimiasVersion.Disable()
        elif(self.cmbType.GetValue() == "Project"):
            self.txtToolkitFile.Disable()
            self.btnSelectToolkitFile.Disable()
            self.txtGimiasFile.Disable()
            self.btnSelectGimiasFile.Disable()
            self.cmbGimiasVersion.Disable()
        elif(self.cmbType.GetValue() == "CommandLine Plugin"):
            self.txtToolkitFile.Disable()
            self.btnSelectToolkitFile.Disable()
            self.txtGimiasFile.Disable()
            self.btnSelectGimiasFile.Disable()
            self.cmbGimiasVersion.Disable()
        else:
            self._handleError("Unsupported module type", ValueError())

    def OnCreateNewProject(self, event): # wxGlade: MainFrame.<event_handler>
        """ Create the new module. """
        # error flag
        withError = False
        # set up frame for creation begin 
        self.mainFrame_statusbar.SetStatusText("Creating module...")
        self.btnCreate.Disable()
        progressDialog = wx.ProgressDialog( "Progress", "Creating module...", maximum = 100, style = wx.PD_CAN_ABORT|wx.PD_AUTO_HIDE|wx.PD_APP_MODAL )
        progressDialog.Update(0)
        # create library
        if( self.cmbType.GetValue() == "Library" ):
            try:
                CreateNewModule.CreateLibrary(
                    self.txtRootPath.GetValue(), 
                    self.txtName.GetValue(), 
                    pathToResources,
                    self.txtToolkitFile.GetValue())
            except ValueError, error:
                self._handleError("Error creating library.", error)
                withError = True
            except IOError, error:
                self._handleError("Error creating library.", error)
                withError = True
        # create plugin
        elif( self.cmbType.GetValue() == "GIMIAS Plugin" ):
            try:
                CreateNewModule.CreatePlugin(
                     self.txtRootPath.GetValue(), 
                     self.txtName.GetValue(), 
                     pathToResources,
                     self.txtToolkitFile.GetValue(),
                     self.txtGimiasFile.GetValue(),
                     self.cmbGimiasVersion.GetValue())
            except ValueError, error:
                self._handleError("Error creating plugin.", error)
                withError = True
            except IOError, error:
                self._handleError("Error creating plugin.", error)
                withError = True
        # create widget
        elif( self.cmbType.GetValue() == "GIMIAS Plugin Widget" ):
            try:
                CreateNewModule.CreatePluginWidget(
                       self.txtRootPath.GetValue(), 
                       self.txtName.GetValue(), 
                       pathToResources,
                       self.cmbGimiasVersion.GetValue())
            except ValueError, error:
                withError = True
                self._handleError("Error creating widget.", error)
            except IOError, error:
                self._handleError("Error creating widget.", error)
                withError = True
        # create thirdParty
        elif( self.cmbType.GetValue() == "ThirdParty" ):
            try:
                CreateNewModule.CreateThirdParty(
                        self.txtRootPath.GetValue(),
                        self.txtName.GetValue(),
                        pathToResources,
                        self.txtToolkitFile.GetValue())
            except ValueError, error:
                withError = True
                self._handleError("Error creating Third Party.", error)
            except IOError, error:
                self._handleError("Error creating Third Party.", error)
                withError = True
        # create Project
        elif( self.cmbType.GetValue() == "Project"):
            try:
                CreateNewModule.CreateProject(
                        self.txtRootPath.GetValue(),
                        self.txtName.GetValue(),
                        pathToResources)
            except ValueError, error:
                withError = True
                self._handleError("Error creating Project.", error)
            except IOError, error:
                self._handleError("Error creating Project.", error)
                withError = True
        # create commandline plugin
        elif( self.cmbType.GetValue() == "CommandLine Plugin" ):
            try:
                CreateNewModule.CreateCommandLine(
                    self.txtRootPath.GetValue(), 
                    self.txtName.GetValue(), 
                    pathToResources)
            except ValueError, error:
                self._handleError("Error creating commandLine Plugin.", error)
                withError = True
            except IOError, error:
                self._handleError("Error creating commandLine Plugin.", error)
                withError = True
        # default
        else:
            self._handleError("Unsupported module type.", ValueError())
            withError = True
        # set up frame for creation end 
        if not withError:
            progressDialog.Update(100)
            self.mainFrame_statusbar.SetStatusText("Module created.")
        else:
            self.mainFrame_statusbar.SetStatusText("Error creating module.")
        # clean up   
        progressDialog.Destroy()
        self.btnCreate.Enable()
        
    def _handleError(self, message, error):
        """ Handle errors. """
        wx.MessageBox("%s\nError: %s\nSee log file for details." % (message, str(error)), 'Error', wx.ICON_ERROR)
        logger.exception("%s" % message)
    
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
    assert os.path.exists("%s/TemplatePlugin13" % pathToResources), "Template plugin folder for gimias 1.3 not found in: %s" % pathToResources
    assert os.path.exists("%s/TemplatePlugin14" % pathToResources), "Template plugin folder for gimias 1.4 not found in: %s" % pathToResources
    assert os.path.exists("%s/TemplatePlugin15" % pathToResources), "Template plugin folder for gimias 1.5 not found in: %s" % pathToResources
    assert os.path.exists("%s/TemplateLibrary" % pathToResources), "Template library folder not found in: %s" % pathToResources
    assert os.path.exists("%s/TemplateThirdParty" % pathToResources), "Template thirdParty folder not found in: %s" % pathToResources
    
    # create log file (mainly for running from source)
    logfilepath = os.path.expanduser("~") + "/.startnewmodule"
    if not os.path.exists(logfilepath):
        os.mkdir(logfilepath)
    logfilename = logfilepath + "/log.txt"
    if not os.path.exists(logfilename):
        logfile = open(logfilename,"w")
        logfile.close()
    # set as environment variable to retrieve it in the log configuration
    os.environ["SNMLOGFILE"] = logfilename
    
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
