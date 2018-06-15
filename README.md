#About the solution

Really basic credits converter for a job code interview

There is an entry point where you just need to enter the instruction file,
but there is also more support classes where you can place the instructions
manually (like the function parse_instructions in the Parser class).
Also there is some functionality that it is useless but i considered
necessary to implement just in case i had to use it in the algorithm
to convert the roman number to literal (like re implement the more
than or less than equal operations in the RomanLiteral Class), i decided to
keep them just if changes on the algorithm in the future would be necessary.

#About how to run the tests and solution

the way to run the tests is:

make test

to run the program just run the following command:

make run FILE="path_to_file"

where path_to_file is the location of the file that contains the commands of the program
