import PyPDF2 
import os
import sys
import logging
from tkinter import*

tkwindow=Tk()
tkwindow.geometry("400x100")

tkwindow.title("pdf merge tool")

global e

def filelst():
    
    global e
    path=e.get()
    os.chdir(path)
    l=[]
    logging.basicConfig(filename="newfile3.log",format='%(asctime)s %(message)s',filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug("tool will satrt the pdf file merging")
    #path=input("ente rthe path : ")
    logger.info("input loction given by the user :".format(path))
    dir_list = os.listdir(path)
    
    for i in dir_list:
        if i.endswith('.pdf'):
            l.append(i)
    
    try:
        if len(l)==0:
            raise NameError
            logger.warning("Its a Warning")
            logger.error("No pdf files in the given location")
            pass
    except:
        logger.error("No pdf files in the given location")
    finally:
        
        if len(l)>0:
            
            mergeFile = PyPDF2.PdfFileMerger()
            for _pdf in l:
                mergeFile.append(PyPDF2.PdfFileReader(_pdf, 'rb'))
            mergeFile.write("New_Merged_File.pdf")
            logging.info('pdf cfreated')

e=Entry(tkwindow)
e.pack()
e.focus_set()



button=Button(tkwindow,text="run",command=filelst)
button.pack()

  
tkwindow.mainloop()


