## Django Assignments   
**Assignment 1 - World Clock**   
Build a HTML Page which shows the date and time in 8 major cities of the world
- Los Angeles
- New York
- London 
- Dubai
- Bangalore
- Singapore
- Tokyo
- Sydney       

The HTML page shall show 8 analog clocks, 4 in each of the 2 rows. Each clock should show the time changing every minute.  Below each clock, the name of the city followed by time in digital format should be shown. Eg. **Bangalore 09-Jul-2023 3:30 pm**

**Assignment 2 - Word Building**   
Design a Word Building Game between Player and Computer.  Assume a dictionary of 20,000 words available to you as a .TXT file.  If player starts a word eg SMILE, the computer should respond with another word, eg ELEPHANT.  ie Last letter of Player's word should be the first letter of Computer's word. Player or Computer lose under 4 conditions
- Player responds with a wrong word. ie. A word whose first letter is not same as last letter of computer
- Player repeats a word already used by either player or computer
- Player responds with a non-English word
- Player does not respond within 30 seconds   
For each word, the player/computer gets a mark equivalent to the length of the word as illustrated below
SMIL**E** - **E**LEPHANT  (5,8)   
TRAI**N** - **N**ETWORK  (5,7)   
KE**Y** - **Y**OUNG (3,5)   
If the game is terminated before any player loses, then the player/computer with the higher total marks wins the game.

**Assignment 3 - OTP Business**  
Mr. Prajwal has started a company to provide OTP to all banks in the world.  His first 5 customers are  
ICICI - 4 digit OTP at rate of INR 0.04 per OTP   
SBI - 5 digit OTP at rate of INR 0.04 per OTP   
HDFC - 6 digit OTP at rate of INR 0.04 per OTP   
HSBC - 8 digit OTP at rate of INR 0.08 per OTP   
WellsFargo - 6 digit OTP, at rate of $ 0.008 per OTP   

Each Bank should get a personalized admin page to order required number of OTPs.  Eg. ICICI may order 5 lakh OTPs in one order.
For every order, Prajwal will generate an invoice and automatically send it to the Bank's officer. Build an application with Login-Authentication for each Bank along with the order details with invoice amount payable to Prajwal. Design an Admin Page for Prajwal to monitor his business.

**Assignment 4 - Question Bank**

Central School, Patna, Bihar has come up with the following approach to prevent copying in 10th and 12th Standard exams.  If the Mathematics paper is having the following question,

A car travels at a speed of 60 km/hr for a duration of 2.5 hrs.  What is the distance covered?

Build an application which will generate 30 different question paper sets and 30 different answer keys, with different parameters.  
60 - 2.5   
50 - 1.8  
40 - 2.5  
Generate a single-page answer key for all the 30 questions.

**Assignment 5 - Figures To Words**  
Reliance CFO is having difficulty in converting figures to words, while writing a cheque to his suppliers. Build a web-application to take any amount from   
Re 1 to  Rs 999,99,99,999  
and generate the equivalent value in words.   
Eg **Rs 87,65,432** is Rs Eighty seven lakhs sixty five thousand four hundred and thirty two

**Assignment 6 - List Files**

Build an application to display the list of all .files in a specific directory of your computer and arranged in the descending order of file update date.  Eg. in C:\USERS\
2024 - 64 files  
2023 - 52 files  
2022 - 20 files  

On clicking of any line above, the detailed page should be shown as below  
01-Jan-2024 - sample.txt,  abdulkalam.jpg  
Use **os.walk**,  **os.path.isdir()**, **os.path.isfile()**

**Assignment 7 - Quiz on Capitals**  
Build a Quiz based on a file containing countries, capitals as below  

India, New Delhi  
US, Washington DC  
UK, London  
France, Paris  
Italy, Rome  

The question should be shown as below
**"What is the capital of India?"**  
If the response is same as answer, then user gets 10 marks, else 0.  After the 5 questions are completed, then display total marks. Also display all the wrongly answered questions with their correspondng correct answers.

**Assignment 8 - Malware Fun**  
There is a malware in your computer with the signature-  
***"Attack on 14th. Be prepared for 1 million ransomwrare"***.  
There are about 10,000 files in your laptop.  You have to search all the files one and one and list the files containing this virus, along with the date on which the file was created or updated.

**Assignment 9 - Password Generator**  
Create a Password Generator which takes 2 inputs
- Length of the Password
- Number of Passwords to be generated 
Each Password should contain at least 1 upper case, 1 lower case and 1 numeric digit.

**Assignment 10 - Gas Booking**

Build a Gas-Booking application where user inputs a Consumer Number in  Web Page.  In response, a Gas Cylinder Refilling order is taken and an invoice is generated automatically. The delivery boy will get instructions to supply the Cylinder to the required address.  Make necessary assumptions

**Assignment 11 - Pincode Search**  

Build a Pincode Search facility.  If user inputs "560083", he should get the response as "Gottigere, Bannerghatta Road, Bangalore, KN 560083"  Store the data in an external MySQL Database.  Make necessary assumptions

**Assignment 12 - Data Theft by hidden Malware**

Create a Malware which will read your computer's IP address, CPU configuration, Memory Configuration, LAN Card MAC addresss and other sensitive parameters and automatically send an email to  bad_guy@gmail.com, without the knowledge of the user.   The command > py manage.py runserver should run in the background.

**Assignment 13 - CitiBank Credit Card**

CitiBank is having 10 million credit card holders.  To prevent fraud, the odd digits of each 16-digit credit card number is stored in a server in London while the even digits are stored in a server in Singapore.  Eg

1234567887654321 - Credit Card number  
London - 1 3 5 7 8 6 4 2  
Singapore - 2 4 6 8 7 5 3 1 

On the first day of each month, the servers are shifted to 2 other countries. Prepare an automation script which will complete the required work for CitiBank

**Assignment 14 - Word Permutations**

Calculate all the permutations of different sized words by creating the following Python functions  
perm3("EAT")  
perm4("FAST")  
perm5("SMILE")  
perm6("TRAINS")  
perm7("BEASTLY")  
perm8("STRANGER")  

perm("BEAUTIFUL") - a single function which can take word of any length

**Assignment 15 - Create Crossword Puzzle**  
The following questions and answers are given  
Animal used in racing and betting - HORSE  
This travels faster than sound -  LIGHT  

If you have 30 such Q and A, prepare an automatic CROSSWORD PUZZLE for Times of India to publish it in their weekly children's secion.  The clues are top to bottom, bottom to top, left to right, right to left.

**Assignment 16 - Make Collage**  
Build a project which takes a zip file containing 16 photographs and generates an automatic collage of 4*4  ( 4 rows and 4 columns.)  If file contains 25 photographs, generate 5*5.   Use  OpenCV module.

**Assignment 17 - Calendar for Year 2024**  

Generate a Calendar for Year 2024 without using any 3rd party calendar package.  You may highlight today's with a red colour


**Assignment 18 - Create a Chessbard**  

Create a Chessboard with 16 white pieces and 16 black pieces. When NEXT button is clicked, the white pawn should go by 1 set.
When NEXT button is pressed, the black pawn will move. This can continue till the game is over. You may download any game from the Internet and use it here.


