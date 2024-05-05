Here I have main.py file that uses openpyxl to open xlsx file and Extract url and id columns form input.xlsx

In the test.py file BeautifulSoup and request to extract title and content from url of extracted from excel input that i have imported from main file

In result.py I have taken data file that i have extracted from websites and saves in 'Files/' path and performed cleaned operation using stopwords that is in 'Assignment/StopWords/'

In result2.y I have takes Cleaned data files that is in 'Clean/' path and implemented all the operations and finding sementic analysis and stored in 'analysis_result.xlsx' file in same order as ouput provided

Note:
	There were some links that does not have any page (title or content) so for those weblink the output is not 	generated.
	
	I have copy pasted the positive-word.txt and negative-word.txt file outside MasterDictionary for my simplycity
	
	I also have taken help of ChatGPT since this is my first project like this which i am not quit familiar with so Be sure 	to check for any error occure that not happen in my computer.