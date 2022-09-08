Hola! Bienvenido a la herramienta para la detección rápida de neumonía.

A continuación le explicaremos cómo empezar a utilizarla

Requerimientos necesarios para el funcionamiento:

- Instalas Anaconda para windows siguiendo las siguientes instrucciones:
	 https://docs.anaconda.com/anaconda/install/windows/
- Abra conda power shell y ejecute las siguientes instrucciones:

	conda create -n tf tensorflow
	
	conda activate tf
	
	cd codes
	
	git clone https://isabella83tr@bitbucket.org/isabella83tr/codes.git

	pip install -r requirements.txt

	python detector_neumonia.py
----------------------------------------------------------------------------------

Uso de la herramienta:

- Ingrese la cédula del paciente en la caja de texto
- Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos
del computador
- Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
- Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel
con extensión .csv
- Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
- Presión el botón 'Limpiar' si desea cargar una nueva imagen
