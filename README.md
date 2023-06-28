# API-Ingenieria-CV
API que se encarga de la detección de objetos para el proyecto de ingeniería de software.
Compuesta por dos clases: una es la API en sí y la otra se encarga de la lógica de la detección.

El modelo está entrenado con YoloV5.

La idea es que la API principal (desarrollada en Java con SpringBoot) se comunique con esta para que realice el proceso de detección y devuelva una lista de las clases detectadas (va a devolver aquellas que tengan una confianza > 50).
