steps involved
1. nlu_md will contains the classification of user input into different category
2. model/domain.yml will contain what action to take for each category
3. story path will contain multiple paths of conversation
4. Then based on user's conversation, bot will reply

Above tutorial contains, how we can use it in a command line utility. 
http://rasa.com/docs/nlu/master/python/ contains the python apis for to do the same stuff.




Need to improve in above model

1. Write out custom class for chat bot reaction  
    solution - use this one http://www.rasa.com/docs/core/customactions/#customactions

2.  users has to type exactly for bot to respond
    sol - To improve it we can add synonyms and regex as in http://rasa.com/docs/nlu/master/dataformat/#section-dataformat

3. How to write a generic story
