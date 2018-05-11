# import os
# from xml.etree import ElementTree
#
# import readConfig
#
#
# proDir = readConfig.proDir
# def get_url_from_xml(name):
#     """
#     By name get url from interfaceURL.xml
#     :param name: interface's url name
#     :return: url
#     """
#     url_list = []
#     url_path = os.path.join(proDir, 'testFile', 'interfaceURL.xml')
#     tree = ElementTree.parse(url_path)
#     for u in tree.findall('url'):
#         url_name = u.get('name')
#         if url_name == 'dataPlatformUser':
#             for c in u.getchildren():
#                 url_list.append(c.text)
#
#     url = '/v2/' + '/'.join(url_list)
#     print(url)
#     return url

