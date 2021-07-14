
package com.py4j.struts2jy4py.clases;


import java.util.List;
import py4j.GatewayServer;

public class StackEntryPoint {

    private Stack stack;

    public StackEntryPoint() {
      stack = new Stack();
      stack.push("Initial Item");
    }

    public Stack getStack() {
        return stack;
    }

    public void iniciar() throws InterruptedException {
        GatewayServer gatewayServer = new GatewayServer(new StackEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
        while(stack.getInternalList().size() < 9){
            Thread.sleep(1000);
            System.out.println("Hay "+stack.getInternalList().size()+" elementos");
        }
        for (String aux : stack.getInternalList()){
            System.out.println("Valor: " + aux);
        }
        
    }

}
