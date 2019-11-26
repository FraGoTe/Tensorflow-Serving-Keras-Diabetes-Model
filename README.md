# Tensorflow-Serving-Keras-Diabetes-Model
We are exposing this model in 

```http://francis-gonzales.info:8501/v1/models/diabetes```

For getting metadata info:

```http://francis-gonzales.info:8501/v1/models/diabetes/metadata```

For calling this service make a POST request to:

```
http://francis-gonzales.info:8501/v1/models/diabetes:predict
```

Send the following parameters:

```
{
 "inputs": {
	"dense_1_input" : 
	[	
		[
            1, 80, 90, 35, 145, 35, 0.7, 30
        ]
	]
 }
}
```

The values of this model are the following:

```['Embarazos', 'Glucosa', 'Presion', 'EspesorPiel', 'Insulina', 'IMC', 'DiabetesFamiliar', 'Edad', 'PacienteDiabetico']```

