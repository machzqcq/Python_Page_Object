__author__ = 'pmacharl'

def print_func(par):
   print("Hello : ", par)
   return


def on(page_class):
  if(page_class in globals().keys()):
     print("in if loop")
     page=globals()[page_class]()
  else:
        print("Page Object:"+page_class+" does not exist")
  return page


 #
 # def class_from_string(str):
 #    module_name, class_name = str.split(".")
 #    # somemodule = importlib.import_module(module_name)
 #    # print(getattr(somemodule, class_name))
 #    return globals()[class_name]
