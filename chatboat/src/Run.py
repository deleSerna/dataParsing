from rasa_nlu.model import Interpreter

# where model_directory points to the model folder
interpreter = Interpreter.load("../projects/default/model_20180812-135546")
output = interpreter.parse(u"looking for chinese food")
print(output)
