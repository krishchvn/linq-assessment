Potential Bug: ID, CLASS_NAME for input field for phone number on linqapp.com/welcome is different on every browser, and can change after click on other links

On Chrome, Brave

Initial occurrence: <input name ="input-4" id ="input-3">

After clicking on Email button: <input name ="input-7" id ="input-6">

On Mozilla

Initial occurrence: <input name ="input-8" id ="input-7">

After clicking on Email button: <input name ="input-14" id ="input-13">

Steps to Reproduce:

Visit 'https://linqapp.com/welcome', open Inspect and go to input field element. You might see Initial Occurence as per browser.

Click on Email Authentication button, you should be navigated to 'https://linqapp.com/auth-page', press back, and open inspect and input element. Fields ID and Class_Name should be changed.

There are also other occurrences such as <input name ="input-18" id ="input-17">, <input name ="input-22" id ="input-21">, etc, which I am not able to reproduce as of now, but I will keep trying

Why I think this is a bug and not a security feature:

1. If this was meant to be a security feature, I think a developer might add a random string to the input id or class-name rather than random numbers with a difference of 1.

2. I could not notice any certain pattern of input-'number' related to number of clicks, or links visited except Email button click and input-7 and input-6
