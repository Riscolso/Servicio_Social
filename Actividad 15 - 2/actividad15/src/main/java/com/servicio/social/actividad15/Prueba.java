/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.servicio.social.actividad15;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


/**
 *
 * @author rrisc
 */
public class Prueba {
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        System.setProperty("webdriver.gecko.driver", "geckodriver.exe");
        WebDriver driver = new FirefoxDriver();
        
        //Mazímizar la ventana
        driver.manage().window().maximize();
        //Dirigirse a la página del login
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1630982020&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d31d92721-752d-3aae-eb63-f2dd027fd57e&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015");
        
        //Inicializar el esperador
        WebDriverWait wait = new WebDriverWait(driver,30);
        //Obtener el input de correo y llenarlo con usuario
        driver.findElement(By.id("i0116")).sendKeys("rriscolso@hotmail.com");
        //Obtener y presionar el botón "Siguiente"
        driver.findElement(By.xpath("//*[@id=\"idSIButton9\"]")).click();
        //Esperar hasta que aparezca el input de contraseña
        WebElement contrasena = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("i0118")));
        //Insertar el valor de la contraseña
        //contrasena.sendKeys("99178352Ra+");
        //Buscar y presionar el botón de Inicio de sesión
        //driver.findElement(By.xpath("//*[@id=\"idSIButton9\"]")).click();
        
    }
}
