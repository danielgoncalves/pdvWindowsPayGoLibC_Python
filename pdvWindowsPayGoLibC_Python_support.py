#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 05, 2019 06:21:36 PM -0300  platform: Windows NT

import sys
from Configs import *  
from  Enums import *
from  CustomObjects import *
import os
from  time import *
#import ctypes.
from ctypes import *
from Interops import *
#from PGWlib import *
import PGWlib
from DialogAddParamWindow import *
posLstParametros = 0

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global combobox
    combobox = tk.StringVar()

#def ButtonMouse1Instala(p1):
#    print('pdvWindowsPayGoLibC_Python_support.ButtonMouse1Instala')
#    #PGWlib.TesteInstalacaoJan()
#    #TesteInstalacaoJan()
#    #PGWlib.TesteIsNull()
#    #PGWlib.TesteManutencao()
#    #PGWlib.TesteVenda()
#    PGWlib.LogaTransactionResult()

def ButtonMouse1btnAdicionar(p1):
    print('pdvWindowsPayGoLibC_Python_support.ButtonMouse1btnAdicionar')
    #######################
    dicionarioPar = dict()
    listaPar = []
    for item in E_PWINFO:
        print(item.value," -> ",item.name)
        dicionarioPar[item.name] = item.value
        listaPar.append(item.name)

    parWindow = DialogAddParamWindow(root,listaPar,'Selecione O parametro a ser inserido:')

    
    root.wait_window(parWindow.top)
    
    if(parWindow.bExit == True): # janela fechou sem OK
       print('Não Adicionou Parametro')
       sys.stdout.flush()
       return

    
    print(parWindow.param)
    print(parWindow.ValParam)
    code_par = dicionarioPar[parWindow.param]

    #strItem = parWindow.param + '(' + str(code_par) +  ')' + ':' + parWindow.ValParam;
    ########################
    PGWlib.addParameter(parWindow.param,code_par,parWindow.ValParam,w)
    #w.lstParameters.insert(tk.END,strItem)

    sys.stdout.flush()

def ButtonMouse1btnCaptura(p1):
    #global MainWindow
    print('pdvWindowsPayGoLibC_Python_support.ButtonMouse1btnCaptura')
    w.Loga("testando ButtonMouse1btnCaptura")
    PGWlib.CaptureWithPinpad()
    sys.stdout.flush()

def ButtonMouse1btnExecutar(p1):
    #print('pdvWindowsPayGoLibC_Python_support.ButtonMouse1btnExecutar')
    #print('get combobox selected',w.cmbOper.get())
    #w.Loga("get combobox selected" + w.cmbOper.get())
    selecionado = w.cmbOper.get()
    code_tran = w.dicionarioOper[selecionado]
    ret=PGWlib.execTrans(code_tran)
    if(ret == 0):
      PGWlib.LogaTransactionResult()
      PGWlib.confirmUndoTransactionGen(ret) 
    PGWlib.LogaTransactionResult()
    #w.btnExecutar.config(relief=SUNKEN)
    #w.btnExecutar.config(state="disabled")
    #w.btnExecutar.config(state="normal")
    w.RessetButtonExecutar()
    #sys.stdout.flush()
    

def ButtonMouse1btnLimpaLog(p1):
    print('pdvWindowsPayGoLibC_Python_support.ButtonMouse1btnLimpaLog')
 
    w.LogDll.config(state="normal")
    w.LogDll.delete("1.0",tk.END)
    w.LogDll.config(state="disabled")

    sys.stdout.flush()

def ButtonMouse1btnLimpar(p1):
    print('pdvWindowsPayGoLibC_Python_support.ButtonMouse1btnLimpar')
    # limpa lista
    PGWlib.CleanParameterList()
    # limpa listbox
    w.lstParameters.delete(0, tk.END)
    # adiciona parametros
    PGWlib.addMandatoryParameters(w)
    sys.stdout.flush()

def ButtonMouse1btnRemover(p1):
    print('pdvWindowsPayGoLibC_Python_support.ButtonMouse1btnRemover')
    posLstParametros = w.lstParameters.curselection()[0]
    print('deleta o item:')
    print(posLstParametros)
    PGWlib.DelParameter(posLstParametros)
    w.lstParameters.delete(tk.ANCHOR)
    sys.stdout.flush()

def ComboboxSelectedCmbOper(p1):
    print('pdvWindowsPayGoLibC_Python_support.ComboboxSelectedCmbOper')
    sys.stdout.flush()

def SelectedlstParameters(p1):
    print('pdvWindowsPayGoLibC_Python_support.SelectedlstParameters')
    posLstParametros = w.lstParameters.curselection()[0]
    print(posLstParametros)
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def Loga(messsage):
    w.Loga(messsage)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import pdvWindowsPayGoLibC_Python
    pdvWindowsPayGoLibC_Python.vp_start_gui()




