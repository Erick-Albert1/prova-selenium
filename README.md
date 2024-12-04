# prova-selenium
prova 

1° Prova: Python e Selenium.
Aluno: Erick Albert Brandão Eduardo Lins Junior
+Questões teóricas
1)	Explique a diferença entre Selenium IDE e Selenium WebDriver.
R= O Selenium IDE é uma extenção dos navegadores que permite o usuário gravar a tela e as sequencias para fazer um teste mais simples. Já o webdriver é algo mais robusto usando uma linguagem de programação para fazer funções automáticas.

2)	Quais são os principais tipos de localizadores (locators) usados no Selenium WebDriver para encontrar elementos na página? Explique dois deles.
R= O primeiro é o driver.find_element_by_id("id_do_elemento") com sua funcionalidade encontrar o elemento por meio do ID dele.
O segundo pode ser o driver.find_element_by_name("nome_do_elemento") com sua funcionalidade de encontrar o elemento por meio do nome.

3)	O que é um WebElement no Selenium? Dê um exemplo de como interagir com um WebElement usando Python. 
R= webElement é literalmente um elemento da pagina web que vc pode interagir seja com click ou preenchendo ele. Seguindo o exemplo:
elemento = driver.find_element_by_id("id_do_elemento_do_codigo")
elemento.click()  //Interagir com o WebElement clicando nele
4)	No Selenium WebDriver, o que acontece se você tentar interagir com um elemento que ainda não está visível ou carregado na página? Qual comando você usaria para resolver isso?
R= Como o elemento não carregou vai da erro na execução, podemos usar o comando time.sleep() para dar uma demora até a pagina carregar.
5)	Cite duas limitações do Selenium IDE que podem levar à escolha do Selenium WebDriver em projetos maiores.
R= limitação funcional, ou seja o selenium IDE é limitado para algumas funcionalidades tipo loops. E para atualizações da plataforma atrapalham na execução da gravação/teste feito. Diferente do teste feito com WebDriver que clica no elemento pela sua referencia e não pela sua posição na tela.

9) Durante a automação de testes, como você lidaria com pop-ups ou alertas usando Selenium WebDriver? Escreva um trecho de código em Python que feche um alerta assim que ele aparecer.

R= usaria a classe alert para simplesmente clicar no botão “ok” do alerta. 

// Iniciar o navegador
driver = webdriver.Chrome()

// Acessar um site de exemplo que gera um alerta
driver.get("https://www.exemplo.com/gera_alerta")

// Esperar até que o alerta esteja presente
WebDriverWait(driver, 10).until(EC.alert_is_present())

alerta = driver.switch_to.alert
alerta.accept()  //Isso clica no botão "OK" do alerta
driver.quit()

