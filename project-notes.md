# Notes that I need to make
- Thought processes
- Solution itself
- Issues that I run into
- Timeframes I work or think about the problem
- Resources or websites I look into to solve the problem
- Insight into the process of working through the problem

# When I submit the code file, also copy and paste into a text file to be uploaded alongside the code file.

"A company named, Fancy Names, specializes in using artists and technology to take a client's submitted name and then making artistic signage of that name, out of a range of materials. 
They have a singular store where a customer can make a purchase to pick up later or an order can be placed online.
Online orders have to be paid for in advance but in store orders can be paid for at pick up.
The production of the product happens at a different location called Art Factory and then is either shipped to the client or over to the store.
Fancy names already has a successful system for taking orders and keeping client information stored for use. The problem they want you to solve comes from the report the system creates that gets sent to Art Factory.
It pulls all order names to be created, the material type, and shipping information into a single excel document that is emailed over to Art Factory. This slows production down because someone has to open the document and sort the information.
Fancy Names wants a program that when fed this file, it breaks the info up appropriately.
After being broken down it prints the info to a new excel document.
An example file has been attached.
The file contains 3 columns of information. The first column contains the names to be created by the artists. It can come in 5 possible forms.
These names need to be broken into many pieces as possible if possible.
a space between parts of the name is where it would be broken apart. Evan Vaverka would become Evan in one column and Vaverka in a seperate column.

- Evan Vaverka
- Evan Patrick Vaverka
- Evan
- E. Vaverka
- Evan V.

The second column contains the material the name will be created with and the third column contains whether it is return to store "Store" or "Shipped" from Art Factory.
     - I am assuming that return to store means being shipped to "Store" which will be implied with the "Store" label.
While this information does not need to be manipulated it is important to have in the new document so Art Factory can sue it for production and shipping, instead of having to look at 2 seperate documents
Fancy Names would like the document sorted by one of the columns of information so that there is some order to the document when it is looked at.


# Most useful resources for using Python
- pandas
     - reads excel files
     - manipulates columns, sorting
     - writes back to Excel file


# Documentation that I referenced:
     - https://pandas.pydata.org/docs/user_guide/io.html#excel-files
     - https://pandas.pydata.org/docs/user_guide/text.html 




# Log of things done
- 6/1/2026
     - Started writing things down in Project Notes.
     - Decided that I would use Python for simplicity.
- 6/11/2026
     - Created a virtual environment on my WSL-Ubuntu so that I can install pandas without affecting my global python configuration
     - Installed pandas