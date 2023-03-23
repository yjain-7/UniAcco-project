# UniAcco-project
Command-line-tool that can parse CSV file in python

1. Open a command-line interface
2. Navigate to the directory containing the CSVTool.py file
3. Run the command python CSVTool.py <file> where <file> is the path to your CSV file
For example, if your CSV file is named data.csv and is located in the same directory as the CSVTool.py file, you would run the command python CSVTool.py data.csv.

After running the command, you will see a > prompt in the command-line interface. From here, you can enter one of the following commands:

- count: Count the number of rows in the currently loaded CSV file.<br>
- mean <column_name>: Calculate the mean of a numeric column in the currently loaded CSV file.<br>
- filter <column_name> <value>: Filter the currently loaded CSV file to include only rows where the specified column matches the specified value. <br>
- sort <column_name>: Sort the currently loaded CSV file where the specified column passed
- std_dev <column_name> : Calculated the standard deviation for the specified column
- print : prints the whole data in the form of list of dictionary
- exit: Exit the program.<br>
For example, if you wanted to calculate the mean of the "Age" column, you would enter the command mean Age at the > prompt. The program will then output the mean value to the console.

- Load the file
<pre><code>python CSVTool.py filename
</code></pre>

- Count the number of data in the file
<pre><code> >count
</code></pre>

- Mean for Integer value
<pre><code> >mean column_name
</code></pre>

- Filter 
<pre><code> >filter column_name value
</code></pre>

- Sort
<pre><code> >sort column_name
</code></pre>

- Standard Deviation
<pre><code> >std_dev
</code></pre>

- Pring
<pre><code> >print
</code></pre>
  
- Exit
<pre><code> >exit
</code></pre>

Following output is the output of the data.csv file attach in the repository
![output](https://user-images.githubusercontent.com/76871563/227264008-d5333e0b-771d-4a77-89cc-c16406b04f32.png)
 
Following output is with the function for Standard Deviation and Sort_by_column. The sorted.csv file is the output of the Sort_by_column function 
  
![output 2](https://user-images.githubusercontent.com/76871563/227284320-472817d5-2a77-458b-8005-5d15f30bc451.png)


Note that you must load a CSV file into memory before you can perform any of the above commands. To load a CSV file, simply provide the path to the file as the argument when running the program (i.e., python CSVTool.py data.csv). The program will automatically load the CSV file into memory.

Also written a code to generate csv file with random values to use while running the file
