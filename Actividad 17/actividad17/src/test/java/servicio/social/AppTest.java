package servicio.social;

import java.io.File;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.apache.commons.io.FileUtils;

import junit.framework.Assert;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

class AppTest {
    public static void main(String[] args)
    {
        System.out.println( "Hello World!" );
        System.setProperty("webdriver.gecko.driver", "./geckodriver.exe");
        WebDriver driver = new FirefoxDriver();
        
        //Mazímizar la ventana
        driver.manage().window().maximize();
        //Dirigirse a la página del login
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1630982020&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d31d92721-752d-3aae-eb63-f2dd027fd57e&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015");
        
        //Inicializar el esperador
        WebDriverWait wait = new WebDriverWait(driver,30);
        //Obtener el input de correo y llenarlo con usuario
        driver.findElement(By.id("i0116")).sendKeys("EMAIL@hotmail.com");
        //Obtener y presionar el botón "Siguiente"
        driver.findElement(By.xpath("//*[@id=\"idSIButton9\"]")).click();
        //Esperar hasta que aparezca el input de contraseña
        WebElement contrasena = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("i0118")));
        //Insertar el valor de la contraseña
        contrasena.sendKeys("CONTRASEÑA");
        //Buscar y presionar el botón de Inicio de sesión
        driver.findElement(By.xpath("//*[@id=\"idSIButton9\"]")).click();

        //Microsorft Pregunta sí se desea mantener la sesión iniciada
        //Esperar hasta que aparezca dicho botón
        WebElement nope = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"idBtn_Back\"]")));
        //Presionarlo
        nope.click();
        //Esperar a que cargue la página
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/a/span")));

        try {
            tomarCaptura(driver,"./Capturas/prueba.png");
            System.out.println("Captura tomada");
        } catch (Exception ex) {
            Logger.getLogger(AppTest.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        //URL que se espera al terminar las operaciones
        String urlActual = "https://outlook.live.com/mail/0/inbox" ;
        String urlEsperada= driver.getCurrentUrl();
        Assert.assertEquals(urlEsperada,urlActual);
        
    }
    
    public static void tomarCaptura(WebDriver webdriver,String destino) throws Exception{
        //Hacer un casteo del webdriver
        TakesScreenshot scrShot =((TakesScreenshot)webdriver);
        //Llamar al método que hace la captura
        File SrcFile=scrShot.getScreenshotAs(OutputType.FILE);
        //Mover la imagen a la tura especificada
        File DestFile=new File(destino);
        //Copiar el archivo a el destino
        FileUtils.copyFile(SrcFile, DestFile);
    }
}
