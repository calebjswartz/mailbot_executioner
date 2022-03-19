# mailbot_executioner
This is a python program that reads code from a drafted email in a gmail account and executes it. Intended to be run on a remote device.

It requires that you enter a username and password for a valid gmail account.

Make sure you enable IMAP and also 'allow access from less secure apps' in your account settings.

The commands are read from the email, written to a text file for editing (to remove leftover HTML elements), read to memory, and finally executed.

To tell the interpreter where the command script ends, include the variable declaration 'parsekillhere = 0' at the end of the drafted email.

As is, the program automatically deletes the drafted email from which it reads the commands when it is done with the email. I have commented out a feature to do the same with the text file.

The timer constant must specify a time in seconds to wait before executing the get_mail function to check the drafts folder for commands.

I have also included two python files ("encode.py" and "exec.py"). The first file encodes a program in a simple attempt to hide the content from static analysis before execution. A program is included as a string in exec.py and will be decoded/executed in memory when it is run. The program is encoded from an input text file and output to another text file.
