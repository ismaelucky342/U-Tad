# Paquetes
# Un paquete extiende la funcionalidad base de R. Los paquetes oficiales están disponibles en CRAN,
# pero existen otros paquetes que solo están disponibles a través de repositorios como GitHub.

# Ejemplo de instalación de un paquete desde CRAN
install.packages("ggplot2")

# Ejemplo de instalación de un paquete desde GitHub
# Necesitas tener el paquete 'devtools' instalado
install.packages("devtools")
library(devtools)
install_github("hadley/ggplot2")