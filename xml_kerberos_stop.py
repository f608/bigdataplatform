#!/usr/local/python
#data: 2018-01-11

from xml.etree.ElementTree import ElementTree,Element
import subprocess

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
    
if __name__ == "__main__":
  tree= read_xml("/usr/local/hadoop/etc/hadoop/core-site.xml")
  root = tree.getroot()
  tags = find_nodes(root,"property")
  change_element(tags,"value","kerberos","simple")
 # subprocess.Popen('rm -rf core-site.xml',shell=True,cwd="/usr/local/hadoop/etc/hadoop")
  write_xml(tree,"/usr/local/hadoop/etc/hadoop/core-site.xml")


