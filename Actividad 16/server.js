const webdriver = require("selenium-webdriver");
const until = webdriver.until
const By = webdriver.By; 
const driver = new webdriver.Builder().forBrowser("firefox").build();

// Dirigirse a una página
driver.navigate().to("https://www.facebook.com/")
//Esperar hasta que se muestre en el navegador los campos de inicio de sesión
.then(() => driver.wait(until.elementLocated(By.id('email'))))
//Ingresar usuario y contraseña
.then(() => driver.findElement(By.id("email")).sendKeys("email@cuentadeEmail.com"))
.then(() => driver.findElement(By.id("pass")).sendKeys("CONTRASEÑA"))
//Presionar el botón de inicio de sesión
.then(() => driver.findElement(By.name('login')).click())
