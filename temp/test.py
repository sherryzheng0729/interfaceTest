import os
import unittest
from xml.etree import ElementTree

import readConfig

proDir = readConfig.proDir
class test:
    def __init__(self):
        self.caselist = []
        self.caseListFile = os.path.join(readConfig.proDir,"caselist.txt")
        self.caseFile = os.path.join(readConfig.proDir, "testCase")



    def set_case_list(self):
        fb = open(self.caseListFile)

        for value in fb.readlines():
            data = str(value)
            if data !="" and not data.startswith("#"):
                self.caselist.append(data.replace("\n",""))

        # print(self.caselist)
        fb.close()

    def run(self):
        url_list = []
        url_path = os.path.join(proDir, 'testFile', 'interfaceURL.xml')
        tree = ElementTree.parse(url_path)
        for u in tree.findall('url'):
            url_name = u.get('name')
            for c in u.getchildren():
                url_list.append(c.text)

        url = '/admin/DataCtrl/' + '/'.join(url_list)+'.do'
        print(url)
            # if url_name == name:
            #     for c in u.getchildren():
            #         url_list.append(c.text)
        # self.set_case_list()
        # suite_module = []
        #
        # for case in self.caselist:
        #     case_name = case.split("/")[-1]
        #     print(case_name+".py")
        #     discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
        #     suite_module.append(discover)
        #     print(suite_module[0])


if __name__ ==  '__main__' :
    obj = test()
    obj.run()



