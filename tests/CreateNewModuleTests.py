# Unit tests for for the csnBuild class
import unittest
import CreateNewModule
import os
import shutil

class CreateNewModuleTests(unittest.TestCase):

    def setUp(self):
        """ Run before test. """

    def tearDown(self):
        """ Run after test. """

    def testCreateLibrary(self):
        """ CreateNewModuleTests: test CreateLibrary. """
        # file names
        testRoot = "./"
        toolkitRoot = testRoot + "/generated"
        modulesRoot = toolkitRoot + "/modules"
        csnToolkitFileName = "csnCISTIBToolkit.py"
        # create hierarchy 
        os.mkdir(toolkitRoot)
        csnToolkitFilePath = toolkitRoot + "/" + csnToolkitFileName
        csnToolkitFile = open(csnToolkitFilePath, 'w')
        csnToolkitFile.close()
        os.mkdir(modulesRoot)
        
        # vars
        projectName = "TestLibrary"
        rootForTemplateFiles = "./../resources"
        # call method
        CreateNewModule.CreateLibrary(modulesRoot, projectName, rootForTemplateFiles, csnToolkitFilePath)
        
        # check results
        projectFolder = modulesRoot + '/' + projectName
        instanceName = projectName[0].lower() + ''.join(projectName[1:])
        csnFileName = "csn%s.py" % projectName
        # check folders and file
        assert os.path.exists(projectFolder)
        assert os.path.exists(projectFolder + "/applications" )
        assert os.path.exists(projectFolder + "/build" )
        assert os.path.exists(projectFolder + "/doc" )
        assert os.path.exists(projectFolder + "/libmodules" )
        assert os.path.exists(projectFolder + "/tests" )
        assert os.path.exists(projectFolder + "/__init__.py" )
        # check project csn file content
        assert os.path.exists(projectFolder + '/' + csnFileName )
        csnFile = open(projectFolder + '/' + csnFileName)
        csnFileContent = csnFile.read()
        assert csnFileContent.find(instanceName) != -1
        csnFile.close()
        # check toolkit csn file content
        csnToolkitFile = open(toolkitRoot + "/" + csnToolkitFileName)
        csnToolkitFileContent = csnToolkitFile.read()
        assert csnToolkitFileContent.find(instanceName) != -1
        csnToolkitFile.close()
       
        # delete created hierarchy
        shutil.rmtree(toolkitRoot)
        
    def testCreatePlugin(self):
        """ CreateNewModuleTests: test CreatePlugin. """
        # file names
        testRoot = "./"
        toolkitRoot = testRoot + "/generated"
        appsRoot = toolkitRoot + "/apps"
        gimiasRoot = appsRoot + "/Gimias"
        pluginsRoot = appsRoot + "/plugins"
        csnToolkitFileName = "csnCISTIBToolkit.py"
        csnGimiasFileName = "csnGIMIAS.py"
        # create hierarchy 
        os.mkdir(toolkitRoot)
        csnToolkitFilePath = toolkitRoot + '/' + csnToolkitFileName
        csnToolkitFile = open(csnToolkitFilePath, 'w')
        csnToolkitFile.close()
        os.mkdir(appsRoot)
        #open(appsRoot + "/csnplugins.py", 'w')
        os.mkdir(gimiasRoot)
        csnGimiasFilePath = gimiasRoot + '/' + csnGimiasFileName
        csnGimiasFile = open(csnGimiasFilePath, 'w')
        csnGimiasFile.write("gimias.AddProjects([DefaultPlugin])")
        csnGimiasFile.close()
        os.mkdir(pluginsRoot)

        # vars
        projectName = "TestPlugin"
        rootForTemplateFiles = "./../resources"
        # call method
        CreateNewModule.CreatePlugin(pluginsRoot, projectName, rootForTemplateFiles, csnToolkitFilePath, csnGimiasFilePath)

        # check results
        projectFolder = pluginsRoot + '/' + projectName
        instanceName = projectName[0].lower() + ''.join(projectName[1:])
        csnFileName = "csn%s.py" % projectName
        # check folders and file
        assert os.path.exists(projectFolder)
        assert os.path.exists(projectFolder + "/build" )
        assert os.path.exists(projectFolder + "/doc" )
        #assert os.path.exists(projectFolder + "/processors" )
        #assert os.path.exists(projectFolder + "/widgets" )
        assert os.path.exists(projectFolder + "/__init__.py" )
        # check project csn file content
        assert os.path.exists(projectFolder + '/' + csnFileName )
        csnFile = open(projectFolder + '/' + csnFileName)
        csnFileContent = csnFile.read()
        assert csnFileContent.find(instanceName) != -1
        csnFile.close()
        # check toolkit csn file content
        csnToolkitFile = open(toolkitRoot + '/' + csnToolkitFileName)
        csnToolkitFileContent = csnToolkitFile.read()
        assert csnToolkitFileContent.find(instanceName) != -1
        csnToolkitFile.close()
        # check gimias csn file content
        csnGimiasFile = open(gimiasRoot + '/' + csnGimiasFileName)
        csnGimiasFileContent = csnGimiasFile.read()
        assert csnGimiasFileContent.find(instanceName) != -1
        csnGimiasFile.close()

        # delete created hierarchy
        #shutil.rmtree(toolkitRoot)
        
    def testCreatePluginWidget(self):
        """ CreateNewModuleTests: test CreatePluginWidget. """
        # file names
        testRoot = "./"
        toolkitRoot = testRoot + "/generated"
        appsRoot = toolkitRoot + "/apps"
        pluginsRoot = appsRoot + "/plugins"
        projectName = "TestPlugin"
        projectRoot = pluginsRoot + '/' + projectName
        csnFileName = "/csn%s.py" % projectName
        # create hierarchy 
        assert os.path.exists(toolkitRoot)
        assert os.path.exists(appsRoot)
        assert os.path.exists(pluginsRoot)
        assert os.path.exists(projectRoot)
        csnPluginFilePath = projectRoot + '/' + csnFileName
        assert os.path.exists(csnPluginFilePath)
        
        # vars
        widgetName = "TestWidget"
        rootForTemplateFiles = "./../resources"
        # call method
        CreateNewModule.CreatePluginWidget(projectRoot, widgetName, rootForTemplateFiles)

        # check results
        projectFolder = pluginsRoot + '/' + projectName
        # check folders and file
        assert os.path.exists(projectFolder)
        assert os.path.exists(projectFolder + "/processors" )
        assert os.path.exists(projectFolder + "/widgets" )
        # check project csn file content
        assert os.path.exists(projectFolder + '/' + csnFileName )
        csnFile = open(projectFolder + '/' + csnFileName)
        csnFileContent = csnFile.read()
        assert csnFileContent.find(widgetName) != -1
        csnFile.close()

        # delete created hierarchy
        shutil.rmtree(toolkitRoot)
                
if __name__ == "__main__":
    unittest.main() 
