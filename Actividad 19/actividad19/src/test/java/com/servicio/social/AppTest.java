package com.servicio.social;


import java.util.concurrent.TimeUnit;
import junit.framework.Assert;

import org.testng.annotations.Test; 
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Parameters;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    public static WebDriver driver;
    
    @BeforeTest
    @Parameters("browser")
    public void setup(String browser) throws Exception{
        //Check if parameter passed from TestNG is 'firefox'
        if(browser.equalsIgnoreCase("firefox")){
            //create firefox instance
            System.setProperty("webdriver.gecko.driver", "./geckodriver.exe");
            driver = new FirefoxDriver();
        }
        
        //Check if parameter passed as 'chrome'
        else if(browser.equalsIgnoreCase("chrome")){
            //set path to chromedriver.exe
            System.setProperty("webdriver.chrome.driver", "./chromedriver.exe");
            driver = new ChromeDriver();
        }
        else if(browser.equalsIgnoreCase("Edge")){
            //set path to Edge.exe
            System.setProperty("webdriver.edge.driver", "./msedgedriver.exe");
            driver = new EdgeDriver();
        }
        else{
            //If no browser is passed throw exception
            throw new Exception("Incorrect Browser");
        }
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }
    
    @Test
    public void testParameterWithXML() throws InterruptedException{
        //Mazímizar la ventana
        driver.manage().window().maximize();
        //Dirigirse a la página del login
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1630982020&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d31d92721-752d-3aae-eb63-f2dd027fd57e&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015");
        
        //Inicializar el esperador
        WebDriverWait wait = new WebDriverWait(driver,15);
        //Obtener el input de correo y llenarlo con usuario
        driver.findElement(By.id("i0116")).sendKeys("EMAIL@hotmail.com");
        //Obtener y presionar el botón "Siguiente"
        driver.findElement(By.xpath("//*[@id=\"idSIButton9\"]")).click();
        //Thread.sleep(4000);
        //Esperar hasta que aparezca el input de contraseña
        WebElement contrasena = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("i0118")));
        //Insertar el valor de la contraseña
        contrasena.sendKeys("CONTRSEÑA");
        //Buscar y presionar el botón de Inicio de sesión
        driver.findElement(By.xpath("//*[@id=\"idSIButton9\"]")).click();
        //Thread.sleep(4000);

        //Microsorft Pregunta sí se desea mantener la sesión iniciada
        //Esperar hasta que aparezca dicho botón
        WebElement nope = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"idBtn_Back\"]")));
        //Presionarlo
        nope.click();
        //Thread.sleep(4000);
        //Esperar a que cargue la página
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/a/span")));
        //URL que se espera al terminar las operaciones
        String urlActual = "https://outlook.live.com/mail/0/inbox" ;
        String urlEsperada= driver.getCurrentUrl();
        Assert.assertEquals(urlEsperada,urlActual);
        driver.close();
    }
    
    
   
}
