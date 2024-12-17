
# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems


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
**EPS Output**
___

**EPS Check Output**
 * Voltage of 25 V, Amperage of 10 A, running for t = 3600 seconds
 * Voltage of 30 V, Amperage of 8 A, running for t = 1800 seconds
 * Voltage of 15 V, Amperage of 12 A, running for t = 7200 seconds
![EPS Check Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/EPS/Check.PNG)
___
**EPS Check Pus Output: [(22,7,300), (40,7,60), (25,10,200), (10,4,600)]**
![EPS Check Plus 1 Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/EPS/Chec_plus_1.PNG)
___
**EPS Check Output: [(0,7,300), (30,10,60), (28,10,200), (10,10,10)]**
![EPS Check Plus 2 Output](https://github.com/FViannay/nps_ss1100_fall24/blob/main/EPS/Check_plus_2.PNG)

