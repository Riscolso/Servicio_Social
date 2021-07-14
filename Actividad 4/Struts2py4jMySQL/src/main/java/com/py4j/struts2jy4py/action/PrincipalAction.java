package com.py4j.struts2jy4py.action;


import com.opensymphony.xwork2.ActionSupport;
import com.py4j.struts2jy4py.clases.AplicacionCliente;
import com.py4j.struts2jy4py.model.Modelo;


public class PrincipalAction extends ActionSupport {
    
    private Modelo modelo;
    
    public String comunicarPython() throws InterruptedException, Exception{
        modelo = AplicacionCliente.iniciar();
        return SUCCESS;
    }

    public Modelo getModelo() {
        return modelo;
    }
    
}
