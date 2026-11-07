# Reporte breve — Ejercicio 1: Encadenamiento en la biblioteca

**¿Por qué `Becario(Ana)` aparece en el encadenamiento hacia adelante de `AccesoNoche(Ana)` y no en el de hacia atrás?**

El encadenamiento hacia adelante revisa todas las reglas y obtiene los hechos que se pueden deducir, aunque no sean necesarios para responder la consulta. Como `Estudiante(Ana)` y `TieneCredencial(Ana)` son verdaderos, se aplica `R_beca` y aparece `Becario(Ana)`. Por otro lado, el encadenamiento hacia atrás comienza con `AccesoNoche(Ana)` y busca únicamente demostrar las condiciones de acceso mediante `R_acceso` y `R_miembro_est`. Por eso no utiliza `R_beca`, ya que ser becario no es un requisito para entrar.

**¿Por qué el encadenamiento hacia atrás prueba `R_miembro_est` al buscar `Miembro(Marta)`, si Marta es profesora?**

Esto ocurre porque el algoritmo revisa las reglas en el orden establecido. Primero intenta `R_miembro_est`, cuya conclusión `Miembro(x)` puede coincidir con `Miembro(Marta)`. Sin embargo, al buscar `Estudiante(Marta)` no encuentra ese hecho y la prueba falla. Después retrocede y utiliza `R_miembro_prof`, que sí permite demostrar la meta a partir de `Profesor(Marta)`. De esta manera, confirma que Marta es miembro y puede acceder durante el horario nocturno.

**Si se añade `TieneCredencial(Luis)` y se vuelve a preguntar `AccesoNoche(Luis)`, ¿qué átomos nuevos aparecen y la consulta queda probada?**

Al agregar el hecho `TieneCredencial(Luis)` y ejecutar nuevamente ambos algoritmos, el encadenamiento hacia adelante infiere tres átomos adicionales respecto a la base original: `Miembro(Luis)` y `Becario(Luis)` en la primera ronda, y `AccesoNoche(Luis)` en la segunda. Esto se debe a que Luis ahora cumple las condiciones de `R_miembro_est`, `R_beca` y `R_acceso`. El encadenamiento hacia atrás también demuestra la consulta mediante `Estudiante(Luis)`, `TieneCredencial(Luis)` y `HorarioNocturno(Hoy)`, sin derivar `Becario(Luis)`. Por lo tanto, **ambos algoritmos responden SÍ**.