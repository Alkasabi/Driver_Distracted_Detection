# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:59:00 2021

@author: m.alkasabi
"""

class watcher():
    
    def __init__(self):
        ## driver = [id , [vio0,vio1,vio2 ...]]
        self.driver_list=[]
        self.black_list=[]
        self.vio_thre=0.6
    
    def check(self,id,vio):
        
        res=[]
        index=self.get_driver_index(id)
        if index== None:
            self.add_new_driver(id)
            self.add_vio(id,vio)
        else:
            self.add_vio(id,vio)
            if len (self.driver_list[index][1] ) >9 :
                vio_avarage=sum(self.driver_list[index][1][-10:]) /10
                if vio_avarage > self.vio_thre :
                    if id not in self.black_list :
                        self.black_list.append(id)
                        res.append(vio_avarage)
        return res
            
    def add_new_driver(self,id):
        self.driver_list.append([id,[]])
        
    def add_vio(self,id,vio):
        index=self.get_driver_index(id)
        self.driver_list[index][1].append(vio)
    
    def get_driver_index(self,driver_id):
        driver_index=None
        list_len=self.driver_list.__len__()
        if list_len>0:
            for x in range(list_len):
                if self.driver_list[x][0]== driver_id:
                    driver_index=x
        return driver_index
     
w=watcher()

w.driver_list

w.check(10,0.8)

w.black_list

