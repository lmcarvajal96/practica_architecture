# practica_architecture Luiss M. de Carvajal

El diseño de nuestra arquitectura se resume en:

-Objetivo: Creación Newsletter que mande semanalmente a usuarios registrados las frases nuevas de la semana de los jugadores de su equipo favorito.

-Tecnologías base: Google Cloud Platform, Dataproc, Sendgrid 

-Pasos:
  1.Web HTML con form donde usuarios se registran con su mail y equipo favorito
  2. API y Scrapping: Conseguiremos de MArca.com las nuevas noticias y de Football-api losjugadores de cada equipo.
  3. Sacamos las frases de las noticias, juntamos en dataproc con lista de usuarios y mandamos con Sendgrid a cada usuario las nuevas frases de sus jugadores de esa semana.
  
 He dejado también un scrapping function para crawlear las noticias de un equipo, en este caso el Sevilla. Para demostrar que podría hacer el scrapeo en vida real.
 
 Gracias

