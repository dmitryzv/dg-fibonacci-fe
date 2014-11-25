# Fibonacci number calculation front end
This Python sample application uses the [Flask](http://flask.pocoo.org/) framework.

This version of the application can be packaged and deployed as a Docker container. 

1. To build the container run (from the directory containing dockerfile):
	
		sudo docker build -t dg-fibonacci-fe .        
        
2. To run the container run:
			
		sudo docker run -d -p 80:80 -e FIBONACCI_BE_ADDRESS="<app-ip>:5000" --name dg-fibonacci-fe dg-fibonacci-fe

3. To access:
		
		http://<app-ip>

 
        
        
