
# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems
- Fabricio da Fonseca Viannay
- Robert De Cort


**1. What was your experience in collaborating? Talk about what steps you used to ensure the inputs from group members worked- code testing, GitHub branch management, etc.- and how you divided up the workload for the project.**

>De Cort: Since it was only Fabricio and myself, collaborating went pretty well. 
    We split up the project so each person had 3 sub systems, however I did ask for some help on some of my portions. 
    We used Teams chat for most of the communication and we met up once in person to go over the code we had done and take stock of what else we needed to do.  
    Using GitHub was a little daunting at first but the GitHub desktop version really helped to streamline pushing and pulling code and its UI did a great job with showing what code was added and deleted. 
    We did not make any branches outside of main when pushing code. 
    I can understand how in a bigger project with more people, it would be much better practice to make separate branches. 
    However, for just the two of us just pushing directly to main worked fine.

>Fabricio: I tried using a test branch but it was very confusing for me, it seems like GitHub uses the same folder to store all branches, so when you change the branch in the desktop software, it replaces all files on the computer. I think it is just a question of a learning curve but I didn't have time to understand completely. Since it was just two and we had a good communication, working on the main branch went very well. Also, the GitHub version control helps a lot if you need to undo something. 
 
**2. What was the most challenging section, and why? Feel free to provide more than one response if there is a difference of opinion in the group.**

>De Cort: For me, the most challenging section was the ADC subsection. Mainly because I did my math backwards when it came to calculating the current vs desired orientation which then threw off the rest of my code            output. Thankfully Fabricio caught it.

>Fabricio: For me, the most challenging was the payload. Understand the np.stack and its axis took a long time and the IDE (Spyder) didn't show the stacked version correctly with the 3 matrix in a 3rd axis or like spreadsheets tabs, which turned everything more difficult.  

**3. If you employed Generative AI tools, how did you do so? Discuss which tools you used, the prompts you utilized, how you ensured the results were valid, and how you integrated the code into your tasks.**

>De Cort: I used ChatGPT as an enhanced Google more than anything else. I found it much quicker to ask coding syntax questions or how to do certain functions rather than clicking on multiple links after a google search.      It was nice to see a basic outline of some rudimentary code which I was then able to add on to and tweak it. I thought it also did a great job explaining coding concepts, something which me scouring Google would not         have really found. Before I would put them in my main body of code, I would have a test file. Then I would play around the code to ensure it was doing what I wanted. Most of the time, ChatGPT would give me a viable          skeleton, I would just need to give it the muscle.
<br>Some prompts:
>- “How to do math on two tuples in a list in python”
>- “How to make the contents of a file into a tuple in python”
>- “Nested for loops in Matlab”
>- “How to iterate through a matrix in Matlab”

>Fabricio: I used to get an explanation on how to use np.stack but it didn't help much.

**4. What other resources did you use to find solutions? Online sites, books, references, etc.**

>De Cort: I utilized the powerpoints used in this class for some reference. However, other than that, I did not use anything else.

>Fabricio: I used the class powerpoints for some quick references, but usually I used Google, Stack Overflow, and w3schools. For the payload task, I also used the library website (matplotlib and numpy).

**5. In what way could this project be improved for future quarters?**

>De Cort: Maybe as the culmination of all the Check Plus’s, they all need to be fed into another program which incorporates all the subsystems outputs.

>Fabricio: I think the image processing could have one or two more steps. It was very educative and could teach a bit more about the subject. Maybe with a small SAR image.
___
___
**RCS Output**
___
**RCS Check Output:**
 * Firing a thruster for 5 seconds, with ˙m = 0.02 and ve = 1000
 * Firing a thruster for 3 seconds, with ˙m = 0.06 and ve = 1000
 * Firing a thruster for 10 seconds, with ˙m = 0.05 and ve = 2000

![RCS Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/RCS/RCS_Check.PNG)
___
**RCS Check Plus Output:**
 * Firing Thruster 1 for 15 seconds, with ˙m = 0.04 and ve = 2000
 * Firing Thruster 2 for 4 seconds, with ˙m = 0.03 and ve = 2000
 * Firing Thruster 3 for 3 seconds, with ˙m = 0.01 and ve = 2000

![RCS Check Plus Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/RCS/RCS_Check_Plus.PNG)
___
___
**TCS Output**
___
**TCS Check Output: 25 total iterations: Images show 1-3 of and 23-25 iterations**

![TCS Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/TCS/TCS_Check_1.PNG)
![TCS Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/TCS/TCS_Check_2.PNG)
___
**TCS Check Plus Output: Images show first 4 iterations and last 3 iterations**

![TCS Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/TCS/TCS_Check_Plus_1.PNG)
![TCS Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/TCS/TCS_Check_Plus_2.PNG)
___
___
**ADC Output**
___
**ADC Check Output: (100,200,300)**

![ADC Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/ADC/Check_One.PNG)
___
**ADC Check Output: (0,0,0)**

![ADC Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/ADC/Check_Two.PNG)
___
**ADC Check Output: (3,30,300)**

![ADC Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/ADC/Check_Three.PNG)
___
___
**C&DH Output**
___
**C&DH Check Output: EPS:CMD01:0**

![C&DH Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/C%26DH/Check_one.PNG)
___
**C&DH Check Output: ACS:CMD04:-1**

![C&DH Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/C%26DH/Check_two.PNG)
___
**C&DH Check Output: RCS:INVALID:0**

![C&DH Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/C%26DH/Check_three.PNG)
___
**C&DH Check Plus Output: EPS:CMD01:0, ACS:CMD04:-1, RCS:INVALID:0**

![C&DH Check Plus Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/C%26DH/Check_plus.PNG)
___
___
**EPS Output**
___
**EPS Check Output**
 * Voltage of 25 V, Amperage of 10 A, running for t = 3600 seconds
 * Voltage of 30 V, Amperage of 8 A, running for t = 1800 seconds
 * Voltage of 15 V, Amperage of 12 A, running for t = 7200 seconds
   
![EPS Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/EPS/Check.PNG)
___
**EPS Check Plus Output: [(22,7,300), (40,7,60), (25,10,200), (10,4,600)]**

![EPS Check Plus 1 Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/EPS/Chec_plus_1.PNG)
___
**EPS Check Plus Output: [(0,7,300), (30,10,60), (28,10,200), (10,10,10)]**

![EPS Check Plus 2 Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/EPS/Check_plus_2.PNG)

___
___
**Payload Output in Payload Folder**

https://github.com/FViannay/nps_ss1100_fall24/tree/main/Payload


# Instructor Comments

### ADC
Good use of the tuple comprehension in the grading_file. Recommend you delete the last two lines of that script - once you're done with testing, you can delete those practice calls of the formula to reduce the chance it will mess something up in the future. Alternatively, comment it all out and leave instructions indicating that it is for testing purposes only.

### C&DH
In your Check script, you have a lot of recurring themes. One thing to consider when working on larger projects is how you can reuse and repurpose code, rather than having to write out every line separately for each element. 
For the Check Plus script, I would recommend breaking down the three parts of the trigram into three separate functions, which are then called by the cpr() function. Speaking of which, "cpr" is a legal, allowed name, but it might be a bit hard to remember what it does - more descriptive is better. Finally, something to consider is working on your functions so that they always return the same type of result, even if it is an "error" or something goes wrong. By this, I mean making sure that you print/return in the same way. I noticed that you had to call "print(cpr(XX:XXX:XX))", wrapping your function call in a print statment. Consider getting that print statment inside the function so you can just call cpr() and be done with it.

### Payload

In your *savefile* function, I'd recommend you use the built-in functions that come with the sys and os modules to help with the issues that you're addressing with that code. Things like combining filenames with "\" characters and checking for empty names are easily solved with tools such as "os.path.join" and "os.path.exists", respectively.