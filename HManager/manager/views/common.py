import functools
from xml.etree.ElementTree import ElementTree,Element, SubElement
from django.shortcuts import redirect

def check_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request=args[0]
        if not request.session.get('admin'):
            return redirect('/kerberos/login/')
        return func(*args, **kwargs)
    return wrapper

'''操作xml文件'''
def read_xml(in_path):
  tree = ElementTree()
  tree.parse(in_path)
  return tree

def write_xml(tree,out_path):
  tree.write(out_path)

def find_nodes(tree,path):
  return tree.findall(path)

def change_element(tags,element,text_original,text_changed):
  for tag in tags:
    value = tag.find(element)
    if value.text == text_original:
      value.text = text_changed

def create_property(root,name,value):
  newproperty = SubElement(root,"property")
  newname = SubElement(newproperty,"name")
  newname.text = name
  newvalue = SubElement(newproperty,"value")
  newvalue.text = value

def remove_property(root,name):
  tags = find_nodes(root,"property")
  for tag in tags:
   namenode = tag.find("name")
   if namenode.text == name:
      root.remove(tag)