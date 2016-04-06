This project is part of a coding challenge that I did with Nauge Networks. The project is a Flask application which uses Python and JavaScript to integrate two different exercises that take user data and provide information. 

After cloning my repo into a folder in your computer, go into terminal and run the following command from the cloned folder:
Create a virtualenv by running the following command:
$ virtualenv venv
$ ./venv/bin/activate
$ pip install -r requirements.txt
$ python server.py
Then point your browser to http://127.0.0.1:5000/

Then copy and paste the IP address that is made into your browser. From there you will reach the home page which has two buttons: One button to access exercise 1 and a different button to access exercise 2. 

Exercise 1:
In exercise 1, the user will provide an IP address and a subnet mask. From there, my task is to validate the information and then provide the corresponding network block and host Id. I used JavaScript and HTML forms to access the user input. My first task was to validate the user input and if there was any error in the input I used an alert box to inform the user. After I was sure the user had valid input, I used the AND operator on each octet of the IP address and the subnet mask to form the correct network block and host Id. 
For exercise 1, I also implemented a bonus feature that allows the user to submit the IP address and the subnet mask in CIDR notation. 

Exercise 2: 
In exercise 2, my job was to use RegEx to validate and then extract information from a user inputted log file. Again, I used JavaScript and HTML forms to access the user input. First I had to validate the components of the log file that the user provided. Then after I was sure that the log file was valid, I then proceeded to access the individual data pieces and output them to the screen  in the appropriate location. 
