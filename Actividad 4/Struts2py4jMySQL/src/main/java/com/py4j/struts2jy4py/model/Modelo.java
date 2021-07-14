
package com.py4j.struts2jy4py.model;


public class Modelo {
    private String grupo;
    private double promedio;

    public Modelo() {
        
    }

    public Modelo(String grupo, double promedio) {
        this.grupo = grupo;
        this.promedio = promedio;
    }

    public String getGrupo() {
        return grupo;
    }

    public void setGrupo(String grupo) {
        this.grupo = grupo;
    }

    public double getPromedio() {
        return promedio;
    }

    public void setPromedio(double promedio) {
        this.promedio = promedio;
    }

    
}
