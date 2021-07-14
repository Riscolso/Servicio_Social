
package com.py4j.struts2jy4py.clases;

import com.py4j.struts2jy4py.model.Modelo;
import py4j.GatewayServer;

public class AplicacionCliente {
    
    public static Modelo iniciar() throws Exception{
        double promedio;
        GatewayServer.turnLoggingOff();
        GatewayServer server = new GatewayServer();
        server.start();
        IFuncionPython funcionPython = (IFuncionPython) server.getPythonServerEntryPoint(new Class[] { IFuncionPython.class });
        promedio = funcionPython.obtenerPromedio("Darwin", 9.8);
        //Terminar la conexión
        server.shutdown();
        return new Modelo("4CV9", promedio);
    }
}

