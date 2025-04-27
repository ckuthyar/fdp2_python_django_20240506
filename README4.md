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

**Assignment 19 - Mathematical Tables**    
a) Display Mathematical Tables from 3 to 20 in the following form     

3 * 1 = 3    
3 * 2 = 6    

3 * 10 = 30      
  
4 * 1 = 4     
4 * 2 = 8              

20 * 1 = 20    
20 * 2 = 40     

b) Take n1=3, n2=20 as input from keyboard and repeat     
c) Read from file in1.txt having 3 and 20 in 2 different lines, one below the other     
    3     
    20     
d) Read form file in2.txt having 3 and 20 in a single line, separated by a comma     
    3,20     
e) Write into a file out1.txt     
f) Write into different files, each corresponding to the table printed     
     out_3.txt     
     out_4.txt     
     out_5.txt     
     ......    
     out_20.txt    

**Assignment 20 - School Clock Angle**    
School Clock is showing 9 am.  Compute the angle between the Hour hand and the Minute hand.  It should show Time: Angle in Degrees from 9:00 am to 8:55 pm with a spacing of 5 minutes.      

Sample Output:    
9:00 - 90.00    
9:05 -     
9:10 -    
9:15 -    
9:20 -    
9:25 -       
9:30 -    
9:35 -    
9:40 -     
9:45 -    
9:50 -    
9:55 -   

10:00 - 60.00    
10:05 -    
....    
10:55    


20:00 -   
20:05 -   
....    
20:55 -   

Clues    
1) What is the exact angle between Hour Hand and Minute Hand at 3 pm ?   
2) What is the exact angle between Hour Hand and Minute Hand at 3:05 pm ?    
3) What is the exact angle between Hour Hand and Minute Hand at 3:10 pm ?    
4) What is the exact angle between Hour Hand and Minute Hand at 3:15 pm ?    

Write a program to read each line of file inConvert.txt and write the equivalent reverse conversion into outConvert.txt

Example 1
If input is 

1 metre = 100 com, 
                 
then output should be

1 metre = 100 cm
1 cm = 0.01 metre

Example 2

If input is
8 kilometres = 5 miles,

then output should be

1 kilometer = (5/8) miles.
1 mile =  (8/5) kilometres

Next, take input with 2 parameters (Unit and Quantity) and print the conversion on console

Eg.  
Pounds
5
should give,   5 Pounds = ??? kgs

**Assignment 21   Andaman  Prisoner  Problem**   
There are 100 prison cells in a row. All cells are locked Jailer is given permission by the Prime Minister of India to release any number of prisoners. In Round 1, Jailer opens all the doors.   In Round 2, he closes every alternate door (2, 4, 6...).  In Round 3, every third door (3, 6, 9,....) if Door is Open,, he closes it.   If Door is Closed, he opens it.  In Round 4, every fourth door (4, 8, 12..), if Door is open,, he closes it.  If Door is Closed, he opens it.  He does this for 100 Rounds.  At the end, who are the lucky prisoners ?      
Clue:    
1. First, take a paper and pencil and solve this manually for 10 prison doors and 10 rounds    
2. Before writing nested For Loops, first write 2 or 3 blocks of code manually, make sure that the program is doing what you want it to do, then convert this into a For Loop carefully without disturbing the code that is doing the job.    
3. First get the full design in your mind first, before you start using the computer. ie. sit away from the computer, visualize the program mentally, after the entire step by step instructions are clear in your mind, then sit on the computer.     

**Assignment 22 Gold Medal**  
There are 26 students in a class who have scored the following marks in 10th Std as per attached file Marks.txt  (Name, Gender, RollNo....).Write a Program to read the contents of the file. Please print the Gold Medalist (overall top scorer) and individual Topper in each subject along with the respective marks.    

Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS    
Babu,M,E80BD46CS0002,English:76,Maths:91,Physics:87,Chemistry:70,Biology:70,PASS    
Charles,M,E80BD46CS0003,English:78,Maths:92,Physics:88,Chemistry:73,Biology:80,PASS    
David,M,E80BD46CS0004,English:80,Maths:93,Physics:89,Chemistry:76,Biology:90,PASS     
Ekalavya,M,E80BD46CS0005,English:82,Maths:94,Physics:90,Chemistry:79,Biology:100,PASS    
Fabin,M,E80BD46CS0006,English:84,Maths:95,Physics:91,Chemistry:82,Biology:90,PASS    
Govind,M,E80BD46CS0007,English:48,Maths:96,Physics:92,Chemistry:85,Biology:80,PASS    
Harnish,M,E80BD46CS0008,English:56,Maths:97,Physics:93,Chemistry:88,Biology:70,PASS    
Irene,F,E80BD46CS0009,English:64,Maths:98,Physics:95,Chemistry:91,Biology:60,PASS    
James,M,E80BD46CS0010,English:72,Maths:99,Physics:96,Chemistry:92,Biology:70,PASS    
Kamaraj,M,E80BD46CS0011,English:80,Maths:100,Physics:97,Chemistry:93,Biology:80,PASS    
Latha,F,E80BD46CS00012,English:88,Maths:99,Physics:98,Chemistry:94,Biology:90,PASS    
Manish,M,E80BD46CS0013,English:70,Maths:98,Physics:99,Chemistry:49,Biology:100,PASS   
Nagesh,M,E80BD46CS0014,English:76,Maths:97,Physics:87,Chemistry:59,Biology:90,PASS     
Omar,M,E80BD46CS0015,English:82,Maths:96,Physics:89,Chemistry:69,Biology:80,PASS     
Padma,F,E80BD46CS0016,English:88,Maths:95,Physics:91,Chemistry:79,Biology:70,PASS    
Queenie,F,E80BD46CS0017,English:60,Maths:94,Physics:93,Chemistry:89,Biology:75,PASS     
Roopa,F,E80BD46CS0018,English:68,Maths:93,Physics:95,Chemistry:79,Biology:80,PASS    
Sundar,M,E80BD46CS0019,English:77,Maths:92,Physics:97,Chemistry:80,Biology:85,PASS    
Tara,F,E80BD46CS0020,English:79,Maths:93,Physics:99,Chemistry:81,Biology:90,PASS    
Ullas,M,E80BD46CS0021,English:75,Maths:94,Physics:87,Chemistry:82,Biology:95,PASS    
Vasu,M,E80BD46CS0022,English:85,Maths:95,Physics:89,Chemistry:83,Biology:90,PASS    
Wendy,F,E80BD46CS0023,English:65,Maths:96,Physics:91,Chemistry:84,Biology:85,PASS    
Xero,M,E80BD46CS0024,English:25,Maths:98,Physics:93,Chemistry:85,Biology:80,PASS    
Yasmin,F,E80BD46CS0025,English:75,Maths:100,Physics:95,Chemistry:86,Biology:85,PASS    
Zafar,M,E80BD46CS0026,English:75,Maths:98,Physics:87,Chemistry:79,Biology:89,PASS   

**Assignment 23 - Create Jumbled Words of all the US States in different files**
Alabama   
Alaska    
Arizona    
Arkansas    
California    
Colorado    
Connecticut   
Delaware    
Florida   
Georgia   
Hawaii   
Idaho   
Illinois   
Indiana   
Iowa    
Kansas   
Kentucky   
Louisiana   
Maine   
Maryland    
Massachusetts    
Michigan   
Minnesota   
Mississippi   
Missouri    
Montana   
Nebraska    
Nevada    
New Hampshire   
New Jersey   
New Mexico    
New York    
North Carolina     
North Dakota    
Ohio    
Oklahoma    
Oregon    
Pennsylvania    
Rhode Island    
South Carolina    
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming

**Assignment 24 - Simple Calculator**    
a) Take numbers num1=8, num2=4.  Calculate sum, difference, product, division, integer division, remainder, exponential
b) Create a function to take any 2 integer inputs and provide above     
num1+num2=12    
num1-num2=4    
num1*num2=32    
num1/num2=2.0    
num1//num2=2    
num1%num2=0    
num1**num2=4096    
